import FWCore.ParameterSet.Config as cms

#process.load("RecoJets.Configuration.GenJetParticles_cff")

from RecoJets.Configuration.GenJetParticles_cff import *

#Use this only to produce the jet and lepton collections
genParticlesForFiducial = cms.EDProducer(
    "SingleTopParticleLevelMCProducer",
    genParticlesSource = cms.InputTag("genParticles"),
    genJetsSource = cms.InputTag("ak5GenJets"),
    ignoreParticleIDs=genParticlesForJets.ignoreParticleIDs,
#    excludeFromResonancePids=genParticlesForJets.excludeFromResonancePids
    excludeFromResonancePids=cms.vuint32(11,12,13,14,16),
    #now only doing genJets selection:
    useJetsNoNu = cms.untracked.bool(False),
    doBaseCollections = cms.untracked.bool(True),
    doDressedCollections = cms.untracked.bool(True),
    doBDescendentJetSelection = cms.untracked.bool(True),
)

genParticlesForFiducialNoNuInJets = genParticlesForFiducial.clone(
    useJetsNoNu = cms.untracked.bool(True)
    )

ak5SelectedGenJetsNoRescaledB = genParticlesForFiducial.clone(
    genJetsSource = cms.InputTag("ak5GenJetsNoRescaledBHadrons"), 
    doBaseCollections = cms.untracked.bool(False),
    doDressedCollections = cms.untracked.bool(False),
    doBDescendentJetSelection = cms.untracked.bool(True),
    )


ak5SelectedGenJetsNoRescaledBNoNuInJets = ak5SelectedGenJetsNoRescaledB.clone(
    genJetsSource = cms.InputTag("ak5GenJetsNoRescaledBHadronsNoNuInJets"),
    )

ak5SelectedGenJetsRescaledB = ak5SelectedGenJetsNoRescaledB.clone(
    genJetsSource = cms.InputTag("ak5GenJetsRescaledBHadrons"), 
    )

FiducialMuons = cms.EDProducer(
    "SingleTopFiducialCrossSectionProducer",
    #input srcs:
    genBareLeptonsSource = cms.InputTag("genParticlesForFiducial","particleLevelLeptons"),
    genNeutrinosSource = cms.InputTag("genParticlesForFiducial","particleLevelNeutrinos"),
    genDressedLeptonsSource = cms.InputTag("ak1DressedLeptons"),
    genJetsSource = cms.InputTag("ak5SelectedGenJetsNoRescaledB","particleLevelJets"),
    genBJetsSource = cms.InputTag("ak5SelectedGenJetsNoRescaledB","particleLevelBJets"),
    lheSource = cms.InputTag("source"),
    
    #add the output collections?
    addOutputCollections = cms.untracked.bool(True),
    
    #lepton selection:
    leptonChannel = cms.untracked.string("muon"),
    vetoDifferentFlavorLeptons = cms.untracked.bool(True),
    useDressedLeptons = cms.untracked.bool(True),

    minLeptonPt = cms.untracked.double(26.0),
    maxLeptonEta = cms.untracked.double(2.1),
    minLeptons = cms.untracked.int32(1),
    maxLeptons = cms.untracked.int32(1),
    
    #Jets selection:
    minJetPt = cms.untracked.double(40.0),
    maxJetEta = cms.untracked.double(5.0),
    maxBJetEta = cms.untracked.double(2.6),

    deltaRCut = cms.untracked.double(-1),

    minJets = cms.untracked.int32(2),
    maxJets = cms.untracked.int32(2),

    minBJets = cms.untracked.int32(1),
    maxBJets = cms.untracked.int32(1),

    
    
    #met/mtw:
    metCut = cms.untracked.double(-1.0),
    #mtwCut = cms.untracked.double(-1.0),

    mtwCut = cms.untracked.double(50.0),
)

FiducialElectrons = FiducialMuons.clone(
    leptonChannel = cms.untracked.string("electron"),
    minLeptonPt = cms.untracked.double(30.0),
    maxLeptonEta = cms.untracked.double(2.5),
    metCut = cms.untracked.double(45.0),
    #metCut = cms.untracked.double(-1.0),
    mtwCut = cms.untracked.double(-1.0),
)

FiducialAllMuEle = FiducialMuons.clone(
    leptonChannel = cms.untracked.string("all"),
)

FiducialMuonsNoNuInJets = FiducialMuons.clone(
    genNeutrinosSource = cms.InputTag("genParticlesForFiducialNoNuInJets","particleLevelNeutrinos"),
    genJetsSource = cms.InputTag("ak5SelectedGenJetsNoRescaledBNoNuInJets","particleLevelJets"),
    genBJetsSource = cms.InputTag("ak5SelectedGenJetsNoRescaledBNoNuInJets","particleLevelBJets"),
)

FiducialElectronsNoNuInJets = FiducialElectrons.clone(
    genNeutrinosSource = cms.InputTag("genParticlesForFiducialNoNuInJets","particleLevelNeutrinos"),
    genJetsSource = cms.InputTag("ak5SelectedGenJetsNoRescaledBNoNuInJets","particleLevelJets"),
    genBJetsSource = cms.InputTag("ak5SelectedGenJetsNoRescaledBNoNuInJets","particleLevelBJets"),
)

FiducialMuonsNoDressLeptons = FiducialMuons.clone(
    useDressedLeptons = cms.untracked.bool(False)    
    )
FiducialElectronsNoDressLeptons = FiducialElectrons.clone(
    useDressedLeptons = cms.untracked.bool(False)    
    )

FiducialMuonsRescaledB = FiducialMuons.clone(
    genJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelJets"),
    genBJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelBJets"),
    )
FiducialElectronsRescaledB = FiducialElectrons.clone(
    genJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelJets"),
    genBJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelBJets"),
    )

FiducialMuonsRescaledBNoDressLeptons = FiducialMuons.clone(
    useDressedLeptons = cms.untracked.bool(False),
    genJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelJets"),
    genBJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelBJets"),
)
FiducialElectronsRescaledBNoDressLeptons = FiducialElectrons.clone(
    useDressedLeptons = cms.untracked.bool(False),
    genJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelJets"),
    genBJetsSource = cms.InputTag("ak5SelectedGenJetsRescaledB","particleLevelBJets"),
)


#############################################

######### EdmNtuples production ##############
from RecoJets.JetProducers.ak5GenJets_cfi import *

#akt algorithm for particle-level definitions:
genParticlesForJetsCheck = genParticlesForJets.clone(
    excludeResonances = cms.bool(False),
)

ak5GenJetsForCheck = ak5GenJets.clone(
    src= cms.InputTag("genParticlesForJetsCheck"),
    rParam       = cms.double(0.5)
    )

ak5GenJetsRescaledBHadrons = ak5GenJets.clone(
    src= cms.InputTag("genParticlesForFiducial","genParticlesForJetsRescaledBHadrons"),
    rParam       = cms.double(0.5)
    )

ak5GenJetsNoRescaledBHadrons = ak5GenJets.clone(
    src= cms.InputTag("genParticlesForFiducial","genParticlesForJetsNoRescaledBHadrons"),
    rParam       = cms.double(0.5)
    )

ak5GenJetsNoRescaledBHadronsNoNuInJets = ak5GenJets.clone(
    src= cms.InputTag("genParticlesForFiducialNoNuInJets","genParticlesForJetsNoRescaledBHadrons"),
    rParam       = cms.double(0.5)
    )

ak1DressedElectrons = ak5GenJets.clone(
    src= cms.InputTag("genParticlesForFiducial","genEGammaForDressing"), 
    rParam       = cms.double(0.1)
    )
ak1DressedMuons = ak5GenJets.clone(
    src= cms.InputTag("genParticlesForFiducial","genMuGammaForDressing"), 
    rParam       = cms.double(0.1)
    )

ak1DressedLeptons = ak5GenJets.clone(
    src= cms.InputTag("genParticlesForFiducial","genLeptonsForDressing"), 
    rParam       = cms.double(0.1)
    )

from TopQuarkAnalysis.SingleTop.SingleTopProducers_cff import PDFInfo

FiducialSeq = cms.Sequence (
    PDFInfo *
    genParticlesForJetsCheck *
    genParticlesForFiducial *
    genParticlesForFiducialNoNuInJets *
    ak5GenJetsRescaledBHadrons *
    ak5GenJetsNoRescaledBHadrons *
    ak5GenJetsNoRescaledBHadronsNoNuInJets *
    ak5GenJetsForCheck *
    ak1DressedLeptons *
    ak1DressedMuons *
    ak1DressedElectrons *
    ak5SelectedGenJetsRescaledB *
    ak5SelectedGenJetsNoRescaledB *
    ak5SelectedGenJetsNoRescaledBNoNuInJets *
    FiducialElectrons * 
    FiducialMuons *
    FiducialAllMuEle
)    
FiducialSeqExtraChecks = cms.Sequence (
    FiducialMuonsNoDressLeptons *
    FiducialMuonsNoNuInJets *
    FiducialMuonsRescaledB *
    FiducialMuonsRescaledBNoDressLeptons *
    FiducialElectronsNoDressLeptons *
    FiducialElectronsNoNuInJets *
    FiducialElectronsRescaledB *
    FiducialElectronsRescaledBNoDressLeptons 
)


#Analyzers:

TreesMuFiducial = cms.EDAnalyzer (
    "SingleTopFiducialCrossSectionAnalyzer",
    channelInfo = cms.PSet(
        crossSection = cms.untracked.double(56.4),
        channel = cms.untracked.string("TChannel"),
        originalEvents = cms.untracked.double(1000000),
        ),
    isFiducialEvent = cms.InputTag("FiducialMuons","isFiducialEvent"),
    x1 = cms.InputTag("PDFInfo","x1"),
    x2 = cms.InputTag("PDFInfo","x2"),
    id1 = cms.InputTag("PDFInfo","id1"),
    id2 = cms.InputTag("PDFInfo","id2"),
    scalePDF = cms.InputTag("PDFInfo","scalePDF"),

)

TreesEleFiducial = TreesMuFiducial.clone(
    isFiducialEvent = cms.InputTag("FiducialElectrons","isFiducialEvent"),
    )
