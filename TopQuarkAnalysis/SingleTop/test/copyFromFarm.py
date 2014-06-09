#!/usr/bin/python
import os
import re
import sys
import commands
#import xmlrpclib

#os.command("grid-proxy-init")


se = "stormfe1.pi.infn.it"
port = "8444"
path = "/cms/store/user/oiorio/SingleTop/Fall12/"#Pisa SE configuration


se = "cmsse02.na.infn.it"
port = "8446"
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Summer12/"#Napoli SE configuration
path = "/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Fall12/ReRecoJun22/"#Napoli SE configuration

#"srm://cmsse02.na.infn.it:8446/srm/managerv2?SFN=/dpm/na.infn.it/home/cms/store/user/oiorio/2012/Summer12/Jul15/"

dir ='"srm://'+se + ":" + port + "/srm/managerv2?SFN=" + path +'"'
command_ls = 'lcg-ls -b -D srmv2 -T srmv2 '+ dir
localdir = "./"#Local directory for storage
localdir = "/tmp/oiorio/"#Local directory for storage


nSimultaneous = 50

channels = [
"MergedJul",
    ]

nstart = 0;

for channel in channels:
    command_ls_channel = command_ls[:-1] + channel +'"'
    files = commands.getoutput(command_ls_channel).split('\n')
    print command_ls_channel
    print "channel " + channel + " files: "
    for file in files:
        print file
        if "Merged" in channel:
        #if "Merged" in channel:
            #filename = str(re.findall(path + "*\.root" , file))[(int(len(path))+2):-2]
            filename = str(re.findall(".*\.root" , file))[(int(len(path))+int(len(channel))+3):-2]
        else: filename = str(re.findall("edmntuple.*\.root" , file))[2:-2]
        if "Mu_" in filename: continue
        print filename
        nstart = nstart +1
        if nstart % nSimultaneous ==0 :
            #print " is multiple " +str(nstart)  
            command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'"'
        else: command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'" &'
        #        command_cp = 'lcg-cp -b -D srmv2 -T srmv2 "srm://'+se + ":" + port + "/srm/managerv2?SFN=" + file + '" "'+ localdir + filename +'" &'
        os.system(command_cp)
        print command_cp
        #print file
        #print filename

    

#print dir
#print command_ls
