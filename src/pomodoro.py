import rumps
from config import Menu_Items, settings

DEBUG = False
BASE_PATH = "../images"
rumps.debug_mode(DEBUG)

class PomodoroTimer(rumps.App):
    def __init__(self, BASE_PATH=BASE_PATH):
        super(PomodoroTimer, self).__init__("Pomodoro Timer")
        self.settings = settings(DEBUG=DEBUG)
        self.menu = Menu_Items().menu

        self.BASE_PATH = BASE_PATH
        self.timer = rumps.Timer(self.update_timer, 1)
        self.states = self.settings.states
        self.times = self.settings.times
        self.state = self.states[0] # current state
        self.remaining_time = self.times[self.state]
        self.is_running = False
        self.display_time = True
        self.display_color = False

    @rumps.clicked("Start")
    def start_timer(self, _):
        self.is_running = True
        self.timer.start()
        self.icon = f"{self.BASE_PATH}/work_icon.png"

    @rumps.clicked("Stop")
    def stop_timer(self, _):
        print("stopped")
        self.is_running = False
        self.timer.stop()
        self.icon = f"{self.BASE_PATH}/stop.png"

    def update_timer(self, _):
        if self.remaining_time > 0 and self.is_running:
            self.remaining_time -= 1
            minutes, seconds = divmod(self.remaining_time, 60)
            if self.display_time:
                self.title = f"{minutes:02d}:{seconds:02d}"
            else:
                self.title = None
        else:
            self.timer.stop()
            if self.state == "work":
                self.state = "break"
                self.icon = f"{BASE_PATH}/break_icon.png"
                # title, subtitle, message, data=None, sound=True
                rumps.notification(title="Break time!!", subtitle="take a break", message="work time done, so you take a break")
            elif self.state == "break":
                self.state = "work"
                self.icon = f"{BASE_PATH}/work_icon.png"
                rumps.notification(title="Work time!!", subtitle="take a work", message="break time done, so you take a work")
            self.remaining_time = self.times[self.state]
            # next timer start
            self.timer.start()
            
    @rumps.clicked("display time")
    def preference_display_time(self, sender):
        sender.state = not sender.state # 0 or 1
        self.display_time = bool(sender.state)
        print("self.display_time:", self.display_time)
