import sys
import time
print("WARNING!!!!!\nThe code you are about to run requires shutil and pandas\nIf you dont have shutil or pandas installed, install it using pip.\nThe code can AND WILL spit out an error if \n1. shutil or pandas is not installed\n2.if healthcare_dataset.csv does not exist\n3. if a file titled answers.txt EXISTS. EXISTS.")
a = input("If these are all checked, type 'y'. if not, type 'n'. ")
if a == 'y' :
    exec(open('analysingthing.py').read())
elif a == 'n' :
    sys.exit
else :
    print("DIE")
    exuse = input("WHY YOU DO DIS?? ")
    print(exuse + "JUST THAT?? TAHT SUCKED.")
    time.sleep(1.0)