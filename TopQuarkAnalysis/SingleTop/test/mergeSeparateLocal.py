#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms
import os,sys,re,shutil,commands


inputDir = "/tmp/oiorio/"
outputDir = "/tmp/oiorio/"

#Original config file
template = "copyFlavorSeparationTemplateSummer"
#fName = "copyFlavorSeparationTemplate.py"
#f = open(fName)


option = "None"
option = "cmsRun"

nparts = 6
channels = [
#"TChannel",
#"TbarChannel",
#"TWChannel",
#"TbarWChannel",
#"SChannel",
#"SbarChannel",
#"TTBar_MassUp",
#"TTBar_MassDown"

#"QCD_Pt_20to30_EMEnriched",
#"QCD_Pt_20to30_BCtoE",
#"QCD_Pt_30to80_BCtoE",
#"QCD_Pt_80to170_BCtoE",
#"QCD_Pt_170to250_BCtoE",

#"TbarWChannelThadWlep_MassDown",
#"TbarWChannelThadWlep_MassUp",#
#"TWChannelTlepWhad_MassUp",
#"TWChannelTlepWhad_MassDown",
#
#"TbarWChannelTlepWhad_MassDown",
#"TbarWChannelTlepWhad_MassUp",
#"TWChannelThadWlep_MassUp",
#"TWChannelThadWlep_MassDown",

#"TbarWChannelFullLep_Q2Up",
#"TbarWChannelFullLep_Q2Down",
#"TWChannelFullLep_Q2Up",
#"TWChannelFullLep_Q2Down",#
#
#"TbarWChannelThadWlep_Q2Up",
#"TbarWChannelThadWlep_Q2Down",
#"TWChannelThadWlep_Q2Up",
#"TWChannelThadWlep_Q2Down",
#
#"TbarWChannelTlepWhad_Q2Up",
#"TbarWChannelTlepWhad_Q2Down",
#"TWChannelTlepWhad_Q2Up",
#"TWChannelTlepWhad_Q2Down",

#"QCD_HT_40_100_GJets",
#"QCD_HT_100_200_GJets",
#"QCD_HT_200_400_GJets",
#"QCD_HT_400_inf_GJets",

#"TbarWChannelFullLep_MassDown",
#"TbarWChannelFullLep_MassUp",
#"TWChannelFullLep_MassDown",
#"TWChannelFullLep_MassUp",
#"TToBTauNu_unphys",
#"TToBTauNu_0100",
#"TToBMuNu_unphys",
#"TToBMuNu_0100",
#"TToBENu",
#"TToBMuNu",
#"TToBTauNu",
#"TToBENu_unphys",
#"TToBENu_0100",
#"TTBar_MassUp",
#"TTBar_MassDown",
#"TTBar_MatchingUp",
#"TTBar_MatchingDown",
#"TTBar_Q2Up",
#"TTBar_Q2Down",
#"TChannel_MassUp",
#"TChannel_MassDown",
#"TbarChannel_MassUp",
#"TbarChannel_MassDown",
#"TBMuNuChannel_Comphep",
#"TBTauNuChannel_Comphep",
#"TBENuChannel_Comphep",
#"TChannel_Q2Down",
#"TbarChannel_Q2Down",
#"TChannel_Q2Up",
#"TbarChannel_Q2Up",

#"TWChannelFullLep_Q2Up",
#"TWChannelFullLep_Q2Down",
#"TbarWChannelFullLep_Q2Up",
#"TbarWChannelFullLep_Q2Down",

#"TWChannelTlepWhad_Q2Up",
#"TWChannelTlepWhad_Q2Down",
#"TbarWChannelTlepWhad_Q2Up",
#"TbarWChannelTlepWhad_Q2Down",

#"TWChannelThadWlep_Q2Up",
#"TWChannelThadWlep_Q2Down",
#"TbarWChannelThadWlep_Q2Up",
#"TbarWChannelThadWlep_Q2Down",
#
#"TTBarSemiLep",
##"TTBarFullLep",
#"TChannel_Q2Up",
#"TbarChannel_Q2Up",
#"TTBar_Q2Down",
#"TTBar_Q2Up",
#"TTBar_MatchingDown",
#"TTBar_MatchingUp",
#"TChannel_Q2Down",
#"TbarChannel_Q2Down",
"QCDMuBig",
#"QCD_Pt_30to80_EMEnriched",
#"QCD_Pt_30to80_BCtoE",
#"QCD_Pt_80to170_BCtoE",
#"QCD_Pt_20to30_EMEnriched",
#"QCD_Pt_30to80_EMEnriched",
#"QCD_Pt_80to170_EMEnriched",
#"QCD_Pt_170to250_EMEnriched",
#"WJetsSherpa",
#"WJetsBig",
#"W3Jets",
#"W1Jet",
#"W2Jets",
#"W4Jets",
#"WJets",
#"WJets_MatchingDown",
#"WJets_MatchingUp",
#"ZJets",
#"TWChannel",
#"TbarWChannel",
#"TChannel",
#"TbarChannel",
#"SChannel",
#"SbarChannel",
#"Mu_A06Aug",
#"Mu_A13Jul",
#"Mu_B13Jul",
#"Mu_C2"
#"Mu_C1"
#"Ele_B1_22Jan","Ele_B2_22Jan","Ele_B3_22Jan","Ele_B4_22Jan",
#"Ele_22Jan"
#"Ele_C1_22Jan","Ele_C2_22Jan","Ele_C3_22Jan","Ele_C4_22Jan","Ele_C5_22Jan","Ele_C6_22Jan",
#"Ele_D1_22Jan","Ele_D2_22Jan","Ele_D3_22Jan","Ele_D4_22Jan","Ele_D5_22Jan","Ele_D6_22Jan",
#"Ele_A06Aug",
#"Ele_A13Jul",
#"Ele_C2",
#"WW",
#"WZ",
#"ZZ",
    ]

for channel in channels: 
    command_ls = "ls " + inputDir + " | grep _"+channel+"_"
    
    files = commands.getoutput(command_ls).split('\n')
    print "channel "+ channel +" n files " + str(len(files))

    templateFile= __import__(template)     

#    for file in files:
#        print file
    print "Removing doubles from list"
    for file in files :
        print file
        fileNameParts = file.split("_")
#        print fileNameParts
        jobNumber = fileNameParts[len(fileNameParts)-3] 
  #      print jobNumber
        for checkFile in files:
            if checkFile == file: continue
            checkFileNameParts = checkFile.split("_")
#            print checkFileNameParts
            checkJobNumber = checkFileNameParts[len(checkFileNameParts)-3] 
            if jobNumber == checkJobNumber:
                print " double: " + str(file) +" vs " + str(checkFile) 
                files.remove(checkFile)
#            Break 
    nfiles = len(files)    
    nraws = nfiles/(nparts)
    
    part = 0

    print channel + " after removal: n files " + str(len(files))
    for file in files: print file
    
    while int(part) < int(nparts):
        templateFileCopy = templateFile 
        templateFileCopy.process.source.fileNames = cms.untracked.vstring([]) 

        part = part +1
        if int(nparts) ==1:
            templateFileCopy.process.skimwall.fileName = cms.untracked.string(outputDir+channel+'Merged.root')
            configFile = open(channel + "_part_" +str(part)+"_cfg.py","w")
        else:
            templateFileCopy.process.skimwall.fileName = cms.untracked.string(outputDir+channel+'_part_'+str(part)+'Merged.root')
            configFile = open(channel + "_part_" +str(part)+"_cfg.py","w")

        
        nr =0
        for file in files:
            nr = nr +1
            if part == nparts:
                if nr > nraws * (part -1):
                    templateFileCopy.process.source.fileNames.append("file:"+inputDir+str(file))
            elif  nr > nraws * (part -1) and  nr <= nraws *part:
    #            print "nr "+str( nr )+" part "+str( part) + " nraws "+str( nraws ) + " filename " + str(file)
                templateFileCopy.process.source.fileNames.append("file:"+inputDir+str(file))
               
        configFile.write(templateFileCopy.process.dumpPython())
        configFile.close()
        if option == "cmsRun":
            launchCommand = 'nohup cmsRun ./' + channel + "_part_" +str(part)+"_cfg.py" +' >  /tmp/oiorio/'+channel+"_part_"+str(part)+'_merge.log &'
            print launchCommand
            os.system(launchCommand)

        
