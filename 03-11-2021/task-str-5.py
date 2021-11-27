"""
U varijablu upišite neki proizvoljni niz znakova. Nad varijablom 
pozovite odgovarajuću funkciju koja će vratiti duljinu upisanoga niza 
znakova te rezultat spremite u varijablu. Na temelju duljine niza 
ispišite sve znakove do polovice niza. Primjer: ako imamo niz od 14
znakova (abcdefghijklmn), potrebno je ispisati 1., 2., 3., 4., 5., 6. i 7. 
znak (abcdefg)
"""

x = "abcdefghijklmn"
l = len(x)
for i in range(l//2):
    print(x[i], end="")