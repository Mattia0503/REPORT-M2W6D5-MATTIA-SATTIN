#Si scriva un programma in Python che in base alla scelta dell'utente permetta ci calcolare
#il perimetro di diverse figure geometriche. Per la risoluzione dell'esercizio abbiamo scelto:
#
# - Quadrato (perimetro = lato*4)
# - Cerchio (circonferenza = 2*pigreco*r)
# - Rettangolo (perimetro = base*2 + altezza*2)
#
#
# RISOLUZIONE: 
# chiedo all'utente quale delle tre proposte vorrebbe fare.
print("Scegliere fa una delle seguenti formule geometriche:")
print("A  -  Perimetro di un Quadrato")
print("B  -  Circonferenza di un Cerchio")
print("C  -  Perimetro di un Rettangolo")

check = input("Inserire l'opzione: ")
if (check == 'a'):
        # per il primo punto chiedo all'utente di inserire il valore del lato
        lato = int(input("Inserire il valore del lato del Quadrato: "))
        # passo a calcolare il perimetro del Quadrato
        perimetro = lato*4
        # stampo a terminale il valore del perimetro calcolato
        print("Il Perimetro del Quadrato è di: ", perimetro)
elif (check == 'b'):
        # per il secondo punto chiedo all'utente di inserire il valore del raggio
        raggio = int(input("Inserire il valore del raggio della Cerchio: "))
        # per calcolare la circonferenza, mi avvalgo della variabile "data" per il calcolo del raggio*2
        data = raggio*2
        # calcolo la circonferenza usando il valore di "data" moltiplicato per il valore di pigreco
        circonferenza = data*3,14
        # stampo a terminale il valore della circonferenza del Cerchio
        print("La Circonferenza del Cerchio è di: ", circonferenza)
elif (check == 'c'):
    # per il terzo punto, ho creato una variabile "x" per la condizione di un ciclo while
    # questo per poi verificare che l'utente inserisca i valori di Base e Altezza che
    # non siano uguali tra di loro e, nel caso lo fossero, metta un messaggio 
    # che avvisa che i valori inseriti sono errati
    x = 0
    while(x == 0):
        # chiedo all'utente di inserire il valore della base
        base = int(input("Inserire la base del rettangolo: "))
        # chiedo all'utente di inserire il valore dell'altezza
        altezza = int(input("impostare l'altezza del rettangolo: "))
        #effettuo un controllo per vedere se i dati inseriti non sono uguali
        if(base != altezza):
            # calcolo il perimetro del rettangolo
            perimetro = base*2 + altezza*2
            # stampo a terminale il valore del perimetro del Rettangolo
            print("Il perimetro del Rettangolo è di: ", perimetro)
            # aggiorno la variabile check a 1 cosi' da poter uscire dal ciclo
            x = 1
        else:
            # se i valori inseriti sono uguali, invio un messaggio a terminale di errore
            print("valori inseriti errati!")
else:
    # se l'utente inserisce un valore che non e' fra quelli proposti
    # stampo a terminale un messaggio di errore
    print("scelta inserita non valida")
