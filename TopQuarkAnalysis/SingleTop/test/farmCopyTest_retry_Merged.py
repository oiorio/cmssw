#!/usr/bin/python
import os
import re
import sys
import commands
import subprocess
#import xmlrpclib

#os.command("grid-proxy-init")

#For Electron data and MC
se = "cmsse02.na.infn.it"
port = "8446"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/"

#For Muon data
#se = "stormfe1.pi.infn.it"
#port = "8444"
#path = "/cms/store/user/mmerola/SingleTop/Analysis/2013/"


dir ='"srm://'+se + ":" + port + "/srm/managerv2?SFN=" + path +'"'
command_ls = 'lcg-ls -b -D srmv2 -T srmv2 '+ dir
localdir = "/tmp/oiorio/"#WARNING this is set to Orso's tmp on lxplus machines!

nSimultaneous = 35

channels = [
#"MergedApr2013/"#MC
#"MergedTreesMVAID2013/Systs"#Systematics
"MergedTreesMVAID2013/"#Data+MC Nominal
#"MergedTreesMVAIDPhiCorr2013/"
#"MergedJul/MC"#MC
#"MergedJul/Data"#Electron Data
#"MergedJul/MC/Systs" #Syst
#"Merged_ReReco" #Muon Data
    ]

#Full path to folders, for manual access:

#Step 1: edm-ntuples
#Monte Carlo nominal samples
#lcg-ls -b -D srmv2 -T srmv2 "srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/MergedJul/MC/Systs"

#Monte Carlo systematics
#lcg-ls -b -D srmv2 -T srmv2 "srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/MergedJul/MC/Systs"

#Data, muons
#lcg-ls -b -D srmv2 -T srmv2 srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/user/mmerola/SingleTop/Analysis/2013/Merged_ReReco

#Data, electrons
#lcg-ls -b -D srmv2 -T srmv2 "srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/MergedJul/Data"

#Step 2: trees for analysis:
#Data+MC nominal
#lcg-ls -b -D srmv2 -T srmv2 "srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/MergedTreesMVAID2013/

#Systematics
#lcg-ls -b -D srmv2 -T srmv2 "srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/MergedTreesMVAID2013/systs


nstart = 0;
nRetries = 1 #How many times you retry if one fails. FIXME: for now do it manually, need to implement a way not to copy the same file twice
nRetries = nRetries+1 #actually the range is +1

for attempt in range(1,nRetries):
    nstart = 0;
    print "attempt number " +str(attempt)
    for channel in channels:
        command_ls_channel = command_ls[:-1] + channel +'"'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep Mu_D'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep QCD'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep Mass'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep TChannel'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep TW'
        command_ls_channel = command_ls[:-1] + channel +'" | grep TTBar'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep W | grep Jet'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep TbarChannel | grep Mass'
#        command_ls_channel = command_ls[:-1] + channel +'" | grep TbarChannel '
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
