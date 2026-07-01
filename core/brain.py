class Brain:
    def __init__(self):
        print("[Brain] Online")

    def think(self, command: str):
        command = command.lower().strip()

        if command.startswith("open "):
            return {
                "intent": "open_app",
                "data": command.replace("open ", "", 1)
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
            key = command.replace("what is ", "", 1)

            return {
                "intent": "recall",
                "data": key
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