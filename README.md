# Vein_Finder_NIR_camera

### Cel?
Celem tego projektu było stworzenia, możliwie najtaniej, urządzenia, które będzie umożliwiało wizualizację, w czasie rzeczywistym, żył podskórnych w celu ułatwienia wkłucia dożylnego. Istnieją obecnie, skutecznem profesionalne urządzenia tego typu, jednak są one bardzo drogie. Ceny zaczynają się od 3000$
### Po co to wszystko?
Istnieją grupy chorych, dla których regularne przyjmowanie leków dożylnie (co 2/3dni) stanowi konieczność, np. w przypadku chorób układu krzepnięcia. Skaner żył jest narzędziem, które pomaga zminimalizować liczbę koniecznych wkłuć.
### Jak to działa?
Skaner żył to urządzenie, które wykorzystuje technologię bliskiej podczerwieni (NIR, ang. Near-InfraRed), aby zobrazować żyły ukryte pod skórą pacjenta. 
Skaner żył działa w sposób następujący: urządzenie emituje bezpieczne dla organizmu fale podczerwone o długości fal między 700 a 1000 nm, które przenikają przez skórę pacjenta. W momencie, gdy fale podczerwone trafiają na żyłę, zostają częściowo pochłonięte przez krew, a otaczające tkanki odbijają światło z powrotem.
W ten sposób kamera pozbawiona filtra IR (NoIR camera = No Infrared filter camera) rejestruje obraz, który następnie jest przetważany przez algorytm CLAHE (ang. Contrast Limited Adaptive Histogram Equalization) w celu podwyższenia kontrastu. Następnie, na obraz, jest nakładany filtr (Median Filter/Gaussian Filter) i wysyłany na wyjście.

### Sprzęt
-Raspberry pi 4B

-Kamera OdSeven Camera HD IR-CUT OV5647 5Mpx + moduły IR (850nm)

