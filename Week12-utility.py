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

def UpdateString(s, a, num):
    t = list(s)
    t[num]= a
    t=''.join(t)
    print("OUTPUT:", t)

def FindWordCount(list, s):
    n=0
    for i in list:
        if i== s:
            n+=1
    return n
