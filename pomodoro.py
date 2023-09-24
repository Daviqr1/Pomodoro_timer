#pomodoro timer

import time
import os
import sys
import streamlit as st



st.title("Pomodoro Timer")
st.write("A simple timer for the Pomodoro Technique")
st.write("By Davi Rezende")
st.write("")


tempo_total = 25 * 60
tempo_restante = tempo_total



if st.button("Iniciar"):
    while tempo_restante > 0:
        mins, secs = divmod(tempo_restante, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        st.write(timer)
        time.sleep(1)
        tempo_restante -= 1
st.write("Fim do tempo!")


time_refresher = st.empty()
while True:
    time_refresher.text(time.strftime("%H:%M:%S"))
    time.sleep(1)
