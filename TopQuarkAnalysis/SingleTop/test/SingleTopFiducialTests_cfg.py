import FWCore.ParameterSet.Config as cms

#Process name:
process = cms.Process("SingleTop")

#MessageLogger options:
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    FailPath = cms.untracked.vstring('ProductNotFound','Type Mismatch')
    )

#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#Input file:
process.source = cms.Source (
    "PoolSource",
    fileNames = cms.untracked.vstring (
      "file:/afs/cern.ch/work/o/oiorio/public/xFrancescoFab/T_t-channel_Synch.root"
#    "file:singleTopSkim.root"
      )
)
ChannelName = "TChannelFiducial"
#process.MessageLogger.cerr.FwkReport.reportEvery = 100

#Part of MC Truth particles production
#Adding particle-level Bare collections as well as genParticles sub-collection for dressing and jet clustering

process.load("SingleTopFiducialModules_cff") 

from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import saveNTuplesSkimLoose
from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import saveNTuplesSkimMu


#Add Fiducial information: 
doFiducial = True 
doFiducialExtraChecks = True 
if doFiducial:
    process.pathFiducial = cms.Path(
        process.FiducialSeq
        
        )
    if doFiducialExtraChecks :
        process.pathFiducial += process.FiducialSeqExtraChecks



    saveNTuplesSkimLoose.append('keep  *_genParticlesForFiducial_*_*')
    saveNTuplesSkimLoose.append('keep  *_genParticlesForFiducialNoNuInJets_*_*')
    saveNTuplesSkimLoose.append('keep *_ak5GenJets_*_*')
    saveNTuplesSkimLoose.append('keep *_ak5GenJetsForCheck_*_*')
    saveNTuplesSkimLoose.append('keep *_ak5GenJetsRescaledBHadrons_*_*')
    saveNTuplesSkimLoose.append('keep *_ak5GenJetsNoRescaledBHadrons_*_*')
    saveNTuplesSkimLoose.append('keep *_ak5GenJetsNoRescaledBHadronsNoNuInJets_*_*')
    saveNTuplesSkimLoose.append('keep *_ak1DressedMuons_*_*')
    saveNTuplesSkimLoose.append('keep *_ak1DressedElectrons_*_*')
    saveNTuplesSkimLoose.append('keep *_ak1DressedLeptons_*_*')


    saveNTuplesSkimLoose.append('keep *_ak5SelectedGenJetsRescaledB_*_*')
    saveNTuplesSkimLoose.append('keep *_ak5SelectedGenJetsNoRescaledB_*_*')

    saveNTuplesSkimLoose.append('keep *_FiducialMuons_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialElectrons_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialAllMuEle_*_*')
    
    saveNTuplesSkimLoose.append('keep *_FiducialMuonsNoDressLeptons_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialMuonsNoNuInJets_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialMuonsRescaledB_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialMuonsRescaledBNoDressLeptons_*_*')
    
    saveNTuplesSkimLoose.append('keep *_FiducialElectronsNoDressLeptons_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialElectronsNoNuInJets_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialElectronsRescaledB_*_*')
    saveNTuplesSkimLoose.append('keep *_FiducialElectronsRescaledBNoDressLeptons_*_*')
    

selectionpath = cms.vstring('pathFiducial')
if doFiducial:
    selectionpath = cms.vstring('pathFiducial')

process.singleTopNTuple = cms.OutputModule("PoolOutputModule",
                   fileName = cms.untracked.string('edmntuple_'+ChannelName+'.root'),
#                  fileName = cms.untracked.string('edmntuple_ele'+ChannelName+'.root'),
                   SelectEvents   = cms.untracked.PSet( SelectEvents = selectionpath),
#                  SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('pathPreselection')),
                   outputCommands = saveNTuplesSkimLoose,
)


process.singleTopNTuple.dropMetaData = cms.untracked.string("ALL")

process.outpath = cms.EndPath(
    process.singleTopNTuple #+    process.singleTopPatTuple 
    )


