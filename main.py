def canConstruct(ransomNote, magazine):
    lst = list(ransomNote)
    answer = []
    for number in lst:
        if magazine.find(number) != -1:
            answer.append(number)
            magazine = magazine.replace(number, '', 1)


    if ''.join(answer) == ransomNote:
        return True
    else:
        print(f'in magazine only hase these symbols {answer}')
        return False

a, b = input('Enter your str        '), input('Enter your str where we will search first str     ')
print(canConstruct(a, b))




