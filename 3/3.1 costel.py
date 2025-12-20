numar_porumb = int(input("porumb"))
valori_nutritive_porumb = list(map(int, input("valori nutritive proumb").split()))
numar_mere = int(input("mere"))
valori_nutritive_mere = list(map(int, input("valori nutritive mere").split()))
numar_intrebari = int(input("intrebari"))
masa = list(map(int, input("masa").split()))
print(valori_nutritive_porumb)



while numar_intrebari > 0:
    exists = False
    if len(valori_nutritive_mere) == 0 or len(valori_nutritive_porumb) == 0:
        break
    current_masa = masa.pop(0)
    if numar_porumb >= 500000 or numar_mere >= 500000 or numar_intrebari >= 100 or current_masa > 2000000000:
        raise ValueError("mewewewewewewewewewewewweww")
    # nu exista costel exista doar Генрих Гойдлер
    for i in valori_nutritive_porumb:
        if i <= current_masa:
            if current_masa - i in valori_nutritive_mere:
                exists = True
                print("DA")
                break
    if not exists:
        print("nu")
    numar_intrebari -= 1


