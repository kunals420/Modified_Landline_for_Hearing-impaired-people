📞 Deaf-Friendly Landline Communication System

(Speech-to-Text Based PyQt5 Application)

📌 Project Overview

This project is a deaf-accessible landline communication system where a caller’s speech is converted into real-time text, allowing a deaf or speech-impaired user to read the conversation and reply via text.
The system follows a turn-based (half-duplex) communication model, similar to a real landline call:

Caller speaks first

Speech is converted to text

User replies using text

Conversation continues alternately

🎯 Key Objectives

Enable speech-to-text communication for deaf users
Provide a realistic landline call flow
Prevent overlapping speaking and typing
Ensure accessibility and usability

🧠 System Features

✔ Real-time speech recognition
✔ Turn-based conversation control
✔ Mute / Unmute functionality
✔ Send text replies
✔ Clean PyQt5 GUI
✔ Background noise calibration
✔ Thread-safe UI updates

🏗️ Project Structure
landline_project/
│
├── landline_ui.py      # UI design code (generated using Qt Designer)
├── main.py             # Application logic and speech processing
├── README.md           # Project documentation

🖥️ Technologies Used

Python 3
PyQt5 – GUI development
SpeechRecognition – Speech-to-text
Google Speech API – Online speech recognition
Qt Signals & Slots – Thread-safe UI updates



⚙️ Installation & Setup
1️⃣ Install Required Libraries
pip install PyQt5 SpeechRecognition pyaudio


⚠️ If pyaudio fails on Windows, install using:

pip install pipwin
pipwin install pyaudio

2️⃣ Run the Application
python main.py

🧪 How the System Works
📞 Call Flow

User clicks ANSWER CALL
Caller speaks → speech converted to text
System switches to reply mode
User types message and clicks SEND
Caller can speak again
Call continues until END CALL

🔄 Turn-Based Communication Logic
State	Action
Caller Turn	Microphone ON, typing disabled
User Turn	Typing enabled, microphone OFF
Muted	Speech ignored
Call Ended	All input disabled

This prevents confusion and overlapping communication.

🧩 UI Design

Large buttons for accessibility

Clear call status labels

Text display area for conversation

Number pad for realism

Simple and distraction-free layout

🛠️ Known Limitations

Requires active internet connection (Google Speech API)

Recognition accuracy depends on microphone quality

Single-language speech recognition

🚀 Future Enhancements

🔊 Text-to-Speech for replying

🌐 Language translation

📴 Offline speech recognition (Vosk)

📞 Incoming call simulation

🎛 Voice speed & clarity controls

👨‍💻 Author

Kunal Kumar Singh

📜 License

This project is for educational and research purposes only.
