"""
15. napisi rjecnik sa proizvoljnim vrijednostima i neka sadrzi duplikate. napisi program koji bi uklonio sve parove koji sadrze duplikate.
"""

d = { "1": "jedan", "2": "dva", "1": "jedan", "tri": "tri", "1": "jedan", "1_dup": "jedan"}
print(d)

result = {}
for key,value in d.items():
    if value not in result.values():
        result[key] = value
        
print(result)