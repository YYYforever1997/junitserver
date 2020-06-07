import sys
sys.path.append("/JavaTest/")
import runtest
import compilefile
import os

# obtain java class name
classlist = os.listdir("/JavaTest/com/trustie/junitest")
classls = []
for d in classlist:
    classls.append(d)

classdict = dict.fromkeys(classls,"None")
print(classdict)

def changetarget(targetClass):
    '''tranverse all class name to run the test '''
    prefix = "/JavaTest/com/trustie/junitest/"
    for k,v in classdict.items():
        if targetClass not in classdict.keys()== True:
                command = "mv"+" "+prefix+k+" "+prefix+targetClass
                os.system(command)
                print(k+" start!!!!!!!!!!!!!!!!!!!!!")
          #      runtest.run()
                print(k+" run!!!!!!!!!!!!!!!!!!!!!")
                command = "mv"+" "+prefix+targetClass+" "+prefix+k
                os.system(command)
        elif k!= targetClass:
                command = "mv"+" "+prefix+targetClass+" "+prefix+"cache.class"
                os.system(command)

                command = "mv"+" "+prefix+k+" "+prefix+targetClass
                os.system(command)

                print(k+" start!!!!!!!!!!!!!!!!!!!!!")
                runtest.run()
                print(k+" run!!!!!!!!!!!!!!!!!!!!!")

                command = "mv"+" "+prefix+targetClass+" "+prefix+k
                os.system(command)

                command = "mv"+" "+prefix+"cache.class"+" "+prefix+targetClass
                os.system(command)
        else:
            runtest.run()
           







