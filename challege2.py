
import regex
z=''
f=open("C:/Users/hind/Desktop/test.txt", "r")
txt='ZERtYURiERToPIT'
x = regex.findall("[^A-Z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]+", f.read())

for i in x:
	z+=i
