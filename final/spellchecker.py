from trie import Trie

def loadDictionary(t):
    d = open('data/brit-a-z.txt','r')
    for w in d:
        wl = w.lower()
        t.insert(wl)
        pass
        
def testSentence(t,s):
    # get rid of punctuation
    s = s.replace('.','')
    s = s.replace(',','')
    s = s.split()
    for w in s:
        r = t.isWord(w)
        if not r:
            print w + ' is misspelled'

if __name__ == "__main__":
    t = Trie()
    loadDictionary(t)
    s = 'the color of the haus is blu.'
    testSentence(t,s)
    # note color is mispelled since we loaded a British dictionary
