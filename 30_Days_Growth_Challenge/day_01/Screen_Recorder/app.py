# import streamlit as st
# import cv2
# import pyautogui
# import numpy as np
# import time
# import os

# st.set_page_config(page_title="Screen Recorder", layout="centered")

# st.markdown("""
#     <style>
#     .main {
#         background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
#         color: white;
#     }
#     .stButton>button {
#         background-color: #ff4b4b;
#         color: white;
#         font-weight: bold;
#         border-radius: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# st.title("🎥 Screen Recorder - Python + Streamlit")

# filename = st.text_input("Enter filename", "recording.mp4")
# duration = st.slider("Select duration (seconds)", 5, 60, 10)
# fps = st.slider("Frames per second (FPS)", 5, 30, 10)

# if st.button("Start Recording"):
#     st.success("Recording started...")

#     screen_size = pyautogui.size()
#     codec = cv2.VideoWriter_fourcc(*"mp4v")
#     out = cv2.VideoWriter(filename, codec, fps, screen_size)

#     start_time = time.time()
#     while True:
#         img = pyautogui.screenshot()
#         frame = np.array(img)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         out.write(frame)

#         if time.time() - start_time > duration:
#             break

#     out.release()
#     st.success(f"Recording saved as {filename}")

#     with open(filename, "rb") as video_file:
#         btn = st.download_button(label="📥 Download Recording", data=video_file, file_name=filename)

#     os.remove(filename)
import streamlit as st
import cv2
import pyautogui
import numpy as np
import time
import os

st.set_page_config(page_title="Screen Recorder", layout="centered")

st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎥 Screen Recorder - Python + Streamlit")

filename = st.text_input("Enter filename", "recording.mp4")
duration = st.slider("Select duration (seconds)", 5, 60, 10)
fps = st.slider("Frames per second (FPS)", 5, 30, 10)

if st.button("Start Recording"):
    st.success("Recording started...")

    screen_size = pyautogui.size()
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(filename, codec, fps, screen_size)

    start_time = time.time()
    progress = st.progress(0)
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

        elapsed = time.time() - start_time
        if elapsed > duration:
            break
        progress.progress(min(int((elapsed / duration) * 100), 100))

    out.release()
    st.success(f"Recording saved as {filename}")

    with open(filename, "rb") as video_file:
        st.download_button(label="📥 Download Recording", data=video_file, file_name=filename)

    os.remove(filename)
