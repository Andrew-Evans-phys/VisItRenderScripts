######################################################################################
# Awful program created by Andrew M Evans
# email: evansa@sonoma.edu
#
# Created date: Tues August 3th 9:33:43 PDT 2020
#
# This code uses VisIt to render images
# This version is built for Linux file systems
# Make sure to remove the not domain changed .visit file from the data file path 
#####################################################################################
import sys
from os import path, remove, listdir, remove, chdir, mkdir, kill, system
import shutil
import gc
import subprocess
configpath = __file__[:-len(__file__.split("/")[-1])] + "rconfig.input"


#file adapter changes \ to \\ for windows
def Visitoff():
    pid = subprocess.check_output(["pidof",'engine_ser'])
    kill(int(pid),9)

def fileadapter(fileInput):
    i = 0
    name = ""
    while i < len(fileInput):
        if fileInput[i] == "\\":
            name += "\\\\"
            i += 1
        else:
            name += fileInput[i]
            i += 1
    return name    

def filepathcheck(path, oldpath):
    if path == "":
        return str(oldpath)
    else:
        return str(path)

def defaultcheck(readline):
    if readline == "Default \n":
        pass
    else:
        return readline

#configuration file class
class config:

    def makeConfig(self):
        global configpath
        self.oldfiletemp = __file__[:-len(__file__.split("/")[-1])] + "/Images/" 
        with open(configpath,"w") as f:
            self.pathtemp = fileadapter(raw_input("Path to VisIt site-packages? "))
            self.filetemp = fileadapter(raw_input("Data folder path? ")) #Make sure to remove the undomain changed visit file from the data file path 
            self.fileName = raw_input("Name of output file? ")
            self.imagefolder = raw_input("Image output folder? (if skipped an image folder will automatically be created in this directory) ")
            self.datatype = self.datatype = raw_input("Data type? (Temp, Ye, and Rho0Phys) ")
            f.write(str(self.pathtemp)+"\n"+str(self.filetemp)+"\n"+str(self.fileName)+"\n"+str(filepathcheck(self.imagefolder, self.oldimagefolder))+"\n"+str(self.datatype)+"\n") 
            check = raw_input("Set threshold bounds? (y/n) ")
            if check[0].lower() == "y":
                self.threshL = raw_input("Lower bound? ")
                self.threshU = raw_input("Upper Bound? ")
                f.write(str(self.threshL)+"\n"+str(self.threshU)+"\n")
            else:
                f.write("Default \n"+"Default \n")
            check = raw_input("Set var bounds? (y/n) ")
            if check[0].lower() == "y":
                self.varL = raw_input("Lower bound? ")
                self.varU = raw_input("Upper Bound? ")
                f.write(str(self.varL)+" \n"+str(self.varU)+" \n")
            else:
                f.write("Default \n"+"Default \n")

    def modConfig(self):
        print 'To skip hit enter \n'
        global configpath
        self.oldpathtemp = self.pathtemp
        self.oldfiletemp = self.filetemp
        self.oldfileName = self.fileName
        self.oldimagefolder = self.imagefolder
        self.olddatatype = self.datatype
        self.oldthreshL = self.threshL
        self.oldthreshU = self.threshU
        self.oldvarL = self.varL
        self.oldvarU = self.varU
        with open(configpath,"w") as f:
            self.pathtemp = fileadapter(raw_input("Path to VisIt site-packages? "))
            self.filetemp = fileadapter(raw_input("Data folder path? "))
            self.fileName = raw_input("Name of output file? ")
            self.imagefolder = raw_input("Image output folder? (if skipped an image folder will automatically be created in this directory) ")
            self.datatype = raw_input("Data type? (Temp, Ye, and Rho0Phys) ")
            f.write(str(filepathcheck(self.pathtemp, self.oldpathtemp))+"\n"+str(filepathcheck(self.filetemp, self.oldfiletemp))+"\n"+str(filepathcheck(self.fileName, self.oldfileName))+"\n"+str(filepathcheck(self.imagefolder, self.oldimagefolder))+"\n"+str(filepathcheck(self.datatype, self.olddatatype))+"\n")
            print 'Warning: if bounds are changed user must specify both'
            check = raw_input("Set threshold bounds? (y/n) ")
            if check[0].lower() == "y":
                self.threshL = raw_input("Lower bound? ")
                self.threshU = raw_input("Upper Bound? ")
                f.write(str(self.threshL)+"\n"+str(self.threshU)+"\n")
            else:
                f.write(str(self.oldthreshL)+"\n"+str(self.oldthreshU)+"\n")
            check = raw_input("Set var bounds? (y/n) ")
            if check[0].lower() == "y":
                self.varL = raw_input("Lower bound? ")
                self.varU = raw_input("Upper Bound? ")
                f.write(str(self.varL)+" \n"+str(self.varU)+" \n")
            else:
                f.write(str(self.oldvarL)+"\n"+str(self.oldvarU)+"\n")

    def getConfig(self):
        global configpath
        with open(configpath,"r") as f:
            self.pathtemp = f.readline()[:-1]
            self.filetemp = f.readline()[:-1]
            self.fileName = f.readline()[:-1]
            self.imagefolder = f.readline()[:-1]
            self.datatype = f.readline()[:-1]
            self.threshL = f.readline()[:-1]
            self.threshU = f.readline()[:-1]
            self.varL = f.readline()[:-1]
            self.varU = f.readline()[:-1]

    #This function just deletes the image folder, because VisIt automatically recreates the folder
    def clearImageFolder(self):
        if path.exists(self.imagefolder): 
            print listdir(self.imagefolder)
            print '####################################################\n# Warning anything in image folder will be deleted #\n####################################################'
            userConfig = raw_input("Clear image folder? (y/n) ")
            if userConfig[0].lower() == "y":
                print 'Images deleted:', listdir(self.imagefolder)
                shutil.rmtree(self.imagefolder)
                mkdir(self.imagefolder)
        else:
            mkdir(self.imagefolder)
c = config()
try:
    c.getConfig()
    sys.path.append(c.pathtemp)
    print(c.pathtemp)
    from visit import * 
except NameError:
    c.makeConfig()
    c.getConfig()
    sys.path.append(c.pathtemp)
    print(c.pathtemp)
    from visit import * 

def main(auto):
    c = config()
    if auto != True:
    #config menu (for the ease of user)
        if path.exists(configpath):
            userConfig = raw_input("Change configuration? (y/n) ")
            if userConfig[0].lower() == "y":
                c.getConfig()
                c.modConfig()
                c.getConfig()
                c.clearImageFolder()
            else:
                c.getConfig()
                c.clearImageFolder()
        else:
            c.makeConfig()
    else:
        c.getConfig()
    #sys.path.append(c.pathtemp)
    #print(c.pathtemp)
    #from visit import * 
    LaunchNowin()
    #opens VisIt
    print listdir(c.filetemp) #Problem HEHERHERHEHHEHERHER
    for i in sorted(listdir(c.filetemp)): #filepath thing 
        try: 
            if i.split(".")[1] == 'visit':
                visit.OpenDatabase(str(c.filetemp)+str(i))
                v = visit.GetView3D()
                v.viewAngle = 90
                print "The view is: ", v
                visit.SetView3D(v)
                visit.AddPlot("Volume", c.datatype) 
                visit.AddOperator("Threshold") 
                t = visit.ThresholdAttributes()
                if c.threshL == "Default ":
                    pass
                else:
                    t.lowerBounds = float(c.threshL)
                    
                if c.threshU == "Default ":
                    pass
                else:
                    t.upperBounds = float(c.threshU)
                    
                t.defaultVarName = c.datatype
                visit.SetOperatorOptions(t)
                b = visit.VolumeAttributes()
                if c.varL == "Default ":
                    b.useColorVarMin = 0
                else:
                    b.useColorVarMin = 1 
                    b.colorVarMin = float(c.varL)
                    
                if c.varL == "Default ":
                    b.useColorVarMax = 0
                else:
                    b.useColorVarMax = 1 
                    b.colorVarMax = float(c.varU)
                b.scaling = b.Linear  # Linear, Log, Skew
                visit.SetPlotOptions(b)
                visit.DrawPlots()
                a = visit.AnnotationAttributes()
                a.axes3D.visible = 0
                a.axes3D.bboxFlag = 0
                visit.SetAnnotationAttributes(a)
                #InvertBackgroundColor() #flips background of the plot to black
                s = visit.SaveWindowAttributes()
                s.outputToCurrentDirectory = 0
                s.outputDirectory = c.imagefolder
                s.fileName = c.fileName
                s.format = s.PNG
                s.progressive = 1
                visit.SetSaveWindowAttributes(s)
                name = visit.SaveWindow()
                print "name = %s" % name
                visit.ClearAllWindows()
                visit.DeleteAllPlots()
                visit.CloseDatabase(str(c.filetemp)+str(i))
                visit.ClearCacheForAllEngines()
                Visitoff()
                visit.CloseComputeEngine()
        except IndexError:
            print 'You got an index error!'
            #visit.ClearCacheForAllEngines()
            visit.CloseComputeEngine()
    print '###################\n# Render finished #\n###################'
    #How do you stop a memory leak? Pain, lots of pain...
    #creates a .gif file 
    visit.CloseComputeEngine()
    visit.Close()



