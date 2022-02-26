from time import sleep


def KMPSearch(pat, txt):
    PAT = len(pat)
    j = 0                                                                   # index for pattern
    lps = [0] * PAT                                                         # lps holds the biggest values for pattern from prefix and suffix
    i = 0                                                                   # index for text
    TXT = len(txt)
    final = 0
    getLPS(pat, PAT, lps)                                                   # preprocessing the pattern aka find the biggest lps
    while i < TXT:
        if pat[j] == txt[i]:                                                # if the letters are the same, the increment raises by 1 for both
            print(i, "==", j, "[", pat[j], "==", txt[i], "]", i+1, j+1,)
            i += 1
            j += 1
            if j == PAT:                                                    # pattern was found
                if i == TXT:                                                # check to not be over bounds
                    final += 1
                else:
                    i = i - j
                    j = lps[j]
                if final == 1 or j != PAT:
                    i = i - j
                    j = 0
                    print("")
                else:
                    print("\n\tPattern spotted at index {}".format(i-j))
                    j = lps[j - 1]                                          # move the index from pattern by taking its value from lps with - 1 THIS IS ABOVE
        elif i < TXT and pat[j] != txt[i]:                                  # if letters are different but still did not browse the entire text
            print(i, "!=", j, "[", pat[j], "!=", txt[i], "]")
            if j != 0:                                                      # if j is not 0, does the same thing as above
                j = lps[j - 1]
                print("\n\tNew j is: ", j, "\n")
            else:                                                           # if j is 0, only i is incremented
                i += 1


def getLPS(pat, M, lps):
    length = 0                                                              # initialize length with 0
    lps[0] = 0                                                              # lps[0] is always 0
    index = []
    x = 0
    index.append(x)
    j = 1                                                                   # we start from 1
    while j < M:
        if pat[j] == pat[length]:                                           # if the i-th value is equal to the length
            length += 1
            lps[j] = length                                                 # the value from length is added in lps
            j += 1
            x += 1
        else:
            if length != 0:                                                 # if length is not 0, does the same thing as above
                length = lps[length - 1]
            else:
                lps[j] = 0                                                  # if there is no lps then all are 0
                j += 1
                x += 1
        index.append(x)
    print("\tIDX is:", index)
    print("\tLPS is:", lps)
    print("")


if __name__ == '__main__':
    answer = True
    while answer:
        print("1)\tInsert pattern\n"
              "2)\tInsert text\n"
              "3)\tShow current pattern and text\n"
              "4)\tExecute KMP algorithm\n"
              "5)\tExit program\n")
        choice = int(input("Choose an option: "))
        if choice == 1:
            pattern = input("\tThis will be searched throughout the text: ")
            print("")
        elif choice == 2:
            text = input("\tThis is the text which will be searched: ")
            print("")
        elif choice == 3:
            print("\tCurrent pattern and text: ")
            try:
                print("\t\tPattern: ", pattern)
                print("\t\tText: ", text)
            except:
                print("Error, variables are not yet defined\n")
        elif choice == 4:
            try:
                KMPSearch(pattern, text)
                print("\n")
            except:
                print("Error, missing the variables required to perform the algorithm\n")
        elif choice == 5:
            print("\tGo to sleep")
            sleep(1)
            print("1 Sheep")
            sleep(2)
            print("2 Sheep")
            sleep(2)
            print("3 Sheep")
            sleep(2)
            print("4 She.. *yawn*")
            sleep(3)
            print("\tGood night, sweet prince")
            answer = False
        else:
            print("\tINVALID choice, try again\n\n")
            sleep(2)
