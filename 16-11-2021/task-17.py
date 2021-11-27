"""
17. Napisi prog koji ce provjeriti predani tip te ovisno o tipu napraviti sljedece: ako je unesen set, napravit ce listu. ako je unesena lista, napravit ce tuple, a ako je unesen tuple, napravit ce set.
"""

def makeAnotherType(data):
    if isinstance(data, set):
        return list(data)
    if isinstance(data, list):
        return tuple(data)
    if isinstance(data, tuple):
        return set(data)

print(makeAnotherType([1, 2, 3]))