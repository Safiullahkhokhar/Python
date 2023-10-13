import os

foldes = os.listdir("lec22OSModule") # list all folders which are present in data folder
print(foldes)

for folder in foldes: #all folders print 
    print(folder)
    print(os.listdir(f"lec22OSModule/{folder}"))# shows all folder 