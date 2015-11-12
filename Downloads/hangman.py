import numpy as np
words = ['train', 'barn', 'soccer', 'baseball', 'california', 'illinois', 'sports', 'luis martinez', 'elephant', 'dog', 'cat', 'running', 'kill']
done = 'False'
wrong = 0
progress = ['_']
word = np.random.choice(words)
print word
word = list(word)
print "The word is", len(word), "letters long"
length = len(word)
while (len(progress) != length):
    progress += "_"
progress = list(progress)
while progress != word:
    letter = raw_input('guess a letter ')
    word = str(word)
    if (word.find(letter) == -1):
        print 'that is not in the word'
        wrong += 1
    else:
        while (word.find(letter) != -1):
            pos = word.find(letter)
            progress[pos] = letter
            word[pos] = '_'
            print str(progress)
        print str(progress)

    
