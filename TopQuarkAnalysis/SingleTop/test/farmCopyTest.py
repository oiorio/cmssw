#!/usr/bin/python
import os
import re
import sys
import commands
#import xmlrpclib

#os.command("grid-proxy-init")


se = "cmsse02.na.infn.it"
port = "8446"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/Apr06/"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/Apr05/"

#se = "stormfe1.pi.infn.it"
#port = "8444"
#path = "/cms/store//user/oiorio/SingleTop/Fall12/gouranga/"

dir ='"srm://'+se + ":" + port + "/srm/managerv2?SFN=" + path +'"'
command_ls = 'lcg-ls -b -D srmv2 -T srmv2 '+ dir
localdir = "/tmp/oiorio/"
#"srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Summer12/Jul15/"

nSimultaneous = 50

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
#"TbarChannel_Q2Up",
#"TChannel_Q2Down",
#"TbarChannel_Q2Down",
#"WJetsBig",
#"WJets",
"W3Jets",
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
#"MergedJun27"
#"MergedJul24"
#"MergedAug_v2"
#"MergedNovTrees",
    ]

nstart = 0;

for channel in channels:
    command_ls_channel = command_ls[:-1] + channel +'"'
    files = commands.getoutput(command_ls_channel).split('\n')
    print command_ls_channel
    print "channel " + channel + " files: "
    for file in files:
        if "Merged" in channel:
            #filename = str(re.findall(path + "*\.root" , file))[(int(len(path))+2):-2]
            filename = str(re.findall(".*\.root" , file))[(int(len(path))+int(len(channel))+3):-2]
        else: filename = str(re.findall("edmntuple.*\.root" , file))[2:-2]
        nstart = nstart +1
        if nstart % nSimultaneous ==0 :
            #print " is multiple " +str(nstart)  
            command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'"'
        else: command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'" &'
        #        command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'" &'
        os.system(command_cp)
        #print command_cp
        #print file
        #print filename

    

#print dir
#print command_ls
