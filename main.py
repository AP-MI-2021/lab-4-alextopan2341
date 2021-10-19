from collections import Counter
def citire_lista_cuvinte():
    l=[]
    string_citit = input("Dati lista: ")
    numere = string_citit.split(" ")
    for x in numere:
        l.append(x)
    return l

def gasire_sir_de_caractere(l, sir):
    '''
    Afiseaza mesajul "Da" daca sirul dat de la tastatura este gasit in lista, iar "Nu" in caz contrar
    :param l: lista de stringuri
    :param sir: sirul dat de la tastatura
    :return: mesajele corespunzatoare
    '''
    ok = 0
    for element in l:
        if str(element) == str(sir):
            ok = 1
    if ok == 1:
        print("Da")
    else:
        print("Nu")
'''
def test_gasire_sir_de_caractere():
    assert gasire_sir_de_caractere(['banana', 'lapte', 'oua'], 'banana') == 'Da'
    assert gasire_sir_de_caractere(['facultate', 'sesiune', 'materie'], 'materie') == Da
    assert gasire_sir_de_caractere(['aaa', 'bbb', 'cmtc', 'aaa'], 'drd') == 'Nu'
'''
def sir_de_caractere_gasit(l):
    '''
    Determina in rezultat ,lista de stringuri care au frecventa de cel putin doua ori, sau mesajul "Unic" in caz contrar
    :param l: lista de stringuri
    :return:
    '''
    rezultat = []
    i = 0
    while i < len(l):
        element = l[i]
        if l.count(element) >= 2:
            rezultat.append(element)
        i = i+1
    if rezultat != None:
        return rezultat
    else:
        print("UNIC")
def sir_palindrom(l):
    '''
    Determina o lista cu siruri palindrom
    :param l: lista de caractere
    :return: lista care indeplineste cerinta
    '''
    rezultat = []
    for i in l:
        if i == i[::-1]:
            rezultat.append(i)
    return rezultat

def test_sir_palindrom():
    assert sir_palindrom(['aaa', 'bbb', 'cmtc', 'drd', 'aaa']) == ['aaa', 'bbb', 'drd', 'aaa']

def exercitiul5(l):
    max = 0
    element = []
    for i in l:
        if l.count(i) > max:
            element = l[i]
            max= l.count(i)
    i = 0
    while i < len(l):
        element1 = l[i]
        if element1 != element:
            element1 = max

def main():
    #test_gasire_sir_de_caractere()
    test_sir_palindrom()
    l = []
    while True:
        print("1. Citire lista numere intregi")
        print("2. Gasirea unui sir de caractere citit in lista")
        print("3. Lista cu toate sirurile care se repeta in lista(apar de cel putin doua ori)")
        print("4. Afiseaza toate sirurile de caractere din lista care sunt palindrom")
        print("5. Exercitiul 5")
        print("a. Afisare lista")
        print("x. Iesire din meniu")
        exercitiu = input("Dati exercitiu: ")
        if exercitiu == "1":
            l = citire_lista_cuvinte()
        elif exercitiu == "2":
           sir = str(input("Dati sirul: "))
           print(gasire_sir_de_caractere(l, sir))
        elif exercitiu == "3":
            print(sir_de_caractere_gasit(l))
        elif exercitiu == "4":
            print(sir_palindrom(l))
        elif exercitiu == "5":
            print(exercitiul5(l))
        elif exercitiu == "a":
            print(l)
        elif exercitiu == "x":
            return 0
        else:
            print("Exercitiul nu exista. Reincercati!")

main()