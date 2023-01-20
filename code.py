import re

ii = int(input())

for i in range(0,ii):
   txt = input()
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   print(txt)

# You are given a text of lines. The text contains && and || symbols. Your task is to modify those symbols to and, or words.



