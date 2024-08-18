
import requests
import html
import random

numero_domande = input('Indicare il numero di domande a cui rispondere: ')

if numero_domande.isdigit():
    numero_domande = int(numero_domande)
else:
    print("E' necessario indicare un numero la prossima volta.")
    quit()

base_url = f'https://opentdb.com/api.php?amount={numero_domande}'

response = requests.get(base_url)

response_json = response.json()

# print(response_json['results'])

risposte_esatte = 0
categorie_indovinate = []

for item in range(numero_domande):

    categoria_output = response_json['results'][item]['category']
    difficolta_output = response_json['results'][item]['difficulty']
    domanda_html = response_json['results'][item]['question']
    risposta_corretta_html = response_json['results'][item]['correct_answer']
    risposte_sbagliate_html = response_json['results'][item]['incorrect_answers']
    
    # faccio una decodifica delle stringhe ottenute da formato stringa html a testo normale 
    domanda_testo = html.unescape(domanda_html)
    risposta_corretta_testo = html.unescape(risposta_corretta_html)
    
    # faccio lo stesso per le risposte sbagliate ma essendo queste una lista devo fare un ciclo for
    risposte_sbagliate_testo = []

    for i in risposte_sbagliate_html:
        risposta_sbagliata_decode = html.unescape(i)
        risposte_sbagliate_testo.append(risposta_sbagliata_decode)
         
    #creo una lista unica di risposte e la riordino casualmente
    risposte_possibili = [risposta_corretta_testo, *risposte_sbagliate_testo]
    random.shuffle(risposte_possibili)

    print('\nDomanda n°', item + 1)
    print('Categoria:', categoria_output)
    print('Livello di difficoltà:', difficolta_output)
    print('Quiz:', domanda_testo)
    print('Opzioni disponibili:', risposte_possibili, '\n')

    risposta_utente = input('Scrivere di seguito la propria risposta:').lower()

    if risposta_utente == risposta_corretta_testo.lower():
        risposte_esatte += 1
        categorie_indovinate.append(categoria_output)
        print('Risposta corretta!!\n')
    else:
        print('Risposta sbagliata.\n')

print('Hai totalizzato', risposte_esatte, 'risposte esatte su un totale di', numero_domande, 'domande.')

if len(categorie_indovinate) > 0:
    print('Hai indovinato le categorie: ', set(categorie_indovinate))
