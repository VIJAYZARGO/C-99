import os
import shutil

#write the name of the directory here that needs to get sorted 
path = input('enter the name of the directory to be sorted :')

#this may create a properly organised list with all the file name that is there in the directory
list_of_files = os.listdir(path)

#this will go through each and every file
for file in list_of_files : 
    name, ext = os.path.splitext(file)

    #this is going to store the extension type
    ext = ext[1:]

    #this forces the next iteration if it is a folder
    if ext == '' :
        continue

    #this will move the files to the directory where the name 'ext' already exists
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    
    #if this will create a new directory if the directory does not already exist
    else : 
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)