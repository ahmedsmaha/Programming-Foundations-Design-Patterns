from camera_plus_app import CameraPlusApp
from txt import Txt
from social import Social
from mail import Mail

if __name__ == "__main__":

    cameraPlusApp = CameraPlusApp()

    cameraPlusApp.setShareStrategy(Mail())
    cameraPlusApp.take()
    cameraPlusApp.edit()
    cameraPlusApp.save()
    cameraPlusApp.share()
