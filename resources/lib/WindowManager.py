# -*- coding: utf8 -*-

from Utils import *
import xbmcaddon
# from dialogs.DialogBaseInfo import DialogBaseInfo

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_ICON = ADDON.getAddonInfo('icon')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")
MAINMENU_XML = "script-Main.xml"
VIDEOCHANNEL_XML = "script-VideoChannel.xml"
VIDEOSEARCH_XML = "script-Search.xml"

YESNO_XML = "script-DialogYesNo.xml"
CONFIRM_XML = "script-ConfirmDialog.xml"


class WindowManager(object):

    def __init__(self):
        self.window_stack = []

    def add_to_stack(self, window):
        """
        add window / dialog to global window stack
        """
        self.window_stack.append(window)

    def pop_stack(self):
        """
        get newest item from global window stack
        """
        if self.window_stack:
            dialog = self.window_stack.pop()
            xbmc.sleep(300)
            dialog.doModal()

    def open_selectdialog(self, listitems):
        """
        open selectdialog, return listitem dict and index
        """
        from dialogs.SelectDialog import SelectDialog
        w = SelectDialog('DialogSelect.xml', ADDON_PATH,
                         listing=listitems)
        w.doModal()
        return w.listitem, w.index

    def open_main_menu(self, prev_window=None):
        """
        open main menu, deal with window stack
        """
        import MainMenu
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = MainMenu.MainMenu(MAINMENU_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_search(self, prev_window=None):
        """
        open main menu, deal with window stack
        """
        from WindowSearch import searchWindowUI
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = searchWindowUI(VIDEOSEARCH_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_channel(self, prev_window=None):
        """
        open main menu, deal with window stack
        """
        from dialogs.channel import Channel
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = Channel(VIDEOCHANNEL_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_yesno_dialog(self, prev_window=None):
        """
        open yesno dialog, deal with window stack
        """
        from dialogs.DialogYesNo import DialogYesNo
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = DialogYesNo(YESNO_XML, ADDON_PATH)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_confirm_dialog(self, title, label1, label2, prev_window=None):
        """
        open confirm dialog, deal with window stack
        """
        from dialogs.DialogConfirm import DialogConfirm
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        dialog = DialogConfirm(CONFIRM_XML, ADDON_PATH, title=title, label1=label1, label2=label2)
        xbmc.executebuiltin("Dialog.Close(busydialog)")
        self.open_dialog(dialog, prev_window)

    def open_dialog(self, dialog, prev_window):
        # dialog.doModal()
        if dialog:
            if prev_window:
                self.add_to_stack(prev_window)
                prev_window.close()
            dialog.doModal()
            self.pop_stack()
        else:
            notify(LANG(32143))

wm = WindowManager()
