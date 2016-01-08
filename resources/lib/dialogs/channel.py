# -*- coding: utf8 -*-

from Utils import *
from Utils import GlobalProperty as GP
from OnClickHandler import OnClickHandler
from BaseClasses import *
from WindowManager import wm
from dialogs.DialogBaseInfo import DialogBaseInfo

ch = OnClickHandler()
C_BUTTON_SEARCH = 300
C_LIST_SHOW = 1000
C_LABEL_TIME = 2000


class Channel(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(Channel, self).__init__(*args, **kwargs)

    @busy_dialog
    def onInit(self):
        pass

    def onAction(self, action):
        super(Channel, self).onAction(action)
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(Channel, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(C_BUTTON_SEARCH)
    def click_channel(self):
        wm.open_search()

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
        self.run = False
