import re

mystr=''' name = saatvik
mobile number = 812e789333
email id = akjsdjasd@gmail.com'''
print(mystr)
d=re.findall(r"d\{1,10}", mystr)
print(d)

print("email:", len(re.findall("[w._%+-]{1-20}@[[\w.-]{2,20}{A-Z}{a-z}{2,3}", mystr)))