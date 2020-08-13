#####################################################################################
# Awful program created by Andrew M Evans
# email: evansa@sonoma.edu
#
# Created date: Tues August 5th 7:28:45 PDT 2020
#
# This code runs all of the scripts created for visualization in one location
# This version is built for Linux file systems
# Make sure to remove the not domain changed .visit file from the data file path 
#####################################################################################

import DomainChange
import RenderCD
import RenderSD
import gifmaker
import ModuleLoad


ModuleLoad.loadv()
end = False
autoRender = True #controls the automation of the rendering process 
auto = False #toggles the menu on or off for this code
userIn = '2'
while end != True:
    if auto != True:
        userIn = raw_input('Domain '+'\n'+'1) Dynamic'+'\n'+'2) Dynamic with current files'+'\n'+'3) Static'+'\n')
    if userIn == '1' or userIn[0].lower() == 'd':
        DomainChange.Active()
        RenderCD.main(autoRender)
        end = True
        

    if userIn == '2' or userIn == 'Dynamic with current files' or userIn[0].lower() == 'c':
        RenderCD.main(autoRender)
        end = True

    if userIn == '3' or userIn[0].lower() == 's':
        RenderSD.smain(autoRender)
        end = True

    else:
        print 'Input not recognized, please try again.'+'\n'

gifmaker.gifCreate('n', 50, 'Output')

ModuleLoad.unloadv()



