import os

for i in range(0,100):   
    folder_path = f"lec22OSModule/Tutorial {i+1}"
    #print(folder_path)
    os.rmdir(folder_path) # remove dir/folders also which are empty
#os.remove() remove a file

   


    