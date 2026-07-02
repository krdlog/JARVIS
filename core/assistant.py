from memory.memory_engine import MemoryEngine
from voice.speaker import Speaker
from voice.listener import Listener

from skills.launcher import Launcher
from skills.search import SearchSkill
from skills.time_skill import TimeSkill
from skills.screenshot import ScreenshotSkill
from skills.folder_manager import FolderManager
from skills.file_finder import FileFinder

from ai.ai_engine import AIEngine

from core.brain import Brain
from core.command_processor import CommandProcessor

import os


class Jarvis:

    def __init__(self):

        self.memory = MemoryEngine()

        self.speaker = Speaker()
        self.listener = Listener(self.speaker)

        self.brain = Brain()
        self.processor = CommandProcessor()

        self.launcher = Launcher()
        self.search = SearchSkill()
        self.time = TimeSkill()
        self.screenshot = ScreenshotSkill()
        self.folders = FolderManager()
        self.finder = FileFinder()

        self.ai = AIEngine()

        self.handlers = {
            "open_app": self.handle_open_app,
            "open_folder": self.handle_open_folder,
            "create_folder": self.handle_create_folder,
            "google_search": self.handle_google_search,
            "youtube_search": self.handle_youtube_search,
            "screenshot": self.handle_screenshot,
            "time": self.handle_time,
            "date": self.handle_date,
            "remember": self.handle_remember,
            "recall": self.handle_recall,
            "exit": self.handle_exit,
        }

    def start(self):

        print("=" * 40)
        print("JARVIS v0.4")
        print("=" * 40)

        self.speaker.speak(
            "Welcome back. All systems are operational."
        )

        while True:

            command = self.listener.listen()

            if not command:
                continue

            thought = self.brain.think(command)

            intent, data = self.processor.process(thought)

            handler = self.handlers.get(intent)

            if handler:

                if handler(data):
                    break

            else:

                reply = self.ai.ask(command)

                self.speaker.speak(reply)

    def handle_open_app(self, data):

        result = self.launcher.open_app(data)

        if result:

            self.speaker.speak(result)
            return

        folder = self.finder.find_folder(data)

        if folder:

            os.startfile(folder)

            self.speaker.speak(f"Opening {data}.")

            return

        self.speaker.speak(f"I couldn't find {data}.")

    def handle_open_folder(self, data):

        result = self.folders.open_folder(data)

        if result:

            self.speaker.speak(result)

        else:

            self.speaker.speak(f"I couldn't open {data}.")

    def handle_create_folder(self, data):

        result = self.folders.create_folder(data)

        self.speaker.speak(result)

    def handle_google_search(self, data):

        result = self.search.google(data)

        self.speaker.speak(result)

    def handle_youtube_search(self, data):

        result = self.search.youtube(data)

        self.speaker.speak(result)

    def handle_screenshot(self, data):

        result = self.screenshot.take()

        self.speaker.speak(result)

    def handle_time(self, data):

        self.speaker.speak(
            self.time.current_time()
        )

    def handle_date(self, data):

        self.speaker.speak(
            self.time.current_date()
        )

    def handle_remember(self, data):

        self.memory.remember(
            data["key"],
            data["value"]
        )

        self.speaker.speak(
            "Understood. I'll remember that."
        )

    def handle_recall(self, data):

        value = self.memory.recall(data)

        if value:

            self.speaker.speak(
                f"{data} is {value}."
            )

        else:

            self.speaker.speak(
                f"I don't know {data} yet."
            )

    def handle_exit(self, data):

        self.speaker.speak(
            "Shutting down. Until next time."
        )

        return True