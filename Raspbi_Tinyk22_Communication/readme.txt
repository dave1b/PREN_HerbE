Falls die UART-Verbindung nicht funktionieren sollte,
sollte man versuchen, das Bluetooth zu disablen (falls dieses nicht benutzt wird)

-- Anleitung --

sudo vi /boot/config/txt
add: #Disable Bluetooth dtoverlay=disable-bt

Reboot to apply changes