from Ler_spm import lerspm
import os

test = input("Name of file")
testVar = test + ".SPM"
print (testVar)
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    try:
        if '.SPM' in f:
            if testVar == f:
                lerspm(f)
            if testVar=="all.SPM":
                lerspm(f)
    except:
        pass
#lerspm("25101913.SPM")
