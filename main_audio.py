# -*- Coding: utf-8 -*-
import os
from plugins import AudioHelp
import threading
import time

class MainAudio:
    """ Clase para probar las funcionalidades del plugin AudioHelp. """

    def __init__(self):
        self.audio_help = AudioHelp()
        self.test_recording()


    def test_recording(self):
        """ 
            Función de ejecución secuencial para probar grabación, 
            reconocimiento de audio a texto y reproducción de audio. 
        """
        print("Grabación de 5 segundos de prueba ...")
        t_stop = threading.Timer(5.0, self.stop_audio) # En 5 segundos ejecuta la función stop_audio
        t_stop.start()
        self.start_audio() # Comerzar a grabar el audio
        self.play_audio() # Reproducir audio guardado
    

    def get_url_save(self):
        """ Función de la ruta absoluta en donde se ubicará el audio nuevo o existente. """
        return os.path.dirname(os.path.abspath(__file__)) + "/plugins/audio/test_audio.wav"
    

    def start_audio(self):
        """ Función para comenzar a grabar. """
        print("Comenzar grabación ..............")
        self.audio_help.start_recording(
            url_path=self.get_url_save(), 
            callback_refresh=self.refresh_window,
            callback_final=self.final_audio
        )


    def stop_audio(self):
        """ Función para detener el audio. """
        print("Detener audio ...................")
        self.audio_help.stop_recording()


    def play_audio(self):
        """ Función para reproducir audio. """
        print("Reproducir audio existente ......")
        self.audio_help.__class__().play_audio(
            url_path=self.get_url_save()
        )


    def refresh_window(self):
        """ 
            Función llamada en start_audio dentro de la variable callback_refresh,
            que se ejecuta mientras el audio continue en estado de grabación.
        """
        print("Grabando ........................")
    

    def final_audio(self):
        """ 
            Función llamada en start_audio dentro de la variable callback_final, 
            que se ejecuta cuando el audio ha sido guardado en la ruta especificada. 
        """
        print("Audio guardado!! ................")
        self.audio_to_text()
    

    def audio_to_text(self):
        """ Función de reconocimiento de audio, convirtiendo audio en texto. """
        text = self.audio_help.__class__().read_audio(
            url_path=self.get_url_save(),
            language='es-ES'   
        )
        print("El audio grabado es: " + str(text.encode()))



def run():
    exec = MainAudio()

if __name__ == '__main__':
    run()