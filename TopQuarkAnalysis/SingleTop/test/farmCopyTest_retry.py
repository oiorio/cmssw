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
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/Apr05/"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/May25/"
#path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/Feb05/"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/May26/"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/ReRecoJul28/"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/ReRecoJun22/"
#path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/"

##se = "stormfe1.pi.infn.it"
#port = "8444"
#path = "/cms/store//user/oiorio/SingleTop/Fall12/ReRecuAug01/"
#path = "/cms/store//user/oiorio/SingleTop/Fall12/gouranga/"
#path = "/cms/store/user/mmerola/SingleTop/Analysis/2013/"


dir ='"srm://'+se + ":" + port + "/srm/managerv2?SFN=" + path +'"'
command_ls = 'lcg-ls -b -D srmv2 -T srmv2 '+ dir
localdir = "/tmp/oiorio/"
#"srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=//cms/store/user/oiorio/SingleTop/Fall12/MergedMayTreesCutID2013/"
#"srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Summer12/Jul15/"

nSimultaneous = 35

channels = [
#"TChannel",
#"TbarChannel",
#"SChannel",
#"SbarChannel",
#"TWChannel",
#"TbarWChannel",
#"TTBar_MassUp"
#"TToBTauNu_unphys",
#"TToBTauNu_0100",
#"TToBTauNu",
#"TToBMuNu_unphys",
#"TToBMuNu_0100",
#"TToBTauNu",
#"TToBMuNu",
#"TToBENu",
#"WJetsSherpa",
#"TToBENu_unphys",
#"TToBENu_0100",
#"TChannel_MassDown",
#"TbarChannel_MassDown",
#"TChannel_MassUp",
#"TbarChannel_MassUp",
#"TTBar_MatchingUp",
#"TTBar_MatchingDown",
#"TTBar_MassUp",
#"TTBar_MassDown",
#"TTBar_Q2Up",
#"TTBar_Q2Down",
#"QCD_Pt_170to250_EMEnriched",
#"QCD_Pt_80to170_EMEnriched",
#"QCD_Pt_30to80_EMEnriched",
##"QCD_Pt_20to30_EMEnriched",
##"QCD_Pt_20to30_BCtoE",
#"QCD_Pt_30to80_BCtoE",
#"QCD_Pt_80to170_BCtoE",
#"QCD_Pt_170to250_BCtoE",
#"QCD_HT_40_100_GJets",
#"QCD_HT_100_200_GJets",
#"QCD_HT_200_400_GJets",
#"QCD_HT_400_inf_GJets",
#"TChannel",
#"TbarChannel",
#"TChannel_Q2Up",
#"TbarChannel_Q2Up",
#"TChannel_Q2Down",
#"TbarChannel_Q2Down",
#"TChannel_MassUp",
#"TbarChannel_MassUp",
#"TChannel_MassDown",
#"TbarChannel_MassDown",
#"WJetsBig",
#"WJets",
#"W1Jet",#
#"W2Jets",
#"W3Jets",
#"W4Jets",
#"SChannel",
#"SbarChannel",
#"TTBarFullLep",
#"TTBarSemiLep",
"QCDMuBig",
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
#"TbarWChannelThadWlep_Q2Down",
#
#"TbarWChannelFullLep_MassUp",
#"TbarWChannelFullLep_MassDown",
#"TWChannelFullLep_MassUp",
#"TWChannelFullLep_MassDown",
#
#"TbarWChannelThadWlep_MassUp",
#"TbarWChannelThadWlep_MassDown",
#"TWChannelThadWlep_MassUp",
#"TWChannelThadWlep_MassDown",
##
#"TbarWChannelTlepWhad_MassUp",
#"TbarWChannelTlepWhad_MassDown",
#"TWChannelTlepWhad_MassUp",
#"TWChannelTlepWhad_MassDown",
#"ZJets",
#"WW",
#"WZ",
#"ZZ",
#"MergedJun27"
#"MergedJul/MC/"
#"MergedJul/Data/"
#"MergedAug_v2"
 #"MergedApr2013"
#"MergedJulTreesMVAID2013"
#"MergedMayTreesCutID2013"
#"MergedMayTreesCutID2013",
#"MergedAprTrees2013",
#"MergedTreesMVAID2013/Systs",
    ]

nstart = 0;
nRetries = 1 #How many times you retry if one fails. FIXME: for now do it manually, need to implement a way not to copy the same file twice
nRetries = nRetries+1 #actually the range is +1

for attempt in range(1,nRetries):
    nstart = 0;
    print "attempt number " +str(attempt)
    for channel in channels:
#        command_ls_channel = command_ls[:-1] + channel +'" | grep _A'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep QCD'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep ZJets'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep TTBarFull'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep W | grep Jet'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep Channel'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep ZZ'
        command_ls_channel = command_ls[:-1] + channel +'"'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep T | grep Channel | grep Mass'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep Channel'
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
                print command_cp
            #print file
            #print filename

    

#print dir
#print command_ls
