text = "ovoJe{Tocan}TekstSa{{Puno}Zagrada}"
#text = "ovoJe{Tocan}TekstSa{{PunoZagrada}"

stack = []
for s in text:
    if s == "{":
        stack.append("{")
    elif s == "}" and len(stack) == 0:
        print("Unos započet zatvorenom zagradaom.")
        break
    elif s == "}" and stack[-1] == "{":
        stack.pop()
    elif s == "}" and stack[-1] != "{":
        print("Nevaljan unos")
        break

print("Valjan unos." if len(stack) == 0 else "Sve zagrade nisu zatvorene.")