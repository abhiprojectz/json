x = [45, 24, 35, 31, 40, 38, 11]

def stockMax(x):
    a1 = []
    a2 = []

    for i in range(len(x)):
        y = x[i+1:]
        for j in y:
            if x[i] < j:
                z = j - x[i]
                a1.append(z)
            if (a1 != []):
                a2.append(max(a1))
    if (a2 == []):
        return -1
    else:
        return max(a2)    

b = stockMax(x)      
print(b)