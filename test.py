'''
# funzione enumerate: crea un oggetto con gli indici degli elementi

risposte = ['caldo', 'freddo', 'tiepido', 'gelido']

risposte_numerate = enumerate(risposte, start=1)

lista_risposte_numerate = list(risposte_numerate)

for i in lista_risposte_numerate:
   print(i)

scelta_utente = input('seleziona una risposta: ')
scelta_utente_indice = int(scelta_utente) - 1
risposta_utente = lista_risposte_numerate[scelta_utente_indice][1]
print(risposta_utente)


# esempio dizionario
dizio = {
    'titolo': 'isola del tesoro',
    'autore': 'stevenson'
}

print(dizio['titolo'])

# aggiungo un item al dizionario
dizio['anno'] = 1883
print(dizio)

# modifico un item esistente del dizionario
dizio['autore'] = 'anonimo'
print(dizio)

'''
# creo un dizionario e modifico i valori di alcune keys in modo dinamico

dizio_nuovo = {
    'categoria_1': 0,
    'categoria_2': 0,
    'categoria_3': 0
}

contatore = dizio_nuovo['categoria_2']
contatore += 1
dizio_nuovo['categoria_2'] = contatore

contatore = dizio_nuovo['categoria_3']
contatore += 3
dizio_nuovo['categoria_3'] = contatore

contatore = dizio_nuovo['categoria_1']
contatore += 1
dizio_nuovo['categoria_1'] = contatore

# print(dizio_nuovo)
'''
for i in dizio_nuovo.items():
    print(*i)
'''

import pandas

df = pandas.DataFrame.from_dict(list(dizio_nuovo.items()))
df.columns = ['categoria','punti']
df.index = ['-','-','-']
df.sort_values(by=['punti'],inplace=True, ascending=False)

print(df)
