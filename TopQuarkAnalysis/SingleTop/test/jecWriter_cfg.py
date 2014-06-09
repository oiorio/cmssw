import FWCore.ParameterSet.Config as cms
process = cms.Process("jectxt")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# define your favorite global tag
#process.GlobalTag.globaltag = 'GR_R_42_V19::All' #DATA
process.GlobalTag.globaltag = 'FT_53_V21_AN4::All' #MC
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source("EmptySource")
process.readAK5PF    = cms.EDAnalyzer('JetCorrectorDBReader',
                                      # below is the communication to the database
                                      payloadName    = cms.untracked.string('AK5PFchs'),
                                      # this is used ONLY for the name of the printed txt files. You can use any name that you like,
                                      # but it is recommended to use the GT name that you retrieved the files from.
                                      #globalTag      = cms.untracked.string('GR_R_42_V19'),#DATA
                                      globalTag      = cms.untracked.string('FT_53_V21_AN4'),#MC
                                      printScreen    = cms.untracked.bool(True),
                                      createTextFile = cms.untracked.bool(True)
                                      )

process.readAK5Calo = process.readAK5PF.clone(payloadName = 'AK5Calo')
process.p = cms.Path(process.readAK5PF * process.readAK5Calo)
