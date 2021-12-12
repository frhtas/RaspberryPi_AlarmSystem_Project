## NodeMCU kurulumu 
#NodeMCU kurmak için önce bağlantı kontrol edilmeli.
`lsusb`
**Bus 001 Device 010: ID 0403:6001 Future Technology Devices International, Ltd FT232 Serial (UART) IC** çıktısı görülmeli. 
`ls -l /dev/ttyUSB*`
ile device'ın olduğundan emin olunur.
# NodeMCU'ya flash atılması.SDK ve başlangıç programı cipe atılmalı .bin ile biten iki dosya
`$ git clone https://github.com/espressif/esptool.git` \n
**flash** atabilmek için esp nin bootloader ı ile iletişim kurmayı sağlayan yazılım `esptool` yüklenir.\n
`./esptool.py --port /dev/ttyUSB0 --baud 115200 erase_flash`\n
eski yazılımlar silinir. **Baud rate 9600**de olabilir.\n
`esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_mode dio 0x00000 İndirilenler/nodemcu-release-9-modules-2021-12-10-13-09-12-float.bin`\n
sdk donanım için gerekli. int versiyonu daha az yer kaplar. Bu** 115200 baud rate **olmalı.\n
`esptool.py --port /dev/ttyUSB0 --baud 9600 write_flash --flash_mode dio 0x3fc000 ESP8266_NONOS_SDK/bin/esp_init_data_default_v08.bin`\n
**sdk** yi başlatacak olan program için gerekli.\n

# Dosya yollamak için\n
NodeMCU-Tools kurulur. `sudo npm install --unsafe-perm nodemcu-tool -g` ile indirilir. kod yollamak için `nodemcu-tool -p /dev/ttyUSB0 -b 115200 upload helloworld.lua` kullanılır.\n

# minicom ile bağlanmak için \n
`sudo minicom --device /dev/ttyUSB0 --baudrate 115200`\n
ile girilir ve ctrl+A ya basılır sonra z ye basılır gelen ekranda configurasyon ayarı değiştirilmesi için **hardware flow control** kapatılır.Sonra cihazın reset tuşuna basılır.\n

# web serveri açmak için LAN
1.`minicom -b 115200 -o -D /dev/ttyUSB0 `\n
2.cihaz reset edilir.\n
3.`wifi.sta.config("wifi SSID adı ","bağlanılan wifi şifresi")`\n
4.`=wifi.sta.getip()` \n
5.`=wifi.sta.status() -- 5 bağlandı 2 bağlanmakta 3 şifre hatalı demek`\n
6.dofile("main.lua") -- bu dosya get ip deki ip de web sayfasını açar.



