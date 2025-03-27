deff = list(open("VirusDataBaseHash.bav", 'r').readlines())

# print(deff)

for i in deff:
    xyz = open("hashes2.unibit",'a').writelines(i[0:64]+'\n')
    abc = open("virusinfo2.unibit", 'a').writelines(i[65:len(i)])


#making the script for hashes along with the info 

