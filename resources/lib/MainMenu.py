# -*- coding: utf8 -*-

from Utils import *
from Utils import GlobalProperty as GP
from OnClickHandler import OnClickHandler
import xbmcgui
from BaseClasses import *
from WindowManager import wm
import time
from dialogs.DialogBaseInfo import DialogBaseInfo

ch = OnClickHandler()
C_MAINMENU = 9000
C_BUTTON_SEARCH = 9001
C_LIST1 = 901001
C_LIST2 = 901002
C_LIST3 = 901003
C_LIST4 = 901004
C_LIST5 = 901005
C_LIST6 = 901006
C_LIST7 = 901007


class MainMenu(WindowXML, DialogBaseInfo):

    def __init__(self, *args, **kwargs):
        super(MainMenu, self).__init__(*args, **kwargs)
        self.first_launch = True

    @busy_dialog
    def onInit(self):
        if self.first_launch:
            menu_data = [
            {'label':u'搜索', 'icon':'home/search'},
            {'label':u'我的足迹', 'icon':'home/mine'},
            {'label':u'海幕精选', 'icon':'home/chosen'},
            {'label':u'电影', 'icon':'home/movie'},
            {'label':u'电视剧', 'icon':'home/tv'},
            {'label':u'纪录片', 'icon':'home/doco'},
            {'label':u'付费专区', 'icon':'home/pay'},
            {'label':u'优惠专区', 'icon':'home/sale'}]
            self.mainmenu = self.getControl(C_MAINMENU)
            for item in menu_data:
                liz = xbmcgui.ListItem(item['label'])
                liz.setIconImage(item['icon'])
                self.mainmenu.addItem(liz)
            self.mainmenu.selectItem(1)

            list_data = []
            list_controls = [C_LIST1, C_LIST2, C_LIST3, C_LIST4, C_LIST5, C_LIST6, C_LIST7]
            list_data.append([
            {'label':u'爱你，罗茜', 'icon':'home/movie1.jpg', 'label2':u'89:00[COLOR=B2F0F0F0]/89:00[/COLOR]'},
            {'label':u'芈月传', 'icon':'home/movie1.jpg', 'label2':u'更新至 20集', 'update':'true'},
            {'label':u'花千骨', 'icon':'home/movie1.jpg', 'label2':u'播放至 50集'},
            {'label':u'影片4', 'icon':'home/movie1.jpg'},
            {'label':u'影片5', 'icon':'home/movie1.jpg'}])

            list_data.append([
            {'label':u'007幽灵党', 'icon':'home/movie2.jpg', 'label2':u'8.5分', 'subtitle':u'开启邦德时刻 珠宝佳人美到心醉'},
            {'label':u'影片2', 'icon':'home/movie2.jpg'},
            {'label':u'影片3', 'icon':'home/movie2.jpg'},
            {'label':u'影片4', 'icon':'home/movie2.jpg'},
            {'label':u'影片5', 'icon':'home/movie2.jpg'},
            {'label':u'影片6', 'icon':'home/movie2.jpg'},
            {'label':u'影片7', 'icon':'home/movie2.jpg'},
            {'label':u'影片8', 'icon':'home/movie2.jpg'}])

            list_data.append([
            {'label':u'全部影片', 'icon':'home/movie_more.png', 'type':'channel'},
            {'label':u'影片2', 'icon':'home/movie3.jpg'},
            {'label':u'影片3', 'icon':'home/movie3.jpg'},
            {'label':u'影片4', 'icon':'home/movie3.jpg'},
            {'label':u'影片5', 'icon':'home/movie3.jpg'},
            {'label':u'影片6', 'icon':'home/movie3.jpg'},
            {'label':u'影片7', 'icon':'home/movie3.jpg'},
            {'label':u'影片8', 'icon':'home/movie3.jpg'}])

            list_data.append([
            {'label':u'全部电视剧', 'icon':'home/tv_more.png', 'type':'channel'},
            {'label':u'影片2', 'icon':'home/movie4.jpg'},
            {'label':u'影片3', 'icon':'home/movie4.jpg'},
            {'label':u'影片4', 'icon':'home/movie4.jpg'},
            {'label':u'影片5', 'icon':'home/movie4.jpg'},
            {'label':u'影片6', 'icon':'home/movie4.jpg'},
            {'label':u'影片7', 'icon':'home/movie4.jpg'},
            {'label':u'影片8', 'icon':'home/movie4.jpg'}])

            list_data.append([
            {'label':u'全部纪录片', 'icon':'home/doco_more.png', 'type':'channel'},
            {'label':u'影片2', 'icon':'home/movie5.jpg'},
            {'label':u'影片3', 'icon':'home/movie5.jpg'},
            {'label':u'影片4', 'icon':'home/movie5.jpg'},
            {'label':u'影片5', 'icon':'home/movie5.jpg'},
            {'label':u'影片6', 'icon':'home/movie5.jpg'},
            {'label':u'影片7', 'icon':'home/movie5.jpg'},
            {'label':u'影片8', 'icon':'home/movie5.jpg'}])

            list_data.append([
            {'label':u'全部付费', 'icon':'home/pay_more.png', 'type':'channel'},
            {'label':u'影片2', 'icon':'home/movie6.jpg'},
            {'label':u'影片3', 'icon':'home/movie6.jpg'},
            {'label':u'影片4', 'icon':'home/movie6.jpg'},
            {'label':u'影片5', 'icon':'home/movie6.jpg'},
            {'label':u'影片6', 'icon':'home/movie6.jpg'},
            {'label':u'影片7', 'icon':'home/movie6.jpg'},
            {'label':u'影片8', 'icon':'home/movie6.jpg'}])

            list_data.append([
            {'label':u'全部优惠', 'icon':'home/sale_more.png', 'type':'channel'},
            {'label':u'影片2', 'icon':'home/movie5.jpg'},
            {'label':u'影片3', 'icon':'home/movie5.jpg'},
            {'label':u'影片4', 'icon':'home/movie5.jpg'},
            {'label':u'影片5', 'icon':'home/movie5.jpg'},
            {'label':u'影片6', 'icon':'home/movie5.jpg'},
            {'label':u'影片7', 'icon':'home/movie5.jpg'},
            {'label':u'影片8', 'icon':'home/movie5.jpg'}])
            for count, control in enumerate(list_controls):
                list_control = self.getControl(control)
                for item in list_data[count]:
                    liz = xbmcgui.ListItem(item.get('label'))
                    liz.setIconImage(item.get('icon'))
                    liz.setLabel2(item.get('label2'))
                    liz.setProperty('update', item.get('update'))
                    liz.setProperty('subtitle', item.get('subtitle'))
                    liz.setProperty('type', item.get('type'))
                    list_control.addItem(liz)

            self.first_launch = False

        self.setFocusId(C_LIST1)

    def onAction(self, action):
        super(MainMenu, self).onAction(action)
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(MainMenu, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(C_LIST3)
    def click_channel(self):
        if self.listitem.getProperty("type") == "channel":
            wm.open_channel()

    @ch.click(C_BUTTON_SEARCH)
    def click_search(self):
        wm.open_search()

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
        self.run = False
