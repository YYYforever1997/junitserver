import runtest
import compilefile
import sys
sys.path.append("/JavaTest/dirlist/")
import listdir

step1 = listdir.lsdir()
print("obtaining docs' names finished! \n")
step2 = compilefile.compile()
print("compiling file finished! \n")

#import multisource
#step3 = multisource.changetarget("calculate.class")
step3 = runtest.run()
print("running junit test finished! \n")


