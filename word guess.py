from random import shuffle
alphabets = ['q', 'w', 'e', 'r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v', 'b','n','m']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

again = 'y'
while again == "y":
    shuffle(alphabets)
    word = []
    i = 0
    n = int(input("How many words do you want for the word? "))
    while i < n:
        word.append(alphabets[i])
        i += 1
    s = ''.join(word)
    m = int(input("How many time you want to try? "))

    alphabets.sort()
    i = 0
    try1 = 0
    word = []
    while i < n:
        if try1 >= m:
            print("You've exceeded the no of tries")
            break
        else:
            inp = input(f"Enter {i+1}th Your  Letter of the Word: ")
            if s[i] == inp:
                print("Correct Letter\n")
                word.append(inp)
                i += 1
                try1 += 1
            else:
                print("Wrong Letter Try Again")
                for j in range(0, 25):
                    for k in range(0, 25):
                        if s[i] == alphabets[j] and inp == alphabets[k] and j <= k:
                            print("The letter is smaller")
                        elif s[i] == alphabets[j] and inp == alphabets[k] and j > k:
                            print("The letter is bigger")
                try1 += 1
    w = ''.join(word)
    if w == s:
        print(f"Congrats!!! You've Won The Game. The letter was {s}. You took {try1} tries.")
    again = input("Do you wanna play again?(y/n) ").lower()
