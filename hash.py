import hashlib 

#get Hash of file
def md5_hash(filename):
    with open(filename,"rb") as f:
        bytes = f.read()
        md5_hash = hashlib.md5(bytes).hexdigest()
        f.close()

    return md5_hash

print(md5_hash("f16.jpg"))  
##Generated hash 

# # Malware detction by Hash

# def malware_checker(path):
#     hash_malware_chck = md5_hash(path)

#     malware_hashes = open("virusfile.txt","r")
#     malware_hashes_read = malware_hashes.read().splitlines()
#     malware_hashes.close()

#     for check in malware_hashes_read:
#         if check == hash_malware_chck:
#             return True
#         else:
#             return False
        
# print(malware_checker("f16.jpg"))

# https://www.youtube.com/watch?v=Mk1hrtsYMwM&list=PLkzUkNupwT3S-lwWGfG6D5Xs2-hKuxXT2&index=7