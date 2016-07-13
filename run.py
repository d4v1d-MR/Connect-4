import games
import heuristic

#game = games.TicTacToe(h=3,v=3,k=3)
game = games.ConnectFour()

state = game.initial

while True:
    dificultad = raw_input("Seleccione una dificultad (facil, media, dificil): ")
    dificultad = str(dificultad).strip()
    if dificultad == "facil":
        dificultad = 1
        break
    elif dificultad == "media":
        dificultad = 2
        break
    elif dificultad == "dificil":
        dificultad = 4
        break
    else:
        print "Seleccion no valida. Intente de nuevo"


while True:
    jugador = raw_input("Seleccione un jugador para empezar (X u O): ")
    if jugador == 'X':
        jugador = 'O'
        break
    elif jugador == 'O':
        jugador= 'X'
        break
    else:
        print "Seleccion no valida. Intente de nuevo"

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    if jugador == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        jugador='X'
    else:
        print "Thinking..."
        #move = games.minimax_decision(state, game)
        #move = games.alphabeta_full_search(state, game)
        #move = games.alphabeta_search(state, game, eval_fn=heuristic.h0)
        move = games.alphabeta_search(state, game, dificultad)

        state = game.make_move(move, state)
        jugador = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break
