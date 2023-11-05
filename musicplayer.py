import tkinter as tk
from tkinter import filedialog
import winsound
import os
import random

# Define the root directory where your music files are stored
root_directory = "C:/Users/tabis/Documents/GitHub/folder/archive"

# Create a list to store the paths of all music files
music_files = []

# Recursively search for music files in the root directory and its subdirectories
for root, dirs, files in os.walk(root_directory):
    for file in files:
        if file.lower().endswith(".wav"):
            music_files.append(os.path.join(root, file))

# Check if there are any music files
if not music_files:
    print("No music files found.")
else:
    # Select a random music file from the list
    random_music_file = random.choice(music_files)
    print(random_music_file)
    

def choosethemusic():
    global selected
    selected = filedialog.askopenfilename(initialdir="D:/", title='Choose Your WAV', filetypes=(("wav files", "*.wav"), ("all files", "*.*")))
    print('Music Mounted', selected)

def playthemusic():
    global selected, playing
    if selected:
        if not playing:
            winsound.PlaySound(None, winsound.SND_PURGE)  # Stop any currently playing sound
            sound = selected
            print("Playing", sound)
            winsound.PlaySound(selected, winsound.SND_ASYNC)
            playbutton.config(text="Pause")
            playing = True
        else:
            winsound.PlaySound(None, winsound.SND_PURGE)  # Pause by stopping the sound
            playbutton.config(text="Play")
            playing = False
    else:
        print('No music selected')

def randommusicselector():
    global selected
    if music_files:
        selected = random.choice(music_files)
        if selected:
            print("Music selected")
        playthemusic()
    else:
        print("No music files found")

def stopmusic():
    global selected, playing
    if selected and playing:
        winsound.PlaySound(None, winsound.SND_PURGE)
        playbutton.config(text="Play")
        playing = False
    else:
        print("No music playing")

playing = False  # Initialize as not playing
selected = random_music_file  # Set the default music file path

root = tk.Tk()
root.title("Simple Music Player")

playbutton = tk.Button(root, text="Play", command=playthemusic)
playbutton.pack()

choosebutton = tk.Button(root, text="Choose music", command=choosethemusic)
choosebutton.pack()

random_selector_button = tk.Button(root, text="Random Music Selector", command=randommusicselector)
random_selector_button.pack()

stop_button = tk.Button(root, text="Stop", command=stopmusic)
stop_button.pack()

root.mainloop()