import pandas as pd
# import stuff
import shutil
# our variables
source_file = 'healthcare_dataset.csv'
destination_file = 'blah.txt'
# copy stuff
shutil.copyfile(source_file, destination_file)
# turn txt to variable
with open('blah.txt', 'r') as file:
  txt = file.read()

  # Now, the content of 'your_file.txt' is stored in the 'file_content' variable
  print("File content successfully loaded:")
cancer = txt.count("Cancer")
obese = txt.count("Obesity")
arthritis = txt.count("Arthritis")
dia = txt.count("Diabetes")
ast = txt.count("Asthma")
hyp = txt.count("Hypertension")
male = txt.count("Male")
fema = txt.count("Female")
integer = male + fema
line1 = " was found "
line2 = " times"
print("Cancer was found " + str(cancer) + "times")
print("Obesity" + line1 + str(obese) + line2)
print("Arthritis" + line1 +str(arthritis) + line2)
print("Diabetes" + line1 + str(dia) + line2)
print("Asthma" + line1 + str(ast) + line2)
print("Hypertension" + line1 + str(hyp) + line2)
print("There are " + str(male) + " males")
print("There are " + str(fema) + " Females")
print("There are " + str(integer) + " all together.")