from flask import Flask, Response
from threading import Lock
from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2

app = Flask('_name_')
camera = PiCamera()
lock = Lock()

# Inicjalizacja kamery przy starcie serwera
def initialize_camera():
    camera.resolution = (640, 480)
    camera.framerate = 30
    # camera.start_preview() # Podglad kamery na urzadzeniu

def apply_clahe(frame_img):
    # Przetwarzanie obrazu - CLAHE
        lab_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab_img)

        for i in range(3):
            clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8+i*4,8+i*4))
            l = clahe.apply(l)

        lab_img = cv2.merge((l,a,b))
        median_lab_img = cv2.medianBlur(lab_img, 3)
        median_bgr_img = cv2.cvtColor(median_lab_img, cv2.COLOR_LAB2BGR)

        return median_bgr_img

# Funkcja generująca strumień wideo
def generate_video_stream():
    global camera
    global lock

    with lock:
        raw_capture = PiRGBArray(camera, size=(640, 480))
        for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
            # Przechwytywanie obecnej klatki
            frame_img = frame.array
            
            # Przetwarzanie obrazu - CLAHE
            processed_frame = apply_clahe(frame_img)

            # Zapisanie strumienia wideo
            ret, jpeg = cv2.imencode('.jpg', processed_frame)

            # Wyślij klatkę jako odpowiedź na żądanie klienta
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

            # Wyczyść bufor
            raw_capture.truncate(0)


# Endpoint do strumienia wideo
@app.route('/')
def video_feed():
    return Response(generate_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Inicjalizuj kamerę przy starcie serwera
    initialize_camera()

    # Uruchom serwer Flask
    app.run(host='0.0.0.0', port=5000)
