import string
def computeValue(name):
    value = 0
    lower = name.lower().strip()
    for letter in lower:
        value += ord(letter)-96
    return value


def mostValuableName():
    f = open("roster.txt","r")
    allnames = f.readlines()
    max_value = -1
    max_name = ""
    for full_name in allnames:
        firstname = full_name.split(" ")[0].strip()
        val = computeValue(firstname)
    if val > max_value:
        max_value = val
        max_name = full_name
    return (max_name.strip(),max_value)


def findPositiveWord(myFirstName):
    myvalue = computeValue(myFirstName)
    f = open("positive-words.txt","r")
    allWords = f.readlines()
    for word in allWords:
        if (computeValue(word.strip())) == myvalue:
            return word.strip()
            return NONE


def main():
    return findPositiveWord("Zirui")

if __name__ == '__main__':
    main()