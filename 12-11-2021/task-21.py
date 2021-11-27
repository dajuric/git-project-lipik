def brakeString(str):
    chars = [char for char in str]
    return tuple(chars)


str = "Ovo je rečenica"
print(brakeString(str))