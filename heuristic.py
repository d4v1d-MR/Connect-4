import games


def h1(state, player):
    horizontales = 0
    verticales = 0
    diagonales = 0

    if not state.utility == 0:
        if player == 'X':
            return state.utility * 10000
        else:
            return -state.utility * 10000
    for x in range(1, 8):
        for y in range(1, 7):
            if ((x, y)) in games.ConnectFour().legal_moves(state):
                equis = x
                ygriega = y
                horizontales = horizontales + chorizontales(state, player, equis, ygriega)
                verticales = verticales + cverticales(state, player, equis, ygriega)
                diagonales = diagonales + cdiagonales(state, player, equis, ygriega)

    return horizontales + verticales + diagonales


def chorizontales(state, player, equis, ygriega):
    suma = 0
    vectores = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
    for z in range(0, 4):
        if equis in vectores[z]:
            suma = suma + valor(state, player, equis, ygriega, vectores[z])

    return suma


def valor(state, player, equis, ygriega, vector):
    count = 0
    rcount = 0
    for x in range(0, 4):
        if equis == vector[x]:
            if player == 'X':
                count = count + 10
                rcount = 0
            else:
                count = 0
                rcount = rcount + 10
            continue
        if state.board.get((vector[x], ygriega)) == 'X':
            count = count + 10
            rcount = 0
        if state.board.get((vector[x], ygriega)) == '.':
            count = count + 1
            rcount = rcount + 1
        if state.board.get((vector[x], ygriega)) == 'O':
            count = 0
            rcount = rcount + 10
            ##if (count == 0 or rcount == 0) and x >= 6:
            ##return 0
    if player == 'O':
        return rcount - count
    return count - rcount


def cverticales(state, player, equis, ygriega):
    count = 0
    rcount = 0
    for y in range(1, 7):
        if ygriega == y:
            if player == 'X':
                count = count + 10
                rcount = 0
            else:
                count = 0
                rcount = rcount + 10
            continue
        if state.board.get((equis, y)) == 'X':
            count = count + 10
            rcount = 0
        if state.board.get((equis, y)) == '.':
            count = count + 1
            rcount = rcount + 1
        if state.board.get((equis, y)) == 'O':
            count = 0
            rcount = rcount + 10
            ##if (count ==0 or rcount ==0) and y > 4:
            ##   return 0
    if player == 'O':
        return rcount - count
    return count - rcount


def cdiagonales(state, player, equis, ygriega):
    seguidas = 0
    rseguidas = 0
    count = 0
    rcount = 0

    x = equis - 5
    y = ygriega - 5
    while x < 8 and y < 7:
        if x < 1 or y < 1:
            x = x + 1
            y = y + 1
            continue
        if state.board.get(x, y) == 'X':
            seguidas = seguidas + 1
            rseguidas = 0
            count = count + 10
            rcount = 0
        if state.board.get(x, y) == 'O':
            seguidas = 0
            rseguidas = rseguidas + 1
            count = 0
            rcount = rcount + 10
        if state.board.get(x, y) == '.':
            count = count + 1
            rcount = rcount + 1
        x = x + 1
        y = y + 1

    aseguidas = 0
    arseguidas = 0
    x = equis + 5
    y = ygriega - 5
    while x > 0 and y < 7:
        if x == equis and y == ygriega:
            if player == 'X':
                aseguidas = aseguidas + 1
                arseguidas = 0
            elif player == 'O':
                arseguidas = arseguidas + 1
                aseguidas = 0
        if x > 7 or y < 1:
            x = x + 1
            y = y + 1
            continue
        if state.board.get(x, y) == 'X':
            aseguidas = aseguidas + 1
            arseguidas = 0
            count = count + 10
            rcount = 0
        if state.board.get(x, y) == 'O':
            aseguidas = 0
            arseguidas = arseguidas + 1
            count = 0
            rcount = rcount + 10
        if state.board.get(x, y) == '.':
            count = count + 1
            rcount = rcount + 1
        x = x - 1
        y = y + 1

    if player == 'O':
        if rseguidas == 3 or arseguidas == 3:
            rseguidas = rseguidas + 1000
        return (rcount - count) + rseguidas
    if seguidas == 3 or aseguidas == 3:
        aseguidas += 1000
    return (count - rcount) + aseguidas
