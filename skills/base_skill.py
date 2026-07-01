class BaseSkill:

    def execute(self, *args):
        raise NotImplementedError(
            "Every skill must implement execute()."
        )