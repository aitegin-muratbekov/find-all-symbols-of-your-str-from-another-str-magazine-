def calPoints(ops):
    result = []
    sum = 0
    for i in ops:
        if i.isdigit() == True:
            result.append(i)
        elif i[0] == '-':
            result.append(i)
        elif i == 'C':
            result.pop(-1)
        elif i == 'D':
            a = int(result[-1]) * 2
            result.append(a)
        elif i == '+':
            a = int(result[-1]) + int(result[-2])
            result.append(a)
        print(result)
    if len(result) > 1:
        for i in result:
            sum += int(i)
    elif len(result) == 1:
        sum = int(result[0])
    else:
        sum = 0

    return sum
print(calPoints(["5","-2","4","C","D","9","+","+"]))

