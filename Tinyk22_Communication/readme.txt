Falls die UART-Verbindung nicht funktionieren sollte,
sollte man versuchen, das Bluetooth zu disablen (falls dieses nicht benutzt wird)

-- Anleitung --

sudo vi /boot/config/txt
add: #Disable Bluetooth dtoverlay=disable-bt

Reboot to apply changes§

------------------------------------------
#sys.close() vorerst behalten, da nicht bekannt, ob es gebraucht wird, wenn EngineOn -> getDistance -> EngineOff