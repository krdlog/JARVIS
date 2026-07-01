class Brain:
    def __init__(self):
        print("[Brain] Online")

    def think(self, command: str):
        command = command.lower().strip()

        if command.startswith("open "):
            app = command.replace("open ", "", 1)
            return {
                "intent": "open_app",
                "data": app
            }

        if "exit" in command:
            return {
                "intent": "exit",
                "data": None
            }

        return {
            "intent": "unknown",
            "data": command
        }