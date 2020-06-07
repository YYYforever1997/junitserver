import os

javapath = "/JavaTest/javalist"
junitpath = "/JavaTest/junitlist"

javadir = os.listdir(javapath)
junitdir = os.listdir(junitpath)

def lsdir():
    fjava = open("/JavaTest/dirlist/javalist.txt","w")
    fjunit = open("/JavaTest/dirlist/junitlist.txt","w") 

    for d in javadir:
        string = d+"\n"
        fjava.write(string)
    fjava.close()

    for d in junitdir:
        string = d+"\n"
        fjunit.write(string)
    fjunit.close()

