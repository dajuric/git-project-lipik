str = "Ovo je nasumični niz znakova"

print("Prva riječ u nizu ima sva velika slova bez obzira na uneseni niz: " + str.split()[0].upper())
print(f"Druga riječ u nizu ima {len(str.split()[1])} znakova")
print("ne postoje bjeline iza unesenog niza znakova: " + str.split()[-1])
print("ne postoje bjeline prije unesenog niza znakova: " + str.split()[0])
print("svi znakovi su ispisani malim slovom: " + str.lower())
print("samo prvo slovo cijelog niza je ispisano velikim slovom te je iza unesenog niza dodan niz “ asdfčlkasdfčlk” odmah nakon zadnjeg alfanumeričkog znaka: <niz znakova + ostatak>: " + str.title() + " asdfčlkasdfčlk")