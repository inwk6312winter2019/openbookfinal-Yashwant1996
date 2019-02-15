def count_the_article():
 count = {}
 for w in open('Book1.txt').read().split():
    if w in count:
        count[w] += 1
    else:
        count[w] = 1
 for word, times in count.items():
    print ("%s :  %d times" % (word, times))
count_the_article()

