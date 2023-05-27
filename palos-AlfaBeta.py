import math
import random

class palos_juego:
    def __init__(self, no_palos):
        self.no_palos = no_palos
        self.max = 4
        self.min = 1
        self.max_profundidad = 9
    
    def quitarPalos(self, palos):
        self.no_palos -= palos
    
    def imprimirPalos(self):
        for i in range(self.no_palos):
            print("|", end = " ")

    def turnoComputadora(self):
        posicion = self.alphabeta(self.no_palos, True,-math.inf, math.inf, 0)[1]
        return posicion

    def alphabeta(self, palos, jugador, alfa, beta, prof):
        if self.no_palos == 0:
            return [1, None] if jugador else [-1, None]
        if prof == self.max_profundidad:
            return [0, None]

        if jugador:
            best = [-math.inf, None]
        else:
            best = [math.inf, None]

        for i in range(self.min, min(self.max, self.no_palos)+1):
            self.no_palos -= i
            resultado = self.alphabeta(palos, not jugador, alfa, beta, prof + 1)
            self.no_palos += i
            resultado[1] = i
            if jugador:
                if resultado[0] > best[0]:
                    best = resultado
                alfa = max(alfa, best[0])
            else:
                if resultado[0] < best[0]:
                    best = resultado
                beta = min(beta, best[0])

            if beta <= alfa:
                break
        return best
    
    def juego(self):
        resultado = 0
        while self.no_palos > 0:    
            self.imprimirPalos()
            while True:
                resultado = int(input(f"\nIngresa la cantidad de palos a quitar entre el {self.min} y el {self.max} "))        
                if self.max >= resultado >= self.min and resultado <= self.no_palos:
                    break; 
            self.quitarPalos(resultado)
            if self.no_palos == 0:
                print("\nLa computadora ha ganado!")
                break
            self.imprimirPalos()   
            computadora = self.turnoComputadora();
            self.quitarPalos(computadora)
            print(f"\nLa computadora ha quitado {computadora}")
            if self.no_palos == 0:
                print("\nEl jugador ha ganado")
            if self.no_palos < self.max:
                self.max = self.no_palos

            

numero_palos = random.randint(10,30)
tablero = palos_juego(numero_palos)

tablero.juego()
