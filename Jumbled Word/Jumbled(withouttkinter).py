import os
import sys
from collections import defaultdict
print " ";
print "................................Jumbled ......................................";
print "NOTE : Please make sure, you enter all the letters necessary to make the word!";
print " ";
print " ";
word=raw_input("Enter the word: ")
print " ";
#word = sys.argv[1]
word1 = word
#print word1


leng=len(word)
no = leng
chek=''
dict = defaultdict(list)

    #word=raw_input("Enter the : ")
word = word.lower()
word = sorted(word)
word = ''.join(word)
word = "\n"+word
word = word.replace(" ", "")
file = open("C:\Python27\Jumbled\Dictionary.txt", "r")
line = file.readline()
print " "
count = 0;
while line:
     if(line!=None):
         line = file.readline()
         j = line
         line = sorted(line)
         line = ''.join(line)
         j = ''.join(j)
         k = sorted(j)
         k = ''.join(k)
         k = k.lower()
         if (word==k):
             if(count<1):
                    print "Solution : "+j+"\n",
             count=count+1;
             if(count>1):
                 print "Another Combnation : "+j
             if(j=="mazahir"):
                    print "'Mazahir' here! :), Hope you liked my program :D"

             #dict[word].append(k)
file.close()

fo = open("C:/Mazahir/now.txt", "w")
line = fo.write( j )
fo.close()

file = open("C:/Mazahir/now1.txt", "w")
file.write( str(no) )
file.close()
