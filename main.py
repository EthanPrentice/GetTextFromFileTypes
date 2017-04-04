'''
Created on 4 Apr 2017

@author: Ethan
'''

import os
import glob

directoryInput=""
directoryOutput=""

#Gets the input directory for getting files
def getDirectoryInput():
    global directoryInput
    directoryInput = raw_input("Enter directory to scan: ")
    try:
        #tests if input directory is real
        os.listdir(directoryInput)
    except:
        #if not real asks user to enter another directory
        print("Directory does not exist.")
        getDirectoryInput()
        
#Gets the output directory/file
def getDirectoryOutput():
    global directoryOutput
    directoryOutput = raw_input("Enter txt file to export to: ")
    
    #Makes sure that the input ends in .txt, if not asks user for new file path
    if(directoryOutput[-4:]!=".txt"):
        print("Enter a txt document.")
        getDirectoryOutput()
    
    #tests if file path is real
    try:
        open(directoryOutput)
    except:
        #If not real asks user for new file path
        print("File does not exist.")
        getDirectoryOutput()

#Will keep running loop until user tells it to exit or closes the window
while True:
    #clears screen on every loop
    try:
        os.system('cls')
    except:
        os.system('clear')
        
    #gets input/output paths
    getDirectoryInput()
    getDirectoryOutput()
    
    #gets the filetype to search for (.txt, .py, ...)
    fileType=raw_input("Enter a file type: ")

    #opens and clears file
    outputFile = open(directoryOutput, 'a')
    outputFile.truncate()           
                
    #loops through all files in directory and subdirectories
    for dirPath, dirNames, fileNames in os.walk(directoryInput):
        for fileName in [f for f in fileNames if f.endswith(fileType)]:
            #if file ended in correct file type add contents to output file
            outputFile.write("\n\n\n----"+fileName[:-len(fileType)]+"----\n\n\n")
            outputFile.write(open(dirPath + "/" + fileName).read())
            #output file directory
            print os.path.join(dirPath, fileName)

    #close & save output file
    outputFile.close()
    print("Info added to output file.")
    
    #ask user if they would like to continue
    while True:
        runAgain=raw_input("Enter another?(y/n): ")
        if runAgain=='y':
            break;
        else: 
            if runAgain=='n':
                exit(0)
            else:
                print("Unknown value.")
        
