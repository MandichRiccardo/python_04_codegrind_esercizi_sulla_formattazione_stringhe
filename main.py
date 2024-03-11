# esercizio 1
nome = "Luca"
cognome = "Rossi"
print(nome + " " + cognome)
# esercizio 2
numero = 42
stringa = "Il numero è: {}".format(numero)
print(stringa)
# esercizio 3
numero = 42
stringa = "Il numero binario di {} è {}".format(numero, bin(numero))
print(stringa)
# esercizio 4
numero = 5
stringa = f"il quadrato di {numero} è {numero ** 2}"
print(stringa)
# esercizio 5
nome = "Luca"
cognome = "Rossi"
stringa = "il mio nome è {nome} e il mio cognome è {cognome}".format(cognome=cognome, nome=nome)
print(stringa)
# esercizio 6
nome = "Luca"
cognome = "Rossi"
stringa = "il mio nome è {nome} e il mio cognome è {cognome}".format(cognome=cognome.replace("s", "K"), nome=nome.upper())
print(stringa)