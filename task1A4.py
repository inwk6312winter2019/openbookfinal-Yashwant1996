test = open("Book2.txt",'r')
test = test.readlines()


def character_word_count(test):
  dict1=dict()
  for line in test:
    line=line.strip()
    line=line.lower()
    line=line.split()
    for word in line:
      if word not in dict1:
             dict1[word]=1
      elif word in dict1:
             dict1[word]+=1
  print(dict1)

character_word_count(test)
