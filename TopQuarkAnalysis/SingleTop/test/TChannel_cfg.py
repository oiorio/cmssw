import FWCore.ParameterSet.Config as cms

process = cms.Process("SingleTopSystematics")


process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    FailPath = cms.untracked.vstring('ProductNotFound','Type Mismatch')
    )

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff") ### real data
process.GlobalTag.globaltag = cms.string("START52_V9::All")



#Load B-Tag
#MC measurements from 36X
#process.load ("RecoBTag.PerformanceDB.PoolBTagPerformanceDBMC36X")
#process.load ("RecoBTag.PerformanceDB.BTagPerformanceDBMC36X")
##Measurements from Fall10
#process.load ("RecoBTag.PerformanceDB.BTagPerformanceDB1011")
#process.load ("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1011")

#Spring11
process.load ("RecoBTag.PerformanceDB.PoolBTagPerformanceDB1107")
process.load ("RecoBTag.PerformanceDB.BTagPerformanceDB1107")


process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(3000))

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (

'file:./singleTopEdmNtuple_TChannel.root',
#'file:/tmp/mmerola/TChannelMerged.root',

),
duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
#eventsToProcess = cms.untracked.VEventRange('1:19517967-1:19517969'),
)




#from TChannel import *
#process.source.fileNames = TChannel_ntuple
#process.source.fileNames = cms.untracked.vstring("file:/tmp/mmerola/TChannelMerged.root")

#PileUpSync  

#Output
process.TFileService = cms.Service("TFileService", fileName = cms.string("/tmp/mmerola/TChannel.root"))
#process.TFileService = cms.Service("TFileService", fileName = cms.string("/tmp/mmerola/edmntuple_TTBar.root"))
#process.TFileService = cms.Service("TFileService", fileName = cms.string("testNoPU.root"))

#process.load("SingleTopAnalyzers_cfi")

process.load("SingleTopRootPlizer_cfi")
process.load("SingleTopFilters_cfi")
#from SingleTopPSets_cfi import *
#from SingleTopPSetsFall11_cfi import *
#from SingleTopPSetsSummer_cfi import *
from SingleTopPSetsFall_cfi import *

process.TreesEle.dataPUFile = cms.untracked.string("pileUpDistr.root")
process.TreesMu.dataPUFile = cms.untracked.string("pileUpDistr.root")


# THESE ARE DEFINED IN THE ROOTPLIZER
#process.TreesEle.doTopPtReweighting = cms.untracked.bool(True)
#process.TreesMu.doTopPtReweighting = cms.untracked.bool(True)

#process.TreesEle.doTopBestMass = cms.untracked.bool(True)
#process.TreesMu.doTopBestMass = cms.untracked.bool(True)

#process.TreesEle.doAsymmetricPtCut = cms.untracked.bool(True)
#process.TreesMu.doAsymmetricPtCut = cms.untracked.bool(True)

#process.TreesEle.doTurnOn = cms.untracked.bool(False)

#doPU = cms.untracked.bool(False)

#process.WeightProducer.doPU = cms.untracked.bool(False)
#process.TreesMu.doQCD = cms.untracked.bool(False)
#process.TreesEle.doQCD = cms.untracked.bool(False)
#process.TreesMu.doResol = cms.untracked.bool(False)
#process.TreesEle.doResol = cms.untracked.bool(False)

#process.TreesMu.doPU = cms.untracked.bool(False)
#process.TreesEle.doPU = cms.untracked.bool(False)


#CHANNEL BY CHANNEL INFO TAKEN FROM PSETS 
process.TreesEle.channelInfo = TChannelEle
process.TreesMu.channelInfo = TChannelMu


channel_instruction = "allmc" #SWITCH_INSTRUCTION
#channel_instruction = "allmc" #SWITCH_INSTRUCTION

MC_instruction = True #TRIGGER_INSTRUCTION

process.HLTFilterMu.isMC = MC_instruction
process.HLTFilterEle.isMC = MC_instruction
process.HLTFilterMuOrEle.isMC = MC_instruction
process.HLTFilterMuOrEleMC.isMC = MC_instruction
    

#process.PUWeightsPath = cms.Path(
#    process.WeightProducer 
#)

if channel_instruction == "allmc":
    #    process.TreesMu.doResol = cms.untracked.bool(True)
    #    process.TreesEle.doResol = cms.untracked.bool(True)
    #    process.TreesEle.doTurnOn = cms.untracked.bool(True) 
    process.PathSysMu = cms.Path(
    process.HLTFilterMu2012 *
    process.TreesMu
    )
    process.PathSysEle = cms.Path(
    process.HLTFilterEle2012 *
#    process.HLTFilterEleMC *
    process.TreesEle
    )

if channel_instruction == "all":
    process.TreesEle.doTurnOn = cms.untracked.bool(False) 
    process.TreesEle.doPU = cms.untracked.bool(False) 
    process.TreesMu.doPU = cms.untracked.bool(False) 
    process.TreesMu.doMCTruth = cms.untracked.bool(False) 
    process.TreesEle.doMCTruth = cms.untracked.bool(False) 
    process.PathSys = cms.Path(
    #    process.PlotsMu +
    #    process.PlotsEle +
    process.HLTFilterMuOrEle *
    process.TreesMu +
    process.TreesEle
    )

if channel_instruction == "mu":
    process.TreesMu.doPU = cms.untracked.bool(False) 
    process.TreesMu.doResol = cms.untracked.bool(False) 
    process.TreesMu.doMCTruth = cms.untracked.bool(False)
    process.TreesMu.doPDF = cms.untracked.bool(False) 
    process.PathSysMu = cms.Path(
    #    process.PlotsMu +
    #    process.PlotsEle +
   process.HLTFilterMu2012 *
    process.TreesMu 
    )

if channel_instruction == "ele":
    process.TreesEle.doTurnOn = cms.untracked.bool(False) 
    process.TreesEle.doPU = cms.untracked.bool(False) 
    process.TreesEle.doResol = cms.untracked.bool(False) 
    process.TreesEle.doMCTruth = cms.untracked.bool(False) 
    process.TreesEle.doPDF = cms.untracked.bool(False)
    process.PathSysMu = cms.Path(
    #    process.PlotsMu +
    #    process.PlotsEle +
    process.HLTFilterEle2012 *
    process.TreesEle 
    )

if channel_instruction == "muqcd":
    process.TreesMu.doPU = cms.untracked.bool(False) 
    process.TreesMu.doResol = cms.untracked.bool(False) 
    process.TreesMu.doMCTruth = cms.untracked.bool(False) 
    process.PathSysMu = cms.Path(
    #    process.PlotsMu +
    #    process.PlotsEle +
    process.HLTFilterMuQCD *
    process.TreesMu 
    )


if channel_instruction == "eleqcd":
    process.TreesEle.doTurnOn = cms.untracked.bool(False) 
    process.TreesEle.doPU = cms.untracked.bool(False) 
    process.TreesEle.doResol = cms.untracked.bool(False) 
    process.TreesEle.isControlSample = cms.untracked.bool(True) 
    process.TreesMu.doMCTruth = cms.untracked.bool(False) 
    process.PathSysEle = cms.Path(
    #    process.PlotsMu +
    #    process.PlotsEle +
    process.HLTFilterEleQCD *
    process.TreesEle
    )
