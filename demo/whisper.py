import whisper
import soundcard as sc
import threading
import queue
import numpy as np
import argparse

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE, channels=1) as mic:
    while True:
        data = mic.record(BUFFER_SIZE)
