import math, numpy
#Part 1: definitions
#Define the analyses
analyses = ["NN7TeV",
            "BDT7TeV",
            "etaj7TeV"]

add8TeV = False
add8TeV = True
convertToVtb = True
#convertToVtb = False

if add8TeV:
    analyses.append("etaj8TeV")


#Define the central values 
centralValues = {}
centralValuesTheor = {}

#Define the uncertainty sources
uncertaintySources = ["stats",
                      "gen",
                      "JES",
                      "MCStats",
                      "JER",
                      "EleTrig",
                      "MuTrig",
                      "HadTrig",
                      "BTag",
                      "PU",
                      "MET",
                      "WLight",
                      "WHF",
                      "WJetsData",
                      "TTBar",
                      "QCDMu",
                      "QCDEle",
                      "OtherBackg",
                      "TTBarQ2",
                      "WJetsQ2",
                      "OtherQ2",
                      "TTBarMatching",
                      "PDF",
                      "lumi"
                      ]


#Define the values for each uncertainty and for each
uncertaintyValues = {};#NOTA BENE: UNCERTAINTIES HAVE TO GO IN RELATIVE VALUE 
for a in analyses:
    print a
    uncertaintyValues[a]={}
    for s in uncertaintySources:
        uncertaintyValues[a][s]=0.
        

uncertaintyCorrelations = {};#Correlations from -1 to 1 
for a in analyses:
    print a
    uncertaintyCorrelations[a]={}
    for a2 in analyses:
        print a2
        uncertaintyCorrelations[a][a2]={}
        for s in uncertaintySources:
            if a == a2:
                uncertaintyCorrelations[a][a2][s]=1.
            else:
                uncertaintyCorrelations[a][a2][s]=-2 #Unphysical value if not set 



#Part 2: setting the values
#Setting the central values in terms of SF WRT the Standard Model
central7TeV=64.57
central8TeV=87.20

centralValues["NN7TeV"]=67.96
centralValues["BDT7TeV"]=66.6
centralValues["etaj7TeV"]=70.0
if add8TeV:
    centralValues["etaj8TeV"]=83.6

centralValuesTheor["BDT7TeV"]=central7TeV
centralValuesTheor["NN7TeV"]=central7TeV
centralValuesTheor["etaj7TeV"]=central7TeV
if add8TeV:
    centralValuesTheor["etaj8TeV"]=central8TeV

#Setting the uncertainties
#NOTA BENE: IN THIS VERSION I TAKE THE UNCERTAINTIES IN RELATIVE VALUE!!!!!!!!!!!!!!!!

#NN 7TeV analysis
uncertaintyValues["NN7TeV"]["stats"]=0.5*(abs(0.061)+abs(0.052))
uncertaintyValues["NN7TeV"]["MCStats"]=0.5*(abs(0.016)+abs(0.022))

uncertaintyValues["NN7TeV"]["JES"]=0.5*(0.0033+0.0193)
uncertaintyValues["NN7TeV"]["JER"]=0.5*(0.0031+0.0055)
uncertaintyValues["NN7TeV"]["BTag"]=0.5*(0.0274+0.0307)
uncertaintyValues["NN7TeV"]["MuTrig"]=0.5*(0.0223+0.0233)
uncertaintyValues["NN7TeV"]["EleTrig"]=0.5*(0.006+0.007)
uncertaintyValues["NN7TeV"]["HadTrig"]=0.0125
uncertaintyValues["NN7TeV"]["PU"]=0.5*(0.0097+0.0089)
uncertaintyValues["NN7TeV"]["MET"]=0.5*(0.0002+0.0021)
uncertaintyValues["NN7TeV"]["WLight"]=0.5*(0.0023+0.0025)
uncertaintyValues["NN7TeV"]["WHF"]=0.5*(0.019+0.029)
uncertaintyValues["NN7TeV"]["WJetsData"]=0.000
uncertaintyValues["NN7TeV"]["TTBar"]=0.0085
uncertaintyValues["NN7TeV"]["QCDMu"]=0.008
uncertaintyValues["NN7TeV"]["QCDEle"]=0.5*(0.0039+0.0043)
uncertaintyValues["NN7TeV"]["OtherBackg"]=0.0033

uncertaintyValues["NN7TeV"]["TTBarQ2"]=0.5*(0.0326+0.0097)
uncertaintyValues["NN7TeV"]["WJetsQ2"]=0.5*(0.028+0.003)
uncertaintyValues["NN7TeV"]["OtherQ2"]=0.5*(0.004+0.01)
uncertaintyValues["NN7TeV"]["gen"]=0.0424

uncertaintyValues["NN7TeV"]["TTBarMatching"]=0.013
uncertaintyValues["NN7TeV"]["PDF"]=0.0115*1.29

uncertaintyValues["NN7TeV"]["lumi"]=0.022

#BDT 7TeV analysis
uncertaintyValues["BDT7TeV"]["stats"]=0.5*(abs(0.047)+abs(0.054))
uncertaintyValues["BDT7TeV"]["MCStats"]=0.031


uncertaintyValues["BDT7TeV"]["JES"]=0.006
uncertaintyValues["BDT7TeV"]["JER"]=0.001
uncertaintyValues["BDT7TeV"]["BTag"]=0.016
uncertaintyValues["BDT7TeV"]["MuTrig"]=0.019
uncertaintyValues["BDT7TeV"]["EleTrig"]=0.012
uncertaintyValues["BDT7TeV"]["HadTrig"]=0.015
uncertaintyValues["BDT7TeV"]["PU"]=0.004
uncertaintyValues["BDT7TeV"]["MET"]=0.002
uncertaintyValues["BDT7TeV"]["WLight"]=0.004
uncertaintyValues["BDT7TeV"]["WHF"]=0.5*(0.025+0.035)
uncertaintyValues["BDT7TeV"]["WJetsData"]=0.000
uncertaintyValues["BDT7TeV"]["TTBar"]=0.01
uncertaintyValues["BDT7TeV"]["QCDMu"]=0.017
uncertaintyValues["BDT7TeV"]["QCDEle"]=0.008
uncertaintyValues["BDT7TeV"]["OtherBackg"]=0.006

uncertaintyValues["BDT7TeV"]["TTBarQ2"]=0.009
uncertaintyValues["BDT7TeV"]["WJetsQ2"]=0.017
uncertaintyValues["BDT7TeV"]["OtherQ2"]=0.002
uncertaintyValues["BDT7TeV"]["TTBarMatching"]=0.004

uncertaintyValues["BDT7TeV"]["gen"]=0.046

uncertaintyValues["BDT7TeV"]["PDF"]=0.0115*1.3

uncertaintyValues["BDT7TeV"]["lumi"]=0.022

#Etalj 7TeV analysis
uncertaintyValues["etaj7TeV"]["stats"]=0.085
uncertaintyValues["etaj7TeV"]["MCStats"]=0.009

uncertaintyValues["etaj7TeV"]["JES"]=0.04
uncertaintyValues["etaj7TeV"]["JER"]=0.5*(0.0069+0.012)
uncertaintyValues["etaj7TeV"]["BTag"]=0.031
uncertaintyValues["etaj7TeV"]["MuTrig"]=0.016
uncertaintyValues["etaj7TeV"]["EleTrig"]=0.5*(0.0076+0.0094)
uncertaintyValues["etaj7TeV"]["HadTrig"]=0.03
uncertaintyValues["etaj7TeV"]["PU"]=0.5*(0.0033+0.0018)
uncertaintyValues["etaj7TeV"]["MET"]=0.0053
uncertaintyValues["etaj7TeV"]["WLight"]=0.00
uncertaintyValues["etaj7TeV"]["WHF"]=0.00
uncertaintyValues["etaj7TeV"]["WJetsData"]=0.059
uncertaintyValues["etaj7TeV"]["TTBar"]=0.033
uncertaintyValues["etaj7TeV"]["QCDMu"]=0.00895
uncertaintyValues["etaj7TeV"]["QCDEle"]=0.5*(0.0037+0.0029)
uncertaintyValues["etaj7TeV"]["OtherBackg"]=0.0054

uncertaintyValues["etaj7TeV"]["TTBarQ2"]=0.5*(0.04+0.021)
uncertaintyValues["etaj7TeV"]["WJetsQ2"]=0.00
uncertaintyValues["etaj7TeV"]["OtherQ2"]=0.0225
uncertaintyValues["etaj7TeV"]["TTBarMatching"]=0.0035

uncertaintyValues["etaj7TeV"]["gen"]=0.025
uncertaintyValues["etaj7TeV"]["PDF"]=0.025*1.3

uncertaintyValues["etaj7TeV"]["lumi"]=0.022


#Etalj 8TeV analysis
if add8TeV:
    uncertaintyValues["etaj8TeV"]["stats"]=0.026900779
    uncertaintyValues["etaj8TeV"]["MCStats"]=0.00689399

    uncertaintyValues["etaj8TeV"]["JES"]=0.0423071
    uncertaintyValues["etaj8TeV"]["JER"]=0.00683646
    uncertaintyValues["etaj8TeV"]["BTag"]=0.02540943
    uncertaintyValues["etaj8TeV"]["MuTrig"]=0.000199509
    uncertaintyValues["etaj8TeV"]["HadTrig"]=0.0
    uncertaintyValues["etaj8TeV"]["PU"]=0.0073079
    uncertaintyValues["etaj8TeV"]["MET"]=0.00321478

    uncertaintyValues["etaj8TeV"]["WLight"]=0.00
    uncertaintyValues["etaj8TeV"]["WHF"]=0.0
    uncertaintyValues["etaj8TeV"]["WJetsData"]=0.0210016

    uncertaintyValues["etaj8TeV"]["TTBar"]=0.00133264
    uncertaintyValues["etaj8TeV"]["QCDMu"]=0.00982039
    uncertaintyValues["etaj8TeV"]["QCDEle"]=0.0204897
    
    uncertaintyValues["etaj8TeV"]["OtherBackg"]=0.00243715
    
    uncertaintyValues["etaj8TeV"]["TTBarQ2"]=0.0
    uncertaintyValues["etaj8TeV"]["WJetsQ2"]=0.0
    uncertaintyValues["etaj8TeV"]["OtherQ2"]=0.024425
    uncertaintyValues["etaj8TeV"]["TTBarMatching"]=0.0

    uncertaintyValues["etaj8TeV"]["gen"]=0.0527564
    uncertaintyValues["etaj8TeV"]["PDF"]=0.0187277

    uncertaintyValues["etaj8TeV"]["lumi"]=0.026

    
#Setting the correlations:
#7TeV BDT vs NN
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["stats"]=0.740
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["gen"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["JES"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["MCStats"]=0.385

uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["JER"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["BTag"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["MuTrig"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["EleTrig"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["HadTrig"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["PU"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["MET"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["WLight"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["WHF"]=0.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["WJetsData"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["TTBar"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["QCDMu"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["QCDEle"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["OtherBackg"]=1.0

uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["TTBarQ2"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["WJetsQ2"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["OtherQ2"]=1.0

uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["TTBarMatching"]=1.0
uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["PDF"]=1.0

uncertaintyCorrelations["BDT7TeV"]["NN7TeV"]["lumi"]=1.0


#7TeV BDT vs 7TeV etalj
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["stats"]=0.7
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["gen"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["JES"]=0.2
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["MCStats"]=0.39

uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["JER"]=0.2
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["BTag"]=0.2
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["MuTrig"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["EleTrig"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["HadTrig"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["PU"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["MET"]=0.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["WLight"]=0.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["WHF"]=0.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["WJetsData"]=0.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["TTBar"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["QCDMu"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["QCDEle"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["OtherBackg"]=1.0

uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["TTBarQ2"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["WJetsQ2"]=0.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["OtherQ2"]=1.0

uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["TTBarMatching"]=1.0
uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["PDF"]=1.0

uncertaintyCorrelations["BDT7TeV"]["etaj7TeV"]["lumi"]=1.0


#7TeV NN vs 7TeV etalj
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["stats"]=0.6
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["gen"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["JES"]=0.2
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["MCStats"]=1.0

uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["JER"]=0.2
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["BTag"]=0.2
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["MuTrig"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["EleTrig"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["HadTrig"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["PU"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["MET"]=0.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["WLight"]=0.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["WHF"]=0.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["WJetsData"]=0.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["TTBar"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["QCDMu"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["QCDEle"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["OtherBackg"]=1.0

uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["TTBarQ2"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["WJetsQ2"]=0.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["OtherQ2"]=1.0

uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["TTBarMatching"]=1.0
uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["PDF"]=1.0

uncertaintyCorrelations["NN7TeV"]["etaj7TeV"]["lumi"]=1.0


if add8TeV:
    #7TeV BDT vs 8TeV etalj
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["stats"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["gen"]=1.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["JES"]=0.20
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["MCStats"]=0.0
    
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["JER"]=0.20
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["BTag"]=0.20
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["MuTrig"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["EleTrig"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["HadTrig"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["PU"]=1.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["MET"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["WLight"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["WHF"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["WJetsData"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["TTBar"]=1.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["QCDMu"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["QCDEle"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["OtherBackg"]=1.0
    
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["TTBarQ2"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["WJetsQ2"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["OtherQ2"]=0.0
    
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["TTBarMatching"]=0.0
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["PDF"]=1.0
    
    uncertaintyCorrelations["BDT7TeV"]["etaj8TeV"]["lumi"]=1.0
    
    #7TeV NN vs 8TeV etalj
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["stats"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["gen"]=1.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["JES"]=0.20
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["MCStats"]=0.0
    
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["JER"]=0.20
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["BTag"]=0.20
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["MuTrig"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["EleTrig"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["HadTrig"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["PU"]=1.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["MET"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["WLight"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["WHF"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["WJetsData"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["TTBar"]=1.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["QCDMu"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["QCDEle"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["OtherBackg"]=1.0
    
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["TTBarQ2"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["WJetsQ2"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["OtherQ2"]=0.0
    
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["TTBarMatching"]=0.0
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["PDF"]=1.0
    
    uncertaintyCorrelations["NN7TeV"]["etaj8TeV"]["lumi"]=1.0

    #7TeV etalj vs 8TeV etalj
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["stats"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["gen"]=1.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["JES"]=1.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["MCStats"]=0.0
    
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["JER"]=1.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["BTag"]=1.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["MuTrig"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["EleTrig"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["HadTrig"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["PU"]=1.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["MET"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["WLight"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["WHF"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["WJetsData"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["TTBar"]=1.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["QCDMu"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["QCDEle"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["OtherBackg"]=1.0
    
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["TTBarQ2"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["WJetsQ2"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["OtherQ2"]=0.0
    
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["TTBarMatching"]=0.0
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["PDF"]=1.0
    
    uncertaintyCorrelations["etaj7TeV"]["etaj8TeV"]["lumi"]=1.0

    
#set the ij->ji member of the matrix:
for u in uncertaintyCorrelations:
    for a in analyses:
        for s in uncertaintySources:
            if (uncertaintyCorrelations[u][a][s]==-2 and uncertaintyCorrelations[a][u][s]!=-2):
                uncertaintyCorrelations[u][a][s] = uncertaintyCorrelations[a][u][s]
                
#Part 3: defining the functions for the conversion from 
def convertCentralValueToVtb(obsXsec,theorXsec):
    return math.sqrt(obsXsec/theorXsec)

def convertUncToVtbUnc(obsXsec,theorXsec,Unc):
    return (Unc/theorXsec)*0.5*math.sqrt(theorXsec/obsXsec)


#Part 4:Testing the output
for u in uncertaintyValues:
    vtbequivalent = convertCentralValueToVtb(centralValues[u],centralValuesTheor[u])
    print "analysis {0}, vtb equivalent is {1}".format(centralValues[u],vtbequivalent)
    for s in uncertaintySources:
        print "analysis: {0} uncertainty: {1}".format(u,s) 
        print "vtb equivalent uncertainty value: {0}".format(convertUncToVtbUnc(centralValues[u],centralValuesTheor[u],uncertaintyValues[u][s]*centralValues[u]))
        for a in analyses:
             print "correlation on uncertainty \"{0}\" between {1} and {2}: {3}".format(s,u,a,uncertaintyCorrelations[u][a][s])
             print "rhoS1S2 = {0}".format(uncertaintyValues[u][s]*centralValues[u]*uncertaintyValues[a][s]*centralValues[a]*uncertaintyCorrelations[u][a][s])

#Part 5: Fully converting to Vtb

if convertToVtb:
    print "\n\n\n <<<<< now converting to vtb <<<<<\n\n\n"
    for u in uncertaintyValues:
        vtbequivalent = convertCentralValueToVtb(centralValues[u],centralValuesTheor[u])
        print "analysis {0}, vtb equivalent is {1}".format(centralValues[u],vtbequivalent)
        for s in uncertaintySources:
            print "analysis: {0} uncertainty: {1}".format(u,s) 
            uncertaintyValues[u][s]= convertUncToVtbUnc(centralValues[u],centralValuesTheor[u],uncertaintyValues[u][s]*centralValues[u])
            #        print "vtb equivalent uncertainty value: {0}".format(uncertaintyValues[u][s]) 
    print "\n\n\n"
    for u in uncertaintyValues:
        print "test analysis {0}".format(u)
        for s in uncertaintySources:
            print "vtb equivalent uncertainty value: {0}".format(uncertaintyValues[u][s]) 
            for a in analyses:
                print "correlation on uncertainty \"{0}\" between {1} and {2}: {3}".format(s,u,a,uncertaintyCorrelations[u][a][s])
                print "separate uncs: {0} vs {1} ; separate centralvals {2} vs {3} ".format(uncertaintyValues[u][s],uncertaintyValues[a][s],centralValues[u],centralValues[a])
                print "rhoS1S2 = {0}".format(uncertaintyValues[u][s]*centralValues[u]*uncertaintyValues[a][s]*centralValues[a]*uncertaintyCorrelations[u][a][s])

    print "\n\n\n <<< now converting central values <<< \n\n\n"
    for a in analyses:
        print "analysis {0} before: {1} ; vtb conv {2}".format(a,centralValues[a],convertCentralValueToVtb(centralValues[a],centralValuesTheor[a]))
        centralValues[a]=convertCentralValueToVtb(centralValues[a],centralValuesTheor[a])
        print "analysis {0} after: {1}".format(a,centralValues[a])





#Part 5:Implementing BLUE in a function:
def getCombinedValue(allAnalyses,allCentralValues,allUncertainties,allCorrelations):
    #Produce Correlation Matrix:
    if (len(allAnalyses)!= len(allCentralValues)) or (len(allAnalyses)!= len(allCentralValues)) or (len(allAnalyses)!= len(allCentralValues)) or (len(allAnalyses)!= len(allCentralValues)):
        print "ERROR! CHECK THE INPUT VECTORS SIZES!!!! THEY DO NOT MATCH WITH THE NUMBER OF ANALYSES!!!!"
        return -9999 
    #Initializing each element
    totalCorrelations = {}
    #nrow=0
    #ncol=0
    for c in allAnalyses:
        totalCorrelations[c] = {}
        for a in allAnalyses: 
            totalCorrelations[c][a] = 0
        #    totalCorrelations.append((x,y))
            

    #Starting the actual sum
    for c in allCorrelations:
        for a in allAnalyses:
            for s in allUncertainties[a]:
                #                print "syst{6} , analyses {0} , {1}, cen.values {2} , {3} , uncs {4} , {5}".format(c,a,)
                rhoS1S2 = allUncertainties[c][s]*allCentralValues[c]*allUncertainties[a][s]*allCentralValues[a]*allCorrelations[c][a][s]
                #            print "analyses {0} , {1}, syst. {2} , rhoS1S2 = {3}".format(a,c,s,rhoS1S2)
                totalCorrelations[c][a] = totalCorrelations[c][a]+rhoS1S2
                if(c==a): print "analysis: {0} unc {1} val {2} diag element{3}".format(c,s,rhoS1S2,totalCorrelations[c][a])

    nummatrix=[]
    for c in allAnalyses:
        tmpVector= []
        for a in allAnalyses:
            tmpVector.append(totalCorrelations[c][a])
        nummatrix.append(tmpVector)


    corrmatrix= numpy.matrix(totalCorrelations)
#    print "\n\n\n matrix of maps...\n\n\n"
#    print corrmatrix
#    print "\n\n\n now magic!!! \n\n\n"
    print "\n\n\n correlation matrix\n\n\n"
    print "   {0}".format( allAnalyses )
    corrmatrix= numpy.matrix(nummatrix)
    print corrmatrix

    invmatrix = corrmatrix.getI()
    print "\n\n\n inverse matrix\n\n\n"
    print "   {0}".format( allAnalyses )
    print invmatrix

    print "\n\n inf matrix sum \n\n"
    print "total: {0}".format(invmatrix.sum())
    sumtot = invmatrix.sum()
    print "by row: {0} ; by column: {1}".format(invmatrix.sum(0),invmatrix.sum(1))
    print "normalized by row: {0} ; normalized by column: {1}".format(invmatrix.sum(0)/sumtot,invmatrix.sum(1)/sumtot)

    rowweightmatrix = invmatrix.sum(0)/sumtot
    colweightmatrix = invmatrix.sum(1)/sumtot

    weightsNum = (invmatrix.sum(0)/sumtot).getA()
    weights = {}
    i =0
    print weightsNum[0][2]
    for a in allAnalyses:
    #    print weightsNum[0][i]
        weights[a]= weightsNum[0][i]
        i=i+1
    print weights    

    finalValue =0.
    for a in allAnalyses:
        finalValue = finalValue + allCentralValues[a]*weights[a]
        print "analysis: {0} value: {1} weight: {2} finalValue: {3} ".format(a,allCentralValues[a],weights[a],finalValue)

    print " final value is :"
    print finalValue

    finalError = math.sqrt(rowweightmatrix*(corrmatrix*colweightmatrix))
    print " final error is :"
    print finalError
    
    #    for i in range(0,len(invmatrix)):
    
    
    return [finalValue,finalError]

#Part 5:Implementing BLUE in a function:
def getCombinedValueIterativeBlue(allAnalysesIter,allCentralValuesIter,allUncertaintiesIter,allCorrelationsIter):
    iter = 0 
    print " starting iterative BLUE, iteration #{0}".format(iter)
    Result = getCombinedValue(allAnalyses=allAnalysesIter,
                           allCentralValues=allCentralValuesIter,
                           allUncertainties=allUncertaintiesIter,
                           allCorrelations=allCorrelationsIter)
    print "result with plain BLUE is is {0} , uncertainty is {1}".format(Result[0],Result[1]) 

    newCentralValues= allCentralValuesIter
    newUncertainties= allUncertaintiesIter
    ResultNew = Result
    while abs(ResultNew[0]-Result[0]) > -1:
        #print " test condition:{0}".format( abs(ResultNew[0]-Result[0]) < (Result[1]*0.1))
        Result = ResultNew
        iter = iter + 1
        print "  iteration #{0} ".format(iter)
        for v in allCentralValuesIter:
            scaleFactorCV = Result[0]/allCentralValuesIter[v]
            for u in allUncertaintiesIter[v]:
                print " unc {0} was {1}".format(u,newUncertainties[v][u] )
                newUncertainties[v][u] = newUncertainties[v][u]*scaleFactorCV
                print " now is {0} ".format(newUncertainties[v][u] )
            newCentralValues[v] =  Result[0]
        ResultNew=getCombinedValue(allAnalyses=allAnalysesIter,
                                   allCentralValues=newCentralValues,#allCentralValuesIter,
                                   allUncertainties=newUncertainties,
                                   allCorrelations=allCorrelationsIter)
        print "result at iteration #{0} is {1} , uncertainty is {2}".format(iter,ResultNew[0],ResultNew[1]) 
        print "previous result was {0} , uncertainty {1} ".format(Result[0],Result[1]) 
        if (abs(ResultNew[0]-Result[0]) < (ResultNew[1]*0.1)): break      

    return ResultNew

#getCombinedValue(allAnalyses=analyses,
#                       allCentralValues=centralValues,
#                       allUncertainties=uncertaintyValues,
#                       allCorrelations=uncertaintyCorrelations)

print getCombinedValueIterativeBlue(allAnalysesIter=analyses,
                       allCentralValuesIter=centralValues,
                       allUncertaintiesIter=uncertaintyValues,
                       allCorrelationsIter=uncertaintyCorrelations)

def ratioCombined(allAnalyses,allCentralValues,allUncertainties,allCorrelations):
    #Default values, we know they are those ones moreless... 
    num = 83.6
    errnum = 7.8
    den = 67.2
    errden = 6.1
    corrnumden = 0.55

    return [num/den,(errnum*errnum / (den*den)) + (errden*errden*num*num / (den*den*den*den) ) - (errnum*errden*num/(den*den*den))*corrnumden]

print "Ratio is {0}".format(ratioCombined(allAnalyses=analyses,
                       allCentralValues=centralValues,
                       allUncertainties=uncertaintyValues,
                       allCorrelations=uncertaintyCorrelations))
