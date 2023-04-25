import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import time
from pygame import mixer


#* Reproducir archivo de audio
def musica(file1, file2):
    
    # Iniciar el mixer
    mixer.init()

    # Cargar y reproducir la canción principal
    mixer.music.load(file1)
    mixer.music.play()

    print('Empezo cancion')
    temp = 0
    

    while True:

        # Reproducir por 10 segundos
        time.sleep(10)

        print('Termino cancion')
        print('----------------')

        # Guardar la posición en tiempo que iba la canción principal
        posicion = mixer.music.get_pos()
        posicion = temp + posicion/1000

        # Pausar la canción principal
        mixer.music.pause()

        # Cargar y reproducir el sonido intermedio
        mixer.music.load(file2)
        mixer.music.play()
        print('Empezo sonido')
            
        # Esperar que el sonido se reproduzca 
        while mixer.music.get_busy():
            continue

        print('Termino sonido')
        print('----------------')

        # Volver a cargar la canción principal
        mixer.music.load(file1)

        # Reproducir la cancion desde donde quedo
        mixer.music.play(-1, posicion)
        mixer.music.unpause()

        print('Empezo cancion')
        
        # Guardar el tiempo que reprodujo la canción
        temp = posicion


if __name__ == '__main__':
    musica('s1.mp3', 's2.mp3')




# antiviolador de piezas musicales, proteger la musica con audios percentiles 

#reproduce la pieza completa y por momentos reproduce una intercalada
#reproduce la pieza y la stop para mostrar la otra y que continue 