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

![hashtable density](https://raw.github.com/rfdickerson/CS241/master/A4/output.png "Hash Table Density")

## Help Resources
