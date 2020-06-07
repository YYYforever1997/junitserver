import os
import re
import sys
sys.path.append(os.path.abspath('/JavaTest/'))
import compilefile


junitlist = compilefile.junitls


#junit running commands
junitPrefix = "java org.junit.runner.JUnitCore"
filePrefix = "com.trustie.test."
allfiles = ''

filelist = [filePrefix+re.sub(".java","",x) for x in junitlist]

for x in filelist:
    allfiles = allfiles +" "+ x
    
'''print(junitPrefix+allfiles)'''
def run():
   return os.system(junitPrefix+allfiles)     #run junit


