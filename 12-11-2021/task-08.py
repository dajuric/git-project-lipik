import random

def mod(nums):
    return max(set(nums), key = nums.count)

x = 52 #neki nausmični broj
ls = [random.randint(0, 1001) for _ in range(x)]

mean = sum(ls) / len(ls)
median = sorted(ls)[len(ls) // 2]

print("Medijan: " + str(median))
print("Mod: " + str(mod(ls)))
print("Mean: " + str(mean))
print("Svi ispred vrijednosti mediana: " + str([x for x in ls if x < median]))
print("Svi ispod  vrijednosti mediana: " + str([x for x in ls if x > median]))

newList = [ x for x in ls if x < ((mean * 0.9) or (x > (mean * 1.1))) ]
print(newList)
