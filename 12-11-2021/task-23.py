def pyramid(n):
    ls = []
    for i in range(n):
        ls.append([1] * (i + 1))

    return ls
    # [ls.append([1] * (i + 1)) for i in range(n)]
    # return ls

print(pyramid(4))
