import pyaudio
import numpy as np
import torch
import whisper
from flask import Flask, render_template, request

model = whisper.load_model("base.en")
def entry():
    return 
def record():
    p = pyaudio.PyAudio()

    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = int(RATE/10)  # 100 ms

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Speak!")

    audio = np.array([], dtype=np.int16)

    for i in range(int(RATE/CHUNK * 3)):
        data = stream.read(CHUNK)
        audio = np.append(audio, np.frombuffer(data, dtype=np.int16))

    torch_audio = torch.from_numpy(audio.flatten().astype(np.float32) / 32768.0)

    result = model.transcribe(torch_audio)
    predicted_text = result["text"]
    stream.stop_stream()
    stream.close()
    p.terminate()
    return predicted_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = record()
        return render_template('index.html', text=text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/record', methods=['GET', 'POST'])
def get_record():
    return record()


if __name__ == '__main__':
    app.run(debug=True)
