import shlex
import subprocess
import os
import re

command='ls -l'
ss = shlex.split("javac -d . javalist/calculate.java")
yy = shlex.split("javac -d . junitlist/calculatetest.java")
args=shlex.split('java org.junit.runner.JUnitCore com.trustie.test.calculatetest')


# read document's name 
javals = []
junitls = []

fjava = open(os.path.abspath('/JavaTest/dirlist/javalist.txt'))
fjunit = open("/JavaTest/dirlist/junitlist.txt")

line = fjava.readline()
while line:
    subline= re.sub(r'\s',"",line)
    javals.append(subline)

    line = fjava.readline()
fjava.close()

line = fjunit.readline()
while line:
    subline = re.sub(r'\s',"",line)
    junitls.append(subline)

    line = fjunit.readline()
fjunit.close()

'''print(javals)'''
'''print(junitls)'''


#compiling commands
compilePrefixJava = "javac -d . /JavaTest/javalist/"
compilePrefixJunit = "javac -d . /JavaTest/junitlist/"

javaCommands = [compilePrefixJava+x for x in javals]
junitCommands = [compilePrefixJunit+x for x in junitls]
'''print(javaCommands)'''
'''print(junitCommands)'''
#compile
def compile():
    for x in javaCommands:      
        os.system(x)
    for x in junitCommands:     
        os.system(x)



