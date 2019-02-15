def Sorted_words():
 file=open("Book1.txt","r+")
 wordcount={}
 for word in file.read().split():
    word = word.lower()
    if word.isalpha == True:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
