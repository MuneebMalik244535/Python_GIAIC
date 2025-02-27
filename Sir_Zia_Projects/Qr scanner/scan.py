import streamlit as st
import cv2
import numpy as np
from pyzbar.pyzbar import decode

st.title("QR Code Scanner with Camera")

# OpenCV se camera ka access lena
cap = cv2.VideoCapture(0)

stframe = st.empty()  # Streamlit ka frame update karne ke liye

while True:
    success, frame = cap.read()
    if not success:
        st.write("Camera not working")
        break
    
    # QR Code detect karna
    for barcode in decode(frame):
        qr_text = barcode.data.decode("utf-8")
        st.write(f"Scanned QR Code: {qr_text}")

        # QR Code ke upar rectangle draw karna
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 0), 5)

    # Streamlit frame update karna
    stframe.image(frame, channels="BGR")

cap.release()
cv2.destroyAllWindows()
