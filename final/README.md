CS241 Final Exam
===================

Posted: Monday  April 28
Due:    Friday  May 2

Rules
--------

+ You are to work alone on these problems
+ You cannot look for solutions (code) to these problems

Text Archiver
----------------

+ Fundamental Data Structure: Associative array (Dictionary)
+ Deliverable: textarchiver.py

You are tasked to create a class for compression and decompression of text for ebooks. Plain-text books encoded as a long string will serve as input to the compress method. As new candidate prefix strings are discovered that are not already in the dictionary, those prefix candidates will be appended to the table. Inside of the data directory is Oliver Twist by Charles Dickins.  You will employ one of the most popular and oldest entropy encoders called the LZW algorithm. The encoding step works as follows:

+ Assume a dictionary is initially empty and used as a symbol table
+ For every character in an input string:
+ Append the character to a candidate 'prefix' string
+ If prefix exists already exists in the dictionary, continue
+ Otherwise, add the prefix to the dictionary with a unique number id describing it
+ Next, place that prefix symbol down to output, and clear the prefix string, and repeat
    
For decoding the compressed output:

+ Flip the key-value pairs in the dictionary with:
+ decodeTable = {y:x for x,y in prefixes.iteritems()}
+ For each integer in the input,
+ Append the character value found in the decodeTable

I was able to achieve roughly 15% compression ratio using the LZW algorithm for this text. Assume spaces and other white space as well as all punctuation are symbols like any other letter.

FAQ:

+ Does the decompressed text have to be exactly the same as the original? Do I need to consider punctuation, whitespace, and case?

> Yes, treat every symbol whether it be a letter or whitespace as a symbol in the prefix string.

+ What exactly is stored in the prefix dictionary?

> For the compression stage, you should store the prefixes as keys, and ids as the value. During decompression the whole dictionary is flipped- so ids become the keys, and the prefixes the values.

+ I got a compression ratio of 0.00011, is that good?

> If you got that kind of compression ratio, you have created one amazing entropy encoder! More likely, however, your decompressed string does not match your input exactly.

+ I got a compression ratio of 0.158, is that good?

> That's what I got, too. If you get below 20%, I think you're good. Let me know if you get something in the 10% range, though.

Signal Processing
----------------------

+ Fundamental Data Structure: Circular Buffer
+ Deliverable: circularbuffer.py

Many signal processing algorithms such as for audio and images, use circular buffers. One reason that circular buffers are used is that they are efficient for inserting and removing samples into a buffer without requiring dynamic allocation of memory during run-time. The values in the buffer create a time-window of samples that have been inserted recently. FIR filters are generally used for all sorts of applications such as smoothing, noise removal, and blurring of the data. We will use our circular buffer to implement an FIR filter.

Circular buffers are essentially fixed-size arrays. Logically, they are a specific kind of queue that stores values conceptually in a ring. The logical beginning and end of the buffer changes with every insert and deletion of values. Upon initialization, the circular buffer is filled with 0's. Should the circular buffer be filled, and a new value is pushed into the queue, the beginning value of the queue is removed. If the circular buffer is filled and a new value is inserted, the value in the beginning of the buffer is removed from memory. The value for the start position can be represented as an integer index. Either an end index or a length of the buffer can be stored to determine the end of the buffer. I recommend using the modulus operator for keeping indices within the size of the array.

![Circular Buffer](data/queue.gif)

FAQ

+ ***What should you pop when the circular buffer is empty?***

> Zero 

+ ***What exactly happens when I push into a filled buffer?***

> consider the array

> [10,8,3,12]

> s is at 1, so the logical view of the buffer would therefore be [8,3,12,10]

> You push 20 into the buffer

> the array now looks like:

> [10,20,3,12]

> s is now 2, therefore the logical view of the buffer is now [3, 12, 10, 20]

Spell Checker
---------------------

+ Fundamental Data Structure: Trie
+ Deliverable: trie.py

Many operations require very fast lookups of strings. One classic application of this is for spell checking in an application. Spell checking should be executed after the completion of writing each word. Checking to see if the word exists in a list of correctly spelled words becomes slow if the number of words in the dictionary are large. Therefore, typically a specific kind of data structure called a trie (named for reTrieval) is used for this purpose. The trie is a special kind of tree where there are 26 children for each node. Each node has a boolean flag for whether ending at that particular letter in the tree represents a correctly spelled word or not. If the next letter is a 'c', make sure that you visit the node stored at children[2]. You can remove all non-letter symbols such as apostrophes before adding to the trie, and also upon spell checking. 

![Circular Buffer](data/trie.png)

FAQ

+ My program is took 30 minutes to compress Oliver Twist

> This is an excellent example of how hashtables can speed things up. Make sure you use the prefix string as the key in the Dictionary, and the index value as the value. Not the other way around. O(1) vs O(n) really makes a difference, since you're doing that operation roughly n times. So you are dealing with O(1) vs O(n^2) total time.

+ There are some words with apostrophes or foreign characters , how do I handle that?

> A simple way to disregard any character that is not one of the 26 is to compute the ord of character (minus the appropriate offset). If the number is not between 0 and 25, then don't do anything just move onto the next character.

> There might be a line in the list of English words that is all whitespace. Disregard that one when loading the words into the trie. You will not be evaluated on French loan words with the accent aigu. However, they could be treated like a letter like any other.
