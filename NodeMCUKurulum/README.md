## NodeMCU kurulumu 
#NodeMCU kurmak için önce bağlantı kontrol edilmeli.
`lsusb`
**Bus 001 Device 010: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC** çıktısı görülmeli. 
`ls -l /dev/ttyUSB*`
ile device'ın olduğundan emin olunur.
# NodeMCU'ya flash atılması.SDK ve başlangıç programı cipe atılmalı .bin ile biten iki dosya
`$ git clone https://github.com/espressif/esptool.git`
**flash** atabilmek için esp nin bootloader ı ile iletişim kurmayı sağlayan yazılım `esptool` yüklenir.
`./esptool.py --port /dev/ttyUSB0 --baud 115200 erase_flash`
eski yazılımlar silinir. **Baud rate 9600**de olabilir.
`esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_mode dio 0x00000 İndirilenler/nodemcu-release-9-modules-2021-12-10-13-09-12-float.bin`
sdk donanım için gerekli. int versiyonu daha az yer kaplar. Bu** 115200 baud rate **olmalı.
`esptool.py --port /dev/ttyUSB0 --baud 9600 write_flash --flash_mode dio 0x3fc000 ESP8266_NONOS_SDK/bin/esp_init_data_default_v08.bin`
**sdk** yi başlatacak olan program için gerekli.

# Dosya yollamak için
NodeMCU-Tools kurulur. `sudo npm install --unsafe-perm nodemcu-tool -g` ile indirilir. kod yollamak için `nodemcu-tool -p /dev/ttyUSB0 -b 115200 upload helloworld.lua` kullanılır.

# minicom ile bağlanmak için 
`sudo minicom --device /dev/ttyUSB0 --baudrate 115200`
ile girilir ve ctrl+A ya basılır sonra z ye basılır gelen ekranda configurasyon ayarı değiştirilmesi için **hardware flow control** kapatılır.Sonra cihazın reset tuşuna basılır.


