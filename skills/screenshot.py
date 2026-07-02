import os
from datetime import datetime

import pyautogui


class ScreenshotSkill:

    def take(self):

        folder = "screenshots"

        os.makedirs(folder, exist_ok=True)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

        path = os.path.join(folder, filename)

        pyautogui.screenshot(path)

        return f"Screenshot saved as {filename}"