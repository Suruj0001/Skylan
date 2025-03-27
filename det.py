import hashlib


#Get hash of file
def md5_hash(filename):
    with open(filename, "rb") as f:
        bytes = f.read()
        md5hash = hashlib.md5(bytes).hexdigest()
        f.close()
    return md5hash

#Malware Detection by Hash
def malware_checker(pathoffile):
    hash_malware_check = md5_hash(pathoffile)
    counter = 0

    malware_hashes = list(open("hashes.txt","r").read().split('\n'))
    

    virusinfo = list(open("virus.info.txt","r").read().split('\n'))

    for i in malware_hashes:
        if i == hash_malware_check:
            return virusinfo[counter]
        counter += 1

    return 0

print(malware_checker("f16.jpg"))


                          