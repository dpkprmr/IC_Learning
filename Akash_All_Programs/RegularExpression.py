import re

Nameage ="Janice is 22 and Theon is 33 and Gabrial is 44 and Joe is 21"

ages = re.findall('\d{1,3}',Nameage)
names = re.findall('[A-Z][a-z]*', Nameage)
print(ages)
print(names)
agedict = {}

# \w [a-zA-Z0-9_]
x = 0
for eachname in names:
 agedict[eachname] = ages[x]
 x= x+1
print(agedict)

#  Finding a word in string using Regex
if re.search("inform","We need to inform about our mental health"):
    print("Search is working fine")

allinform = re.findall("inform",'we need to inform him to inform her')

for variable in allinform:
    print(variable)


# get start and ending index  of a string
str = "My name is Akash and Akash"

for variable in re.finditer("Akash",str):
     x= variable.span()
     y= variable.start()
     print(x)
     print(y)

# Match words with particualr pattern
strg = "Sat, Mat, Pat, Bat"
allfind = re.findall("[SMPB]at", strg)
allfind2 = re.findall("[h-z]at", strg)
print(allfind)
for variable in allfind:
    print(variable)

# Replace a word
strgw = "Sat, Mat, Pat, Bat"
regex = re.compile("[M]at")
food = regex.sub("Food", strgw)
print(food)

randstr = '''My Name is Akash
I am not that good in python
trying to be good
'''
print(randstr)

regex = re.compile("\n")
randstrnew = regex.sub(" ",randstr)
print(randstrnew)

string = "Akash is a good boy also Akash is also a bad boy"
print("Matches:",len(re.findall(r"[A-Z][a-z]",string)))
print(re.findall(r"[A-Z][a-z]*",string))

phn = "444-555-6666"
if re.search("\d{3}-\d{3}-\d{4}",phn):
    print("It is a valid phone number")

fullname = "Akash Gupta"
if re.search("\w{0,20}\s\w{0,20}",fullname):
    print("Full name is valid")
else:
    print("Not valid")


email = "akash@gmail.com abc@123.com @ytr.com pop@09.com"
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
print("emailmatches:", len(re.findall("\w._%+-]{1,20}@[\w]{1,20}.[A-Za-z]{2,3}",email)))

# Problem Statement : Try using List and Dict to print words and their frequency in above string
string1 = "Twinkle twinkle little star. Star little galaxy."
Y = string1.split()
print(Y)
print("Frequency:",len(re.findall("[a]",string1)))




#Permission
perm = {1: "Read", 2: "write", 3: "execute", 4:"view", 5:"All_db"}
# #Group Permissions
Dict1 = {"G1":[1,2,3], "G2":[4,5,3]}
#Server Config
Dict2 = {"S1": [1.1,1.2, 1.3], "S2": [2.1,2.2, 2.3]}
#Users permissions
Dict3 = {"G1": ["U1","U2","U3"], "G2":["U2","U3","U4","U5"]}
# -----------------------TRY---------------------------------------------------------------
Dict4 = {"C1" : Dict3['G1'], "C2":Dict3['G2'],'A1':Dict1['G1'],'A2':Dict1['G2'],'B1':Dict2['S1'],'B2':Dict2['S2']}
Dict5 = {'C1' : Dict2['S1'],'C2':Dict2['S2']}
print(Dict4['C1'])
print(Dict4['A1'])
print(Dict4['B1'])
print(Dict5['C1'])








