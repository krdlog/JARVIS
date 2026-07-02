from datetime import datetime


class TimeSkill:

    def current_time(self):

        now = datetime.now()

        return now.strftime("The time is %I:%M %p")

    def current_date(self):

        today = datetime.now()

        return today.strftime("Today is %A, %d %B %Y")