stack = []
pr = []
v = list(input())
while v[0] != 'e':
    if v[1] == 'u':
        dit = 0
        r = 1
        if len(v) > 4 and v[5] == '-':
            for i in range(len(v) - 1, 5, -1):
                dit += int(v[i])*r
                r = r*10
            dit = -dit
        else:
            for i in range(len(v) - 1, 4, -1):
                dit += int(v[i])*r
                r = r*10
        stack.append(dit)
        pr.append("ok")
    elif v[1] == 'o':
        pr.append(stack[0])
        stackcopy = []
        for i in range(1, len(stack)):
            stackcopy.append(stack[i])
        stack = stackcopy
    elif v[0] == 'f':
        pr.append(stack[0])
    elif v[0] == 'c':
        stack = []
        pr.append('ok')
    elif v[0] == 's':
        pr.append(len(stack))
    v = list(input())
pr.append('bye')
for i in range(len(pr)):
    print(pr[i])