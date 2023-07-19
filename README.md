# Skaner Żył (VF)
### WYNIKI
#### Obraz zarejestrowany przez kamere NoIR
![ori](https://user-images.githubusercontent.com/120425774/219521156-9f1e4441-8b21-4a45-9fe9-f68e8397a692.jpg)
#### CLAHE
![CLAHE_samo](https://user-images.githubusercontent.com/120425774/219521268-9f01fa3c-147e-4599-993e-a9984521db71.jpg)
#### CLAHE + Median Filter
![CLAHE MEDIAN](https://user-images.githubusercontent.com/120425774/219521323-53cdf4f9-16bd-412f-8ff5-160d1b7c01ad.jpg)




https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/f13306c6-81f2-46cd-a9c3-44226708a6eb


https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/f4ae1858-503d-4e02-aeb1-d0add9eca223

![IMG_3943](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/4bb40ecc-bddd-4162-85d8-aa9c357c2cc0)
![IMG_3931](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/d06b8bcf-821c-4de1-869d-04d43e366243)
![IMG_3![IMG_3926](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/b6290d1f-58a9-46dd-89af-a377deae4e1f)
927](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/6744febc-6d50-4e62-b44a-f42dff8407c9)
![IMG_3934](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/54cb7e86-337c-464c-8b67-39fff949aa32)
![IMG_3935](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/5c358f75-2281-4b6e-bf50-e1683b1b8d12)
![IMG_3939](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/d26c2ed2-585e-4b78-8941-c1485a3a9323)
![IMG_3942](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/9d718d83-160a-46a9-937c-891f6c2ef3b4)
![IMG_3924](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/71a12c79-befc-4bad-bccc-51676bb44ec6)
![IMG_3944](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/8fc68709-9a70-4c9f-8a74-6e2d0ee2bee9)






### Cel?
Celem tego projektu było stworzenie **przenośnego urządzenia do wizualizacji żył podskórnych w czasie rzeczywistym**, który będzie dostępny za znacznie niższą cenę niż obecnie dostępne profesjonalne urządzenia tego typu, których ceny zaczynają się od **3000$**. **Wykorzystano gotowe i łatwo dostępne do kupienia komponenty, aby zapewnić rozwiązanie jak najbardziej ekonomiczne i stosunkowo proste do samodzielnego złożenia.**
### Po co to wszystko?
Istnieją grupy chorych, dla których regularne przyjmowanie leków dożylnie (co 2/3 dni) stanowi konieczność, np. w przypadku chorób układu krzepnięcia. **Skaner żył jest narzędziem, które pomaga zminimalizować liczbę koniecznych wkłuć**, dzięki czemu można zmniejszyć niepotrzebny stres i ból dla pacjenta oraz zminimalizować liczbę prób, co jest szczególnie ważne w przypadku niemowląt i dzieci.
### Jak to działa?
![how_works](https://user-images.githubusercontent.com/120425774/219519729-e103330e-1e00-4065-a052-114915c339bf.png)

**Skaner żył** to urządzenie, które wykorzystuje technologię **bliskiej podczerwieni _(NIR, ang. Near-InfraRed)_**, aby zobrazować żyły ukryte pod skórą pacjenta. 
Skaner żył działa w sposób następujący: urządzenie emituje bezpieczne dla organizmu fale podczerwone o długości fal w zakresie **700nm-1000nm _(w tym przypadku 850nm)_**, które przenikają przez skórę pacjenta. W momencie, gdy fale podczerwone trafiają na żyłę, zostają częściowo pochłonięte przez krew, a otaczające tkanki odbijają światło z powrotem.
W ten sposób kamera pozbawiona filtra **IR _(NoIR camera = No Infrared filter camera)_** rejestruje obraz, który następnie jest przetwarzany przez algorytm **CLAHE _(ang. Contrast Limited Adaptive Histogram Equalization)_** w celu podwyższenia kontrastu. 
Proces przetwarzania obejmuje następujące kroki: <br>
**1)** Konwersja obrazu do przestrzeni **barw LAB**.<br>
**2)** Zastosowanie **CLAHE** na kanale **L** **_(jasność)_**.<br>
**3)** Połączenie kanałów **LAB** z powrotem do obrazu **BGR**.<br>
**4)** Na obraz nakładany jest **filtr** **_(Median Filter)_**.<br>
Po przetworzeniu obrazu, jest on wysyłany na lokalny serwer **Flask** działający na urządzeniu. Dzięki temu możemy połączyć się z urządzeniem przez sieć **Wi-Fi** **i zobaczyć obraz w czasie rzeczywistym na dowolnym urządzeniu** (smartfon, tablet, telewizor, laptop), które ma dostęp do tej samej sieci **Wi-Fi** _**(w tym przypadku sieć "VF")**_.
Urządzenie posiada baterie **3000mah**, która pozwala na kilkadziesiąt minut pracy.

### Sprzęt
**-Raspberry pi 4B 4GB**<br>
![raspberry](https://user-images.githubusercontent.com/120425774/219519043-36ef3765-eb90-4844-9529-c078ed58def6.jpg)<br>
**-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)** <br>
![kamera](https://user-images.githubusercontent.com/120425774/219519215-5b22be91-8f97-4141-aab5-ef4c1bae8114.jpg)<br>
**-WaveShare Li-polymer Battery HAT** <br>
![bateria](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/7badb618-1665-44c1-9f1f-cbea8764bc78)<br>
**-Karta microSD** <br>
![karta](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/8f0bd16a-ce50-422c-904e-543d0d7a3185)<br>
**-Obudowa** _(zaprojektowana w Autocad 2024, należy wysłać plik Case_stl.stl do wydruku 3d)_ <br>
![caser](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/b5f1bbe0-2185-49ea-93d2-5db69a813369)
<br>

### Koszty:
-Raspberry pi 4B 4GB - **599zł** <br>
-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm) - **100zł** <br>
-WaveShare Li-polymer Battery HAT - **90zł** <br>
-Karta microSD - **20zł** <br>
-Obudowa - Koszt wydruku ok **100zł** <br>
**RAZEM ok 910zł**


