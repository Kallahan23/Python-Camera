'''
Python Camera
==============

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import time

class CameraScreen(BoxLayout):

    def __init__(self, **kwargs):
        """Constructor - bind keyboard event to self.onKey."""
        super(CameraScreen, self).__init__(**kwargs)

        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        self._keyboard.bind(on_key_down=self._on_keyboard_down)


    def _keyboard_closed(self):
        print('My keyboard has been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        if keycode[1] == 'h':
            Window.hide()

        if keycode[1] == 'enter':
            self.capture()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("Pictures/IMG_{}.png".format(timestr))
        print("Captured")
        return True


class PythonCameraApp(App):

    def build(self):
        return CameraScreen()

if __name__ == "__main__":
    PythonCameraApp().run()
