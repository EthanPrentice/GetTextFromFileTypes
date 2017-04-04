'''
Created on 4 Apr 2017

@author: Ethan
'''

import os
import glob

directoryInput=""
directoryOutput=""

def getDirectoryInput():
    global directoryInput
    directoryInput = raw_input("Enter directory to scan: ")
    try:
        os.listdir(directoryInput)
    except:
        print("Directory does not exist.")
        getDirectoryInput()
        
def getDirectoryOutput():
    global directoryOutput
    directoryOutput = raw_input("Enter txt file to export to: ")
    #print("Exporting to " + directoryOutput.split("/")[len(directoryOutput.split("/"))-1][:-4])
    if(directoryOutput[-4:]!=".txt"):
        print("Enter a txt document.")
        getDirectoryOutput()
    try:
        open(directoryOutput)
    except:
        print("File does not exist.")
        getDirectoryOutput()

while True:
    try:
        os.system('cls')
    except:
        os.system('clear')
        
    getDirectoryInput()
    getDirectoryOutput()

    fileType=raw_input("Enter a file type: ")

    folders = [name for name in os.listdir(directoryInput)]

    
    outputFile = open(directoryOutput, 'a')
    outputFile.truncate()
    outputString=""              
                
    for dirPath, dirNames, fileNames in os.walk(directoryInput):
        for fileName in [f for f in fileNames if f.endswith(fileType)]:
            outputFile.write("\n\n\n----"+fileName[:-len(fileType)]+"----\n\n\n")
            outputFile.write(open(dirPath + "/" + fileName).read())
            print os.path.join(dirPath, fileName)
        

    #outputFile.write(outputString)
    outputFile.close()
    print("Info added to output file.")
    while True:
        runAgain=raw_input("Enter another?(y/n): ")
        if runAgain=='y':
            break;
        else: 
            if runAgain=='n':
                exit(0)
            else:
                print("Unknown value.")
        