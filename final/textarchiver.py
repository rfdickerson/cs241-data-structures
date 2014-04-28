
class TextArchiver (object):

    def __init__(self):
        """ initialize an empty dictionary of prefix to integer index pairs """
        self.prefixes = {}

    def compress(self, s):
        """ s is a string to compress
        returns a list of integers for the compressed data
        """
        pass


    def decompress(self, s):
        """ s is a list of integers
        returns an uncompressed string of the original text
        """
        pass
         



if __name__ == "__main__":

    archive = TextArchiver()
    # load Oliver Twist
    with open('data/olivertwist.txt', 'r') as contentfile:
        content = contentfile.read()
    e = archive.compress(content)

    # compute the compression ratio
    c = float(len(e))/float(len(content))
    print "Compression ratio: " + str(c)
    print "Should be roughly 0.15"

    print "First 100 chars decompressed is:"
    decomp = archive.decompress( e)
    print decomp[0:100]
    
