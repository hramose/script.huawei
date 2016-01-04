# -*- coding: utf8 -*-

from Utils import *
from DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
from BaseClasses import DialogXML
from aniu import AniuAPI
from WindowManager import wm

ch = OnClickHandler()

C_LABEL_TITLE = 5000
C_BUTTON_CONFIRM = 5001
C_BUTTON_CANCEL = 5002


class DialogConfirm(DialogXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(DialogConfirm, self).__init__(*args, **kwargs)
        self.TITLE = kwargs['title']
        self.LABLE_OK = kwargs['label1']
        self.LABLE_CANCLE = kwargs['label2']

    def onInit(self):
        super(DialogConfirm, self).onInit()
        self.getControl(C_LABEL_TITLE).setText(self.TITLE)
        self.getControl(C_BUTTON_CONFIRM).setLabel(self.LABLE_OK)
        self.getControl(C_BUTTON_CANCEL).setLabel(self.LABLE_CANCLE)

    def onAction(self, action):
        super(DialogConfirm, self).onAction(action)
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(DialogConfirm, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(C_BUTTON_CONFIRM)
    def login_click(self):
        self.close()
        wm.open_account_login()

    @ch.click(C_BUTTON_CANCEL)
    def cancel_click(self):
        self.close()
