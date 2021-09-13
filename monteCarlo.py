import random
import matplotlib.pyplot as plt
import math


turns = int(input("Zadejte počet kapek:"))
r = 10

circle = 0
square = 0
piSum = 0

xpoints = []
ypoints = []

xCircle = []
yCircle = []
xSquare = []
ySquare = []



while turns < 1:
    turns = int(input("Zadejte reálný počet kapek:"))

for i in range(1, turns+1):
    randomX = random.uniform(-r, r)
    randomY = random.uniform(-r, r)
    if randomX**2 + randomY**2 <= r**2:
        circle += 1
        xCircle.append(randomX)
        yCircle.append(randomY) 
    else:
        xSquare.append(randomX)
        ySquare.append(randomY)
    square += 1
    if circle and square:
        pi =(4*circle)/square
        xpoints.append(i)
        ypoints.append(pi)

        piSum += pi


fig, ax = plt.subplots(2)

ax[0].plot(xpoints, ypoints)
ax[0].plot([1, i], [math.pi, math.pi], marker = 's')
ax[0].plot([1, i], [piSum/i, piSum/i], marker = 'o')
ax[0].set_title("Pi = {}; Pi(průměr) = {}; Pi(výpočet) ~ {}".format(math.pi, piSum/i, pi))

ax[1].add_patch(plt.Circle((0, 0), r, color='blue', fill=False))
ax[1].scatter(xCircle, yCircle, color = 'red')
ax[1].scatter(xSquare, ySquare, color = 'green')
ax[1].set_title("Σ(kruh) = {}; Σ(čtverec) = {}".format(int(circle), int(square)))

plt.show()

