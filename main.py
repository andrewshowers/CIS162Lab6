def countVotes(names):
    votes = names
    al = 0
    gh = 0
    for x in votes:
     if x == 'Ada Lovelace':
        al += 1
    if x == 'Grace Hopper':
        gh += 1
    print("Grace Hopper's votes total ", gh, "Ada Lovelace' votes total ", al)

def withinRange(numbers, low, high):
    list = []
    for x in numbers:
        if low < x < high:
            list.append(x)
    return list

def findHighest(numbers):
    highest = 0
    for x in numbers:
        if x > highest:
            highest = x
    return highest

def countDivideNines(numbers):
    count = 0
    for x in numbers:
        if x%9 == 0:
            count +=1
    return count

def determineWin(numbers, actual):
    output = ''
    for x in numbers:
        if x == actual:
            output += 'YOU GOT IT \n\n'
            break
        if x < actual:
            output += 'Too small \n'
        if x > actual:
            output += 'Too large \n'
    print(output)
