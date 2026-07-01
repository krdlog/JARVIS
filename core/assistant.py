from memory.memory_engine import MemoryEngine
from voice.speaker import Speaker
from voice.listener import Listener

from skills.launcher import Launcher

from core.brain import Brain
from core.command_processor import CommandProcessor


class Jarvis:

    def __init__(self):

        self.memory = MemoryEngine()
        self.speaker = Speaker()
        self.listener = Listener()

        self.brain = Brain()
        self.processor = CommandProcessor()

        self.launcher = Launcher()

    def start(self):

        print("=" * 40)
        print("JARVIS v0.2")
        print("=" * 40)

        self.speaker.speak("Hello Joseph. JARVIS is online.")

        while True:

            command = self.listener.listen()

            if not command:
                continue

            thought = self.brain.think(command)
            intent, data = self.processor.process(thought)

            if intent == "open_app":

                result = self.launcher.open_app(data)

                if result:
                    self.speaker.speak(result)
                else:
                    self.speaker.speak(f"I couldn't open {data}")

            elif intent == "remember":

                key = data["key"]
                value = data["value"]

                self.memory.remember(key, value)

                self.speaker.speak(f"I'll remember that. {key} is {value}.")

            elif intent == "recall":

                value = self.memory.recall(data)

                if value:
                    self.speaker.speak(f"{data} is {value}.")
                else:
                    self.speaker.speak(f"I don't know what {data} is yet.")

            elif intent == "exit":

                self.speaker.speak("Goodbye Joseph.")
                break

            else:

                self.speaker.speak("I don't know how to do that yet.")