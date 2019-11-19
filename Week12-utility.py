#https://github.com/Schmidt37/Week-12.git
#Andrew Schmidt
# CSCI 102- Section B
#Week 12 Part A

def PrintOutput(word):
    print("OUTPUT", word)

def LoadFile(filename):
    file= filename.open()
    filelines = file.readlines()
    file.close()
    filelist=[]
    for line in filelines:
        filelist.append(line)
    return filelist
