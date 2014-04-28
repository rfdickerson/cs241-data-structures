class Node (object):
    
    def __init__(self, letter):
        self.letter = letter
        self.children = [None] * 26
        self.isWord = False


class Trie (object):

    def __init__(self):
        self.headNode = Node(' ')

    def insert(self, word):
        # inserts word into the trie
        pass
    
    def isWord(self, word):
        # returns true if the word is an accepting node in the trie
        pass

if __name__ == "__main__":
    t = Trie()
    t.insert('cat')
    t.insert('cartoon')
    print 'cat is word?'
    print t.isWord('cat')
    print 'rabbit is word?'
    print t.isWord('rabbit')

            


