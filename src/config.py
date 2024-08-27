from rumps import MenuItem

class Menu_Items:
    def __init__(self):
        self.menu=[
            MenuItem("Start", key="s"),
            MenuItem("Stop", key="q"),
            # [
                # MenuItem("Preferences..."),
                # [
                #     MenuItem("display time"),
                #     MenuItem("display color"),
                # ]
            # ],
            MenuItem("display time", key="t"),
        ]

class settings:
    def __init__(self, DEBUG = False):
        self.states = ["work", "break"] # manage state
        self.times = {"work": 25 * 60, "break": 5 * 60} # 25分働き5分休むポモドーロ
        if DEBUG:
            self.times = {"work": 10, "break": 5}