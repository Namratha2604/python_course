#players=open('tennis players','w')
# do some
# how to do iter
#players.close()
#IMPORTANT--IF A FILE IS OPENED WITH MODE(W), IT CLEARS THE EXISTING CONTENTS OF THE FILE
#SO IT IS BETTER TO USE THE MODE(a)Append to preserve the contentsin that writing happens at end
players=open("tennis players","w")
players.write("namratha\n")
players.write("Dimple\n")
players.write("shanmukh\n")
players.write("nitesh\n")
players.close()

countries=open("tennis countries","w")
countries.write("India\n")
countries.write("abhilasha\n")
countries.write("parth\n")
countries.write("adithi\n")
countries.close()

print(players)#players is file variable 
print(countries)

n=open("tennis players","r")
print(n)
pn=n.read()#read all contents of the file
print(pn)
n.close()

n=open("tennis players","r")
c=open("tennis countries","r")
pn,pc=[],[]
for l in n:
    pn.append(l[:-1])
n.close()

for l in c:
    pc.append(l[:-1])
c.close()
print(pn,"\n",pc)

name_country=[]
for u in range(len(pn)):
    name_country.append((pn[u],pc[u]))
print(name_country)

n2c=dict(name_country)
print(n2c)
print(n2c["namratha"])#created a dictionary andf asking for the pair corresponding to it


theFile.seek(pos, ref)
numRead = theFile.read(size)
theFile.readline
theFile.closed
theFile.tell()
