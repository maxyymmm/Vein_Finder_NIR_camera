# ENG BELOW! <br> <br>
# Skaner Żył NIR (Near-Infrared)  (VF)
### WYNIKI
#### Obraz zarejestrowany przez kamere NoIR
![ori](https://user-images.githubusercontent.com/120425774/219521156-9f1e4441-8b21-4a45-9fe9-f68e8397a692.jpg)
#### CLAHE
![CLAHE_samo](https://user-images.githubusercontent.com/120425774/219521268-9f01fa3c-147e-4599-993e-a9984521db71.jpg)
#### CLAHE + Median Filter
![CLAHE MEDIAN](https://user-images.githubusercontent.com/120425774/219521323-53cdf4f9-16bd-412f-8ff5-160d1b7c01ad.jpg)



https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/e6118d30-405e-4acc-8fe4-dadf006c9961


https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/f9007cd2-94c9-444e-a737-4586e2fbef74




![IMG_3943](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/4bb40ecc-bddd-4162-85d8-aa9c357c2cc0)
![IMG_3967](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/a94b1ef2-6fe1-4d4b-b0e7-1062c13fda35)
![IMG_3966](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/fdf7836a-3201-4026-86aa-58aa66711463)
![IMG_3934](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/54cb7e86-337c-464c-8b67-39fff949aa32)
![IMG_3935](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/5c358f75-2281-4b6e-bf50-e1683b1b8d12)
![IMG_3968](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/ebc6b44f-d4dd-423a-a30d-b14be451522f)
![IMG_3942](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/9d718d83-160a-46a9-937c-891f6c2ef3b4)
![IMG_3924](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/71a12c79-befc-4bad-bccc-51676bb44ec6)
![IMG_3944](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/8fc68709-9a70-4c9f-8a74-6e2d0ee2bee9)






### Cel?
Celem tego projektu było stworzenie **przenośnego urządzenia do wizualizacji żył podskórnych w czasie rzeczywistym**, który będzie dostępny za znacznie niższą cenę niż obecnie dostępne profesjonalne urządzenia tego typu, których ceny zaczynają się od **3000$**. **Wykorzystano gotowe i łatwo dostępne do kupienia komponenty, aby zapewnić rozwiązanie jak najbardziej ekonomiczne i stosunkowo proste do samodzielnego złożenia.**
### Po co to wszystko?
Istnieją grupy chorych, dla których regularne przyjmowanie leków dożylnie (co 2/3 dni) stanowi konieczność, np. w przypadku chorób układu krzepnięcia. **Skaner żył jest narzędziem, które pomaga zminimalizować liczbę koniecznych wkłuć**, dzięki czemu można zmniejszyć niepotrzebny stres i ból dla pacjenta oraz zminimalizować liczbę prób, co jest szczególnie ważne w przypadku niemowląt i dzieci.
### Jak to działa?
![scheme](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/67e30692-eaae-4d8a-b628-c2d68beab24c)


**Skaner żył** to urządzenie, które wykorzystuje technologię **bliskiej podczerwieni _(NIR, ang. Near-InfraRed)_**, aby zobrazować żyły ukryte pod skórą pacjenta. 
Skaner żył działa w sposób następujący: urządzenie emituje bezpieczne dla organizmu fale podczerwone o długości fal w zakresie **700nm-1000nm _(w tym przypadku 850nm)_**, które przenikają przez skórę pacjenta. W momencie, gdy fale podczerwone trafiają na żyłę, zostają częściowo pochłonięte przez krew, a otaczające tkanki odbijają światło z powrotem. **_Zastosowanie kilku diod o różnych długościach fali może dać nieznacznie lepsze rezultaty, jednak nie ma gotowych układów pozwalających na taką funkcjonalność. Zbudowanie takiego skanera wymagałoby lutowania, stosowania oddzielnych źródeł napięcia i byłoby bardziej skomplikowane. Celem tego projektu było stworzenie stosunkowo prostego urządzenia, które spełnia swoje podstawowe funkcje w bezpieczny i skuteczny sposób._** <br>
W ten sposób kamera pozbawiona filtra **IR _(NoIR camera = No Infrared filter camera)_** rejestruje obraz, który następnie jest przetwarzany przez algorytm **CLAHE _(ang. Contrast Limited Adaptive Histogram Equalization)_** w celu podwyższenia kontrastu. 
Proces przetwarzania obejmuje następujące kroki: <br>
**1)** Konwersja obrazu do przestrzeni **barw LAB**.<br>
**2)** Zastosowanie **CLAHE** na kanale **L** **_(jasność)_**.<br>
**3)** Połączenie kanałów **LAB** z powrotem do obrazu **BGR**.<br>
**4)** Na obraz nakładany jest **filtr** **_(Median Filter)_**.<br>
Po przetworzeniu obrazu, jest on wysyłany na lokalny serwer **Flask** działający na urządzeniu. Aby zobaczyć strumień wideo ze skanera żył na innym urządzeniu, należy podłączyć się do hotspotu lokalnego Raspberry Pi. Następnie zeskanować naklejony na obudowę kod qr. <br>
**LUB** otworzyć przeglądarkę internetową na urządzeniu i wpisać ręcznie ustawiony adres IP Raspberry Pi oraz port **5000** (np. http://192.168.1.254:5000/). <br>
Urządzenie zostało wyposażone w baterię o pojemności **3000mah**, która pozwala na kilkanaście minut pracy.

### Sprzęt
**-Raspberry pi 4B 4GB**<br>
![raspberry](https://user-images.githubusercontent.com/120425774/219519043-36ef3765-eb90-4844-9529-c078ed58def6.jpg)<br>
**-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)** <br>
![kamera](https://user-images.githubusercontent.com/120425774/219519215-5b22be91-8f97-4141-aab5-ef4c1bae8114.jpg)<br>
**-WaveShare Li-polymer Battery HAT** <br>
![bateria](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/7badb618-1665-44c1-9f1f-cbea8764bc78)<br>
**-Karta microSD** <br>
![karta](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/8f0bd16a-ce50-422c-904e-543d0d7a3185)<br>
**-Obudowa** _(zaprojektowana w Autocad 2024, należy wysłać plik **Case_stl.stl** do wydruku 3d)_ <br>
![caser](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/b5f1bbe0-2185-49ea-93d2-5db69a813369)
![case_autocad](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/61d7e37c-27e4-435d-b0ac-f01d436fdc7f)

<br>

### Koszty:
-Raspberry pi 4B 4GB - **599 PLN** <br>
-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm) - **100 PLN** <br>
-WaveShare Li-polymer Battery HAT - **90 PLN** <br>
-Karta microSD - **20 PLN** <br>
-Obudowa - Koszt wydruku ok **100 PLN** <br>
**RAZEM ok 910 PLN**

### Wymagania
Raspberry Pi z zainstalowanym **Raspberry Pi OS w wersji 4.3 (September 2022)** lub nowszej.
**Python** w wersji **3.9.2** lub nowszej.

### Konfiguracja Raspberry Pi
**1)** Pobranie pliu _**veinfinder.py**_ oraz _**requirements.txt**_ na raspberry pi <br>
**2)** Instalacja potrzebnych bibliotek z pliku _**requirements.txt**_

```console
vf@raspberrypi:~$ pip install -r requirements.txt
```
**3)** Włączenie **"Legacy Camera Enable"** _(do poprawnego działania kamery)_:
```console
vf@raspberrypi:~$ sudo raspi-config
```
![raspi1](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/5e73c265-1815-4603-b06f-4b85b63463dd)
![raspi2](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/3534fcf2-035f-4327-8576-b97477de719e)
**4)** Utworzenie hotspotu **Wifi**
![wifi2](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/7b26dd16-d31b-4e4e-ac30-df37cba40614)
**5)** **Ustawienie priorytetu wybierania sieci przy starcie urządzenie** (urządzenie będzie łączyć się automatycznie z naszą siecią jako pierwszy wybór przy starcie urządzenia)
![356582114_658103286376636_258303166703897224_n](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/eea4dcd2-d3bb-428d-b232-ea2b2d729b20)
![357157389_660844529267880_1522471513100033015_n](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/09969ced-c56b-499a-8d47-dad4aed6b909)
**6)** Ustawienie **statycznego adresu IP**
![358653618_933626021062454_8678450154277752298_n](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/131d3b6f-fb84-4fbf-8084-a24947c43ad7)
**7)** Ustawienie automatycznego włączania przy starcie urządzenia programu _**veinfinder.py**_
```console
vf@raspberrypi:~$ sudo nano /etc/rc.local
```
Dopisujemy: 
```console
sudo python3 SCIEŻKA_PLIKU/veinfinder.py &
```
![rtc2](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/ebbde9b5-2d02-49a1-b965-127ef5896980)
**GOTOWE!**

### Użytkowanie
Urzędzenie włączamy przyciskiem **ON/OFF** <br>
Urządzenie wyłączamy naciskając dwukrotnie przycisk **ON/OFF** <br>
Urządzenie można ładować za pomocą **USB TYP C (Quick charge)** lub **Micro USB (Charge)** (5 diod LED wskazuje poziomu naładowania baterii oraz statusu ładowania) <br> <br>

# ENG
# Vein Finder NIR (Near-Infrared) (VF)
### RESULTS
#### Image captured by NoIR camera
![ori](https://user-images.githubusercontent.com/120425774/219521156-9f1e4441-8b21-4a45-9fe9-f68e8397a692.jpg)
#### CLAHE
![CLAHE_samo](https://user-images.githubusercontent.com/120425774/219521268-9f01fa3c-147e-4599-993e-a9984521db71.jpg)
#### CLAHE + Median Filter
![CLAHE MEDIAN](https://user-images.githubusercontent.com/120425774/219521323-53cdf4f9-16bd-412f-8ff5-160d1b7c01ad.jpg)



https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/e6118d30-405e-4acc-8fe4-dadf006c9961


https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/f9007cd2-94c9-444e-a737-4586e2fbef74




![IMG_3943](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/4bb40ecc-bddd-4162-85d8-aa9c357c2cc0)
![IMG_3967](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/a94b1ef2-6fe1-4d4b-b0e7-1062c13fda35)
![IMG_3966](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/fdf7836a-3201-4026-86aa-58aa66711463)
![IMG_3934](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/54cb7e86-337c-464c-8b67-39fff949aa32)
![IMG_3935](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/5c358f75-2281-4b6e-bf50-e1683b1b8d12)
![IMG_3968](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/ebc6b44f-d4dd-423a-a30d-b14be451522f)
![IMG_3942](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/9d718d83-160a-46a9-937c-891f6c2ef3b4)
![IMG_3924](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/71a12c79-befc-4bad-bccc-51676bb44ec6)
![IMG_3944](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/8fc68709-9a70-4c9f-8a74-6e2d0ee2bee9)






### Purpose?
The aim of this project was to create a **portable device for visualizing subcutaneous veins in real-time**, which would be available at a much lower cost than currently available professional devices of this type, which start at **$3000**. **Ready-made and easily accessible components were used to provide the most economical and relatively simple solution for self-assembly.**
### Why all this?
There are groups of patients for whom regular intravenous drug administration (every 2/3 days) is necessary, e.g., in the case of coagulation system disorders. **Vein finder is a tool that helps minimize the number of necessary punctures**, thus reducing unnecessary stress and pain for the patient and minimizing the number of attempts, which is particularly important for infants and children.
### How does it work?
![scheme](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/67e30692-eaae-4d8a-b628-c2d68beab24c)


**Vein scanner** is a device that uses **near-infrared technology (NIR)** to visualize veins hidden under the patient's skin. The vein scanner works as follows: the device emits safe infrared waves with wavelengths in the range of **700nm-1000nm _(in this case 850nm)_**, which penetrate the patient's skin. When the infrared waves hit the vein, they are partially absorbed by the blood, and the surrounding tissues reflect the light back. **_The use of several diodes with different wavelengths may give slightly better results, but there are no ready-made circuits that allow for such functionality. Building such a scanner would require soldering, separate voltage sources, and would be more complicated than what has been achieved in this project. The goal of this project was to create a relatively simple device that fulfills its basic functions in a safe and effective way._** <br>
The camera that is devoid of an **IR filter _(NoIR camera = No Infrared filter camera)_**, records the image, which is then processed by the **CLAHE algorithm _(Contrast Limited Adaptive Histogram Equalization)_** to enhance the contrast.
The processing process involves the following steps: <br>
**1)** Conversion of the image to the **LAB color space**.<br>
**2)** Applying **CLAHE** to the **L channel _(Lightness)_**.<br>
**3)** Merging the **LAB channels** back to the **BGR** image.<br>
**4)** A **filter (Median Filter)** is applied to the image.<br>
After processing the image, it is sent to a local **Flask** server running on the device. To view the video stream from the vein scanner on another device, connect to the Raspberry Pi's local hotspot.Then, scan the QR code attached to the device's casing. <br>
**Alternatively**, you can open a web browser on your device and manually enter the Raspberry Pi's statically assigned IP address and port **5000** (e.g., http://192.168.1.254:5000/). This will display the real-time video stream from the vein scanner. <br>
The device is equipped with a **3000mAh battery**, which allows for several minutes of operation.
### Hardware
**-Raspberry pi 4B 4GB**<br>
![raspberry](https://user-images.githubusercontent.com/120425774/219519043-36ef3765-eb90-4844-9529-c078ed58def6.jpg)<br>
**-Camera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)** <br>
![kamera](https://user-images.githubusercontent.com/120425774/219519215-5b22be91-8f97-4141-aab5-ef4c1bae8114.jpg)<br>
**-WaveShare Li-polymer Battery HAT** <br>
![bateria](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/7badb618-1665-44c1-9f1f-cbea8764bc78)<br>
**-MicroSD Card** <br>
![karta](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/8f0bd16a-ce50-422c-904e-543d0d7a3185)<br>
**-Case** _(zaprojektowana w Autocad 2024, należy wysłać plik **Case_stl.stl** do wydruku 3d)_ <br>
![caser](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/b5f1bbe0-2185-49ea-93d2-5db69a813369)
![case_autocad](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/61d7e37c-27e4-435d-b0ac-f01d436fdc7f)

<br>

### Costs:
-Raspberry pi 4B 4GB - **599zł** <br>
-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm) - **100zł** <br>
-WaveShare Li-polymer Battery HAT - **90zł** <br>
-Karta microSD - **20zł** <br>
-Obudowa - Koszt wydruku ok **100zł** <br>
**TOTAL** approximately **910 PLN** ~ **230 USD**

### Requirements
Raspberry Pi with **Raspberry Pi OS version 4.3 (September 2022**) or newer.
**Python** version **3.9.2** or newer.

### Raspberry Pi Configuration
**1)** Download the **_veinfinder.py_** file and **_requirements.txt_** to the Raspberry Pi. <br>
**2)** Install the required libraries from the **_requirements.txt_** file:

```console
vf@raspberrypi:~$ pip install -r requirements.txt
```
**3)** Enable **"Legacy Camera Enable"** _(required for proper camera operation):_
```console
vf@raspberrypi:~$ sudo raspi-config
```
![raspi1](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/5e73c265-1815-4603-b06f-4b85b63463dd)
![raspi2](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/3534fcf2-035f-4327-8576-b97477de719e)
**4)** Create a **Wi-Fi** hotspot.
![wifi2](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/7b26dd16-d31b-4e4e-ac30-df37cba40614)
**5)** **Set priority for network selection at startup** (the device will automatically connect to our network as the first choice at startup).
![356582114_658103286376636_258303166703897224_n](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/eea4dcd2-d3bb-428d-b232-ea2b2d729b20)
![357157389_660844529267880_1522471513100033015_n](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/09969ced-c56b-499a-8d47-dad4aed6b909)
**6)** Set **static IP** address
![358653618_933626021062454_8678450154277752298_n](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/131d3b6f-fb84-4fbf-8084-a24947c43ad7)
**7)** Set up automatic startup of the **_veinfinder.py_** program when the device boots:
```console
vf@raspberrypi:~$ sudo nano /etc/rc.local
```
Add the following line:
```console
sudo python3 PATH_TO_FILE/veinfinder.py &
```
![rtc2](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/ebbde9b5-2d02-49a1-b965-127ef5896980)
**READY!**

### Usage
To turn on the device, press the **ON/OFF** button. <br>
To turn off the device, press the **ON/OFF** button twice. <br>
The device can be charged using **USB TYPE C (Quick charge)** or** Micro USB (Charge)**. _(The five LED indicators will display the battery capacity and charging status)_

   
   

   
   


