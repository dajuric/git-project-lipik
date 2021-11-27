"""
8. Napisi program koji za ucitane dvije liste (prezimena, godine) sortira podatke iz obje liste
po prezimenu.
"""

#%%

listA = [3, 2, 4, 1, 1]
listB = ['three', 'two', 'four', 'one', 'one2']

indexList = list(range(len(listA)))
indexList.sort(key = lambda x: listA[x])

listA = [listA[i] for i in indexList]
listB = [listB[i] for i in indexList]

print(listA)
print(listB)


#%%

listA = [3, 2, 4, 1, 1]
listB = ['three', 'two', 'four', 'one', 'one2']

zipLists = list(zip(listA, listB))
zipLists.sort(key = lambda x: x[0])

listA = [a for a, b in zipLists]
listB = [b for a, b in zipLists]

print(listA)
print(listB)

# %%
