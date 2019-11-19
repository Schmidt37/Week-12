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

def ScoreFinder(players, scores, s):
    i=0
    for word in players:
        if players[i] == s:
            print("OUTPUT:", s, scores[i])
        elif i == len(players) and s not in players:
            print( "OUTPUT: Player not found")
        i+=1

def Union(list1, list2):
    for i in list2:
        list1.append(i)
    return list1

def Intersection(list1, list2):
    matchlist=[]
    for item in list1:
        for word in list2:
            if word == item:
                matchlist.append(word)
    return matchlist
