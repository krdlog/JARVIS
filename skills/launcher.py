import subprocess


class Launcher:

    def open_app(self, command):

        if "notepad" in command:
            subprocess.Popen("notepad.exe")
            return "Opening Notepad."

        elif "calculator" in command:
            subprocess.Popen("calc.exe")
            return "Opening Calculator."

        elif "paint" in command:
            subprocess.Popen("mspaint.exe")
            return "Opening Paint."

        elif "explorer" in command:
            subprocess.Popen("explorer.exe")
            return "Opening File Explorer."

        return None