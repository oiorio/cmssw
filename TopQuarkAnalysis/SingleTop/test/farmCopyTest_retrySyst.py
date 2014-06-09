#!/usr/bin/python
import os
import re
import sys
import commands
import subprocess
#import xmlrpclib

#os.command("grid-proxy-init")


se = "cmsse02.na.infn.it"
port = "8446"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/Apr06/"
#path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/Apr05/"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12//"

se = "stormfe1.pi.infn.it"
port = "8444"
#path = "/cms/store//user/oiorio/SingleTop/Fall12/gouranga/"
path = "/cms/store/user/mmerola/SingleTop/Analysis/2013/MC/"
path = "/cms/store/user/mmerola/SingleTop/Analysis/2013/"

dir ='"srm://'+se + ":" + port + "/srm/managerv2?SFN=" + path +'"'
command_ls = 'lcg-ls -b -D srmv2 -T srmv2 '+ dir
localdir = "/tmp/oiorio/"

#path = "srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/mmerola/SingleTop/Analysis/2013/MC/"
#"srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Summer12/Jul15/"
"srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/mmerola/SingleTop/Analysis/2013/"
#lcg-ls -l -b -D srmv2 -T srmv2 "srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/mmerola/SingleTop/Analysis/2013/Merged_ReReco"
nSimultaneous = 25

channels = [
#"TChannel",
#"TbarChannel",
#"TTBar_MassUp"
#"TToBTauNu_unphys",
#"TToBTauNu_0100",
#"TToBTauNu",
#"TToBMuNu_unphys",
#"TToBMuNu_0100",
#"TToBMuNu",
#"TToBENu_unphys",
#"TToBENu_0100",
#"TChannel_MassDown",
#"TbarChannel_MassDown",
#"TChannel_MassUp",
#"TbarChannel_MassUp",
#"TTBar_MassUp",
#"TTBar_MassDown",#"QCD_Pt_80to170_BCtoE",
#"QCD_Pt_80to170_EMEnriched",
#"QCD_Pt_30to80_EMEnriched",
#"QCD_Pt_30to80_BCtoE",
#"TChannel",
#"TbarChannel",
#"TChannel_Q2Up",
#"TTBar_Q2Down",
#"TTBar_Q2Up",
#"TTBar_MatchingDown",
#"TTBar_MatchingUp",
#"TbarChannel_Q2Up",
#"TChannel_Q2Down",
#"TbarChannel_Q2Down",
#"WJetsBig",
#"WJets",
#"W3Jets",
#"W1Jet",
#"W2Jets",
#"W4Jets",
#"SChannel",
#"SbarChannel",
#"TTBarFullLep",
#"TTBarSemiLep",
#"QCDMuBig",
#"Ele_v1_A",
#"Mu_A06Aug",
#"Mu_A13Jul",
#"Mu_B13Jul",
#"Mu_v1_B1",
#"Mu_v1_B2",
#"Ele_v1_B2",
#"WJets",
#"TbarWChannel",
#"TWChannel",
#"ZJets",
#"WW",
#"WZ",
#"ZZ",
"Merged/Systematics"
#"MergedJun27"
#"Merged_ReReco"
#"MergedJul24"
#"MergedAug_v2"
#"Merged",
#"MergedAprTrees2013",
    ]

nstart = 0;
nRetries = 1 #How many times you retry if one fails. FIXME: for now do it manually, need to implement a way not to copy the same file twice
nRetries = nRetries+1 #actually the range is +1

for attempt in range(1,nRetries):
    nstart = 0;
    print "attempt number " +str(attempt)
    for channel in channels:
#        command_ls_channel = command_ls[:-1] + channel +'" | grep A | grep Mu'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep Mu | grep _A_'
        #        command_ls_channel = command_ls[:-1] + channel +'"'
        command_ls_channel = command_ls[:-1] + channel +'"'
        files = commands.getoutput(command_ls_channel).split('\n')
        print command_ls_channel
        print "channel " + channel + " files: "
        for file in files:
            size = len(files)
            if "Merged" in channel:
                #filename = str(re.findall(path + "*\.root" , file))[(int(len(path))+2):-2]
                filename = str(re.findall(".*\.root" , file))[(int(len(path))+int(len(channel))+3):-2]
            else: filename = str(re.findall("edmntuple.*\.root" , file))[2:-2]
            command_check_doubles = 'ls ' + localdir + filename
            doubles_check = commands.getstatusoutput(command_check_doubles)
            #if nstart==size: print " I think I'm the last one " + filename 
            if doubles_check[0]==512:
                nstart = nstart +1
                #print " is multiple " +str(nstart)
                command_cp = ""
                if (nstart % nSimultaneous ==0):
                    command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'"'
                    print "test once "+str(nstart)
                else:
                    command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'" &'
                #If it's not found try to get it
                print "check  "+str(doubles_check)
                os.system(command_cp)
#                print command_cp
            #print file
            #print filename

    

#print dir
#print command_ls
