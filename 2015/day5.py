select = input("1 or 2: ")

def VowelCheck(string):
    vowels = {"a": 1, "e": 1, "o": 1, "i": 1, "u": 1,}
    amount = 0
    for c in string:
        amount += vowels.get(c, 0)
    return amount >= 3
def DoubleLetter(string):
    for i, c in enumerate(string):
        if i != 0:
            if c == string[i-1]:
                return True
    return False
def InvalidStringCheck(string):
    invalid = {"ab": 1, "cd": 1, "pq": 1, "xy": 1}
    invStrings = 0
    for i, c in enumerate(string):
        if i != 0:
            j = string[i-1] + string[i]
            invStrings += invalid.get(j, 0)
            if  invStrings > 0:
                return False
    return True

if select == "1":
    with open("input_day5.txt") as f:
        strings = f.read().split("\n")
        niceStrings = 0
        for s in strings:
            if VowelCheck(s) and DoubleLetter(s) and InvalidStringCheck(s): 
                niceStrings += 1  
                
                
        print("There are " + str(niceStrings) + " nice strings")
            
        
def pair_no_overlap(s):
    #contains two instances of any pair of letters(aauaa but not aaa)    
    for i in range(len(s)-1):
        pair = s[i:i+2]
        if pair in s[i+2:]:
            return True
    return False
            
def repeating_spaced_letters(s):
    #contains a letter that repeats with 1 letter inbetween (xyx)
    for i in range(len(s)-2):
            if s[i] == s[i+2]:  
                return True
    return False

if select == "2":
    with open("input_day5.txt") as f:
        strings = f.read().split("\n")
        niceStrings = 0
        for s in strings:
            if pair_no_overlap(s) and repeating_spaced_letters(s):
                niceStrings += 1
        print("There are " + str(niceStrings) + " nice strings")
