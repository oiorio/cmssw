#ifndef Single_Top_Fiducial_h
#define Single_Top_Fiducial_h

/* \Class SingleTopFiducialCrossSectionProducer
 *
 * \Authors: A. Orso M. Iorio
 * 
 * \ version $Id: SingleTopFiducialCrossSectionProducer.h,v 1.1.2.2 2013/06/21 20:40:24 oiorio Exp $
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



class SingleTopFiducialCrossSectionProducer : public edm::EDProducer {
  
public:
  
  explicit SingleTopFiducialCrossSectionProducer(const edm::ParameterSet & iConfig);
  ~SingleTopFiducialCrossSectionProducer();
  virtual void produce(edm::Event & iEvent, const edm::EventSetup & iSetup);
  
private:
  
  //InputTags
  edm::InputTag genBareLeptonsSrc_,genDressedLeptonsSrc_,genJetsSrc_,genBJetsSrc_,lheSrc_,genNeutrinosSrc_;
  std::string leptonChannel_;
  double minLeptonPt_,minJetPt_,metCut_,mtwCut_,leptonJetDeltaRCut_,TotalCrossSection_,maxJetEta_,maxBJetEta_,maxLeptonEta_;

  double mtw(math::PtEtaPhiELorentzVector lepton, math::PtEtaPhiELorentzVector met);
  
  int minLeptons_,maxLeptons_,minJets_,maxJets_,minBJets_,maxBJets_;

  bool countLeptons(int selectedLeptons, int allLeptons, int min, int max);
  bool countJets(int njets, int min, int max);
  
  int TotalEvents_;
  long int PreCutEventCounter_,PostCutEventCounter_;
  
  bool vetoDifferentFlavorLeptons_,useDressedLeptons_, addOutputCollections_;
  std::vector<math::PtEtaPhiELorentzVector> selectedLeptons,allLeptons,selectedJets,selectedBJets,allJets,allBJets,allNeutrinos;

};



#endif
