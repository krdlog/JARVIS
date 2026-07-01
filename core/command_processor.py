class CommandProcessor:

    def process(self, result):

        intent = result["intent"]
        data = result["data"]

        print(f"[Intent] {intent}")

        return intent, data