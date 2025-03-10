import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

st.title("QR Code Generator")

# Get user input
input_user = st.text_input("Please enter your social media account link:")

if input_user:
    # Create QR code object
    qr_object = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        border=4,
        box_size=10
    )
    qr_object.add_data(input_user)
    qr_object.make(fit=True)

    # Generate the QR code image
    image = qr_object.make_image(fill_color="orange", back_color="white")

    # Save image to buffer
    buf = BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)  # Reset buffer position

    # Display the QR code
    st.image(Image.open(buf), caption="QR Code", use_container_width=True)

    # Provide a download button
    st.download_button(
        label="Download QR Code",
        data=buf.getvalue(),
        file_name="QR_CODE.png",
        mime="image/png"
    )
