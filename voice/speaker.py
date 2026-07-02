from threading import Lock
import asyncio
import edge_tts
import pygame
import tempfile
import os
import time


class Speaker:

    def __init__(self):

        pygame.mixer.init()

        self.voice = "en-US-AndrewMultilingualNeural"

        self.lock = Lock()

        self.is_speaking = False

    async def _tts(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate="+5%",
            pitch="+0Hz"
        )

        await communicate.save(filename)

    def speak(self, text):

        print(f"JARVIS: {text}")

        with self.lock:

            self.is_speaking = True

            temp = None

            try:

                temp = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp3"
                )

                temp.close()

                asyncio.run(
                    self._tts(text, temp.name)
                )

                pygame.mixer.music.load(temp.name)
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)

                pygame.mixer.music.unload()

            except Exception as e:

                print(f"TTS Error: {e}")

            finally:

                time.sleep(0.8)

                self.is_speaking = False

                if temp and os.path.exists(temp.name):
                    os.remove(temp.name)