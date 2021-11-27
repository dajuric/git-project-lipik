num = 123456789
nums = str(num)[::2]
nums = [int(x) for x in nums]

for x in nums:
    print("{:.3f}".format(x))

print("Suma je: " + str(sum(nums)))