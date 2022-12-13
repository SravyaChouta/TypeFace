def soundex_generator(t):
    t = t.upper()

    soundex = ""
    soundex += t[0]
    dictionary1 = {"BFPV": "1", "CGJKQSXZ": "2",
                  "DT": "3",
                  "L": "4", "MN": "5", "R": "6",
                  "AEIOUHWY": "."}
    
    for char in t[1:]:
        for key in dictionary1.keys():
            if char in key:
                code = dictionary1[key]
                if code != '.':
                    if code != soundex[-1]:
                        soundex += code

    soundex = soundex[:7].ljust(7, "0")
    return soundex


inputstr = input()
sndx = soundex_generator(inputstr)

file1 = open("2.txt","w")
L = ["Moorthy ", "Moorthi ", "Murthi ","sun ","son "]
file1.writelines(L)
file1.close()

file1 = open("2.txt","r")
for lines in file1.readlines():
    for words in list(lines.split()):
        wordsndx = soundex_generator(words)
        if wordsndx == sndx:
            print(words)
file1.close()