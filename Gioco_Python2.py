#Si scriva un programma in Python che in base alla scelta dell'utente permetta ci calcolare
#il perimetro di diverse figure geometriche. Per la risoluzione dell'esercizio abbiamo scelto:
#
# - Quadrato (perimetro = lato*4)
# - Cerchio (circonferenza = 2*pigreco*r)
# - Rettangolo (perimetro = base*2 + altezza*2)
#
#
# RISOLUZIONE:

# per il primo punto chiedo all'utente di inserire il valore del lato
lato = int(input("Inserire il valore del lato del Quadrato: "))
# passo a calcolare il perimetro del Quadrato
perimetro = lato*4
# stampo a terminale il valore del perimetro calcolato
print("Il Perimetro del Quadrato è di: ", perimetro)

# per il secondo punto chiedo all'utente di inserire il valore del raggio
raggio = int(input("Inserire il valore del raggio della Cerchio: "))
# per calcolare la circonferenza, mi avvalgo della variabile "data" per il calcolo del raggio*2
data = raggio*2
# calcolo la circonferenza usando il valore di "data" moltiplicato per il valore di pigreco
circonferenza = data*3,14
# stampo a terminale il valore della circonferenza del Cerchio
print("La Circonferenza del Cerchio è di: ", circonferenza)

# per il terzo punto, ho creato una variabile "x" per la condizione di un ciclo while
# questo per poi verificare che l'utente inserisca i valori di Base e Altezza che
# non siano uguali tra di loro e, nel caso lo fossero, metta un messaggio 
# che avvisa che i valori inseriti sono errati
x = 0
while(x == 0):
    base = int(input("Inserire la base del rettangolo: "))
    altezza = int(input("impostare l'altezza del rettangolo: "))
    if(base != altezza):
        perimetro = base*2 + altezza*2
        print("Il perimetro del Rettangolo è di: ", perimetro)
        x = 1
    else:
        print("valori inseriti errati!")

