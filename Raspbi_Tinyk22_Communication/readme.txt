Falls die UART-Verbindung nicht funktionieren sollte,
sollte man versuchen, das Bluetooth zu disablen (falls dieses nicht benutzt wird)

-- Anleitung --

sudo vi /boot/config/txt
add: #Disable Bluetooth dtoverlay=disable-bt

Reboot to apply changes







--------------
Bim programm zemefüege:

con und ser mönd probably bi de Initialisierig erstellt werde
    con = tinyk22_con.tinyk22_con()
    ser = con.getconnection()


    try:
    finally: ser.close();