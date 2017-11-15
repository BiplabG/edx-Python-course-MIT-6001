#Creating a dictionary
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    common = []
    for word in freqs:
        if freqs[word] == best:
            common.append(word)
    return (common, best)
    
def words_often(freqs, minTimes):
    result = []
    flag = True
    while flag:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            flag = False
    return result
