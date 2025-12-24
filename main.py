import sys
import speech_recognition as sr
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
from landline_ui import Ui_Form


class LandlineApp(QWidget, Ui_Form):

    # Signal to safely update UI from background thread
    speech_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Button connections
        self.pushButton_2.clicked.connect(self.answer_call)   # ANSWER
        self.pushButton_3.clicked.connect(self.end_call)      # END
        self.pushButton_4.clicked.connect(self.toggle_mute)   # MUTE
        self.pushButton.clicked.connect(self.send_message)    # SEND

        # Speech Recognition setup
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Improve accuracy
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True

        # Flags
        self.speech_active = False
        self.muted = False
        self.listener = None

        # Connect signal to text box
        self.speech_signal.connect(self.plainTextEdit.appendPlainText)

        # Calibrate microphone ONCE
        self.label.setText("Calibrating Microphone...")
        QApplication.processEvents()

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)

        self.label.setText("READY")

    # ---------------- CALL CONTROLS ----------------

    def answer_call(self):
        if not self.speech_active:
            self.label.setText("CALL ANSWERED")
            self.speech_active = True
            self.muted = False

            self.listener = self.recognizer.listen_in_background(
                self.microphone,
                self.process_speech,
                phrase_time_limit=5
            )

    def end_call(self):
        self.label.setText("CALL ENDED")
        self.speech_active = False
        self.muted = False

        if self.listener:
            self.listener(wait_for_stop=False)
            self.listener = None

    def toggle_mute(self):
        if self.speech_active:
            self.muted = not self.muted
            self.label.setText("MUTED" if self.muted else "CALL ANSWERED")

    # ---------------- TEXT MESSAGE ----------------

    def send_message(self):
        message = self.lineEdit.text().strip()
        if message:
            self.plainTextEdit.appendPlainText(f"You: {message}")
            self.lineEdit.clear()

    # ---------------- SPEECH HANDLING ----------------

    def process_speech(self, recognizer, audio):
        if not self.speech_active or self.muted:
            return

        try:
            text = recognizer.recognize_google(audio)
            self.speech_signal.emit(f"Caller: {text}")

        except sr.UnknownValueError:
            pass  # Ignore unclear speech

        except sr.RequestError:
            self.speech_signal.emit("⚠️ Internet error")


# ---------------- MAIN ----------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LandlineApp()
    window.show()
    sys.exit(app.exec_())
