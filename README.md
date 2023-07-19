# Vein_Finder_NIR_camera
### WYNIKI
#### Obraz zarejestrowany przez kamere NoIR
![ori](https://user-images.githubusercontent.com/120425774/219521156-9f1e4441-8b21-4a45-9fe9-f68e8397a692.jpg)
#### CLAHE
![CLAHE_samo](https://user-images.githubusercontent.com/120425774/219521268-9f01fa3c-147e-4599-993e-a9984521db71.jpg)
#### CLAHE + Median Filter
![CLAHE MEDIAN](https://user-images.githubusercontent.com/120425774/219521323-53cdf4f9-16bd-412f-8ff5-160d1b7c01ad.jpg)


### Cel?
Celem tego projektu było stworzenie, możliwie najtaniej, przenośnego urządzenia, które będzie umożliwiało wizualizację, w czasie rzeczywistym, żył podskórnych w celu ułatwienia wkłucia dożylnego. Istnieją obecnie, skuteczne, profesionalne urządzenia tego typu, jednak są one bardzo drogie. Ceny zaczynają się od 3000$
### Po co to wszystko?
Istnieją grupy chorych, dla których regularne przyjmowanie leków dożylnie (co 2/3 dni) stanowi konieczność, np. w przypadku chorób układu krzepnięcia. Skaner żył jest narzędziem, które pomaga zminimalizować liczbę koniecznych wkłuć, dzięki czemu można zmniejszyć niepotrzebny stres i ból dla pacjenta oraz zminimalizować liczbę prób, co jest szczególnie ważne w przypadku niemowląt i dzieci.
### Jak to działa?
![how_works](https://user-images.githubusercontent.com/120425774/219519729-e103330e-1e00-4065-a052-114915c339bf.png)

Skaner żył to urządzenie, które wykorzystuje technologię bliskiej podczerwieni (NIR, ang. Near-InfraRed), aby zobrazować żyły ukryte pod skórą pacjenta. 
Skaner żył działa w sposób następujący: urządzenie emituje bezpieczne dla organizmu fale podczerwone o długości fal między 700 a 1000 nm (w tym przypadku 850nm), które przenikają przez skórę pacjenta. W momencie, gdy fale podczerwone trafiają na żyłę, zostają częściowo pochłonięte przez krew, a otaczające tkanki odbijają światło z powrotem.
W ten sposób kamera pozbawiona filtra IR (NoIR camera = No Infrared filter camera) rejestruje obraz, który następnie jest przetwarzany przez algorytm CLAHE (ang. Contrast Limited Adaptive Histogram Equalization) w celu podwyższenia kontrastu. 
Proces przetwarzania obejmuje następujące kroki:
1) Konwersja obrazu do przestrzeni barw LAB.
2) Zastosowanie CLAHE na kanale L (jasność).
3) Połączenie kanałów LAB z powrotem do obrazu BGR.
4) Na obraz nakładany jest filtr (Median Filter).
Po przetworzeniu obrazu, jest on wysyłany na lokalny serwer Flask działający na urządzeniu. Dzięki temu możemy połączyć się z urządzeniem przez sieć Wi-Fi i zobaczyć obraz w czasie rzeczywistym na dowolnym urządzeniu (smartfon, tablet, telewizor, laptop), które ma dostęp do tej samej sieci Wi-Fi (w tym przypadku sieć "VF").
Urządzenie posiada baterie 3000mah, która pozwala na kilkadziesiąt minut pracy.

### Sprzęt
-Raspberry pi 4B 4GB<br>
![raspberry](https://user-images.githubusercontent.com/120425774/219519043-36ef3765-eb90-4844-9529-c078ed58def6.jpg)<br>
-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)<br>
![kamera](https://user-images.githubusercontent.com/120425774/219519215-5b22be91-8f97-4141-aab5-ef4c1bae8114.jpg)<br>
-WaveShare Li-polymer Battery HAT<br>
![bateria](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/7badb618-1665-44c1-9f1f-cbea8764bc78)<br>
-Karta microSD<br>
![karta](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/8f0bd16a-ce50-422c-904e-543d0d7a3185)<br>
-Obudowa (zaprojektowana w Autocad 2024, należy wysłać plik Case_stl.stl do wydruku)<br>
![caser](https://github.com/maxyymmm/Vein_Finder_NIR_camera/assets/120425774/b5f1bbe0-2185-49ea-93d2-5db69a813369)
<br>

### Koszty:
-Raspberry pi 4B 4GB<br>
-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)<br>
-WaveShare Li-polymer Battery HAT<br>
-Karta microSD - <br>
-Obudowa - Koszt wydruku ok 100zł
