from RealtimeSTT import AudioToTextRecorder
import time


class Listener:

    def __init__(self, speaker):

        self.speaker = speaker

        print("[Whisper] Loading... (first launch may take a minute)")

        self.recorder = AudioToTextRecorder(
            model="base",
            language="en",
            spinner=False,
            silero_sensitivity=0.4,
            webrtc_sensitivity=2,
            post_speech_silence_duration=0.5,
            min_length_of_recording=0.3,
            min_gap_between_recordings=0.2
        )

        print("[Whisper] Ready")

    def listen(self):

        while self.speaker.is_speaking:
            time.sleep(0.1)

        print("🎤 Listening...")

        try:

            text = self.recorder.text()

            if text is None:
                return ""

            text = (
                text.lower()
                .replace(".", "")
                .replace(",", "")
                .replace("?", "")
                .replace("!", "")
                .strip()
            )

            if not text:
                return ""

            print(f"You: {text}")

            return text

        except KeyboardInterrupt:
            raise

        except Exception as e:

            print(f"Speech Error: {e}")

            return ""