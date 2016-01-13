# -*- coding: utf8 -*-

from Utils import *
from Utils import GlobalProperty as GP
from OnClickHandler import OnClickHandler
import xbmc
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
C_LIST_CONTROLS = [C_LIST1, C_LIST2, C_LIST3, C_LIST4, C_LIST5, C_LIST6, C_LIST7]

ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")


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
            list_data.append([
            {'label':u'冰美人', 'icon':'home/mine1.jpg', 'label2':u'34:00[COLOR=B2F0F0F0]/89:00[/COLOR]'},
            {'label':u'魔卡行动', 'icon':'home/mine2.jpg', 'label2':u'56:00[COLOR=B2F0F0F0]/110:00[/COLOR]'},
            {'label':u'美丽的秘密', 'icon':'home/mine3.jpg', 'label2':u'播放至 50集'},
            {'label':u'狐影', 'icon':'home/mine4.jpg', 'label2':u'播放至 12集'},
            {'label':u'家国纪事', 'icon':'home/mine5.jpg', 'label2':u'播放至 5集'}])

            list_data.append([
            {'label':u'不可思异', 'icon':'home/chosen1.jpg', 'label2':u'9.1分', 'bg':'home/chosen1_bg.jpg', 'subtitle':u'王宝强小沈阳的奇葩科幻'},
            {'label':u'我的少女时代', 'icon':'home/chosen2.jpg', 'label2':u'8.5分', 'bg':'home/chosen2_bg.jpg', 'subtitle':u'无敌青春爱情大电影'},
            {'label':u'芈月传', 'icon':'home/chosen3.jpg', 'label2':u'全81集', 'bg':'home/chosen3_bg.jpg', 'subtitle':u'第一太后被芈月演活了'},
            {'label':u'煮妇神探', 'icon':'home/chosen4.jpg', 'label2':u'更新至 5集', 'bg':'home/chosen4_bg.jpg', 'subtitle':u'李小璐贾乃亮版史密斯夫妇', 'update':'true'},
            {'label':u'地雷英雄传', 'icon':'home/chosen5.jpg', 'label2':u'更新至 40集', 'bg':'home/chosen5_bg.jpg', 'subtitle':u'宁静变“穆桂英”', 'update':'true'},
            {'label':u'解救吾先生', 'icon':'home/chosen6.jpg', 'label2':u'9.6分', 'bg':'home/chosen6_bg.jpg', 'subtitle':u'直击明星绑架第一案'},
            {'label':u'剩者为王', 'icon':'home/chosen7.jpg', 'label2':u'7.8分', 'bg':'home/chosen7_bg.jpg', 'subtitle':u'剩女舒淇恋上鲜肉彭于晏'},
            {'label':u'前任2:备胎反击战', 'icon':'home/chosen8.jpg', 'label2':u'8.4分', 'bg':'home/chosen8_bg.jpg', 'subtitle':u'郑恺为约郭采洁花样百出'}])

            list_data.append([
            {'label':u'全部影片', 'icon':'home/movie_more.png', 'type':'channel'},
            {'label':u'藏羚王之雪域', 'icon':'home/movie1.jpg', 'label2':u'9.1分'},
            {'label':u'王朝的女人', 'icon':'home/movie2.jpg', 'label2':u'9.3分'},
            {'label':u'恶棍天使', 'icon':'home/movie3.jpg', 'label2':u'6.6分'},
            {'label':u'少年班', 'icon':'home/movie4.jpg', 'label2':u'7.4分'},
            {'label':u'命中注定', 'icon':'home/movie5.jpg', 'label2':u'8.3分'},
            {'label':u'恋爱中的城市', 'icon':'home/movie6.jpg', 'label2':u'9.6分'},
            {'label':u'赤道', 'icon':'home/movie7.jpg', 'label2':u'7.9分'}])

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
            {'label':u'影片2', 'icon':'home/movie7.jpg'},
            {'label':u'影片3', 'icon':'home/movie7.jpg'},
            {'label':u'影片4', 'icon':'home/movie7.jpg'},
            {'label':u'影片5', 'icon':'home/movie7.jpg'},
            {'label':u'影片6', 'icon':'home/movie7.jpg'},
            {'label':u'影片7', 'icon':'home/movie7.jpg'},
            {'label':u'影片8', 'icon':'home/movie7.jpg'}])

            for count, control in enumerate(C_LIST_CONTROLS):
                list_control = self.getControl(control)
                for item in list_data[count]:
                    liz = xbmcgui.ListItem(item.get('label'))
                    liz.setIconImage(item.get('icon'))
                    liz.setLabel2(item.get('label2'))
                    liz.setProperty('update', item.get('update'))
                    liz.setProperty('subtitle', item.get('subtitle'))
                    liz.setProperty('type', item.get('type'))
                    liz.setProperty('bg', item.get('bg', 'home/bg_home.png'))
                    list_control.addItem(liz)

            self.first_launch = False

        self.setFocusId(C_LIST1)

    def onAction(self, action):
        super(MainMenu, self).onAction(action)
        ch.serve_action(action, self.getFocusId(), self)

    def onClick(self, control_id):
        super(MainMenu, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(C_LIST_CONTROLS)
    def click_channel(self):
        if self.listitem.getProperty("type") == "channel":
            wm.open_channel()
        else:
            xbmc.executebuiltin('XBMC.StartAndroidActivity("","com.pivos.videoplayer","text/html","data://path={0}")'.format(ADDON_PATH + '/resources/skins/Default/media/test.mp4'))

    @ch.click(C_BUTTON_SEARCH)
    def click_search(self):
        wm.open_search()

    @ch.action("back", "*")
    @ch.action("previousmenu", "*")
    def exit_script(self):
        self.close()
        self.run = False
