"""
25. U toj igri slucajnim se odabirom izvlaci 7 kuglica tj. brojeva. Pero je smislio novu igru tj. pogadjanje Joker broja.
Joker broj nastaje tako da se stvori od znamenki jedinica prvih pet izvucenih brojeva.Npr. ako
su izvuceni brojevi 23,12,4,10,15,19,33 tada ce Joker broj biti 32405. Napisi program koji za ucitanih
7 brojeva ispisuje joker broj.
25a) Međutim, Pero nije osvojio ništa. Tad je shvatio da je pogriješio, i zaključio da je trebao koristit desetice. Implementirajte i tu metodu.`
"""

arr = list(map(int, input("7 brojeva: ").split()))
if len(arr) != 7:
    print("nevaljani unos")
    exit(1)

lastDigits = map(lambda x: x % 10, arr[0:5])
num = "".join([str(x) for x in lastDigits])
num = int(num)
print(num)


penultDigits = map(lambda x: (x // 10) % 10, arr[0:5])
num = "".join([str(x) for x in penultDigits])
num = int(num)
print(num)

