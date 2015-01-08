#ifndef Single_Top_TChannel_Particle_Level_Producer_h
#define Single_Top_TChannel_Particle_Level_Producer_h

/* \Class SingleTopParticleLevelMCProducer
 *
 * \Authors: A. Orso M. Iorio
 * 
 * \ version $Id: SingleTopParticleLevelMCProducer.h,v 1.1.2.2 2013/06/21 20:40:24 oiorio Exp $
 */

//Single Top MC Producer
// Original 
// Adapted by O.Iorio

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include <FWCore/Framework/interface/Run.h>

#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/TriggerResults.h"
#include "FWCore/Framework/interface/TriggerNamesService.h"
#include "FWCore/ServiceRegistry/interface/Service.h" 


#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
//#include "FWCore/ParameterSet/interface/InputTag.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/View.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

#include "DataFormats/PatCandidates/interface/UserData.h"
#include "PhysicsTools/PatAlgos/interface/PATUserDataHelper.h"


#include "DataFormats/PatCandidates/interface/Lepton.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/PATObject.h"

#include "DataFormats/Candidate/interface/NamedCompositeCandidate.h"



//class JetFlavourIdentifier;



  class SingleTopParticleLevelMCProducer : public edm::EDProducer {

    public:


    typedef std::vector<bool>     ParticleBitmap;
    typedef std::vector<const reco::GenParticle*> ParticleVector;
        
    explicit SingleTopParticleLevelMCProducer(const edm::ParameterSet & iConfig);
    ~SingleTopParticleLevelMCProducer();
    virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);

    enum ResonanceState {
           kNo = 0,
           kDirect =1,
	   kIndirect = 2
    };

    bool isFinalStateParticle(int status);
    bool isRadiation(int status);

    bool isPromptLepton( const reco::GenParticle * particle, const ParticleVector &allParticles);
    bool isParton(int pdgid);

    bool isIgnored(int pdgid);
    bool isExcludedFromResonance(int pdgid);

    bool isHadron(int pdgid);
    bool isFromHadron(const reco::GenParticle * particle, const ParticleVector &allParticles);
   
    bool isResonance(int pdgid);
    ResonanceState isFromResonance( const reco::GenParticle * particle, const ParticleVector &allParticles, ParticleBitmap &map);
    
    bool isBHadron(int pdgid);
    bool isBHadronRescaled( const reco::GenParticle * particle, const ParticleVector &allParticles);
    bool isBHadronRescaledDecayProduct( const reco::GenParticle * particle, const ParticleVector &allParticles, const ParticleVector &rescaledBHadrons);
    
    //       static void fillDescriptions(edm::ConfigurationDescriptions & descriptions);

    void setExcludeFromResonancePids(const std::vector<unsigned int> &particleIDs);
    void setIgnoredParticles(const std::vector<unsigned int> &particleIDs);
    

  private:

    //InputTags
    edm::InputTag genParticlesSrc_,genJetsSrc_; 
    std::string hadronizer_, channel_;
    std::vector<unsigned int> ignoreParticleIDs;
    std::vector<unsigned int> excludeFromResonancePids;    
    bool doDressedCollections_,doBaseCollections_,doBDescendentJetSelection_, useJetsNoNu_;

  };



#endif
