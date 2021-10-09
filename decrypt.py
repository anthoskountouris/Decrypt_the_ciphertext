from collections import Counter

string =  """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
    bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
    ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
    yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
    lmird jk xjubt trmui jx ibndt
    wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
    iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
    vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
    wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
    jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
    ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
    mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
    bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
    wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
    riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb""".upper()


# Python3 code to remove whitespace
stringNoSpaces = string.replace(" ", "").replace('\n', '')

counter = Counter(stringNoSpaces)
letters = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

# for i in range(len(counter)):
#     if counter.values(i+1) > counter.values(i)

# print(counter.values())

dictReverseSorted = {k: v for k, v in sorted(counter.items(),reverse = True ,key=lambda item: item[1])};
stringLetters = ''
for key in dictReverseSorted:
    print(key)
    stringLetters += key

stringLettersCaps = stringLetters.upper();
print(stringLettersCaps)

# for char1 in stringLettersCaps:
#     for char2 in letters:
#         if char1.find() == char2.find():
#             string.replace(char1,char2);

finalDict={}
for i in range(len(stringLettersCaps)):
    for j in range(len(letters)):
        if i == j:
            print(stringLettersCaps[i], letters[i])
            finalDict[stringLettersCaps[i]] = letters[i]

print(finalDict)
transTable = string.maketrans(finalDict)
finalString = string.translate(transTable)

print(finalString)
print('')

def swap(string,letter1,letter2):
    udpated = string.replace(letter1,'-').replace(letter2,letter1).replace('-',letter2)
    return udpated
    
updatedString = swap(finalString,'G','B')
print(updatedString)
print('')
updatedString = swap(updatedString,'U','C')
print(updatedString)
print('')
updatedString = swap(updatedString,'F','U')
print(updatedString)
print('')
updatedString = swap(updatedString,'R','H')
print(updatedString)
print('')
updatedString = swap(updatedString,'Y','P')
print(updatedString)
print('')
updatedString = swap(updatedString,'N','I')
print(updatedString)
print('')
updatedString = swap(updatedString,'N','O')
print(updatedString)
print('')
updatedString = swap(updatedString,'Y','K')
print(updatedString)
print('')
updatedString = swap(updatedString,'W','Y')
print(updatedString)
print('')
updatedString = swap(updatedString,'W','X')
print(updatedString)








