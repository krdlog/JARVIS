import os
import subprocess
from pathlib import Path


class FolderManager:

    def __init__(self):

        self.locations = {
            "desktop": Path.home() / "Desktop",
            "documents": Path.home() / "Documents",
            "downloads": Path.home() / "Downloads",
            "pictures": Path.home() / "Pictures",
            "music": Path.home() / "Music",
            "videos": Path.home() / "Videos",
        }

    def open_folder(self, name):

        name = name.lower().strip()

        if name not in self.locations:
            return None

        path = self.locations[name]

        subprocess.Popen(f'explorer "{path}"')

        return f"Opening {name}."

    def create_folder(self, name):

        path = Path.home() / "Desktop" / name

        os.makedirs(path, exist_ok=True)

        return f"Folder {name} created on your Desktop."