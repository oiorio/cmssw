import FWCore.ParameterSet.Config as cms

logErrorTooManyClusters = cms.EDFilter("LogErrorEventFilter",
                                       src = cms.InputTag("logErrorHarvester"),
                                       maxErrorFractionInLumi = cms.double(1.0),
                                       maxErrorFractionInRun  = cms.double(1.0),
                                       maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                       categoriesToWatch = cms.vstring("TooManyClusters"),
                                       modulesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds",
                                                                     "PhotonConversionTrajectorySeedProducerFromSingleLeg:photonConvTrajSeedFromSingleLeg")
                                                                              )

logErrorTooManyTripletsPairs = cms.EDFilter("LogErrorEventFilter",
                                            src = cms.InputTag("logErrorHarvester"),
                                            maxErrorFractionInLumi = cms.double(1.0),
                                            maxErrorFractionInRun  = cms.double(1.0),
                                            maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                            categoriesToWatch = cms.vstring("TooManyTriplets","TooManyPairs","PixelTripletHLTGenerator"),
                                            modulesToIgnore = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:regionalCosmicTrackerSeeds",
                                                                          "PhotonConversionTrajectorySeedProducerFromSingleLeg:photonConvTrajSeedFromSingleLeg")
                                            )


logErrorTooManyTripletsPairsMainIterations = cms.EDFilter("LogErrorEventFilter",
                                                          src = cms.InputTag("logErrorHarvester"),
                                                          maxErrorFractionInLumi = cms.double(1.0),
                                                          maxErrorFractionInRun  = cms.double(1.0),
                                                          maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                                          categoriesToWatch = cms.vstring("TooManyTriplets","TooManyPairs","PixelTripletHLTGenerator"),
                                                          modulesToWatch = cms.vstring("SeedGeneratorFromRegionHitsEDProducer:initialStepSeeds",
                                                                                       "SeedGeneratorFromRegionHitsEDProducer:pixelPairStepSeeds"
                                                                                       )
                                                          )

logErrorTooManySeeds = cms.EDFilter("LogErrorEventFilter",
                                    src = cms.InputTag("logErrorHarvester"),
                                    maxErrorFractionInLumi = cms.double(1.0),
                                    maxErrorFractionInRun  = cms.double(1.0),
                                    maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                    categoriesToWatch = cms.vstring("TooManySeeds"),
                                    )

logErrorTooManySeedsMainIterations = cms.EDFilter("LogErrorEventFilter",
                                                  src = cms.InputTag("logErrorHarvester"),
                                                  maxErrorFractionInLumi = cms.double(1.0),
                                                  maxErrorFractionInRun  = cms.double(1.0),
                                                  maxSavedEventsPerLumiAndError = cms.uint32(100000),
                                                  categoriesToWatch = cms.vstring("TooManySeeds"),
                                                  modulesToWatch = cms.vstring("CkfTrackCandidateMaker:initialStepTrackCandidate",
                                                                               "CkfTrackCandidateMaker:pixelPairTrackCandidate"
                                                                               )
                                                  )
