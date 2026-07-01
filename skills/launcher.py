from AppOpener import open as open_app
import subprocess


class Launcher:

    def __init__(self):

        self.aliases = {
            "file explorer": "explorer",
            "explorer": "explorer",
            "calculator": "calculator",
            "calc": "calculator",
            "paint": "paint",
            "notepad": "notepad",
        }

    def open_app(self, app_name):

        app_name = app_name.lower().strip()

        if app_name in self.aliases:
            app_name = self.aliases[app_name]

        try:

            if app_name == "notepad":
                subprocess.Popen("notepad.exe")
                return "Opening Notepad."

            if app_name == "calculator":
                subprocess.Popen("calc.exe")
                return "Opening Calculator."

            if app_name == "paint":
                subprocess.Popen("mspaint.exe")
                return "Opening Paint."

            if app_name == "explorer":
                subprocess.Popen("explorer.exe")
                return "Opening File Explorer."

            open_app(app_name, match_closest=True, throw_error=True)

            return f"Opening {app_name}."

        except Exception:
            return None