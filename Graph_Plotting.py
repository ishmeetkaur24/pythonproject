import matplotlib.pyplot as pt

x = [3,9,15]
y = [1,11,19]

pt.plot(x,y)
pt.ylabel("Aggregate Expenditure")
pt.xlabel("Aggregate Output")
pt.bar(x,y)
pt.show()
