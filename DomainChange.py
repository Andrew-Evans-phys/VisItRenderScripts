#########################################################################################
# Awful program created by Andrew M Evans
# email: evansa@sonoma.edu
#
# Created date: Thur July 30th 9:02:12 PDT 2020
#
# This code converts .visit files with changing domains into files with constant domains
# This version is built for Linux file systems
########################################################################################
import os 
def Active():
    FVD = [[]]
    dn = 0

    configpath = __file__[:-len(__file__.split("/")[-1])] + "domainchangeconfig.input"
    altconfigpath = __file__[:-len(__file__.split("/")[-1])] + "rconfig.input"

    try:
        with open(configpath,'r') as f:
            l1 = f.readline()[:-1]
            l2 = f.readline()[:-1]
        print 'config file:'+'\n'+'line 1 '+str(l1)+'\n'+'line 2 '+str(l2)
    except IOError:
        print 'no config path found'
    userConfig = raw_input('Change Domain change config? (y/n) ')
    if userConfig[0].lower() == "y":
        iData = raw_input('initial data path ')
        oData = raw_input('output data path (hit enter to skip) ')
        if oData == '':
            with open(altconfigpath,'r') as f:
                f.readline()[:-1]
                oData = str(f.readline()[:-1])
                print oData
        with open(configpath,"w") as f:
            f.write(iData+'\n'+oData+'\n')
    else:
        with open(configpath,'r') as f:
            iData = f.readline()[:-1]
            oData = f.readline()[:-1]

    with open(iData,"r") as f:
        f.readline()
        for i in f.readlines():
            newdn = int(i.split("-")[2].split(".")[0])
            if newdn < dn:
                FVD.append([])
            dn = newdn 
            FVD[len(FVD)-1].append(i)

    for i in range(0, len(FVD)):
        with open(oData+'FVD'+str(i).zfill(3)+'.visit',"w") as f:
            f.write("!NBLOCKS "+str(len(FVD[i]))+'\n')
            for j in FVD[i]:
                f.write(str(j))
                print j





