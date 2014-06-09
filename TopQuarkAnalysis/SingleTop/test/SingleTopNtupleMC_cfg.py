import FWCore.ParameterSet.Config as cms

#Process name:
process = cms.Process("SingleTopNTUPLE")

#MessageLogger options:
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True),
    FailPath = cms.untracked.vstring('ProductNotFound','Type Mismatch')
    )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#Input file:
process.source = cms.Source (
    "PoolSource",
    fileNames = cms.untracked.vstring (
#      "file:/afs/cern.ch/work/o/oiorio/public/xFrancescoFab/T_t-channel_Synch.root"
    "file:singleTopSkim.root"
    )
)

#process.MessageLogger.cerr.FwkReport.reportEvery = 100

#Data or MC:
isData = False
##################### SERVE??? #########################
process.load("PhysicsTools.HepMCCandAlgos.flavorHistoryPaths_cfi")
########################################################

######### GET generator info ##############
#genJets:
process.genJetsPF = cms.EDProducer(
    "SingleTopGenJetPtEtaProducer",
    jetsSource = cms.InputTag("topJetsPF"),
)
#PU Info
process.NVertices = cms.EDProducer("SingleTopPileUpProducer")

#n gen particles Info
process.NGenParticles = cms.EDProducer("SingleTopNGenParticlesProducer")

#PDF Info
process.PDFInfo = cms.EDProducer( "PDFInfoDumper" )

#Part of MC Truth particles production
process.MCTruthParticles = cms.EDProducer(
    "SingleTopMCProducer",
    genParticlesSource = cms.InputTag("genParticles")
)
#############################################

######### EdmNtuples production ##############
process.load("TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff")

########################### just load the all in one shot #####################################
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleTopJetsPF
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleVertices

#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplePatMETsPF
#
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleMuons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleVetoMuons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleAllMuons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleQCDMuons
#
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleElectrons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleVetoElectrons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleAllElectrons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleVetoElectronsMVA
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleZVetoElectrons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleQCDElectrons
#
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTupleAllJets
#
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCNeutrinos
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCLeptons
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCQuarks
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCBQuarks
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTops
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsW
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsBQuark
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsQuark
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsQuarkBar
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsLepton
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import singleTopMCTopsNeutrino
#
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplesSkim
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import nTuplesSkimMCTruth
#############################################################################################


process.nTuplePatMETsPF.src = cms.InputTag('patMETs')

# Overall path
process.singleTopNtuplePath = cms.Path(
    process.genJetsPF +
    process.NVertices +
    process.NGenParticles +
    process.PDFInfo +          
    process.nTuplesSkim 
)


from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import saveNTuplesSkimLoose

#Add MC Truth information:
doMCTruth = True
if isData:
    doMCTruth = False

if doMCTruth:
    process.MCTruth = cms.Path (
        process.MCTruthParticles +
        process.nTuplesSkimMCTruth
    )

    saveNTuplesSkimLoose.append('keep  floats_MCTruthParticles_*_*')
    saveNTuplesSkimLoose.append('keep  ints_MCTruthParticles_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCLeptons_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCQuarks_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCNeutrinos_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCBQuarks_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCTops_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCTopsW_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCTopsBQuark_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCTopsLepton_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCTopsNeutrino_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCTopsQuark_*_*')
    saveNTuplesSkimLoose.append('keep  floats_singleTopMCTopsQuarkBar_*_*')
                                                            

###################################################################################
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import saveNTuplesSkimLoose
####### needed???? ########
#from TopQuarkAnalysis.SingleTop.SingleTopNtuplizers_cff import saveNTuplesSkimMu
###################################################################################

  
## Output module configuration
process.singleTopNTupleOut = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('singleTopEdmNtuple_.root'),
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('singleTopNtuplePath')),
    outputCommands = saveNTuplesSkimLoose,
    )

process.singleTopNTupleOut.dropMetaData = cms.untracked.string("ALL")


process.outpath = cms.EndPath(
    process.singleTopNTupleOut 
    )

