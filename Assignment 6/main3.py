wordlist = [line.strip() for line in open('wordlist.txt')]
for word in wordlist:
    if len(word) == 5 and word[:2]=="ap" and word[-2:]=="le":
        print(word)
    # if len(word)==5 and word.endswith("le") and word.startswith("ap"):
    #     print(word)