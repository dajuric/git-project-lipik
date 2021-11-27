"""
7. napravite program koji konkatenira (spaja) tri zadana rjecnika u jedan. 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
"""

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

d = dict()
d.update(dic1); d.update(dic2); d.update(dic3)
print(d)
