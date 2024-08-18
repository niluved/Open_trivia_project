

import requests
import random
import pandas

numero_domande = input('Inserire il numero di domande a cui rispondere (max 50): ')

if numero_domande.isdigit():
    numero_domande = int(numero_domande)
else:
    print("E' necessario indicare un numero la prossima volta.")
    quit()

final_url = f'https://the-trivia-api.com/api/questions?limit={numero_domande}&region=IT'

response = requests.get(final_url)

response_json = response.json()

# print(response_json[0])

# definisco il dizionario con i punteggi per categoria

dizionario_punteggio = {
    "Arts & Literature": 0,
    "Film & TV": 0,
    "Food & Drink": 0,
    "General Knowledge": 0,
    "Geography": 0,
    "History": 0,
    "Music": 0,
    "Science": 0,
    "Society & Culture": 0,
    "Sport & Leisure": 0
}

risposte_esatte = 0

for item in range(numero_domande):

    categoria_output = response_json[item]['category']
    difficolta_output = response_json[item]['difficulty']
    domanda = response_json[item]['question']
    risposta_corretta = response_json[item]['correctAnswer']
    risposte_sbagliate = response_json[item]['incorrectAnswers']
    
             
    # creo una lista unica di risposte e la riordino casualmente
    risposte_possibili = [risposta_corretta, *risposte_sbagliate]
    random.shuffle(risposte_possibili)

    print('\nDomanda n°', item + 1)
    print('Categoria:', categoria_output)
    print('Livello di difficoltà:', difficolta_output)
    print('Quiz:', domanda)
    # print('Opzioni disponibili:', risposte_possibili, '\n')

    # uso la funzione enumerate per avere un oggetto che comprende gli indici relativi alle opzioni possibili
    risposte_numerate = enumerate(risposte_possibili, start=1)

    lista_risposte_numerate = list(risposte_numerate)

    for i in lista_risposte_numerate:
        print(i)

    scelta_utente = input('seleziona una risposta: ')
    
    # verifico se il numero selzionato è minore o pari a 4
    if scelta_utente.isdigit():
        if int(scelta_utente) > 4 or int(scelta_utente) < 0:
            print('inserito valore non corretto.')
            continue
    else:
        print('non è stato inserito un numero valido.')
        continue

    scelta_utente_indice = int(scelta_utente) - 1
    risposta_utente = lista_risposte_numerate[scelta_utente_indice][1]

    # verifico se la risposta è esatta
    if risposta_utente == risposta_corretta:
        # aggiungo un punto alle risposte esatte totali
        risposte_esatte += 1
        # aggiungo un punto alla categoria indovinata modificando il dizionario dei punteggi
        punteggio = dizionario_punteggio[categoria_output]
        punteggio += 1
        dizionario_punteggio[categoria_output] = punteggio

        print('Risposta corretta!!\n')
        input('premere un tasto per continuare...')
    else:
        print('Risposta sbagliata.\n')
        input('premere un tasto per continuare...')

print('Hai totalizzato', risposte_esatte, 'risposte esatte su un totale di', numero_domande, 'domande.\n')

tabella_punti = pandas.DataFrame.from_dict(list(dizionario_punteggio.items()))
tabella_punti.columns = ['Categoria','Punteggio']
tabella_punti.index = ['-'] * 10
tabella_punti.sort_values(by=['Punteggio'], inplace=True, ascending=False)
print(tabella_punti)
