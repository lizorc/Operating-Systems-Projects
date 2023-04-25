import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import time
from pygame import mixer
from multiprocessing import Process


#* Reproducir archivo de audio
def musica(file, posicion, tiempo, texto):
    
    # Iniciar el mixer
    mixer.init()

    # Cargar el archivo
    mixer.music.load(file)

    # Reproducir el archivo desde la posicion dicha
    mixer.music.play(-1, posicion)

    print(f'Empezo {texto}')

    # Reproducir por el tiempo dicho
    time.sleep(tiempo)

    # Pausar el archivo
    mixer.music.stop()

    print(f'Termino {texto}')
    print('----------------')


if __name__ == '__main__':

    # Segundos que se va a reproducir la cancion principal
    tiempo = 10
    posicion = 0

    # Crear y empezar el proceso de la cancion principal
    song1 = Process(target = musica, args = ("s1.mp3", -0.001, tiempo, 'cancion'))
    song1.start()

    # Esperar el tiempo de reproduccion
    time.sleep(tiempo+0.1)

    # Terminar el proceso
    song1.terminate()

    while True:

        # Guardar la posición en tiempo que iba la canción principal
        posicion = posicion + tiempo
        
        # Crear y empezar el sonido de intermitencia
        sound = Process(target = musica, args = ("s2.mp3", -0.001, 5, 'sonido'))
        sound.start()

        # Esperar el tiempo de reproduccion
        time.sleep(5.1)

        # Crear y empezar el proceso de la cancion principal
        song = Process(target = musica, args = ("s1.mp3", posicion, tiempo, 'cancion'))
        song.start()

        # Esperar el tiempo de reproduccion
        time.sleep(tiempo+0.1)
    
