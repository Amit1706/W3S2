import Matplotlib
import matplotlib.pyplot as plt
import numpy as np

apoints = np.array([0, 6])
bpoints = np.array([0, 250])
plt.plot(apoints, bpoints)
plt.show()

cpoints = np.array([1, 8])
dpoints = np.array([3, 10])
plt.plot(cpoints, dpoints)
plt.show()

epoints = np.array([1, 8])
fpoints = np.array([3, 10])
plt.plot(epoints, fpoints, 'o')
plt.show()

gpoints = np.array([1, 2, 6, 8])
hpoints = np.array([3, 8, 1, 10])
plt.plot(gpoints, hpoints)
plt.show()

ipoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ipoints)
plt.show()
...
plt.plot(ipoints, marker = '*')
...

#           Marker	            Description
#           'o'	                Circle	
#           '*'	                Star	
#           '.'	                Point	
#           ','	                Pixel	
#           'x'	                X	
#           'X'	                X (filled)	
#           '+'	                Plus	
#           'P'	                Plus (filled)	
#           's'	                Square	
#           'D'	                Diamond	
#           'd'	                Diamond (thin)	
#           'p'	                Pentagon	
#           'H'	                Hexagon	
#           'h'	                Hexagon	
#           'v'	                Triangle Down	
#           '^'	                Triangle Up	
#           '<'	                Triangle Left	
#           '>'	                Triangle Right	
#           '1'	                Tri Down	
#           '2'	                Tri Up	
#           '3'	                Tri Left	
#           '4'	                Tri Right	
#           '|'	                Vline	
#           '_'	                Hline


# Color Syntax	Descriptionimport matplotlib.pyplot as plt

kpoints = np.array([3, 8, 1, 10])

plt.plot(kpoints, marker = 'o', ms = 20)
plt.show()
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White


jpoints = np.array([3, 8, 1, 10])
plt.plot(jpoints, marker = 'o', ms = 20)
plt.show()


kpoints = np.array([3, 8, 1, 10])
plt.plot(kpoints, linestyle = 'dotted')
plt.show()

# Matplotlib Support
l = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
m = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(l, m)
plt.show()

# Matplotlib Grid
n = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
o = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(n, o)
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()

# Matplotlib Subplot
#plot 1:
p = np.array([0, 1, 2, 3])
q = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)
plt.plot(p,q)
#plot 2:
p = np.array([0, 1, 2, 3])
q = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(p,q)
plt.show()

#Matplotlib Scatter
r = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
s = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(r, s, color = 'hotpink')
r = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
s = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(r, s, color = '#88c999')
plt.show()

#Matplotlib Bars
t = np.array(["A", "B", "C", "D"])
u = np.array([3, 8, 1, 10])
plt.bar(t, u, width = 0.1)
plt.show()

# Matplotlib Histogram
v = np.random.normal(170, 10, 250)
plt.hist(v)
plt.show() 

# Matplotlib Piechart
w = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(w, labels = mylabels, startangle = 90)
plt.show() 

x = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(x, labels = mylabels, explode = myexplode)
plt.show()