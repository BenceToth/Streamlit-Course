import streamlit as st

# Image
st.header('Display Image using st.image')
st.image('./media/image.jpg', caption='City aerial view', width=500)

# Video
st.header('Display Video using st.video')
video_file = open('./media/waterfalls.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

# Audio
st.header('Display Audio using st.audio')
audio_file = open('./media/audio.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')