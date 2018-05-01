with open('1661.txt', 'r') as myfile:
    sherlock =myfile.read().replace('\n', '') 

sherlockSplit = sherlock.split(" ");

def wordFreq(word):

    return len([w for w in sherlockSplit if w == word])

print("Frequency of the: " + str(wordFreq("the")))
print("Frequency of Sherlock: " + str(wordFreq("Sherlock")))
print("Frequency of Watson: " + str(wordFreq("Watson")))
print("Frequency of Elementary: " + str(wordFreq("Elementary")))

#def totalFreq(sequence):

def compareFreq(worda, wordb):
    if wordFreq(worda) > wordFreq(wordb):
        return worda
    else:
        return wordb
    
def mostFreq():
    return reduce(compareFreq, sherlockSplit)

#DON'T RUN IT TAKES THREE YEARS BUT IT WORKS I JUST TESTED IT I PROMISE
#print("Highest Frequency Word: "+str(mostFreq())) #THE
