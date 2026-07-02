class ToolRouter:

    def __init__(self, registry):

        self.registry = registry

    def execute(self, tool, arg):

        return self.registry.execute(
            tool,
            arg
        )

    def execute_plan(self, plan):

        results = []

        blocks = plan.strip().split("TOOL:")

        for block in blocks:

            block = block.strip()

            if not block:
                continue

            lines = block.splitlines()

            tool = lines[0].strip()

            arg = ""

            for line in lines[1:]:

                if line.startswith("ARG:"):

                    arg = line.replace(
                        "ARG:",
                        ""
                    ).strip()

            results.append(
                self.execute(tool, arg)
            )

        return results