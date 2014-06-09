// -*- C++ -*-
//
// Package:    SiStripTools
// Class:      APVCyclePhaseProducerFromL1TS
// 
/**\class APVCyclePhaseProducerFromL1TS APVCyclePhaseProducerFromL1TS.cc DPGAnalysis/SiStripTools/plugins/APVCyclePhaseProducerFromL1TS.cc

 Description: EDproducer for APVCyclePhaseCollection which uses the configuration file to assign a phase to the run

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Andrea Venturi
//         Created:  Mon Jan 12 09:05:45 CET 2009
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"

#include <map>
#include <vector>
#include <string>

#include "TH1F.h"
#include "TProfile.h"

#include "DataFormats/Scalers/interface/Level1TriggerScalers.h"
#include "DPGAnalysis/SiStripTools/interface/APVCyclePhaseCollection.h"

//
// class decleration
//

class APVCyclePhaseProducerFromL1TS : public edm::EDProducer {
   public:
      explicit APVCyclePhaseProducerFromL1TS(const edm::ParameterSet&);
      ~APVCyclePhaseProducerFromL1TS();

private:
  virtual void beginJob() ;
  virtual void beginRun(edm::Run&, const edm::EventSetup&);
  virtual void endRun(edm::Run&, const edm::EventSetup&);
  virtual void produce(edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  
      // ----------member data ---------------------------

  const edm::InputTag _l1tscollection;
  const std::vector<std::string> _defpartnames;
  const std::vector<int> _defphases;
  const bool _wantHistos;
  const bool _useEC0;
  const int _magicOffset;

  TH1F* _hsize;
  TH1F* _hlresync;
  TH1F* _hlOC0;
  TH1F* _hlTE;
  TH1F* _hlEC0;
  TH1F* _hlstart;
  TH1F* _hlHR;

  TH1F* _hdlec0lresync;
  TH1F* _hdlresynclHR;

  const unsigned int _firstgoodrun;
  
  long long _lastResync;
  long long _lastHardReset;
  long long _lastStart;
  long long _lastEventCounter0;
  long long _lastOrbitCounter0;
  long long _lastTestEnable;


};

//
// constants, enums and typedefs
//


//
// static data member definitions
//

//
// constructors and destructor
//
APVCyclePhaseProducerFromL1TS::APVCyclePhaseProducerFromL1TS(const edm::ParameterSet& iConfig):
  _l1tscollection(iConfig.getParameter<edm::InputTag>("l1TSCollection")),
  _defpartnames(iConfig.getParameter<std::vector<std::string> >("defaultPartitionNames")),
  _defphases(iConfig.getParameter<std::vector<int> >("defaultPhases")),
  _wantHistos(iConfig.getUntrackedParameter<bool>("wantHistos",false)),
  _useEC0(iConfig.getUntrackedParameter<bool>("useEC0",false)),
  _magicOffset(iConfig.getUntrackedParameter<int>("magicOffset",8)),
  _firstgoodrun(131768),
  _lastResync(-1),_lastHardReset(-1),_lastStart(-1),
  _lastEventCounter0(-1),_lastOrbitCounter0(-1),_lastTestEnable(-1)
{

  produces<APVCyclePhaseCollection,edm::InEvent>();

   //now do what ever other initialization is needed

}


APVCyclePhaseProducerFromL1TS::~APVCyclePhaseProducerFromL1TS()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
APVCyclePhaseProducerFromL1TS::beginRun(edm::Run& iRun, const edm::EventSetup& iSetup) 

{

  // reset offset vector

  if(_wantHistos) {

    edm::Service<TFileService> tfserv;

    char dirname[300];
    sprintf(dirname,"run_%d",iRun.run());
    TFileDirectory subrun = tfserv->mkdir(dirname);

    _hsize = subrun.make<TH1F>("size","Level1TriggerScalers Collection size",20,-0.5,19.5);

    _hlresync = subrun.make<TH1F>("lresync","Orbit of last resync",3600,0.,3600*11223);
    _hlresync->GetXaxis()->SetTitle("Orbit");     _hlresync->GetYaxis()->SetTitle("Events");
    _hlresync->SetBit(TH1::kCanRebin);

    _hlOC0 = subrun.make<TH1F>("lOC0","Orbit of last OC0",3600,0.,3600*11223);
    _hlOC0->GetXaxis()->SetTitle("Orbit");     _hlOC0->GetYaxis()->SetTitle("Events");
    _hlOC0->SetBit(TH1::kCanRebin);

    _hlTE = subrun.make<TH1F>("lTE","Orbit of last TestEnable",3600,0.,3600*11223);
    _hlTE->GetXaxis()->SetTitle("Orbit");     _hlTE->GetYaxis()->SetTitle("Events");
    _hlTE->SetBit(TH1::kCanRebin);

    _hlstart = subrun.make<TH1F>("lstart","Orbit of last Start",3600,0.,3600*11223);
    _hlstart->GetXaxis()->SetTitle("Orbit");     _hlstart->GetYaxis()->SetTitle("Events");
    _hlstart->SetBit(TH1::kCanRebin);

    _hlEC0 = subrun.make<TH1F>("lEC0","Orbit of last EC0",3600,0.,3600*11223);
    _hlEC0->GetXaxis()->SetTitle("Orbit");     _hlEC0->GetYaxis()->SetTitle("Events");
    _hlEC0->SetBit(TH1::kCanRebin);

    _hlHR = subrun.make<TH1F>("lHR","Orbit of last HardReset",3600,0.,3600*11223);
    _hlHR->GetXaxis()->SetTitle("Orbit");     _hlHR->GetYaxis()->SetTitle("Events");
    _hlHR->SetBit(TH1::kCanRebin);

    _hdlec0lresync = subrun.make<TH1F>("dlec0lresync","Orbit difference EC0-Resync",4000,-1999.5,2000.5);
    _hdlec0lresync->GetXaxis()->SetTitle("lastEC0-lastResync"); 

    _hdlresynclHR = subrun.make<TH1F>("dlresynclHR","Orbit difference Resync-HR",4000,-1999.5,2000.5);
    _hdlresynclHR->GetXaxis()->SetTitle("lastEC0-lastResync"); 

  }

  if(iRun.run() < _firstgoodrun) {
    LogDebug("UnreliableMissingL1TriggerScalers") << 
      "In this run L1TriggerScalers is missing or unreliable for phase determination: default phases will be used"; 
  }

}

void 
APVCyclePhaseProducerFromL1TS::endRun(edm::Run&, const edm::EventSetup&)
{
  // summary of absolute bx offset vector

}


void
APVCyclePhaseProducerFromL1TS::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  using namespace edm;
  
  std::auto_ptr<APVCyclePhaseCollection> apvphases(new APVCyclePhaseCollection() );
  

  const std::vector<int>& phases = _defphases;
  const std::vector<std::string>& partnames = _defpartnames;

  int phasechange = 0;

  if(iEvent.run() >= _firstgoodrun ) {
    
    Handle<Level1TriggerScalersCollection> l1ts;
    iEvent.getByLabel(_l1tscollection,l1ts);
    
    if(_wantHistos) _hsize->Fill(l1ts->size());

    // offset computation
    
    long long orbitoffset = 0;

    if(l1ts->size()>0) {

      if((*l1ts)[0].lastResync()!=0) {
	orbitoffset = _useEC0 ? (*l1ts)[0].lastEventCounter0() + _magicOffset : (*l1ts)[0].lastResync() + _magicOffset;
      }
      
      if(_wantHistos) {
	_hlresync->Fill((*l1ts)[0].lastResync());
	_hlOC0->Fill((*l1ts)[0].lastOrbitCounter0());
	_hlTE->Fill((*l1ts)[0].lastTestEnable());
	_hlstart->Fill((*l1ts)[0].lastStart());
	_hlEC0->Fill((*l1ts)[0].lastEventCounter0());
	_hlHR->Fill((*l1ts)[0].lastHardReset());
      }
      
      if(_lastResync != (*l1ts)[0].lastResync()) {
	_lastResync = (*l1ts)[0].lastResync();
	if(_wantHistos) _hdlec0lresync->Fill((*l1ts)[0].lastEventCounter0()-(*l1ts)[0].lastResync());
	LogDebug("TTCSignalReceived") << "New Resync at orbit " << _lastResync ;
      }
      if(_lastHardReset != (*l1ts)[0].lastHardReset()) {
	_lastHardReset = (*l1ts)[0].lastHardReset();
	if(_wantHistos) _hdlresynclHR->Fill((*l1ts)[0].lastResync()-(*l1ts)[0].lastHardReset());
	LogDebug("TTCSignalReceived") << "New HardReset at orbit " << _lastHardReset ;
      }
      if(_lastTestEnable != (*l1ts)[0].lastTestEnable()) {
	_lastTestEnable = (*l1ts)[0].lastTestEnable();
	//      LogDebug("TTCSignalReceived") << "New TestEnable at orbit " << _lastTestEnable ;
      }
      if(_lastOrbitCounter0 != (*l1ts)[0].lastOrbitCounter0()) {
	_lastOrbitCounter0 = (*l1ts)[0].lastOrbitCounter0();
	LogDebug("TTCSignalReceived") << "New OrbitCounter0 at orbit " << _lastOrbitCounter0 ;
      }
      if(_lastEventCounter0 != (*l1ts)[0].lastEventCounter0()) {
	_lastEventCounter0 = (*l1ts)[0].lastEventCounter0();
	LogDebug("TTCSignalReceived") << "New EventCounter0 at orbit " << _lastEventCounter0 ;
      }
      if(_lastStart != (*l1ts)[0].lastStart()) {
	_lastStart = (*l1ts)[0].lastStart();
	LogDebug("TTCSignalReceived") << "New Start at orbit " << _lastStart ;
      }
      
      phasechange = ((long long)(orbitoffset*3564))%70;
      
    }
  }
    

  if(phases.size() < partnames.size() ) {
    // throw exception
    throw cms::Exception("InvalidAPVCyclePhases") << " Inconsistent phases/partitions vector sizes: " 
					     << phases.size() << " " 
					     << partnames.size();
  }

  for(unsigned int ipart=0;ipart<partnames.size();++ipart) {
    if(phases[ipart]>=0) {
      apvphases->get()[partnames[ipart]] = (phases[ipart]+phasechange)%70;

    }
  }


  iEvent.put(apvphases);

}

// ------------ method called once each job just before starting event loop  ------------
void 
APVCyclePhaseProducerFromL1TS::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
APVCyclePhaseProducerFromL1TS::endJob() {
}

//define this as a plug-in
DEFINE_FWK_MODULE(APVCyclePhaseProducerFromL1TS);
