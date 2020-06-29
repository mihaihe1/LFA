#fisierul de intrare
#linia 1 - n nr noduri, m muchii, tr nr valori alfabet(pt 2 inseamna ca avem 0 si 1, pt 3 - 0, 1, 2..)
#se citesc m linii de forma stare 1, stare 2, litera(cifra) prin care se trece din 1 in 2
#starile se citesc sub forma de cifra(a=0,b=1,...)
#se citeste starea initiala
#se citesc starile finale
f = open("date.in", "r")
x = f.readline().split()
n = int(x[0]) #numar noduri
m = int(x[1]) #numar muchii
tr = int(x[2]) #numar tranzitii
d1 = {}

for i in range(m): # d1 dictionar de forma (nod1, a):[nod2,..] i.e.  nod1 --> nod2 prin a
    t = f.readline().split()
    x = int(t[0])
    y = int(t[1])
    c = int(t[2])
    if (x, c) in d1:
        d1[(x, c)].append(y)
    else:
        d1[(x, c)] = []
        d1[(x, c)].append(y)

start = int(f.readline()) #se citeste starea initiala
fi = f.readline().split() #se citesc starile finale
final = []
for i in fi:
    final.append(int(i))  #adaug starile finale intr-un vector

#print(start)
#print(final)
#print(d1)

stari = [[start]] #stari este vector de vectori ce va contine toate starile prin care voi trece in afd
afd = [] #va contine valorile din tabelul afd
total = 1
viz = [0]*10 #marchez starile vizitate cu 1
list = []
for i in range(0, tr): #completez primul rand din tabelul cu afd(pentru starea de start)
    if (start, i) in d1:
        list.append(d1[(start, i)])
        stari.append(d1[(start, i)])
        total += 1
    else:
        list.append([-1])
afd.append(list) # adaug primul rand in tabel
viz[0] = 1 #si marchez prima stare ca fiind vizitata si trecuta in tabel
poz = 2

while len(stari) + 1 != poz: #parcurg starile pana devin toate vizitate
    for i in range(0, total):
        if viz[i] == 0: # caut prima stare nevizitata
            total += 1
            viz[i] = 1
            princip = [] #princip este vector ce corespunde coloanelor din afd
            for j in range(0, tr):#parcurg alfabetul
                list = []
                for k in stari[poz-1]: #caut in starea curenta afd, daca exista tranzitii pt aceasta stare in afn
                    if (k, j) in d1:   #daca exista tranzitie ce pleaca din k prin j
                        for l in d1[(k, j)]:
                            if l not in list: #verific daca starea n-a fost deja adaugata
                                list.append(l)
                if len(list) == 0:  #daca n-a fost gasita tranzitia, adaug -1 (multimea vida)
                    princip.append([-1])
                else:
                    list.sort()
                    if list not in stari:   #daca am gasit o stare noua, o adaug
                        stari.append(list)
                    princip.append(list)
            afd.append(princip)  #completez linia in tabelul afd
            break
    poz += 1

for i in range(0, len(stari)):
    print(stari[i],end=" se duce in ")
    for j in range(0, len(afd[i])): #parcurg toate starile din tabelul afd si afisez pt fiecare litera din alfabet starea corespunzatoare
        if afd[i][j][0] != -1:
            print(afd[i][j],end=" prin ")
            if j != len(afd[i])-1:
                print(j,end=" ,in ")
            else:
                print(j,end=" ")
        else:
            print("multimea vida prin",j,end="; ")
    print("\n")

print("Stari finale : ",end=" ")
for i in range(0, len(stari)):
    for j in final:
        if j in stari[i]:
            print(stari[i],end=", ")
            break

f.close()