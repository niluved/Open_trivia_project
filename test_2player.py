

game_running = True
turno_player_1 = True
turno_player_2 = False

numero_domande = 10

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

    def aggiorna_punteggio(self,categoria_output):
        # aggiorno il numero di risposte esatte
        self.risposte_esatte += 1
        # aggiorno il punteggio della categoria passata come argomento
        punteggio = self.dizionario_punteggio[categoria_output]
        punteggio += 1
        self.dizionario_punteggio[categoria_output] = punteggio

player_1 = Player()
player_2 = Player()

contatore = 0

while game_running:

        # turno del giocatore 1 
        while turno_player_1:
            # aggiorno il contatore delle domande
            contatore += 1
            print('Domanda n°:', contatore)

            if numero_domande == contatore:
                game_running = False
                break
            else:

                risposta_utente = input('digita un numero Player 1: ')
                if int(risposta_utente) > 5:

                        # in caso di risposta esatta aggiorno il punteggio
                    player_1.aggiorna_punteggio('Sport & Leisure')
                    
                else:
                        # cambio turno per risposta sbagliata
                    turno_player_1 = False
                    turno_player_2 = True

        # turno del giocatore 2
        while turno_player_2:
            # aggiorno il contatore delle domande
            contatore += 1
            print('contatore', contatore)

            if numero_domande == contatore:
                game_running = False
                break
            else:

                risposta_utente = input('digita un numero Player 2:')
                if int(risposta_utente) > 5:
                        # in caso di risposta esatta aggiorno il punteggio
                    player_2.aggiorna_punteggio('Science')
                    
                else:
                        # cambio turno per risposta sbagliata
                    turno_player_1 = True
                    turno_player_2 = False


print(player_1.dizionario_punteggio)
print(player_1.risposte_esatte)

print(player_2.dizionario_punteggio)
print(player_2.risposte_esatte)