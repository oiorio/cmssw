#!/usr/bin/python
import os
import re
import sys
import commands
#import xmlrpclib

#os.command("grid-proxy-init")

dir = "/tmp/oiorio/"

channels = [#"WW",
#"TChannel",
#"WJetsSherpa",
#"TbarChannel",
#"SbarChannel",
#"TChannel",
#"SChannel",
#"TbarChannel",
#"SbarChannel",
#"WW",
#"WZ",
#"ZZ",
#"TToBENu",
#"TToBMuNu",
#"TToBTauNu",
#"TToBMuNu_unphys",
#"TToBTauNu_unphys",
#"TToBMuNu_0100",
#"TToBTauNu_0100",
#"TChannel_Q2Up",
#"TbarChannel_Q2Up",
#"TChannel_Q2Down",
#"TbarChannel_Q2Down",
#"TChannel_MassUp",
#"TbarChannel_MassUp",
#"TChannel_MassDown",
#"TbarChannel_MassDown",
#"TTBar_Q2Up",
#"TTBar_Q2Down",
#"TTBar_MassDown",
#"TTBar_MassUp",
#"W1Jet",
#"W2Jets",
#"W3Jets",
#"W4Jets",
#"WJets_Q2Down",
#"WJets_Q2Up",
#"ZJets",
"QCDMuBig",
#"TTBarFullLep",
#"TTBarSemiLep",
#"TChannel",
#"TbarChannel",
#"TWChannel",
#"TbarWChannel",
#"SChannel",
#"SbarChannel",
#"Mu_B13Jul",
#"Mu_A13Jul",
#"Mu_A06Aug",
#"Mu_v1_B1",
#"Mu_v1_B2",
#"Mu_A_22Jan",
#"Ele_A_22Jan",
#"Mu_B1_22Jan","Mu_B2_22Jan","Mu_B3_22Jan","Mu_B4_22Jan",
#"Ele_B1_22Jan","Ele_B2_22Jan","Ele_B3_22Jan","Ele_B4_22Jan",
#"Mu_C1_22Jan","Mu_C2_22Jan","Mu_C3_22Jan","Mu_C4_22Jan","Mu_C5_22Jan","Mu_C6_22Jan",
#"Mu_D1_22Jan","Mu_D2_22Jan","Mu_D3_22Jan","Mu_D4_22Jan","Mu_D5_22Jan","Mu_D6_22Jan",
#"Ele_C1_22Jan","Ele_C2_22Jan","Ele_C3_22Jan","Ele_C4_22Jan","Ele_C5_22Jan","Ele_C6_22Jan",
#"Ele_D1_22Jan","Ele_D2_22Jan","Ele_D3_22Jan","Ele_D4_22Jan","Ele_D5_22Jan","Ele_D6_22Jan",
#"Mu_C1",
#"Mu_D1",
#"Mu_D2",
#"Ele_D2",
#"Ele_D1",
#"Ele_C1",
#"Ele_C2",
#"Ele_C3",
#"Ele_A13Jul",
#"Ele_A06Aug",
#"Ele_B13Jul",
#"MergedJun27"
#"TChannel_Q2Up",
#"TChannel_Q2Down",
#"TbarChannel_Q2Up",
#"TbarChannel_Q2Down",
#"TChannel_MassUp",
#"TChannel_MassDown",
#"TbarChannel_MassUp",
#"TbarChannel_MassDown",
#"TTBar_Q2Up",
#"TTBar_Q2Down",
#"TTBar_MatchingUp",
#"TTBar_MatchingDown",
#"TTBar_MassUp",
#"TTBar_MassDown",
    ]

for channel in channels:
    command_ls_channel = "ls " +dir+ " | grep " +channel +" | grep part | grep root" 
    files = commands.getoutput(command_ls_channel).split('\n')
    listC = []  
    for file in files:
        if "Merged" in file: continue
        if "edmntuple" in file: continue
        listC.append(file) 
            
    #print listC        
    command_hadd = "hadd -f " + dir + channel +".root" 
    for l in listC:
        command_hadd = command_hadd + " " + dir + l
    command_hadd = command_hadd + " & "
    print command_hadd
    os.system(command_hadd)

