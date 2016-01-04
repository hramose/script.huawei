# -*- coding: utf8 -*-

from Utils import *
from DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
from BaseClasses import DialogXML
from aniu import AniuAPI

ch = OnClickHandler()

C_BUTTON_CONFIRM = 5001
C_BUTTON_CANCEL = 5002


class DialogYesNo(DialogXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(DialogYesNo, self).__init__(*args, **kwargs)

    def onInit(self):
        super(DialogYesNo, self).onInit()

    def onAction(self, action):
        super(DialogYesNo, self).onAction(action)
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(DialogYesNo, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(C_BUTTON_CONFIRM)
    def vip_click(self):
        self.close()

    @ch.click(C_BUTTON_CANCEL)
    def logout_click(self):
        self.close()



