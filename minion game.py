'''
Minion Game
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
''' 

def minion_game(s):
    '''
    first we make a list of possible characters
    '''
    l1 = ['A','E','I','O','U']
    l2 = list('bcdfghjklmnpqrstvwxyz'.upper())
    li = []
    #counting the number of characters by making a list of vowels
    for i in range(len(s)):
        if s[i] in l1:
            for n in range(len(s)+1):
                li.append(s[i:n])
    #adding numbers expects those equal to ''
    count1  = 0
    for l in li:
        if l != '':
            count1 +=1
    
    #counting by consonents
    li = []
    for i in range(len(s)):
        if s[i] in l2:
            for n in range(len(s)+1):
                li.append(s[i:n])
    count2  = 0
    for l in li:
        if l != '':
            count2 +=1
    
    #now we're creating the logic for the proper output
    if count1 > count2:
        print(f"Kevin {count1}")
    elif count1 == count2:
        print('Draw')
    else:
        print(f"Stuart {count2}")
