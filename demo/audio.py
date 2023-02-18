import whisper
import sounddevice as sd
import threading
import numpy as np
import argparse

model = whisper.load_model('base')

samplerate = sd.query_devices(kind='input')['default_samplerate']
block_duration = 3

options = whisper.DecodingOptions()

def callback(indata, frames, time, status):
    if status:
        print(status)
        audio = whisper.pad_or_trim(indata)

        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        # detect the spoken language
        _, probs = model.detect_language(mel)

        # decode the audio
        result = whisper.decode(model, mel, options)

        # print the recognized text
        print(f'{max(probs, key=probs.get)}: {result.text}')

    else:
        print('no input')

with sd.InputStream(device=1, channels=1, callback=callback,
                    blocksize=int(samplerate * block_duration),
                    samplerate=samplerate):
    print('press Ctrl+C to stop the recording')
    while True:
        response = input()
        if response in ('', 'q', 'Q'):
            break
