This repository contains a cmssw version tailored to produce pvss info per run and per lumi-section and put them in the offline database of cms.

In the future it will be extended to add other RPC objects as well.

It contains several directories.

1) The following four are used to define a database object for the RPC:

CondCore/RPCPlugins  
CondCore/Utilities
CondFormats/DataRecord  
CondFormats/RPCObjects

More info on how a CondDB object is produced can be found in :

https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCondObjectsTutorial
 
2) The last one:

CondTools/RPC

Contains the application currently under development.

2A) In particular the following create the object :

CondTools/RPC/src/RPCImonPerRunSH.cc
CondTools/RPC/src/RPCImonPerLumiSH.cc

2B) And the algorithm for calculating the pvss mean per run and lumi is stored here:

CondTools/RPC/src/RPCFwPerRun.cc

2C) An example of cfg file to get an average per lumi is to be found here:

CondTools/RPC/test/rpcimonperrun_cfg.py

Where the databases to be interfaced are to be set.
