class SkillRegistry:

    def __init__(self):

        self.skills = {}

    def register(self, name, function):

        self.skills[name] = function

    def execute(self, name, argument=None):

        if name not in self.skills:
            return None

        return self.skills[name](argument)

    def list_skills(self):

        return list(self.skills.keys())