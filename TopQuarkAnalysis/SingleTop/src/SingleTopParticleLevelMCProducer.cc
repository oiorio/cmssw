/*
 *\Authors: A. Orso M. Iorio 
 *
 *
 *\version  $Id: SingleTopParticleLevelMCProducer.cc,v 1.1.2.2 2013/06/21 20:40:25 oiorio Exp $ 
 */

// Single Top MC particle-level object producer
// This produces sets of particle-level objects (leptons, jets, neutrinos) with different definitions
// There are different possibilities for defining particle-level objects:
// 1) Leptons: one should use only leptons stemming from resonances (W,Z,a*) and not hadrons
// 1.1) One has the option to "dress" leptons with photons, i.e. defining collections of leptons and photons to use ak1 jet clustering onto
// 2) Jets: should be made out of the non-leptons and non-photons for dressing.
// 3) b-Jets: one possibility is to define b-jets clustering the "rescaled b-hadrons" instead of their decay products. For this definition, a b-jet will be a jet that has a rescaled b-hadrons amongst its component
// 3.1) Another possibility is to use the "rescaled b-hadron descendants", i.e. not modify the jet clustering but just going back to the b-decay products for identification.


#define DEBUG    0 // 0=false
//#define DEBUG    1 // 0=false

#include "PhysicsTools/PatAlgos/plugins/PATJetProducer.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Common/interface/Association.h"
#include "DataFormats/Candidate/interface/CandAssociation.h"

#include "DataFormats/JetReco/interface/JetTracksAssociation.h"
#include "DataFormats/BTauReco/interface/JetTag.h"
#include "DataFormats/BTauReco/interface/TrackProbabilityTagInfo.h"
#include "DataFormats/BTauReco/interface/TrackIPTagInfo.h"
#include "DataFormats/BTauReco/interface/TrackCountingTagInfo.h"
#include "DataFormats/BTauReco/interface/SecondaryVertexTagInfo.h"
#include "DataFormats/BTauReco/interface/SoftLeptonTagInfo.h"

#include "DataFormats/Candidate/interface/CandMatchMap.h"
#include "SimDataFormats/JetMatching/interface/JetFlavourMatching.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "DataFormats/PatCandidates/interface/JetCorrFactors.h"

#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSetDescription.h"

#include "FWCore/Framework/interface/Selector.h"



#include "TVector3.h"

////////Part to be made official
#include "TopQuarkAnalysis/SingleTop/interface/SingleTopParticleLevelMCProducer.h"
#include "DataFormats/Candidate/interface/NamedCompositeCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
//#include "TLorentzVector.h"
#include "TopQuarkAnalysis/SingleTop/interface/EquationSolver.h"

#include <vector>
#include <memory>



//using namespace pat;


SingleTopParticleLevelMCProducer::SingleTopParticleLevelMCProducer(const edm::ParameterSet& iConfig) 
{
  // initialize the configurables
  hadronizer_ =  iConfig.getUntrackedParameter<std::string>("hadronizer","Pythia6"); // Hadronizer for the choice of gen-particle statuses 
  channel_ =  iConfig.getUntrackedParameter<std::string>("channel","singleTop"); // Physics channel ("data","singleTop","TTbar","other")
  genParticlesSrc_ = iConfig.getParameter<edm::InputTag>( "genParticlesSource" );
  genJetsSrc_ = iConfig.getParameter<edm::InputTag>( "genJetsSource" );
  
  if (iConfig.exists("ignoreParticleIDs"))
    setIgnoredParticles(iConfig.getParameter<std::vector<unsigned int> >
			("ignoreParticleIDs"));
  setExcludeFromResonancePids(iConfig.getParameter<std::vector<unsigned int> >
			      ("excludeFromResonancePids"));
  
  doDressedCollections_ = iConfig.getUntrackedParameter<bool>("doDressedCollections",true); //
  doBaseCollections_ = iConfig.getUntrackedParameter<bool>("doBaseCollections",true); //
  doBDescendentJetSelection_  = iConfig.getUntrackedParameter<bool>("doBDescendentJetSelection",true);//
  useJetsNoNu_ = iConfig.getUntrackedParameter<bool>("useJetsNoNu",false); //
  //  No particle level top defined yet
  //  produces<std::vector<reco::NamedCompositeCandidate> >("particleLevelTops").setBranchAlias("particleLevelTops");
  
  if(doBaseCollections_){
  //Part 1: particle-level defined "bare" objects, no dressing:
  //Leptons from resonances ("bare" leptons):
  produces<std::vector<reco::GenParticle> >("particleLevelLeptons").setBranchAlias("particleLevelLeptons");

  //Jets using the plain resonance definition:
  produces <reco::GenParticleRefVector> ("genParticlesForJetsNoRescaledBHadronsNoDressLeptons").setBranchAlias("genParticlesForJetsNoRescaledBHadronsNoDressLeptons");
  produces <reco::GenParticleRefVector> ("genParticlesForJetsRescaledBHadronsNoDressLeptons").setBranchAlias("genParticlesForJetsRescaledBHadronsNoDressLeptons");
  }
  
  if(doDressedCollections_){
    //Part 2: particles for dressing:
    //Leptons and photons for dressing:
    produces <reco::GenParticleRefVector> ("genLeptonsForDressing").setBranchAlias("genEGammaForDressing");
    produces <reco::GenParticleRefVector> ("genEGammaForDressing").setBranchAlias("genEGammaForDressing");
    produces <reco::GenParticleRefVector> ("genMuGammaForDressing").setBranchAlias("genMuGammaForDressing");
 
    // using the lepton dressing definition
    //Jets: Adding Rescaled B-Hadrons for particle-level b-jet definition:
    produces <reco::GenParticleRefVector> ("genParticlesForJetsNoRescaledBHadrons").setBranchAlias("genParticlesForJetsNoRescaledBHadrons");
    
    //Jets without rescaled b-hadrons:   
    produces <reco::GenParticleRefVector> ("genParticlesForJetsRescaledBHadrons").setBranchAlias("genParticlesForJetsRescaledBHadrons");
  }


  //Part 3: selecting jets using the b-descendent definition
  if(doBDescendentJetSelection_){
    //Selection of genJets, using the "b-descendent" definition:
    produces<std::vector<reco::GenJet > >("particleLevelJets").setBranchAlias("particleLevelJets");
    produces<std::vector<reco::GenJet > >("particleLevelBJets").setBranchAlias("particleLevelBJets");
    //Note: if there is a rescaled b-hadron, it will automatically be a b-descendent.

  }
  
  if(doBaseCollections_){
  //Neutrinos from resonances and MET = SUM of nu-4 momenta
    produces<std::vector<reco::GenParticle> >("particleLevelNeutrinos").setBranchAlias("particleLevelNeutrinos");
    //    produces<std::vector<reco::NamedCompositeCandidate> >("particleLevelMET").setBranchAlias("particleLevelMET");
  }
  
  size_t nignored = ignoreParticleIDs.size();
  for (size_t ig = 0;  ig < nignored;++ig) {
    std::cout << "ignored# "<< ig <<":"<< ignoreParticleIDs.at(ig)<<std::endl;
  }
  
  size_t nexcluded = excludeFromResonancePids.size();
  for (size_t ig = 0;  ig < nexcluded;++ig) {
    std::cout << "ignored# "<< ig <<":"<< excludeFromResonancePids.at(ig)<<std::endl;
  }
}

void SingleTopParticleLevelMCProducer::produce(edm::Event & iEvent, const edm::EventSetup & iEventSetup){


  //edm::Handle<edm::View<reco::genParticle> > looseJets;
  //iEvent.getByLabel(looseJetsSrc_, looseJets);


  //#if DEBUG
  //  std::cout << "producer 1" << std::endl;
  //#endif


edm::Handle<std::vector<reco::GenParticle> > genParticles;
iEvent.getByLabel(genParticlesSrc_, genParticles);

edm::Handle<std::vector<reco::GenJet> > genJets;
iEvent.getByLabel(genJetsSrc_, genJets);

 //#if DEBUG
 //  std::cout << "producer 2" << std::endl;
 //#endif

  //  No particle level top defined yet
//  std::auto_ptr< std::vector< reco::NamedCompositeCandidate > > particleLevelTops( new std::vector<reco::NamedCompositeCandidate> );
  
  std::auto_ptr< std::vector< reco::GenParticle > > particleLevelLeptons( new std::vector<reco::GenParticle> );
  
  std::auto_ptr<reco::GenParticleRefVector> genLeptonsForDressing (new reco::GenParticleRefVector);

  std::auto_ptr<reco::GenParticleRefVector> genEGammaForDressing (new reco::GenParticleRefVector);
  std::auto_ptr<reco::GenParticleRefVector> genMuGammaForDressing (new reco::GenParticleRefVector);
  
  std::auto_ptr< std::vector< reco::GenJet > > particleLevelJets( new std::vector<reco::GenJet> );
  std::auto_ptr< std::vector< reco::GenJet > > particleLevelBJets( new std::vector<reco::GenJet> );
  

  std::auto_ptr<reco::GenParticleRefVector> genParticlesForJetsRescaledBHadronsNoDressLeptons(new reco::GenParticleRefVector);
  std::auto_ptr<reco::GenParticleRefVector> genParticlesForJetsNoRescaledBHadronsNoDressLeptons(new reco::GenParticleRefVector);

  std::auto_ptr<reco::GenParticleRefVector> genParticlesForJetsRescaledBHadrons(new reco::GenParticleRefVector);
  std::auto_ptr<reco::GenParticleRefVector> genParticlesForJetsNoRescaledBHadrons(new reco::GenParticleRefVector);

  std::auto_ptr< std::vector< reco::GenParticle > > particleLevelNeutrinos( new std::vector<reco::GenParticle> );
  //  std::auto_ptr< std::vector< reco::NamedCompositeCandidate > > particleLevelMET( new std::vector<reco::NamedCompositeCandidate> );
  
  
  
  //  int nDau =0;
  //  int dauOneId=-9999, dauTwoId =-9999, dauThreeId=-9999,dauFourId=-9999 ;
  
  //  int verbosity_= 0;

  using namespace std;
  using namespace edm;
  using namespace reco;
  
  std::map<const reco::GenParticle*,size_t> particlePtrIdxMap;
  ParticleVector particles,bHadParticles;

  for (reco::GenParticleCollection::const_iterator iter=genParticles->begin();iter!=genParticles->end();++iter){
    particles.push_back(&*iter);
    particlePtrIdxMap[&*iter] = (iter - genParticles->begin());
    
  }
  std::sort(particles.begin(), particles.end());
  unsigned int size = particles.size();
  ParticleBitmap invalidFromResonance(size,false);
  ParticleBitmap selectedForNeutrinos(size, false), invalidForNeutrinos(size, false);
  ParticleBitmap selectedForBJets(size, false), invalidForBJets(size, false);
  ParticleBitmap selectedForJets(size, false), invalidForJets(size, false);
  ParticleBitmap selectedForLeptons(size, false), invalidForLeptons(size, false);
  ParticleBitmap selectedForMuGamma(size, false), invalidForMuGamma(size, false);
  ParticleBitmap selectedForEGamma(size, false), invalidForEGamma(size, false);
  

    
  for(unsigned int i = 0; i < size; i++) {
    const reco::GenParticle *particle = particles[i];
    if (isBHadronRescaled(particle,particles))bHadParticles.push_back(particle);
  }


  for(unsigned int i = 0; i < size; i++) {
    const reco::GenParticle *particle = particles[i];
    int pdgid = particle->pdgId();

    bool selected = false; //bool invalid = false;
    
    selectedForMuGamma[i]= false; selectedForEGamma[i]= false; selectedForJets[i]= false; selectedForLeptons[i]= false;
    selectedForBJets[i]=false;
    invalidForMuGamma[i]= false; invalidForEGamma[i]= false; invalidForJets[i]= false; invalidForLeptons[i]= false;
    invalidForBJets[i]=false;
    
    //Basic selection of final state particles: not always good, e.g. rescaled b-hadrons have daughters.
    //if (particle->status() == 1 || particle->numberOfDaughters()==0 )
    //      selected = true;
    if (particle->status() == 1 ) selected = true;
    //    else invalid = true;
    
    bool isRescaledBHadron = isBHadronRescaled(particle,particles);
    bool isRescaledBHadronProduct = isBHadronRescaledDecayProduct(particle,particles,bHadParticles);
    ResonanceState rstate = isFromResonance(particle,particles,invalidFromResonance);
    bool fromHadron = isFromHadron(particle,particles);
    bool isnotfromresonance = (!rstate);
    
    /*    std::cout <<" parid "<< particle->pdgId() << " status "<< particle->status()<<std::endl;
    if(particle->status()==3){
      // std::cout << " status3? "<< particle->status()<<std::endl;
      if ((abs(pdgid)>10&& abs(pdgid)<17) || (abs(pdgid)==22)) { cout << "islhelepgamma id "<< pdgid << std::endl;
      }
      }*/
    //   bool isLeptonOrPhoton = (abs(pdgid)>10&& abs(pdgid)<17) || (abs(pdgid)==22);    if(selected) std::cout << " islepgamma " << isLeptonOrPhoton << " isresonance "<< !isnotfromresonance << " isfromhadron "<<fromHadron<< " id "<< pdgid <<endl;
    
    if(selected && !isnotfromresonance)invalidFromResonance[i]=true;
    
    //If comes from a rescaled b hadron: remove it from lepton list
    //    if(isRescaledBHadronProduct) invalid=true;
    
    //if is a prompt lepton
    if(selected && !fromHadron) {//Note: resonances do not include taus at this stage!
      //      std::cout<< "selected particle id "<< pdgid<< std::endl;
      //      if(!isnotfromresonance ){
      if(fabs(pdgid)==13 ) selectedForMuGamma[i]= true;
      if(fabs(pdgid)==11 ) selectedForEGamma[i]= true;
	//      }
      if(fabs(pdgid)==22 ) {selectedForMuGamma[i]= true;selectedForEGamma[i]= true;}
      selectedForLeptons[i]= selectedForMuGamma[i] || selectedForEGamma[i];
      
      if(fabs(pdgid)== 12 || fabs(pdgid)==14 || fabs(pdgid)==16){ selectedForNeutrinos[i]=true;
	//	std::cout << " neutrino found"<<std::endl;
      }
    }
    else{
      invalidForMuGamma[i]= true; invalidForEGamma[i]= true;
      invalidForLeptons[i]= true; invalidForNeutrinos[i]= true;
    }

	

    
    //if it's a prompt lepton it should not be in a jet
    if(selectedForLeptons[i]){ 
      invalidForJets[i] = true; 
      invalidForBJets[i] =true;
    }

   
    //   std::cout << pdgid<<" isignored? "<< isIgnored(pdgid)<< " is from resonance? "<< !isnotfromresonance <<std::endl;
    selected = selected && !(isIgnored(pdgid) && particle->pt()>=0);    

    //Jet selection: remove resonances
    if(fromHadron){// we need to  choose the ones that are not from hadrons. If you ask "! fro resonance" you'll get the leptons from taus
      if(selected) selectedForJets[i] = true;
      else invalidForJets[i] = true; 
    
      if (useJetsNoNu_){
	if(selected &&  (fabs(pdgid)== 12 || fabs(pdgid)==14 || fabs(pdgid)==16)){
	  selectedForJets[i] = false;
	  invalidForJets[i] = true;
	  selectedForNeutrinos[i]=true;
	  invalidForNeutrinos[i]=false;
	}
      }
      //bHadrons: adding rescaled hadron definition
      if((selected && !isRescaledBHadronProduct))selectedForBJets[i] = true;
      else if(isRescaledBHadron) selectedForBJets[i] = true;
      else invalidForBJets[i]= true;
      
    }
    else {
      invalidForJets[i] = true; 
      invalidForBJets[i] = true; 
    }
  }
  
  //Jet Collection Loop
  for(size_t idx = 0; idx < size; ++idx){   
    const reco::GenParticle *particle = particles[idx];
    if (!selectedForJets[idx] || invalidForJets[idx]){
      continue;
    }
    edm::Ref<reco::GenParticleCollection> particleRef(genParticles,particlePtrIdxMap[particle]);
    genParticlesForJetsNoRescaledBHadrons->push_back(particleRef);
   
  }

  for(size_t idx = 0; idx < size; ++idx){   
    const reco::GenParticle *particle = particles[idx];
    if (!selectedForBJets[idx] || invalidForBJets[idx]){
      continue;
    }
    edm::Ref<reco::GenParticleCollection> particleRef(genParticles,particlePtrIdxMap[particle]);
    genParticlesForJetsRescaledBHadrons->push_back(particleRef);
  }
  
  //Lepton Collection Loop
  for(size_t idx = 0; idx < size; ++idx){   
    const reco::GenParticle *particle = particles[idx];
    if (!selectedForLeptons[idx] || invalidForLeptons[idx]){
      continue;
    }
    edm::Ref<reco::GenParticleCollection> particleRef(genParticles,particlePtrIdxMap[particle]);
    genLeptonsForDressing->push_back(particleRef);
    particleLevelLeptons->push_back(*particle);
  }

  //Neutrino Collection Loop
  for(size_t idx = 0; idx < size; ++idx){   
    const reco::GenParticle *particle = particles[idx];
    if (!selectedForNeutrinos[idx] || invalidForNeutrinos[idx]){
      continue;
    }
    particleLevelNeutrinos->push_back(*particle);
  }

  //EGamma Collection Loop
  for(size_t idx = 0; idx < size; ++idx){   
    const reco::GenParticle *particle = particles[idx];
    if (!selectedForEGamma[idx] || invalidForEGamma[idx]){
      continue;
    }
    edm::Ref<reco::GenParticleCollection> particleRef(genParticles,particlePtrIdxMap[particle]);
    genEGammaForDressing->push_back(particleRef);
  }
  
  //MuGamma Collection Loop
  for(size_t idx = 0; idx < size; ++idx){   
    const reco::GenParticle *particle = particles[idx];
    if (!selectedForMuGamma[idx] || invalidForMuGamma[idx]){
      continue;
    }
    edm::Ref<reco::GenParticleCollection> particleRef(genParticles,particlePtrIdxMap[particle]);
    genMuGammaForDressing->push_back(particleRef);
  }
  
  for (reco::GenParticleCollection::const_iterator t = genParticles->begin (); t != genParticles->end (); ++t){
    ;    
  }
  if(doBDescendentJetSelection_){
    
    //    std::cout << "#genJets collection is "<<  genJets->size()<<std::endl;
    for (size_t j = 0; j < genJets->size();++j){
      std::vector<const reco::Candidate*> constituents = genJets->at(j).getJetConstituentsQuick();
      //      std::cout << "ak5GenJet #"<<j+1<<" #constituents is "<< constituents.size()<<std::endl;
      bool isBJet = false;
      for(size_t c = 0; c < constituents.size();++c){
	//	std::cout << "constituent #"<< c+1 << " pdgId "<< constituents.at(c)->pdgId() <<std::endl;
	
	const reco::GenParticle *particle = dynamic_cast <const reco::GenParticle*>(constituents.at(c));  
	bool isBHadronDP=isBHadronRescaledDecayProduct(particle,particles,bHadParticles);
	//     if(isBHadron(constituents.at(c)->pdgId()))isBJet = true;
	if(isBHadronDP)isBJet = true;
	
	//	std::cout << "is b hadron? "<< isBHadron(constituents.at(c)->pdgId())<< std::endl;
	//	std::cout << "has rescaled b-hadron product? "<< isBHadronDP <<std::endl;
      }
      if (isBJet)particleLevelBJets->push_back(genJets->at(j));
      particleLevelJets->push_back(genJets->at(j));
      //      std::cout << " is it a b jet? "<< isBJet<<std::endl;
    }
  }
  //cout<<"AT THE END"<<endl;
  // iEvent.put(particleLevelTops,"particleLevelTops");
  
 if(doBaseCollections_){
   iEvent.put(particleLevelLeptons,"particleLevelLeptons");
   iEvent.put(genParticlesForJetsNoRescaledBHadronsNoDressLeptons,"genParticlesForJetsNoRescaledBHadronsNoDressLeptons");
   iEvent.put(genParticlesForJetsRescaledBHadronsNoDressLeptons,"genParticlesForJetsRescaledBHadronsNoDressLeptons");
 }
 
 
 if(doDressedCollections_){
  iEvent.put(genLeptonsForDressing,"genLeptonsForDressing");
  iEvent.put(genEGammaForDressing,"genEGammaForDressing");
  iEvent.put(genMuGammaForDressing,"genMuGammaForDressing");
  iEvent.put(genParticlesForJetsRescaledBHadrons,"genParticlesForJetsRescaledBHadrons");
  iEvent.put(genParticlesForJetsNoRescaledBHadrons,"genParticlesForJetsNoRescaledBHadrons");
 }

 if(doBaseCollections_){
   iEvent.put(particleLevelNeutrinos,"particleLevelNeutrinos");
   //   iEvent.put(particleLevelMET, "particleLevelMET");
 }  
 if(doBDescendentJetSelection_){
   iEvent.put(particleLevelBJets,"particleLevelBJets");
   iEvent.put(particleLevelJets,"particleLevelJets");
 }
 
}


SingleTopParticleLevelMCProducer::ResonanceState SingleTopParticleLevelMCProducer::isFromResonance( const reco::GenParticle * particle, const ParticleVector &allParticles, ParticleBitmap &invalid){

  unsigned int partIdx(const SingleTopParticleLevelMCProducer::ParticleVector &p,
			      const reco::GenParticle *particle);

  int id = particle->pdgId();
  unsigned int idx = partIdx(allParticles, particle);
  //  std::cout << " id is "<< id <<std::endl;
  
  if (isResonance(id) && (particle->status() == 3 || particle->status() == 22) ){  
    //    std::cout << " id "<< id <<" is direct resonance "<<std::endl; 
    return kDirect;
  }
  if (invalid[idx]) return kIndirect;
  
  if(!isIgnored(id) && isParton(id)) {
    //    std::cout << " isignored or isparton kNo "<<std::endl;
    return kNo;
  }  
  unsigned int nMo=particle->numberOfMothers();
  if (!nMo)
    {//  std::cout << " has no mom kNo "<<std::endl;

      return kNo;
    }
  for(unsigned int i=0;i<nMo;++i){
    bool result = isFromResonance(dynamic_cast<const reco::GenParticle*>(particle->mother(i)),allParticles,invalid);
    switch(result){
    case kNo: 
      //      std::cout << " mother " <<i <<"is kNo "<<std::endl;
      break;
    case kDirect:
      if (dynamic_cast<const reco::GenParticle*>(particle->mother(i))->pdgId()==id || isResonance(id))
	{
	  //  std::cout << " mother "<< i << " id "<< dynamic_cast<const reco::GenParticle*>(particle->mother(i))->pdgId() <<" is resonance " <<std::endl;
	  return kDirect;
	}
      if(!isExcludedFromResonance(id))break;
    case kIndirect: 
      return kIndirect;
    }
    
  }
  //  std::cout << "reached end kNo "<<std::endl;
  return kNo;
}

bool SingleTopParticleLevelMCProducer::isParton(int pdgId)
{
  pdgId = (pdgId > 0 ? pdgId : -pdgId) % 10000;
  return (pdgId > 0 && pdgId < 6) ||
    pdgId == 9 || pdgId == 21;
  // tops are not considered "regular" partons
  // but taus eventually are (since they may hadronize later)
   
}
bool SingleTopParticleLevelMCProducer::isIgnored(int pdgId)
{
  
  pdgId = pdgId > 0 ? pdgId : -pdgId;
  std::vector<unsigned int>::const_iterator pos =
    std::lower_bound(ignoreParticleIDs.begin(),
		     ignoreParticleIDs.end(),
		     (unsigned int)pdgId);
  return pos != ignoreParticleIDs.end() && *pos == (unsigned int)pdgId;
  
}

bool SingleTopParticleLevelMCProducer::isExcludedFromResonance(int pdgId)
{
  pdgId = pdgId > 0 ? pdgId : -pdgId;
  std::vector<unsigned int>::const_iterator pos =
    std::lower_bound(excludeFromResonancePids.begin(),
		     excludeFromResonancePids.end(),
		     (unsigned int)pdgId);
  return pos != excludeFromResonancePids.end() && *pos == (unsigned int)pdgId;
  
}

unsigned int partIdx(const SingleTopParticleLevelMCProducer::ParticleVector &p,
			    const reco::GenParticle *particle){
  SingleTopParticleLevelMCProducer::ParticleVector::const_iterator pos =
    std::lower_bound(p.begin(), p.end(), particle);
  if (pos == p.end() || *pos != particle)
    throw cms::Exception("CorruptedData")
      << "reco::GenEvent corrupted: Unlisted particles"
      " in decay tree." << std::endl;
  
  return pos - p.begin();
}

bool SingleTopParticleLevelMCProducer::isResonance(int pdgId)
{
  // gauge bosons and tops
  pdgId = (pdgId > 0 ? pdgId : -pdgId) % 10000;
  return (pdgId > 21 && pdgId <= 42) || pdgId == 6 || pdgId == 7 || pdgId == 8 ;  //BUG! was 21. 22=gamma..
}

bool SingleTopParticleLevelMCProducer::isPromptLepton( const reco::GenParticle * particle, const ParticleVector &allParticles){
  return true;
}

bool SingleTopParticleLevelMCProducer::isBHadronRescaled( const reco::GenParticle * particle, const ParticleVector &allParticles){

  if(isBHadron(particle->pdgId())){
    size_t ndaughters = particle->numberOfDaughters();
    bool hasBHadronDaughters = false;
    //    std::cout<< " inside b rescaled func, particle id "<< particle->pdgId() << " pt "<< particle->pt()<< " daughters "<< ndaughters<<std::endl;
    for (size_t d = 0; d < ndaughters;++d ){
      //#if DEBUG
      //std::cout<< " daughterd "<< d << " id "<< particle->daughter(d)->pdgId()<<std::endl; 
      //#endif
    if(isBHadron(particle->daughter(d)->pdgId())) hasBHadronDaughters = true;
    }
    if(!hasBHadronDaughters && particle->pt()>5.0){
      //#if DEBUG
      //      std::cout << " is rescaled b "<<std::endl;
      //#endif
      return true;
    }
  }
  return false;
}

bool SingleTopParticleLevelMCProducer::isHadron( int pdgId ){
  pdgId = (pdgId > 0 ? pdgId : -pdgId) % 10000;
  return (pdgId > 100 && pdgId < 900) || (pdgId > 1000 && pdgId < 9000);
}

bool SingleTopParticleLevelMCProducer::isFromHadron( const reco::GenParticle * particle, const ParticleVector &allParticles){
  bool result = false;
  int pdgid = particle->pdgId();
  size_t nmothers = particle->numberOfMothers();
  result = isHadron(pdgid)|| isParton(pdgid);
  //  std::cout<< "id "<< pdgid << " nmothers "<< nmothers << " result "<<result<<std::endl;
  
  if(result) return true;
  for (size_t m = 0; m < nmothers;++m ){
    int motherid =  dynamic_cast<const reco::GenParticle*>(particle->mother(m))->pdgId();
    //    std::cout<< " mother m " << m << " id "<< motherid<<std::endl;
    //    if(motherid ==24)std::cout << " mother status " << dynamic_cast<const reco::GenParticle*>(particle->mother(m))->status()<< " mother from had? " << isFromHadron(dynamic_cast<const reco::GenParticle*>(particle->mother(m)), allParticles)<<std::endl;
    if( isHadron (motherid)|| isParton(motherid)) { result = true; break;}
    
    if( (motherid == pdgid) || (abs(motherid)==15)){//Hadrons in taus are also considered
      

      result = result || isFromHadron(dynamic_cast<const reco::GenParticle*>(particle->mother(m)), allParticles);
    }
  }
  return result;
}


bool SingleTopParticleLevelMCProducer::isBHadronRescaledDecayProduct( const reco::GenParticle * particle, const ParticleVector &allParticles, const ParticleVector &rescaledBHadrons){
  bool result = false;
  size_t nrescaled = rescaledBHadrons.size();
  size_t nmothers = particle->numberOfMothers();
#if DEBUG
  std::cout<< " inside b rescaled product func, particle id "<< particle->pdgId() << " pt "<< particle->pt()<< " nmothers " << nmothers << std::endl; 
#endif
  for(size_t r=0;r<nrescaled;++r){
    if( rescaledBHadrons.at(r)==particle) return true;
  } 
  
  for (size_t m = 0; m < nmothers;++m ){
#if DEBUG
    std::cout<< " mother m " << m << std::endl;
#endif
    result = result || isBHadronRescaledDecayProduct(dynamic_cast <const reco::GenParticle*>(particle->mother(m)), allParticles, rescaledBHadrons);
    if(result) return result;
  }
  
  return result;
}

bool SingleTopParticleLevelMCProducer::isBHadron(int pdgid){
  //Bottom mesons
  if (fabs(pdgid)==511) return true;
  if (fabs(pdgid)==521) return true;
  if (fabs(pdgid)==10511) return true;
  if (fabs(pdgid)==10521) return true;


  if (fabs(pdgid)==513) return true;
  if (fabs(pdgid)==523) return true;
  if (fabs(pdgid)==20513) return true;
  if (fabs(pdgid)==20523) return true;


  if (fabs(pdgid)==515) return true;
  if (fabs(pdgid)==525) return true;

  if (fabs(pdgid)==531) return true;
  if (fabs(pdgid)==10531) return true;

  if (fabs(pdgid)==533) return true;
  if (fabs(pdgid)==10533) return true;
  if (fabs(pdgid)==20533) return true;

  if (fabs(pdgid)==535) return true;

  if (fabs(pdgid)==541) return true;
  if (fabs(pdgid)==10541) return true;

  if (fabs(pdgid)==543) return true;
  if (fabs(pdgid)==10543) return true;
  if (fabs(pdgid)==20543) return true;

  if (fabs(pdgid)==545) return true;

  //BBbar mesons

  if (fabs(pdgid)==551) return true;
  if (fabs(pdgid)==10551) return true;
  if (fabs(pdgid)==100551) return true;
  if (fabs(pdgid)==110551) return true;
  if (fabs(pdgid)==200551) return true;
  if (fabs(pdgid)==210551) return true;


  if (fabs(pdgid)==553) return true;
  if (fabs(pdgid)==10553) return true;

  if (fabs(pdgid)==553) return true;
  if (fabs(pdgid)==10553) return true;
  if (fabs(pdgid)==20553) return true;
  if (fabs(pdgid)==30553) return true;

  if (fabs(pdgid)==100553) return true;
  if (fabs(pdgid)==110553) return true;
  if (fabs(pdgid)==120553) return true;
  if (fabs(pdgid)==130553) return true;

  if (fabs(pdgid)==200553) return true;
  if (fabs(pdgid)==210553) return true;
  if (fabs(pdgid)==220553) return true;

  if (fabs(pdgid)==300553) return true;

  if (fabs(pdgid)==9000553) return true;
  if (fabs(pdgid)==9010553) return true;

  if (fabs(pdgid)==555) return true;
  if (fabs(pdgid)==10555) return true;
  if (fabs(pdgid)==20555) return true;
  if (fabs(pdgid)==100555) return true;
  if (fabs(pdgid)==110555) return true;
  if (fabs(pdgid)==120555) return true;
  if (fabs(pdgid)==200555) return true;

  if (fabs(pdgid)==557) return true;
  if (fabs(pdgid)==10557) return true;

  //Bottom baryons
  
  if (fabs(pdgid)==5122) return true;
  if (fabs(pdgid)==5112) return true;
  if (fabs(pdgid)==5212) return true;
  if (fabs(pdgid)==5222) return true;
  if (fabs(pdgid)==5114) return true;
  if (fabs(pdgid)==5214) return true;
  if (fabs(pdgid)==5224) return true;
  if (fabs(pdgid)==5132) return true;
  if (fabs(pdgid)==5232) return true;
  

  if (fabs(pdgid)==5312) return true;
  if (fabs(pdgid)==5322) return true;
  if (fabs(pdgid)==5314) return true;
  if (fabs(pdgid)==5324) return true;
  if (fabs(pdgid)==5332) return true;
  if (fabs(pdgid)==5334) return true;
  
  if (fabs(pdgid)==5142) return true;
  if (fabs(pdgid)==5242) return true;
  if (fabs(pdgid)==5412) return true;
  if (fabs(pdgid)==5422) return true;
  if (fabs(pdgid)==5414) return true;
  if (fabs(pdgid)==5424) return true;
  if (fabs(pdgid)==5342) return true;
  if (fabs(pdgid)==5432) return true;
  if (fabs(pdgid)==5434) return true;
  if (fabs(pdgid)==5442) return true;
  if (fabs(pdgid)==5444) return true;

  if (fabs(pdgid)==5512) return true;
  if (fabs(pdgid)==5522) return true;
  if (fabs(pdgid)==5514) return true;
  if (fabs(pdgid)==5524) return true;
  if (fabs(pdgid)==5532) return true;
  if (fabs(pdgid)==5534) return true;
  if (fabs(pdgid)==5542) return true;
  if (fabs(pdgid)==5544) return true;
  if (fabs(pdgid)==5554) return true;
  
  return false;
;}

void SingleTopParticleLevelMCProducer::setIgnoredParticles(const std::vector<unsigned int> &particleIDs){
  ignoreParticleIDs = particleIDs;
  std::sort(ignoreParticleIDs.begin(), ignoreParticleIDs.end());
   }
 
void SingleTopParticleLevelMCProducer::setExcludeFromResonancePids(const std::vector<unsigned int> &particleIDs)
 {
      excludeFromResonancePids = particleIDs;
      std::sort( excludeFromResonancePids.begin(), excludeFromResonancePids.end());
       }

bool SingleTopParticleLevelMCProducer::isRadiation(int status){
  return false;
;}

bool SingleTopParticleLevelMCProducer::isFinalStateParticle(int pdgid){
  return false;
;}

SingleTopParticleLevelMCProducer::~SingleTopParticleLevelMCProducer(){;}

DEFINE_FWK_MODULE( SingleTopParticleLevelMCProducer );

//  LocalWords:  MCtopsQuarkBar
