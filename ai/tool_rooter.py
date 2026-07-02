class ToolRouter:

    def __init__(self, registry):

        self.registry = registry

    def execute(self, tool, argument=None):

        return self.registry.execute(
            tool,
            argument
        )