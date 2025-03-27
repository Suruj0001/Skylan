import hashlib
import os
#Global Variable

malware_hashes = list(open("hashes2.unibit","r").read().split('\n'))
virusinfo = list(open("virusinfo2.unibit","r").read().split('\n'))

#Get Hash of File

def sha256(filename):
    with open(filename, 'rb') as f:
        bytes = f.read()
        sha256hash = hashlib.sha256(bytes).hexdigest()

        f.close()
        # print("sha256 hash")

    return sha256hash

#Malware Detection by Hash Algorithm
def malware_detection(pathoffile):
    global malware_hashes
    global virusinfo2

    hash_malware_chck = sha256(pathoffile)
    counter = 0

    for i in malware_hashes:
        if i == hash_malware_chck:
            return virusinfo2(counter)
        counter += 1

    return 0;

#Malware Detection in Folder
virusName = []

def folderScanner():

    #Get the list of files in the directory 
    path = "  "
    dir_list = os.listdir(path)
    
    fileN = ""

    for i in dir_list:
        fileN = path + "\\"+i
        if malware_detection(fileN) !=0:
            virusName.append(malware_detection(fileN) +" ::file :: " + i)

folderScanner()

print(virusName)

        
#https://www.youtube.com/watch?v=H0fg-6PUHhw&list=PLkzUkNupwT3S-lwWGfG6D5Xs2-hKuxXT2&index=9