class Brain:

    def __init__(self):
        print("[Brain] Online")

    def think(self, command: str):

        command = command.lower().strip()

        if command.startswith("open "):

            target = command.replace("open ", "", 1)

            folders = [
                "desktop",
                "documents",
                "downloads",
                "pictures",
                "music",
                "videos",
            ]

            if target in folders:
                return {
                    "intent": "open_folder",
                    "data": target
                }

            return {
                "intent": "open_app",
                "data": target
            }

        if command.startswith("create folder "):
            return {
                "intent": "create_folder",
                "data": command.replace("create folder ", "", 1)
            }

        if command.startswith("search google for "):
            return {
                "intent": "google_search",
                "data": command.replace("search google for ", "", 1)
            }

        if command.startswith("search youtube for "):
            return {
                "intent": "youtube_search",
                "data": command.replace("search youtube for ", "", 1)
            }

        if "screenshot" in command:
            return {
                "intent": "screenshot",
                "data": None
            }

        if "what time" in command or command == "time":
            return {
                "intent": "time",
                "data": None
            }

        if (
            "what date" in command
            or "today's date" in command
            or command == "date"
        ):
            return {
                "intent": "date",
                "data": None
            }

        if command.startswith("remember "):

            parts = command.split(maxsplit=2)

            if len(parts) == 3:
                return {
                    "intent": "remember",
                    "data": {
                        "key": parts[1],
                        "value": parts[2]
                    }
                }

        if command.startswith("what is "):
            return {
                "intent": "recall",
                "data": command.replace("what is ", "", 1)
            }

        if command == "exit":
            return {
                "intent": "exit",
                "data": None
            }

        return {
            "intent": "unknown",
            "data": command
        }