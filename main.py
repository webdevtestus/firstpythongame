"""
main.py instancia de la clase Game para ejecutar el metodo
Start a fin de correr el juego
"""
# importo la Clase Game desde file game, Clase Game
from game import Game

# creo la funcion main()
def main():
    # genero una instancia de la Clase Game
    alien_warfare = Game()
    alien_warfare.start()
        
# y ahora ejecutamos la funcion main()
if __name__ == '__main__':
    main()
    
    
    

