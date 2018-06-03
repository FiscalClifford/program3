#Programming Assignment 3
#Classification stage
#Brennan Giles

import sys, os, random, re, math

# GLOBAL VARIABLES
ppTrainingFile = "preprocessed_train.txt"
ppTestFile     = "preprocessed_test.txt"

def selectMode():
    if sys.argv[1] == "training":
        mode = "training"
    elif sys.argv[1] == "test":
        mode = "test"
    else:
        print ("please use: python main.py <training> or <test>")
        sys.exit(1)
    return mode;

def main():

#Grab info from the files





    main()