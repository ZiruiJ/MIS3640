import random
import string

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        # INSERT CODE BELOW
        strippables= string.punctuation+ string.whitespace

        for word in line.split():
            word= word.strip (strippables)
            word= word.lower()

            hist[word]= hist.get (word, 0) + 1

            # if word in hist:
            #     hist [word]+=1
            # else:
            #     hist[word]= 1

        

    return hist

def most_common(hist ,excluding_stopwords= True):
    """Makes a list of word-freq pairs in descending order of frequency.
    excluding_stopwords: a boolean value. If it is True, do not include 
    any stopwords in the list.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    stop = process_file('session13/stopwords.txt', skip_header=True)
    print (stop)