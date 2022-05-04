from unittest import result


l_egz = int(input())

egzemplarze = {}

class Ksiazka:
    def __init__(self,data):
        self.nazwa = data[0]
        self.autor = data[1]
        self.rok_produkcji = data[2]

    def dodaj_egzemplarz(self):
        
        if str((self.nazwa, self.autor)) in egzemplarze.keys():
            egzemplarze[str((self.nazwa, self.autor))]+=1
        else:
            egzemplarze[str((self.nazwa, self.autor))]=1

for ee in range(l_egz):
    Ksiazka(eval(input())).dodaj_egzemplarz()

results = []
for key,value in egzemplarze.items():
    results.append(eval(key)+(value,))

for ss in sorted(results,key=lambda x:x[0]):
    print(ss)