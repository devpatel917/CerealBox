import random
import numpy as np
import matplotlib.pyplot as plt
numbersArray=[1,2,3,4,5,6]
boxesArray=[]
count=0
for r in range(10000):
    prizesArray = []
    prizes = np.random.random_integers(1, 6, 6)
    for i in range(6):
        prizesArray.append(prizes[i])

    for u in range(6):
        for x in range(u + 1, 6):
            if prizesArray[u] == prizesArray[x]:
                Duplicate = True

    if Duplicate == True:
        newBox = np.random.random_integers(1, 6, 1)

        prizesArray.append(newBox[0])

    if numbersArray[0] in prizesArray and numbersArray[1] in prizesArray and numbersArray[2] in prizesArray and \
            numbersArray[3] in prizesArray and numbersArray[4] in prizesArray and numbersArray[5] in prizesArray:
        Done = True
    else:
        Done = False
        newBox = np.random.random_integers(1, 6, 1)

        prizesArray.append(newBox[0])

    while Done == False:
        newBox = np.random.random_integers(1, 6, 1)

        prizesArray.append(newBox[0])

        if numbersArray[0] in prizesArray and numbersArray[1] in prizesArray and numbersArray[2] in prizesArray and \
                numbersArray[3] in prizesArray and numbersArray[4] in prizesArray and numbersArray[5] in prizesArray:
            Done = True
        else:
            Done = False

    boxesArray.append(len(prizesArray))
holder=0
for w in range(10000):
    sum=holder+boxesArray[w]
    holder=sum
mean=(sum/10000)
print(mean)

median=np.median(boxesArray)
print(median)

plt.hist(boxesArray,bins = range(min(boxesArray),max(boxesArray)+2),align="mid",color="blue")
plt.show()