from memory.memory_engine import MemoryEngine
from voice.speaker import Speaker
from voice.listener import Listener

from skills.launcher import Launcher
from skills.search import SearchSkill
from skills.time_skill import TimeSkill
from skills.screenshot import ScreenshotSkill
from skills.folder_manager import FolderManager
from skills.file_finder import FileFinder
from skills.registry import SkillRegistry

from ai.ai_engine import AIEngine
from ai.conversation import Conversation
from ai.planner import Planner
from ai.tool_router import ToolRouter

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

        self.ai = AIEngine()

        self.conversation = Conversation()
        self.planner = Planner()

        self.launcher = Launcher()
        self.search = SearchSkill()
        self.time = TimeSkill()
        self.screenshot = ScreenshotSkill()
        self.folders = FolderManager()
        self.finder = FileFinder()

        self.registry = SkillRegistry()

        self.router = ToolRouter(self.registry)

        self.register_skills()

    def register_skills(self):

        self.registry.register(
            "open_app",
            self.handle_open_app
        )

        self.registry.register(
            "open_folder",
            self.handle_open_folder
        )

        self.registry.register(
            "create_folder",
            self.handle_create_folder
        )

        self.registry.register(
            "google_search",
            self.handle_google_search
        )

        self.registry.register(
            "youtube_search",
            self.handle_youtube_search
        )

        self.registry.register(
            "screenshot",
            self.handle_screenshot
        )

        self.registry.register(
            "time",
            self.handle_time
        )

        self.registry.register(
            "date",
            self.handle_date
        )

        self.registry.register(
            "remember",
            self.handle_remember
        )

        self.registry.register(
            "recall",
            self.handle_recall
        )

        self.registry.register(
            "exit",
            self.handle_exit
        )

    def start(self):

        print("=" * 40)
        print("JARVIS v0.5")
        print("=" * 40)

        self.speaker.speak(
            "Welcome back. All systems are online."
        )

        while True:

            command = self.listener.listen()

            if not command:
                continue

            self.conversation.add(
                "user",
                command
            )

            thought = self.planner.plan(command)

            intent, data = self.processor.process(
                self.brain.think(thought)
            )

            result = self.router.execute(
                intent,
                data
            )

            if result is True:
                break

            if result is None:

                reply = self.ai.ask(command)

                self.conversation.add(
                    "assistant",
                    reply
                )

                self.speaker.speak(reply)

    def handle_open_app(self, data):

        result = self.launcher.open_app(data)

        if result:

            self.speaker.speak(result)
            return

        folder = self.finder.find_folder(data)

        if folder:

            os.startfile(folder)

            self.speaker.speak(
                f"Opening {data}."
            )

            return

        self.speaker.speak(
            f"I couldn't find {data}."
        )

    def handle_open_folder(self, data):

        result = self.folders.open_folder(data)

        if result:

            self.speaker.speak(result)

        else:

            self.speaker.speak(
                f"I couldn't open {data}."
            )

    def handle_create_folder(self, data):

        self.speaker.speak(
            self.folders.create_folder(data)
        )

    def handle_google_search(self, data):

        self.speaker.speak(
            self.search.google(data)
        )

    def handle_youtube_search(self, data):

        self.speaker.speak(
            self.search.youtube(data)
        )

    def handle_screenshot(self, data):

        self.speaker.speak(
            self.screenshot.take()
        )

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
            "Powering down. See you soon."
        )

        return True