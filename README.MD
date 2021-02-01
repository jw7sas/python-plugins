* Crear entorno virtual
    pip install virtualenv
    virtualenv venv

* Inicializar entorno virtual en windows
    cd venv/Scripts
    activate
    cd ../../

* Instalar los requirimientos 
    pip install -r requirements.txt

# Documentación:

* File audio_help.py 
    -> Class - AudioHelp in forder plugins/audio
        * Clase para grabar, reproducir y reconocer audio en texto.
        -> Dependencias: pip install
            * PyAudio==0.2.11
            * SpeechRecognition==3.8.1
            * google_api_python_client==1.12.8

* File pyqt5_custom.py
    -> Class - pyqt5_custom.py in folder plugins/interface
        * Clases que contienen campos personalizados de PyQt5
        -> Dependencias: pip install
            * PyQt5==5.15.2 


* Nota: 
Las pruebas de los plugins empiezan con la palabra main, seguida de raya al piso y el nombre de lo que se va a probar.