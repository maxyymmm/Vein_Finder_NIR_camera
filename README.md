# Vein_Finder_NIR_camera
### WYNIKI
#### Obraz zarejestrowany przez kamere
![ori](https://user-images.githubusercontent.com/120425774/219521156-9f1e4441-8b21-4a45-9fe9-f68e8397a692.jpg)
#### CLAHE
![CLAHE_samo](https://user-images.githubusercontent.com/120425774/219521268-9f01fa3c-147e-4599-993e-a9984521db71.jpg)
#### CLAHE + Median Filter
![CLAHE MEDIAN](https://user-images.githubusercontent.com/120425774/219521323-53cdf4f9-16bd-412f-8ff5-160d1b7c01ad.jpg)
#### CLAHE + Gaussian Filter
![CLAHE GAUSSIAN](https://user-images.githubusercontent.com/120425774/219521338-c64d28ba-8005-43e1-a37b-6b83e03c05dc.jpg)
#### CLAHE GRAY + Median Filter
![CLAHE GRAY MEDIAN](https://user-images.githubusercontent.com/120425774/219521435-039208a7-3266-4f1f-9f91-9a278c4e08fb.jpg)


### Cel?
Celem tego projektu było stworzenia, możliwie najtaniej, urządzenia, które będzie umożliwiało wizualizację, w czasie rzeczywistym, żył podskórnych w celu ułatwienia wkłucia dożylnego. Istnieją obecnie, skutecznem profesionalne urządzenia tego typu, jednak są one bardzo drogie. Ceny zaczynają się od 3000$
### Po co to wszystko?
Istnieją grupy chorych, dla których regularne przyjmowanie leków dożylnie (co 2/3dni) stanowi konieczność, np. w przypadku chorób układu krzepnięcia. Skaner żył jest narzędziem, które pomaga zminimalizować liczbę koniecznych wkłuć.
### Jak to działa?
![how_works](https://user-images.githubusercontent.com/120425774/219519729-e103330e-1e00-4065-a052-114915c339bf.png)

Skaner żył to urządzenie, które wykorzystuje technologię bliskiej podczerwieni (NIR, ang. Near-InfraRed), aby zobrazować żyły ukryte pod skórą pacjenta. 
Skaner żył działa w sposób następujący: urządzenie emituje bezpieczne dla organizmu fale podczerwone o długości fal między 700 a 1000 nm, które przenikają przez skórę pacjenta. W momencie, gdy fale podczerwone trafiają na żyłę, zostają częściowo pochłonięte przez krew, a otaczające tkanki odbijają światło z powrotem.
W ten sposób kamera pozbawiona filtra IR (NoIR camera = No Infrared filter camera) rejestruje obraz, który następnie jest przetważany przez algorytm CLAHE (ang. Contrast Limited Adaptive Histogram Equalization) w celu podwyższenia kontrastu. Następnie, na obraz, jest nakładany filtr (Median Filter/Gaussian Filter) i wysyłany na wyjście.

### Sprzęt
-Raspberry pi 4B
![raspberry](https://user-images.githubusercontent.com/120425774/219519043-36ef3765-eb90-4844-9529-c078ed58def6.jpg)
-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)
![kamera](https://user-images.githubusercontent.com/120425774/219519215-5b22be91-8f97-4141-aab5-ef4c1bae8114.jpg)

