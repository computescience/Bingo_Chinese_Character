# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:35:39 2018

@author: Michael
"""
import string
import random



def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

class CardMaker(object):
 
       # Tweaked so that it will fit in 80 columns...
 #wordstring = 'add land shall glass wrap catch chapter bell spell step dress chest length shelf fill drink thick print since grip wrist doll cross block strong'
  #words example:
    #words = ["爱","世","人","马","可","福","音","第",
          #"一","章","节","活","出","平","安","夜",
         # "圣","善","照","着","亲","婴","儿"]
 #words = ["add" ,"land","shall","glass","wrap","catch","chapter"]
 wordstring = input('Enter words with space in between')
 bingosize = int (input('Enter row number of bingo'))
 input_words = wordstring.split()
 bingo = int(bingosize**2)
 
 if bingo == len(input_words):
    words = input_words
 elif bingo < len(input_words):
    words = random.sample(input_words,bingo)

 elif bingo > len(input_words):
    print ('Enter', bingo-len(input_words), 'more words','or reduce row number of bingo to', int((bingosize)**(0.5)))
    words = [random_string(4) for i in range(bingo)]
#  print the words to double check   
 print ('Words to play are', words)
 print ('Size of bingo is', bingosize)
 maxlen = max([len(w) for w in words])
  #row = "|" + ("%%%ss|"%maxlen)*5 +"\n"
 spacer = "+" + ("-"*maxlen + "+")*bingosize + "\n"
  #template = (spacer + row)*5 + spacer
 #83 for 3 per page
  #row = "<tr>" + "<td align=center width=190 height=198><font size=30>%s</td>"*5 + "</tr>"
 row = "<tr>" + "<td align=center width=83 height=83><font size=>%s</td>"*bingosize + "</tr>"
 
 template = "<HTML><table border=1>" + row*bingosize + "</table></font>"+"</HTML>"
  
  
 def __call__(self, use_wild=False, template=None):
     if not template:
      template = self.template
      words = self.words[:]
      n = int(len(words)/2)
      random.shuffle(words)
     if use_wild:
      #words[12] = "*WILD*"
      words[n] = ""
      return template % tuple(words)
   
#Quick and dirty usage examples - may need to fix file paths:
def make_one_webpage():
    make_card = CardMaker()
    #people = ["John", "Jane", "Sally", "Mark"]
# the save path need to be changed
    with open("C:\\Users\\Michael\\Documents\\python\\Bingo\\bingo_1.htm", "w") as f:
     bingo_number = int(input('Enter bingo game numbers you want to play'))

     for person in range(bingo_number):
         f.write("%s:"%person)
         f.write("\n")
         f.write(make_card(use_wild=True).rstrip('\n'))
         
         #print (f, "%s:"%person)
         #print (f, make_card(use_wild=True))
    f.close()
make_one_webpage()

