__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"
#import module os
import os
#import shell utilities
import shutil
from zipfile import ZipFile

def main():
    clean_cache()
    cache_zip(data_path, cache_path)
    cached_files()
    find_password(cached_files())
#opslaan definitie
currentPath = os.getcwd()
print(currentPath)
cache_path = os.path.join(currentPath, "cache")
data_path = os.path.join(currentPath, "data.zip")

#function no arguments
def clean_cache():
    if os.path.exists(cache_path):
    #if already exists, delete folder cache
        shutil.rmtree(cache_path)
    #create empty folder named cache in curr dir
    os.mkdir(cache_path)

clean_cache()

#specified path

#function w 2 arguments in specfc order
def cache_zip(zip_file_path, cache_dir_path):
    #unpack zipfile into clean cache folder
    #open the zip_file in read mode
    with ZipFile(zip_file_path, "r") as zip_ref:
        #extract all files to another directory
        zip_ref.extractall(cache_path)


#function no arguments(returns list of all the files in the cache)
def cached_files():
    #moet uiteindelijk n lijst opleveren dus
    files_list = []
    abs_path = os.path.abspath(cache_path)
    #for loop check every file make a path to every file
    #"path aangemaakt zodat hij absoluut blijft"   
    filenames = os.listdir(abs_path)
    print (filenames)
    for filename in filenames:
        filepath = os.path.join(abs_path, filename)
        files_list.append(filepath)
    #moet uiteindelijk gereturned worden
    print(files_list)
    return files_list

#definieer variabele word
word = "password"
#om list te bewaren die ik in cached_files hb gemaakt
list_of_files = cached_files()
#functie met een argument
def find_password(list_of_files):
    #itereer over files
    for file in list_of_files:
        with open(file, "r") as f:
            lines = f.readlines()
            print (lines)
            for line in lines: 
                word_in_line = line.split("\n")
                for detail in word_in_line:
                    if word in detail:
                        return detail[detail.find(" ")+1:]
            
                    
                    #use split method to extract word from given string
    

if __name__ == "__main__":
    main()