#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms
import os,sys,re,shutil


#Original config file
fileName = "Mu_May10_crab.cfg"
fileName2 = "SingleTopData_Mu_May10_cfg.py"
#fileName = "SingleTopSystematics_cfg.py"
#fileName = "SingleTopSystematics_split_cfg.py"
#fileName = "SingleTopNEvents_cfg.py"

#Channels to include
channels = [
#"Ele_A13Jul",
#"Ele_A06Aug",
#"Ele_B13Jul",
#"Ele_C1",
#"Ele_C2",
#"Ele_C3",
#"Ele_D1",
#"Ele_D2",
#"Mu_A13Jul",
#"Mu_A06Aug",
#"Mu_B13Jul",
#"Mu_C1",
#"Mu_C2",
#"Mu_C3",
#"Mu_D1",
#"Mu_D2",

"Mu_A_22Jan",
"Mu_B_22Jan",
"Mu_C1_22Jan",
"Mu_C2_22Jan",
"Mu_C3_22Jan",
"Mu_D1_22Jan",
"Mu_D2_22Jan",
"Mu_D3_22Jan",

"Ele_A_22Jan",
"Ele_B_22Jan",
"Ele_C1_22Jan",
"Ele_C2_22Jan",
"Ele_C3_22Jan",
"Ele_D1_22Jan",
"Ele_D2_22Jan",
"Ele_D3_22Jan",

#"Mu_v1_B1",
#"Mu_v1_B2",
##"Mu_Aug05",
#"MuHad_Oct03",
#"Ele_May10",
#"Ele_v1_A",
#"Ele_v1_B1",
#"Ele_v1_B2",
#"EleHad_Aug05",
#"EleHad_Oct03",
  ]

#Path to take data merged files
dataPath = "file:/tmp/oiorio/"

#Choose if you want to run or just prepare the configuration files
mode = ""
#mode = "cmsRun"



#Implementation:

def datasetmap(channel):
    if channel == "TChannel":
        return "/T_TuneZ2_t-channel_7TeV-powheg-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM"
    if channel == "TbarChannel":
        return "/Tbar_TuneZ2_t-channel_7TeV-powheg-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM"

    if channel == "SChannel":
        return "/T_TuneZ2_s-channel_7TeV-powheg-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM"
    if channel == "SbarChannel":
        return "/Tbar_TuneZ2_s-channel_7TeV-powheg-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM"

    if channel == "TWChannel":
        return "/T_TuneZ2_tW-channel_7TeV-powheg-tauola-DS/Fall11-PU_S6_START42_V14B-v1/AODSIM"
    if channel == "TbarWChannel":
        return "/Tbar_TuneZ2_tW-channel_7TeV-powheg-tauola-DS/Fall11-PU_S6_START42_V14B-v1/AODSIM"

    if channel == "TTBar":
        return "/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v2/AODSIM"
    if channel == "WJets":
        return "/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM"

    if channel == "Ele_A13Jul":
        return "/SingleElectron/Run2012A-13Jul2012-v1/AOD"
    if channel == "Ele_A06Aug":
        return "/SingleElectron/Run2012A-recover-06Aug2012-v1/AOD"
    if channel == "Ele_B13Jul":
        return "/SingleElectron/Run2012B-13Jul2012-v1/AOD"

    if channel == "Ele_C1":
        return "/SingleElectron/Run2012C-24Aug2012-v1/AOD"
    if channel == "Ele_C2" in channel :#PromptReco
        return "/SingleElectron/Run2012C-PromptReco-v2/AOD"
    if channel == "Ele_C3" in channel :#PromptReco
        return "/SingleElectron/Run2012C-EcalRecover_11Dec2012-v1/AOD"
    
    if channel == "Ele_D1" in channel :#PromptReco
        return "/SingleElectron/Run2012D-PromptReco-v1/AOD"
    if channel == "Ele_D2" in channel :#PromptReco
        return "/SingleElectron/Run2012D-PromptReco-v1/AOD"

    if channel == "Mu_A13Jul":
        return "/SingleMu/Run2012A-13Jul2012-v1/AOD"
    if channel == "Mu_A06Aug":
        return "/SingleMu/Run2012A-recover-06Aug2012-v1/AOD"
    if channel == "Mu_B13Jul":
        return "/SingleMu/Run2012B-13Jul2012-v1/AOD"

    if channel == "Mu_C1":
        return "/SingleMu/Run2012C-24Aug2012-v1/AOD"
    if channel == "Mu_C2":
        return "/SingleMu/Run2012C-PromptReco-v2/AOD"
    if channel == "Mu_C3" in channel :#PromptReco
        return "/SingleMu/Run2012C-EcalRecover_11Dec2012-v1/AOD"

    if channel == "Mu_D1" in channel :#PromptReco
        return "/SingleMu/Run2012D-PromptReco-v1/AOD"
    if channel == "Mu_D2" in channel :#PromptReco
        return "/SingleMu/Run2012D-PromptReco-v1/AOD"

    if channel == "Mu_A_22Jan":
        return "/SingleMu/Run2012A-22Jan2013-v1/AOD"
    if channel == "Mu_B_22Jan":
        return "/SingleMu/Run2012B-22Jan2013-v1/AOD"

    if channel == "Mu_C1_22Jan":
        return "/SingleMu/Run2012C-22Jan2013-v1/AOD"
    if channel == "Mu_C2_22Jan":
        return "/SingleMu/Run2012C-22Jan2013-v1/AOD"
    if channel == "Mu_C3_22Jan":
        return "/SingleMu/Run2012C-22Jan2013-v1/AOD"

    if channel == "Mu_D1_22Jan":
        return "/SingleMu/Run2012D-22Jan2013-v1/AOD"
    if channel == "Mu_D2_22Jan":
        return "/SingleMu/Run2012D-22Jan2013-v1/AOD"
    if channel == "Mu_D3_22Jan":
        return "/SingleMu/Run2012D-22Jan2013-v1/AOD"



    if channel == "Ele_A_22Jan":
        return "/SingleEle/Run2012A-22Jan2013-v1/AOD"
    if channel == "Ele_B_22Jan":
        return "/SingleEle/Run2012B-22Jan2013-v1/AOD"

    if channel == "Ele_C1_22Jan":
        return "/SingleEle/Run2012C-22Jan2013-v1/AOD"
    if channel == "Ele_C2_22Jan":
        return "/SingleEle/Run2012C-22Jan2013-v1/AOD"
    if channel == "Ele_C3_22Jan":
        return "/SingleEle/Run2012C-22Jan2013-v1/AOD"

    if channel == "Ele_D1_22Jan":
        return "/SingleEle/Run2012D-22Jan2013-v1/AOD"
    if channel == "Ele_D2_22Jan":
        return "/SingleEle/Run2012D-22Jan2013-v1/AOD"
    if channel == "Ele_D3_22Jan":
        return "/SingleEle/Run2012D-22Jan2013-v1/AOD"


def entriesmap(channel):
    if channel == "TChannel" or channel == "TbarChannel" or channel == "TTBar" or channel == "TWChannel" or channel == "TbarWChannel" or channel == "SChannel" or channel == "SbarChannel":
        return 100000
    if channel == "WJets":
        return 300000
    if "_A13Jul" in channel or "_B13Jul" in channel :#Re-Reco
        return 100
    if "_A06Aug" in channel:#Re-Reco
        return 25
    if "_C1" in channel :#Re-Reco
        return 150
    if "_C2" in channel :#PromptReco
        return 100
    if "_C3" in channel :#PromptReco
        return 100
    if "_D1" in channel :#PromptReco
        return 100
    if "_D2" in channel :#PromptReco
        return 100
    if "_D3" in channel :#PromptReco
        return 100

def globaltag_maskmap(channel):
    if "_A13Jul" in channel or "_B13Jul" in channel :#Re-Reco
        return "cms.string('FT_53_V6C_AN3::All')"
    if "_A06Aug" in channel:#Re-Reco
        return "cms.string('FT_53_V6C_AN3::All')"
    if "_C1" in channel :#Re-Reco
        return "cms.string('FT_53_V10_AN3::All')"
    if "_C2" in channel :#PromptReco
        return "cms.string('GR_P_V42_AN3::All')"
    if "_C3" in channel :#Recover Re-Reco
        return "cms.string('FT_P_V42C_AN3::All')"
    if "_D1" in channel :#PromptReco, first part 
        return "cms.string('GR_P_V42_AN3::All')"
    if "_D2" in channel :#PromptReco, second part
        return "cms.string('GR_P_V42_AN3::All')"



def lumi_maskmap(channel):
    if "_A13Jul" in channel or "_B13Jul" in channel :#Re-Reco
        return "Cert_190456-196531_8TeV_13Jul2012ReReco_Collisions12_JSON_v2.txt"
    if "_A06Aug" in channel:#Re-Reco
        return "Cert_190782-190949_8TeV_06Aug2012ReReco_Collisions12_JSON.txt"
    if "_C1" in channel :#Re-Reco
        return "Cert_198022-198523_8TeV_24Aug2012ReReco_Collisions12_JSON.txt"
    if "_C2" in channel :#PromptReco
        return "Cert_190456-203002_8TeV_PromptReco_Collisions12_JSON_v2.txt"
    if "_C3" in channel :#PromptReco
        return "Cert_201191-201191_8TeV_11Dec2012ReReco-recover_Collisions12_JSON.txt"
    if "_D1" in channel :#PromptReco
        return "Cert_203768-206227_8TeV_PromptReco_Collisions12_JSON.txt"
    if "_D2" in channel :#PromptReco
        return "Cert_206228-208686_8TeV_PromptReco_Collisions12_JSON.txt"
        #return "Cert_203768-204601_8TeV_PromptReco_Collisions12_JSON.txt"
    
#Function to replace a sequence of characters channelOld to channelNew in a file 
def changeChannel(fileName,channelOld,channelNew): 
    print " Channel test " + channelNew
    channelToReplace = channelNew
    file = open(fileName)
    #    print " file name " + fileName + " ; channel old " +channelOld
    lines = file.readlines()
    name = fileName.replace(channelOld,channelToReplace)
    print name
    o = open(name,"w")
    for line in lines:
        if "user_remote_dir" in line or "pset" in line or "output_file" in line or "ui_working_dir" or "ChannelName" or "process.GlobalTag.globaltag" in line:
            words = line.split()
            for word in words:
                if channelOld in word:  
                    line = line.replace(word,word.replace(channelOld,channelToReplace))
        if "datasetpath" in line and not "#datasetpath" in line:
            line = "datasetpath = " + datasetmap(channelNew) +"\n"
        if "events_per_job" in line and not "#events_per_job" in line :
            line = "events_per_job ="+ str(entriesmap(channelToReplace))+ "\n"
        if "lumis_per_job" in line and not "#lumis_per_job" in line :
            line = "lumis_per_job ="+ str(entriesmap(channelToReplace)) + "\n"
        if "lumi_mask" in line and not "#lumi_mask" in line:
            line = "lumi_mask = " + str(lumi_maskmap(channelToReplace)) +"\n"
#        if "process.GlobalTag.globaltag" in line and not "#process.GlobalTag.globaltag" in line:
#            line = "process.GlobalTag.globaltag = " + str(globaltag_maskmap(channelToReplace)) +"\n"
        o.write(line)   
    o.close()
    return o

#Implementation of the loop part:

#Channel in the original file
startChannel = "Mu_May10"#channels[0]

f= open(fileName)
f2= open(fileName2)

tmpName = "temp.py"
shutil.copy(fileName,tmpName)

for channel in channels:

    channelOld = startChannel
    
    cfg_file = changeChannel(fileName,channelOld,channel)
    pset_file = changeChannel(fileName2,channelOld,channel)

#    os.system("bg") 
#    os.system('rm '+channel+'_cfg.py' ) 

os.system('rm '+tmpName) 
#changeChannel(f,aChannel,startChannel)

#os.system(command)



