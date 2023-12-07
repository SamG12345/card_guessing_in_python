import random

deck = {'spade': ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 'diamond': ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 'heart': ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'], 'lf': ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']}
dec = []
start = True
for i in deck:
    for j in deck[i]:
        dec.append([i, j])

def shuffle(start, dec):
    print("\nShuffling......\n")
    times = 0
    if start:
        times = 52
    else:
        times = 7
    for i in range(times):
        if i%2==0:
            a = random.randint(0, len(dec))
            b = random.randint(a, len(dec))
            dec = dec[a:b]+(dec[:a]+dec[b:])
        else:
            a = random.randint(0, len(dec))
            dec = dec[a:]+dec[:a]
    return dec

def ac(l, dec):
    if l == [[],[],[]]:
        d=dec
    else:
        d = l[0]+l[1]+l[2]
    ind = 0
    cp = [[],[],[]]
    for i in d:
        cp[ind].append(i)
        ind+=1
        if ind >= 3:
            ind=0
    return cp
    

print("Primary deck = \n", dec)

dec = shuffle(start, dec)
print(dec)

print("\nChose a card from the deck\n")

l = [[],[],[]]

l = ac(l, dec)


def chk(l):
    for i in range(3):
        print("\nIs your card in this\n",l[i],"\n")
        if input("Enter y for yes and n for no : ") == 'y':
            if i == 1 and start == False:
                return i
            cp = []
            for j in l:
                if j != l[i]:
                    cp.append(j)
            cp.insert(1, l[i])
            return cp


while True:
    x=chk(l)
    if isinstance(x, int):
        z = len(l[x])
        if z == 17:
            i = len(l[x])//2
        else:
            i = len(l[x])//2+1
        
        print("\nIs your card = ",l[x][i],"\n")
        break

    else:
        print("\nx = \n",x)
        l=[[],[],[]]
        l = ac(x, dec)
        print("\nl = \n",l)
    
    start = False