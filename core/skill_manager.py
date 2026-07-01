class SkillManager:

    def __init__(self):

        self.skills = {}

    def register(self, name, skill):

        self.skills[name] = skill

        print(f"[Skill] Registered: {name}")

    def execute(self, name, *args):

        if name not in self.skills:
            return None

        return self.skills[name](*args)