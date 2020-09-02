import string
from collections import Counter
alpha=list(string.ascii_lowercase)

			
alpha2=alpha*2	

x="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


y=''
for i in x :
	for a in alpha2 :
		if i==a :
			y+=alpha2[alpha2.index(a)+2]
			break
		elif i==" " or i=='.':
			y+=i
			break
			
		

with open("C:/Users/hind/Desktop/ocr.txt", "r") as f:
    text = f.read()
c = Counter(text)
res = c.most_common()[:-10-1:-1]




d = {}
for c in open("C:/Users/hind/Desktop/ocr.txt", "r").read():
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

#print(d)

sort = sorted(d.items(), key=lambda x: x[1])
for i in sort:
	print(i[0], i[1])


#print(y)			








