from pathlib import Path
import os


class FileFinder:

    def __init__(self):

        self.search_roots = [
            Path.home(),
            Path.home() / "Desktop",
            Path.home() / "Documents",
            Path.home() / "Downloads",
            Path.home() / "Pictures",
            Path.home() / "OneDrive",
        ]

    def find_folder(self, folder_name):

        folder_name = folder_name.lower()

        for root in self.search_roots:

            if not root.exists():
                continue

            try:

                for current, dirs, files in os.walk(root):

                    for d in dirs:

                        if d.lower() == folder_name:

                            return Path(current) / d

            except PermissionError:
                pass

        return None