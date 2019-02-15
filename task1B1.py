import sys
import collections

def top_20_common_words(textfile, top=10):    
    """  text file IS book1 here """
  textfile = open(textfile)
    text = textfile.read().lower()
    textfile.close()
    words = collections.Counter(text.split()) # how often each word appears

    return dict(words.most_common(top))

filename = sys.argv[0]
top_20_common_words('Book1.txt')

