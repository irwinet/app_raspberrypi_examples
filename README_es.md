## README

Este repositorio contiene el código usado en los videos de YouTube sobre la Raspberry Pi.

## Proyectos

* 01 LED de 2 Pins: [código](01_basic_led/01_basic_led.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](01_basic_led/circuit_basic_led.png)

* 02 RGB LED: [código](02_rgb_led/02_rgb_led.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](02_rgb_led/circuit_rgb_led.png)

* 03 Botón: [código](03_button/03_button.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](03_button/circuit_button.png)

* 04 7Led LMS 5161AS: [código](04_7led_cathode/04_7led_cathode.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](04_7led_cathode/circuit_7led_cathode.png)

* 05 RGB LED + botón: [código](05_rgb_led_button/05_rgb_led_button.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](05_rgb_led_button/circuit_rgb_btn.png)

* 06 Sensor de temperature LM35 + MCP3008: [código](06_lm35_mcp3008/06_lm35_mcp3008.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](06_lm35_mcp3008/circuit_lm35_mcp3008.png)

* 07 Sensor de temperatura DS18B20 (KY-001): [código](07_ky001_temp/07_ky001_temp.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](07_ky001_temp/07_ky001_circuit.png)

* 08 Sensor de vibración (KY-002): [código](08_ky002_vibration/08_ky002_vibration.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](08_ky002_vibration/08_ky002_circuit.png)

* 09 Sensor magnético (KY-003): [código](09_ky003_magnetic/09_ky003_magnetic.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](09_ky003_magnetic/09_ky003_circuit.png)

* 10 Zumbador pasivo (KY-006): [código](10_ky006_pbuzzer/10_ky006_pbuzzer.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](10_ky006_pbuzzer/10_ky006_circuit.png)

* 11 LED RGB SMD (KY-009): [código](11_ky009_rgb_smd_led/11_rgb_smd_led.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](11_ky009_rgb_smd_led/11_ky009_circuit.png)

* 12 Fotointerruptor (KY-010): [código](12_ky010_photointerruptor/12_ky010_photointerruptor.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](12_ky010_photointerruptor/12_ky010_circuit.png)

* 13 LED de 2 Colores (KY-011): [código](13_ky011_2Color_led/13_ky011_2Color_led.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](13_ky011_2Color_led/13_ky011_circuit.png)

* 14 Zumbador activo (KY-012): [código](14_ky012_abuzzer/14_ky012_abuzzer.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](14_ky012_abuzzer/14_ky012_circuit.png)

* 15 Temperatura y Humedad DHT-11 (KY-015): [código](15_ky015_temperature_humidity/15_ky015_temperature_humidity.py)&nbsp;&nbsp;-&nbsp;&nbsp;[circuito](15_ky015_temperature_humidity/15_ky015_circuit.png)

## GPIO.setmode

**GPIO.BOARD**: Este es el modo GPIO que se usa en todos los ejemplos en este repositorio, este modo significa que para referirse a un PIN en el código se utiliza el número de PIN.

**GPIO.BCM**: Este es el otro modo disponible, para identificar los PINs en este modo se utiliza el número GPIO.

_En la imagen de abajo se pueden ver los números de PIN y GPIO_

## Esquema GPIO 

![GPIO Pins](RaspberryGPIO.png)
