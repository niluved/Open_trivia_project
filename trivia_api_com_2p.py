import requests
import random
import pandas

numero_domande = input('Inserire il numero di domande a cui rispondere (max 50): ')
livello = input('Scegliere il livello di difficoltà (easy/medium/hard): ')

if numero_domande.isdigit():
    numero_domande = int(numero_domande)
else:
    print("E' necessario indicare un numero la prossima volta.")
    quit()

final_url = f'https://the-trivia-api.com/api/questions?limit={numero_domande}&region=IT&difficulty={livello}'

response = requests.get(final_url)

response_json = response.json()

# print(response_json,'\n')

# definisco la funzione che legge la domanda iesima dal json scaricato
def spara_domanda(contatore):
    
    categoria_output = response_json[contatore]['category']
    difficolta_output = response_json[contatore]['difficulty']
    domanda = response_json[contatore]['question']
    risposta_corretta = response_json[contatore]['correctAnswer']
    risposte_sbagliate = response_json[contatore]['incorrectAnswers']
    
             
    # creo una lista unica di risposte e la riordino casualmente
    risposte_possibili = [risposta_corretta, *risposte_sbagliate]
    random.shuffle(risposte_possibili)

    print('Domanda n°', contatore + 1)
    print('Categoria:', categoria_output)
    print('Livello di difficoltà:', difficolta_output)
    print('Quiz:', domanda)
    
    # uso la funzione enumerate per avere un oggetto che comprende gli indici relativi alle opzioni possibili
    risposte_numerate = enumerate(risposte_possibili, start=1)

    lista_risposte_numerate = list(risposte_numerate)

    for i in lista_risposte_numerate:
        print(i)

    scelta_utente = input('seleziona una risposta: ')
    
    '''
    # verifico se il numero selzionato è minore o pari a 4
    if scelta_utente.isdigit():
        if int(scelta_utente) > 4 or int(scelta_utente) < 0:
            print('inserito valore non corretto.')
            continue
    else:
        print('non è stato inserito un numero valido.')
        continue
    '''

    scelta_utente_indice = int(scelta_utente) - 1
    risposta_utente = lista_risposte_numerate[scelta_utente_indice][1]

    # verifico se la risposta è esatta
    if risposta_utente == risposta_corretta:
        indovinato = 1
    else:
        indovinato = 0

    return indovinato, categoria_output

game_running = True
turno_player_1 = True
turno_player_2 = False

class Player:
    def __init__(self):
        self.risposte_esatte = 0
        self.dizionario_punteggio = {
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

        self.tabella_punti = {}

    def aggiorna_punteggio(self,categoria_output):
        # aggiorno il numero di risposte esatte
        self.risposte_esatte += 1
        # aggiorno il punteggio della categoria passata come argomento
        punteggio = self.dizionario_punteggio[categoria_output]
        punteggio += 1
        self.dizionario_punteggio[categoria_output] = punteggio

    def crea_tabella(self):
        self.tabella_punti = pandas.DataFrame.from_dict(list(self.dizionario_punteggio.items()))
        self.tabella_punti.columns = ['Categoria','Punteggio']
        self.tabella_punti.index = ['-'] * 10
        self.tabella_punti.sort_values(by=['Punteggio'], inplace=True, ascending=False)

player_1 = Player()
player_2 = Player()

contatore = 0

while game_running:

        # turno del giocatore 1 
        while turno_player_1:
                   
            if numero_domande == contatore:
                game_running = False
                break
            else:
                print('Giocatore 1:\n')

                # lancio la funzione che legge la domanda e conservo i valori delle variabili ritornate
                indovinato, categoria_output = spara_domanda(contatore)

                if indovinato == 1:
                    print('Risposta esatta! Puoi continuare a giocare...\n')
                    input('premere un tasto per continuare...\n')
                    # in caso di risposta esatta aggiorno il punteggio
                    player_1.aggiorna_punteggio(categoria_output)
                                        
                else:
                    # cambio turno per risposta sbagliata
                    print("Risposta sbagliata. Il turno passa all'avversario.\n")
                    input('premere un tasto per continuare...\n')
                    turno_player_1 = False
                    turno_player_2 = True
                
                # aggiorno il contatore delle domande
                contatore += 1  

        # turno del giocatore 2
        while turno_player_2:
                        
            if numero_domande == contatore:
                game_running = False
                break
            else:                 
                print('Giocatore 2:\n')

                # lancio la funzione che legge la domanda e conservo i valori delle variabili ritornate
                indovinato, categoria_output = spara_domanda(contatore)

                if indovinato == 1:
                    # in caso di risposta esatta aggiorno il punteggio
                    print('Risposta esatta! Puoi continuare a giocare...\n')
                    input('premere un tasto per continuare...\n')
                    player_2.aggiorna_punteggio(categoria_output)
                    
                    
                else:
                    # cambio turno per risposta sbagliata
                    print("Risposta sbagliata. Il turno passa all'avversario.\n")
                    input('premere un tasto per continuare...\n')
                    turno_player_1 = True
                    turno_player_2 = False

                # aggiorno il contatore delle domande
                contatore += 1 

print('Partita terminata. Ecco i risultati:\n')

# print(player_1.dizionario_punteggio)
print('\nGiocatore 1 ha totalizzato', player_1.risposte_esatte, 'risposte esatte.\n')
player_1.crea_tabella()
print(player_1.tabella_punti)

# print(player_2.dizionario_punteggio)
print('\nGiocatore 2 ha totalizzato', player_2.risposte_esatte, 'risposte esatte.\n')
player_2.crea_tabella()
print(player_2.tabella_punti)