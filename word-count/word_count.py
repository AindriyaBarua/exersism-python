import re
import string
def word_count(text):
    # Remove whitespace and \n and toss into array
    #words = text.strip().replace("\n", " ").split(" ")
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    out = regex.sub(' ', text)
    # Remove empty strings
    words=[]
    words = text.strip().replace("\n", " ").replace('\t', ' ').replace('.', ' ').replace('_', ' ').replace('!', ' ').replace('&', ' ').replace('$', ' ').replace('%', ' ').replace('^', ' ').replace(',', ' ').replace(':', ' ').replace('@', ' ').lower().split(" ")

    words = filter(None, words)
    count = {}
    for word in words:
        count[word] = 1 if word not in count else count[word] + 1
    return count


