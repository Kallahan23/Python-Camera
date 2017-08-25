'''
Python Camera
==============

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import time

class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("Pictures/IMG_{}.png".format(timestr))
        print("Captured")


class PythonCameraApp(App):

    def build(self):
        return CameraClick()

if __name__ == "__main__":
    PythonCameraApp().run()
