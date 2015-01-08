/*
 *\Authors: A. Orso M. Iorio 
 *
 *
 *\version  $Id: SingleTopFiducialCrossSectionProducer.cc,v 1.1.2.2 2013/06/21 20:40:25 oiorio Exp $ 
 */

// Calculates the particle-level efficiency of a given set of cuts on the dataset.


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
#include "TopQuarkAnalysis/SingleTop/interface/SingleTopFiducialCrossSectionProducer.h"
#include "DataFormats/Candidate/interface/NamedCompositeCandidate.h"
#include "DataFormats/Candidate/interface/Candidate.h"
//#include "TLorentzVector.h"
#include "TopQuarkAnalysis/SingleTop/interface/EquationSolver.h"

#include <vector>
#include <memory>


//using namespace pat;

SingleTopFiducialCrossSectionProducer::SingleTopFiducialCrossSectionProducer(const edm::ParameterSet& iConfig){
  //Get the collection tags:
  genBareLeptonsSrc_ = iConfig.getParameter<edm::InputTag>( "genBareLeptonsSource" );
  genDressedLeptonsSrc_ = iConfig.getParameter<edm::InputTag>( "genDressedLeptonsSource" );
  genJetsSrc_ = iConfig.getParameter<edm::InputTag>( "genJetsSource" );
  genBJetsSrc_ = iConfig.getParameter<edm::InputTag>( "genBJetsSource" );
  genNeutrinosSrc_ = iConfig.getParameter<edm::InputTag>( "genNeutrinosSource" );
  lheSrc_ = iConfig.getParameter<edm::InputTag>( "lheSource" );

  //Add the selected objects collections?
  addOutputCollections_ = iConfig.getUntrackedParameter<bool>("addOutputCollections",true);
  
  //Initialize cross section and number of events:
  //Note: if kept negative will give just the observed efficiency
  TotalEvents_ = iConfig.getUntrackedParameter<int>("TotalEvents",-1);
  TotalCrossSection_ = iConfig.getUntrackedParameter<double>("TotalCrossSection",-1);

  
  //Cuts details
  //Note: wherever -1 (or an unphysical negative number) is present, it means the cut is not applied.
  //Use only muons/electrons for the main selection
  leptonChannel_ = iConfig.getUntrackedParameter<std::string>("leptonChannel","all");
  
  //Mininmum pt of leptons:
  minLeptonPt_ = iConfig.getUntrackedParameter<double>( "minLeptonPt", 26.0 ); 
  maxLeptonEta_ = iConfig.getUntrackedParameter<double>( "maxLeptonEta", 2.5 ); 

  //Number of leptons to choose
  minLeptons_ = iConfig.getUntrackedParameter<int>( "minLeptons", 1 );
  maxLeptons_ = iConfig.getUntrackedParameter<int>( "maxLeptons", 1 );
  vetoDifferentFlavorLeptons_ = iConfig.getUntrackedParameter<bool>("vetoDifferentFlavorLeptons",true);
  useDressedLeptons_ = iConfig.getUntrackedParameter<bool>("useDressedLeptons",true);

  //Mininmum pt of jets:
  minJetPt_ = iConfig.getUntrackedParameter<double>( "minJetPt", 40.0 ); 

  maxJetEta_ = iConfig.getUntrackedParameter<double>( "maxJetEta", 5.0 ); 
  maxBJetEta_ = iConfig.getUntrackedParameter<double>( "maxBJetEta", 2.6 ); 
  
  //Number of Jets / b-jets:

  minJets_ = iConfig.getUntrackedParameter<int>( "minJets", 2 ); 
  maxJets_ = iConfig.getUntrackedParameter<int>( "maxJets", 2 );
  
  minBJets_ = iConfig.getUntrackedParameter<int>( "minBJets", 1 );
  maxBJets_ = iConfig.getUntrackedParameter<int>( "maxBJets", 1 );

  //Met or W transverse mass cut
  metCut_ = iConfig.getUntrackedParameter<double>( "metCut", -1 );
  mtwCut_ = iConfig.getUntrackedParameter<double>( "mtwCut", -1 );

  //Add a DR cut
  leptonJetDeltaRCut_ = iConfig.getUntrackedParameter<double>( "deltaRCut", -1 );
  
  //Output calculation:
  produces< bool >("isFiducialEvent").setBranchAlias("isFiducialEvent");

 
  if(addOutputCollections_){
    produces< double >("selectedParticleLevelMetPt").setBranchAlias("selectedParticleLevelMetPt");
    produces< double >("selectedParticleLevelMetPhi").setBranchAlias("selectedParticleLevelMetPhi");
    produces< double >("selectedParticleLevelMetPx").setBranchAlias("selectedParticleLevelMetPx");
    produces< double >("selectedParticleLevelMetPy").setBranchAlias("selectedParticleLevelMetPy");

    produces< double >("selectedParticleLevelMTW").setBranchAlias("selectedParticleLevelMTW");

    produces< int >("selectedParticleLevelNJets").setBranchAlias("selectedParticleLevelNJets");
    produces< int >("selectedParticleLevelNBJets").setBranchAlias("selectedParticleLevelNBJets");
    produces< int >("selectedParticleLevelNLeptons").setBranchAlias("selectedParticleLevelNLeptons");
    produces< int >("selectedParticleLevelNAllLeptons").setBranchAlias("selectedParticleLevelNAllLeptons");
    

    //Selection of genJets, using the "b-descendent" definition:
    produces<std::vector<reco::GenJet > >("selectedParticleLevelJets").setBranchAlias("selectedParticleLevelJets");
    produces<std::vector<reco::GenJet > >("selectedParticleLevelBJets").setBranchAlias("selectedParticleLevelBJets");

    if(useDressedLeptons_){
      produces<std::vector<reco::GenJet > >("selectedParticleLevelDressedLeptons").setBranchAlias("selectedParticleLevelDressedLeptons");
      produces<std::vector<reco::GenJet > >("selectedParticleLevelAllDressedLeptons").setBranchAlias("selectedParticleLevelAllDressedLeptons");
      produces<std::vector<reco::GenJet > >("selectedParticleLevelAllDressedLeptonsAndPhotons").setBranchAlias("selectedParticleLevelAllDressedLeptonsAndPhotons");
    }
    else{
      produces<std::vector<reco::GenParticle > >("selectedParticleLevelBareLeptons").setBranchAlias("selectedParticleLevelBareLeptons");
      produces<std::vector<reco::GenParticle > >("selectedParticleLevelAllBareLeptons").setBranchAlias("selectedParticleLevelAllBareLeptons");
      produces<std::vector<reco::GenParticle > >("selectedParticleLevelAllBareLeptonsAndPhotons").setBranchAlias("selectedParticleLevelAllBareLeptonsAndPhotons");
    }
  }
  
  PreCutEventCounter_=0;PostCutEventCounter_=0;// Those two start from zero
}

void SingleTopFiducialCrossSectionProducer::produce(edm::Event & iEvent, const edm::EventSetup & iEventSetup){

  //  double fidAcc,fidDSigma;
  bool isFid;
  
  std::auto_ptr< std::vector< reco::GenJet > > selectedParticleLevelJets( new std::vector<reco::GenJet> );
  std::auto_ptr< std::vector< reco::GenJet > > selectedParticleLevelBJets( new std::vector<reco::GenJet> );

  std::auto_ptr< std::vector< reco::GenParticle > > selectedParticleLevelBareLeptons( new std::vector<reco::GenParticle> );
  std::auto_ptr< std::vector< reco::GenParticle > > selectedParticleLevelAllBareLeptons( new std::vector<reco::GenParticle> );
  std::auto_ptr< std::vector< reco::GenParticle > > selectedParticleLevelAllBareLeptonsAndPhotons( new std::vector<reco::GenParticle> );

  std::auto_ptr< std::vector< reco::GenJet > > selectedParticleLevelDressedLeptons( new std::vector<reco::GenJet> );
  std::auto_ptr< std::vector< reco::GenJet > > selectedParticleLevelAllDressedLeptons( new std::vector<reco::GenJet> );
  std::auto_ptr< std::vector< reco::GenJet > > selectedParticleLevelAllDressedLeptonsAndPhotons( new std::vector<reco::GenJet> );

  
  ++PreCutEventCounter_;

  edm::Handle<std::vector<reco::GenParticle> > genBareLeptons,genNeutrinos;
  iEvent.getByLabel(genBareLeptonsSrc_, genBareLeptons);
  iEvent.getByLabel(genNeutrinosSrc_, genNeutrinos);
  
  edm::Handle<std::vector<reco::GenJet> > genJets,genBJets,genDressedLeptons;
  iEvent.getByLabel(genJetsSrc_, genJets);
  iEvent.getByLabel(genBJetsSrc_, genBJets);
  iEvent.getByLabel(genDressedLeptonsSrc_, genDressedLeptons);
  
  //  int nMuons,nElectrons;
  //  double leptonPt;
  int leptonIdToSelect= -1;
  if(leptonChannel_=="all"){
    leptonIdToSelect = -1;}
  if(leptonChannel_=="muon"){
    leptonIdToSelect = 13;}
  if(leptonChannel_=="electron"){
    leptonIdToSelect = 11;}

  selectedLeptons.clear();
  allNeutrinos.clear();
  allLeptons.clear();
  selectedJets.clear();
  selectedBJets.clear();
  
  math::PtEtaPhiELorentzVector met;
  //  std::cout << "starting met pt "<< met.pt()<<std::endl;
  for (size_t l = 0; l< genNeutrinos->size();++l){
    math::PtEtaPhiELorentzVector vec(genNeutrinos->at(l).pt(), genNeutrinos->at(l).eta(), genNeutrinos->at(l).phi(), genNeutrinos->at(l).energy());
    met = met + vec;
    //    std::cout << "neutrino # "<< l << " pt "<< vec.pt() << " px "<< vec.px() << " py "<< vec.py()<< " met now is " <<  met.pt()<<std::endl;
  }
  double metPt = met.pt();
  double metPy = met.py();
  double metPx = met.px();
  double metPhi = met.phi();
  if(useDressedLeptons_){
    for (size_t l = 0; l< genDressedLeptons->size();++l){
      double leptonPt = genDressedLeptons->at(l).pt();
      double leptonEta = fabs(genDressedLeptons->at(l).eta());
      
      int mainComponentId=0;
      std::vector<const reco::Candidate*> constituents = genDressedLeptons->at(l).getJetConstituentsQuick();
      //      std::cout << "lepton #"<<l<<" #constituents is "<< constituents.size()<< " pt is "<< leptonPt<<std::endl;
      double maxPt=0.;
      for(size_t c = 0; c < constituents.size();++c){
	double ptcomp = constituents.at(c)->pt();
	int cid = constituents.at(c)->pdgId();
	if(ptcomp >maxPt){
	  maxPt = ptcomp;
	}
	if((cid!=22 && mainComponentId == 22) || (mainComponentId==0)) mainComponentId = cid;
	
	//	std::cout << "component # "<<c<<" id is "<< constituents.at(c)->pdgId() <<" pt is "<< ptcomp<< " eta " << constituents.at(c)->eta()<< " phi "<< constituents.at(c)->phi()<<" maxpt is "<<maxPt<<std::endl;
	
      }
      //Selection part:
      //      std::cout << "lepton flavor is "<< mainComponentId<<std::endl;
      if(leptonPt< minLeptonPt_)continue;
      if(leptonEta> maxLeptonEta_)continue;
      if(addOutputCollections_)selectedParticleLevelAllDressedLeptonsAndPhotons->push_back(genDressedLeptons->at(l));
      if(mainComponentId==22)continue;
      
      math::PtEtaPhiELorentzVector vec(genDressedLeptons->at(l).pt(), genDressedLeptons->at(l).eta(), genDressedLeptons->at(l).phi(), genDressedLeptons->at(l).energy());
      
      if((abs(mainComponentId) == leptonIdToSelect) || (leptonIdToSelect<0)){
	selectedLeptons.push_back(vec);
	if(addOutputCollections_)selectedParticleLevelDressedLeptons->push_back(genDressedLeptons->at(l));
      }
      allLeptons.push_back(vec);
      if(addOutputCollections_)selectedParticleLevelAllDressedLeptons->push_back(genDressedLeptons->at(l));
    }
  }
  if(!useDressedLeptons_){
    for (size_t l = 0; l< genBareLeptons->size();++l){
      double leptonPt = genBareLeptons->at(l).pt();
      double leptonEta = fabs(genBareLeptons->at(l).eta());

      int mainComponentId=genBareLeptons->at(l).pdgId();
     
      //Selection part:
      if(leptonPt< minLeptonPt_)continue;
      if(leptonEta> maxLeptonEta_)continue;
      if(addOutputCollections_)selectedParticleLevelAllBareLeptonsAndPhotons->push_back(genBareLeptons->at(l));
      if(mainComponentId==22)continue;
      
      math::PtEtaPhiELorentzVector vec(genBareLeptons->at(l).pt(), genBareLeptons->at(l).eta(), genBareLeptons->at(l).phi(), genBareLeptons->at(l).energy());
      
      if((abs(mainComponentId) == leptonIdToSelect) || (leptonIdToSelect<0)){
	selectedLeptons.push_back(vec);
	if(addOutputCollections_)selectedParticleLevelBareLeptons->push_back(genBareLeptons->at(l));
      }
      allLeptons.push_back(vec);
      if(addOutputCollections_)selectedParticleLevelAllBareLeptons->push_back(genBareLeptons->at(l));
    }
    
  }

  double mtW=0;
  double maxLepPt=-1;
  for (size_t l = 0; l< selectedLeptons.size();++l){
    if(selectedLeptons.at(l).pt()>maxLepPt){
      maxLepPt = selectedLeptons.at(l).pt();
      mtW = mtw(selectedLeptons.at(l),met);
    }
  }
 
  for (size_t j = 0; j< genJets->size();++j){
    double jetPt = genJets->at(j).pt();
    double jetEta = fabs(genJets->at(j).eta());
    if(jetPt< minJetPt_)continue;
    if(jetEta > maxJetEta_)continue;
    math::PtEtaPhiELorentzVector vec(genJets->at(j).pt(), genJets->at(j).eta(), genJets->at(j).phi(), genJets->at(j).energy());
    selectedJets.push_back(vec);
    if(addOutputCollections_)selectedParticleLevelJets->push_back(genJets->at(j));
  }

  for (size_t j = 0; j< genBJets->size();++j){
    double jetPt = genBJets->at(j).pt();
    double jetEta = fabs(genBJets->at(j).eta());
    if(jetPt< minJetPt_)continue;
    if(jetEta > maxBJetEta_)continue;
    math::PtEtaPhiELorentzVector vec(genBJets->at(j).pt(), genBJets->at(j).eta(), genBJets->at(j).phi(), genBJets->at(j).energy());
    selectedBJets.push_back(vec);
    if(addOutputCollections_)selectedParticleLevelBJets->push_back(genBJets->at(j));
  }
  

  bool leptonsPass = countLeptons((int)selectedLeptons.size(),(int)allLeptons.size(),minLeptons_,maxLeptons_);
  bool jetsPass= countJets((int)selectedJets.size(),minJets_,maxJets_);
  bool bjetsPass= countJets((int)selectedBJets.size(),minBJets_,maxBJets_);
  
  bool metPass= (metPt> metCut_) || (metCut_<0);
  bool mtwPass= (mtW> mtwCut_) || (mtwCut_<0);
  bool eventPass = leptonsPass&& jetsPass && bjetsPass && metPass && mtwPass;
  
  // std::cout << " nleptons = " << selectedLeptons.size() << " njets = "<< selectedJets.size()<< " nbjets = " << selectedBJets.size()<< " met = " << metPt << " mtw = "<< mtW<< " pass? "<< eventPass <<std::endl;
  
  //  fidAcc= 1.0;
  //  fidDSigma = fidAcc*TotalCrossSection_;
  isFid= eventPass;
  
  //  std::cout << "fidAcc "<< fidAcc<< " fidDSigma " << fidDSigma << " isFid "<< isFid<<std::endl;

  //  std::auto_ptr< double > fiducialAcceptance( new double(fidAcc) );
  //  std::auto_ptr< double > fiducialDSigma( new double(fidDSigma) );
  std::auto_ptr< bool > isFiducialEvent( new bool(isFid) );

  std::auto_ptr< int > nl( new int((int)selectedLeptons.size()) ), nal(new int((int)allLeptons.size())), 
    nj(new int((int)selectedJets.size())),nbj(new int((int)selectedBJets.size()));
  
  std::auto_ptr< double > genMetPt( new double(metPt) ), genMetPhi( new double(metPhi) ), genMetPx(new double(metPx)), genMetPy(new double(metPy)), genMTW (new double(mtW));
  
  
  //  std::cout << " isFid point "<< *isFiducialEvent <<std::endl;
  
  //  iEvent.put(fiducialAcceptance,"fiducialAcceptance");
  //  iEvent.put(fiducialDSigma,"fiducialDSigma");
  iEvent.put(isFiducialEvent,"isFiducialEvent");

  
  if(addOutputCollections_){
    iEvent.put(genMetPt,"selectedParticleLevelMetPt");
    iEvent.put(genMetPx,"selectedParticleLevelMetPx");
    iEvent.put(genMetPy,"selectedParticleLevelMetPy");
    iEvent.put(genMetPhi,"selectedParticleLevelMetPhi");

    iEvent.put(genMTW,"selectedParticleLevelMTW");


    iEvent.put(nl,"selectedParticleLevelNLeptons");
    iEvent.put(nal,"selectedParticleLevelNAllLeptons");
    iEvent.put(nj,"selectedParticleLevelNJets");
    iEvent.put(nbj,"selectedParticleLevelNBJets");

    iEvent.put(selectedParticleLevelJets,"selectedParticleLevelJets");
    iEvent.put(selectedParticleLevelBJets,"selectedParticleLevelBJets");

    if(useDressedLeptons_){
      iEvent.put(selectedParticleLevelAllDressedLeptonsAndPhotons,"selectedParticleLevelAllDressedLeptonsAndPhotons");
      iEvent.put(selectedParticleLevelAllDressedLeptons,"selectedParticleLevelAllDressedLeptons");
      iEvent.put(selectedParticleLevelDressedLeptons,"selectedParticleLevelDressedLeptons");
    }
    else{
      iEvent.put(selectedParticleLevelAllBareLeptonsAndPhotons,"selectedParticleLevelAllBareLeptonsAndPhotons");
      iEvent.put(selectedParticleLevelAllBareLeptons,"selectedParticleLevelAllBareLeptons");
      iEvent.put(selectedParticleLevelBareLeptons,"selectedParticleLevelBareLeptons");
    }
  }
}

bool SingleTopFiducialCrossSectionProducer::countLeptons( int selectedLeptons, int totalLeptons, int min, int max){
  bool leptonsPass = false;
  leptonsPass= (selectedLeptons >= minLeptons_) && ((selectedLeptons<=max)|| (max<0));
  if(vetoDifferentFlavorLeptons_) leptonsPass= (selectedLeptons >= minLeptons_) && ((totalLeptons<=max) || (max <0));//If I have to veto extra leptons, I ask that there is at least 1 lepton of the right flavor and at most 1 of the right or wrong flavor.
  return leptonsPass;
}

bool SingleTopFiducialCrossSectionProducer::countJets(int selectedJets, int min, int max){
  return (selectedJets >= min) && ( (selectedJets<=max) || (max<0));
}



double SingleTopFiducialCrossSectionProducer::mtw(math::PtEtaPhiELorentzVector lepton,math::PtEtaPhiELorentzVector met){
  return sqrt((lepton.pt() + met.pt()) * (lepton.pt() + met.pt())  - (lepton.px() + met.px()) * (lepton.px() + met.px()) - (lepton.py() + met.py()) * (lepton.py() + met.py())); }

SingleTopFiducialCrossSectionProducer::~SingleTopFiducialCrossSectionProducer(){;}

DEFINE_FWK_MODULE( SingleTopFiducialCrossSectionProducer );

