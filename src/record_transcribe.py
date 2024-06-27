import tkinter as tk
from tkinter import messagebox
import pyaudio
import wave
import whisper
import threading
import ollama

class AudioRecorder:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False
        self.messages = []

    def start_recording(self):
        self.frames = []
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=1024)
        self.recording = True
        self.record_audio()

    def record_audio(self):
        if self.recording:
            data = self.stream.read(1024)
            self.frames.append(data)
            # Call this method again after a short delay
            root.after(1, self.record_audio)

    def stop_recording(self):
        self.recording = False
        self.stream.stop_stream()
        self.stream.close()

    def save_recording(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(self.frames))
        wf.close()

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language="english")
    return result["text"]

def start_recording():
    recorder.start_recording()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop_recording():
    recorder.stop_recording()
    recorder.save_recording(output_filename)
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    transcribed_text = transcribe_audio(output_filename)
    # messagebox.showinfo("Transcription", transcribed_text)
    print(transcribed_text)
    LLM_chat(transcribed_text=transcribed_text)

def LLM_chat(transcribed_text):
    recorder.messages.append(
    {
        'role': 'user',
        'content': transcribed_text,
    })

    response = ollama.chat(model='llama3:instruct', messages=recorder.messages)
    recorder.messages.append(response['message'])
    print()
    print(response['message']['content'])
    print()
if __name__ == "__main__":
    # Initialize the audio recorder
    recorder = AudioRecorder()
    output_filename = "../data/recorded_audio.wav"

    # Create the main window
    root = tk.Tk()
    root.title("Audio Recorder")

    # Create and place the buttons
    start_button = tk.Button(root, text="Start Recording", command=start_recording)
    start_button.pack(pady=10)

    stop_button = tk.Button(root, text="Stop Recording", command=stop_recording, state=tk.DISABLED)
    stop_button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()
    print()
