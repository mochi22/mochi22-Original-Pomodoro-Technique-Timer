# # https://rumps.readthedocs.io/en/latest/examples.html
# import rumps


# class AwesomeStatusBarApp(rumps.App):
#     def __init__(self):
#         super(AwesomeStatusBarApp, self).__init__("Awesome App")
#         self.menu = ["Preferences", "Silly button", "Say hi"]

#     @rumps.clicked("Preferences")
#     def prefs(self, _):
#         rumps.alert("jk! no preferences available!")

#     @rumps.clicked("Silly button")
#     def onoff(self, sender):
#         sender.state = not sender.state

#     @rumps.clicked("Say hi")
#     def sayhi(self, _):
#         rumps.notification("Awesome title", "amazing subtitle", "hi!!1")

# if __name__ == "__main__":
#     AwesomeStatusBarApp().run()

import rumps

rumps.debug_mode(True)

@rumps.clicked('Print Something')
def print_something(_):
    rumps.alert(message='something', ok='YES!', cancel='NO!')


@rumps.clicked('On/Off Test')
def on_off_test(_):
    print_button = app.menu['Print Something']
    if print_button.callback is None:
        print_button.set_callback(print_something)
    else:
        print_button.set_callback(None)


@rumps.clicked('Clean Quit')
def clean_up_before_quit(_):
    print('execute clean up code')
    rumps.quit_application()


app = rumps.App('Hallo Thar', menu=['Print Something', 'On/Off Test', 'Clean Quit'], quit_button=None)
app.run()