# Hashtable

## Overview

The hash table is the data structure used to implement an associative array which
maps keys to values. A hash function is used to compute an index value which is used for
finding the appropriate bucket to find the key-value pair in the collection.
This indexing allows the hash table to achieve O(1) lookup times in many cases.
However, this may not always be true.  The hash function may map
different key values to the same bucket- this is called a collision. In this
case, hash tables often chain key-value pairs into a linked list or array for
linear lookup. Collisions should be minimized of course because lookups will
degrade to O(n) time in the worst case.

## Specification

You are tasked to creating a hash table in Python that has similiar behavior to
a Dictionary with most of the methods and operator syntax. 

+ Create a Node class with a key, value, and nextNode attributes.
+ Create or import in a LinkedList class 
+ Your HashTable class should take a hashFunction and number of buckets (n) as the argument
+ Your constructor should create n linkedlists, 1 per bucket
+ When inserting a key-value pair, append the node to the end of the linked list

Refer to the template in hashtabletemplate.py

## Visualization for the Hash Table density

Next, we will plot the number of elements that are stored for each of the buckets in the hash table. 

+ Create a new Python source file
+ Use open to open the uscities.txt file
+ Iterate through each of the city entries, split base of commas, and insert the second field (the city name) as the key. You can set the value to anything you want like the lat and lng.
+ Use your getNumBuckets function to allow you to iterate over each of the buckets and return the size
+ Dump the results to a new datafile - the bucket ID and the count
+ Use GNUplot, Matlab, R, Excel, SPSS, etc to load the file and render a barplot (histogram) for the hashtable.



![hashtable density](https://raw.github.com/rfdickerson/CS241/master/A4/output.png "Hash Table Density")

## Help Resources
