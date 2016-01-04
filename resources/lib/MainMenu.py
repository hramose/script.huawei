# -*- coding: utf8 -*-

from Utils import *
from Utils import GlobalProperty as GP
from OnClickHandler import OnClickHandler
import VideoPlayer
from BaseClasses import *
from WindowManager import wm
import time
from dialogs.DialogBaseInfo import DialogBaseInfo

PLAYER = VideoPlayer.VideoPlayer()
ch = OnClickHandler()
C_LIST_MAINMENU = 1000
C_LIST_SHOW = 2000
C_LABEL_TIME = 2100


class MainMenu(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)

    @busy_dialog
    def onInit(self):
        pass

    def onAction(self, action):
        super(MainMenu, self).onAction(action)
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(MainMenu, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
        self.run = False
