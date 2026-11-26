# las 9 caracteristicas del tablero, igual que en el .pde

PEON, CABALLO, ALFIL, TORRE, DAMA, REY = 1, 2, 3, 4, 5, 6
VALOR = [0, 1, 3, 3, 5, 9, 0]
SALTOS_CABALLO = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
DIR_REY = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
DIR_TORRE = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DIR_ALFIL = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def dentro(f, c):
    return 0 <= f < 8 and 0 <= c < 8


def desde_fen(fen):
    partes = fen.split()
    b = [[0] * 8 for _ in range(8)]
    for f, fila in enumerate(partes[0].split("/")):
        c = 0
        for ch in fila:
            if ch.isdigit():
                c += int(ch)
            else:
                v = "pnbrqk".index(ch.lower()) + 1
                b[f][c] = v if ch.isupper() else -v
                c += 1
    enroque = ["K" in partes[2], "Q" in partes[2], "k" in partes[2], "q" in partes[2]]
    ep = None if partes[3] == "-" else (8 - int(partes[3][1]), ord(partes[3][0]) - ord("a"))
    return b, enroque, ep


def rayo(b, f, c, dirs, p1, p2):
    for df, dc in dirs:
        nf, nc = f + df, c + dc
        while dentro(nf, nc):
            p = b[nf][nc]
            if p != 0:
                if p == p1 or p == p2:
                    return True
                break
            nf += df
            nc += dc
    return False


def atacada(b, f, c, por_blancas):
    s = 1 if por_blancas else -1
    pf = f + s
    if dentro(pf, c - 1) and b[pf][c - 1] == s * PEON:
        return True
    if dentro(pf, c + 1) and b[pf][c + 1] == s * PEON:
        return True
    for df, dc in SALTOS_CABALLO:
        if dentro(f + df, c + dc) and b[f + df][c + dc] == s * CABALLO:
            return True
    for df, dc in DIR_REY:
        if dentro(f + df, c + dc) and b[f + df][c + dc] == s * REY:
            return True
    if rayo(b, f, c, DIR_TORRE, s * TORRE, s * DAMA):
        return True
    if rayo(b, f, c, DIR_ALFIL, s * ALFIL, s * DAMA):
        return True
    return False


def contar_pseudo(b, s, enroque, ep):
    n = 0
    for f in range(8):
        for c in range(8):
            p = b[f][c]
            if p * s <= 0:
                continue
            t = abs(p)
            if t == PEON:
                d = -s
                inicio = 6 if s > 0 else 1
                f2 = f + d
                if not dentro(f2, c):
                    continue
                corona = f2 == 0 or f2 == 7
                if b[f2][c] == 0:
                    n += 4 if corona else 1
                    if f == inicio and b[f + 2 * d][c] == 0:
                        n += 1
                for dc in (-1, 1):
                    c2 = c + dc
                    if not dentro(f2, c2):
                        continue
                    if b[f2][c2] * s < 0:
                        n += 4 if corona else 1
                    elif ep == (f2, c2):
                        n += 1
            elif t == CABALLO or t == REY:
                for df, dc in (SALTOS_CABALLO if t == CABALLO else DIR_REY):
                    nf, nc = f + df, c + dc
                    if dentro(nf, nc) and b[nf][nc] * s <= 0:
                        n += 1
                if t == REY:
                    n += contar_enroques(b, f, c, s, enroque)
            else:
                dirs = DIR_ALFIL if t == ALFIL else DIR_TORRE if t == TORRE else DIR_ALFIL + DIR_TORRE
                for df, dc in dirs:
                    nf, nc = f + df, c + dc
                    while dentro(nf, nc):
                        if b[nf][nc] * s > 0:
                            break
                        n += 1
                        if b[nf][nc] != 0:
                            break
                        nf += df
                        nc += dc
    return n


def contar_enroques(b, f, c, s, enroque):
    fila = 7 if s > 0 else 0
    if f != fila or c != 4:
        return 0
    rival = s < 0
    corto, largo = (0, 1) if s > 0 else (2, 3)
    if atacada(b, fila, 4, rival):
        return 0
    n = 0
    if (enroque[corto] and b[fila][5] == 0 and b[fila][6] == 0 and b[fila][7] == s * TORRE
            and not atacada(b, fila, 5, rival) and not atacada(b, fila, 6, rival)):
        n += 1
    if (enroque[largo] and b[fila][1] == 0 and b[fila][2] == 0 and b[fila][3] == 0 and b[fila][0] == s * TORRE
            and not atacada(b, fila, 3, rival) and not atacada(b, fila, 2, rival)):
        n += 1
    return n


def buscar_rey(b, blancas):
    rey = REY if blancas else -REY
    for f in range(8):
        for c in range(8):
            if b[f][c] == rey:
                return f, c
    return -1, -1


def escudo_rey(b, blancas):
    rf, rc = buscar_rey(b, blancas)
    s = 1 if blancas else -1
    fila = rf - s
    if fila < 0 or fila > 7:
        return 0
    n = 0
    for dc in (-1, 0, 1):
        c = rc + dc
        if 0 <= c < 8 and b[fila][c] == s * PEON:
            n += 1
    return n


def malos_peones(b, blancas):
    s = 1 if blancas else -1
    por_col = [0] * 8
    for f in range(8):
        for c in range(8):
            if b[f][c] == s * PEON:
                por_col[c] += 1
    malos = 0
    for c in range(8):
        if por_col[c] > 1:
            malos += por_col[c] - 1
        izq = c > 0 and por_col[c - 1] > 0
        der = c < 7 and por_col[c + 1] > 0
        if por_col[c] > 0 and not izq and not der:
            malos += por_col[c]
    return malos


def caracteristicas(fen):
    b, enroque, ep = desde_fen(fen)
    atB = [[atacada(b, f, c, True) for c in range(8)] for f in range(8)]
    atN = [[atacada(b, f, c, False) for c in range(8)] for f in range(8)]

    mat = centro = peones = desarrollo = amenazas = espacio = 0.0
    for f in range(8):
        for c in range(8):
            p = b[f][c]
            s = 1 if p > 0 else (-1 if p < 0 else 0)
            t = abs(p)
            mat += s * VALOR[t]
            if 3 <= f <= 4 and 3 <= c <= 4:
                centro += s
                centro += (0.5 if atB[f][c] else 0) - (0.5 if atN[f][c] else 0)
            if t == PEON:
                peones += (6 - f) if s > 0 else -(f - 1)
            if t == CABALLO or t == ALFIL:
                if s > 0 and f != 7:
                    desarrollo += 1
                if s < 0 and f != 0:
                    desarrollo -= 1
            if s < 0 and atB[f][c]:
                amenazas += VALOR[t]
            if s > 0 and atN[f][c]:
                amenazas -= VALOR[t]
            if f <= 3 and atB[f][c]:
                espacio += 1
            if f >= 4 and atN[f][c]:
                espacio -= 1

    movB = contar_pseudo(b, 1, enroque, ep)
    movN = contar_pseudo(b, -1, enroque, ep)

    return [
        mat / 39.0,
        (movB - movN) / 40.0,
        centro / 6.0,
        peones / 20.0,
        (escudo_rey(b, True) - escudo_rey(b, False)) / 3.0,
        desarrollo / 4.0,
        amenazas / 15.0,
        espacio / 20.0,
        (malos_peones(b, False) - malos_peones(b, True)) / 6.0,
    ]
