#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
from dialogs.DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
ch = OnClickHandler()


class SearchWindowUI(xbmcgui.WindowXML, DialogBaseInfo):

    ID_EDIT = 9201
    ID_LETTER = 9202
    ID_NUMBER = 9203
    ID_DEAFAULT_INFO = 9220
    ID_HOT_SEARCH = 9221
    ID_SEARCH_WORD = 9231
    ID_RESULT_MOVIE = 9241
    ID_RESULT_CARTOON = 9251
    ID_RESULT_SELECT_TITLE = 9252
    ID_RESULT_NUM = 9253
    ID_MOVIE_NUM = 9242
    ID_CARTOON_NUM = 9255
    ID_RESULT_PAGE = 9233
    ID_SEARCH_BG = 9211
    ID_KEYBOARD = 9212
    ID_DOWN_ICON = 9254
    ID_LETTER_FOCUS = 9204
    ID_NUMBER_FOCUS = 9205

    VAL_DEL = 'del'

    def __init__(self, *args, **kwargs):
        print('nenaTest_ SearchWindowUI __init__: ')

    def onInit(self):
        print('nenaTest_ SearchWindowUI onInit: ')
        self.window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
        self.searchKey = ''
        self.searchWord = ''
        self.TEXT_VAL = True
        self.lastFocusId = -1
        self.addData()
        self.setFocusId(self.ID_LETTER)

    # add data of keyboard and hot search list
    def addData(self):
        print('nenaTest_ SearchWindowUI addData: ')
        dataLetter = []
        dataLetter = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', self.VAL_DEL,
            '', 'V', 'W', 'X', 'Y', 'Z']
        self.letters = self.getControl(self.ID_LETTER)
        self.letters.reset()
        for val in dataLetter:
            letter = xbmcgui.ListItem(val)
            self.letters.addItem(letter)

        dataNumber = []
        dataNumber = [
            '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0']
        self.numbers = self.getControl(self.ID_NUMBER)
        self.numbers.reset()
        for val in dataNumber:
            number = xbmcgui.ListItem(val)
            self.numbers.addItem(number)

        dataHotSearch = []
        dataHotSearch = [
            {'label': '杜拉拉追婚记', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '克拉恋人', 'label2': '7.4分', 'icon': 'home/movie1.jpg'},
            {'label': '盗墓笔记', 'label2': '7.9分', 'icon': 'home/movie1.jpg'}]
        self.hotSearch = self.getControl(self.ID_HOT_SEARCH)
        self.hotSearch.reset()
        for val in dataHotSearch:
            info = xbmcgui.ListItem(val['label'])
            info.setLabel2(val['label2'])
            info.setIconImage(val['icon'])
            self.hotSearch.addItem(info)

    def onAction(self, action):
        super(SearchWindowUI, self).onAction(action)
        ch.serve_action(action, self.getFocusId(), self)
        if self.control:
            nowId = self.control.getId()
            if -1 == self.lastFocusId:
                self.lastFocusId = nowId
            if nowId != self.lastFocusId:
                self.dealSearchWordListLabelColor(self.lastFocusId, nowId)
                self.lastFocusId = nowId

    def dealSearchWordListLabelColor(self, lastId, nowId):
        if nowId == self.ID_SEARCH_WORD and (lastId == self.ID_RESULT_MOVIE or lastId == self.ID_RESULT_CARTOON):
            self.dealSearchWordList(nowId)
            self.setFocusId(nowId)
        elif lastId == self.ID_SEARCH_WORD and (nowId == self.ID_RESULT_MOVIE or nowId == self.ID_RESULT_CARTOON):
            self.dealSearchWordList(nowId)
            self.setFocusId(nowId)

    def dealSearchWordList(self, nowId):
        dataSearchWord = []
        val = nowId in [self.ID_SEARCH_WORD, self.ID_SEARCH_BG, self.ID_LETTER, self.ID_NUMBER]
        if val:
            dataSearchWord = [
                '[COLOR FF26B7BC]A[/COLOR]计划',
                '多啦[COLOR FF26B7BC]A[/COLOR]梦',
                '[COLOR FF26B7BC]阿[/COLOR]尔卑斯少女',
                '[COLOR FF26B7BC]阿[/COLOR]杜',
                '[COLOR FF26B7BC]阿[/COLOR]鹦爱说笑',
                '神奇[COLOR FF26B7BC]阿[/COLOR]哟',
                '匈奴王·[COLOR FF26B7BC]阿[/COLOR]提拉',
                '[COLOR FF26B7BC]阿[/COLOR]甘正传',
                '[COLOR FF26B7BC]阿[/COLOR]呆与阿瓜',
                '[COLOR FF26B7BC]A[/COLOR]计划',
                '多啦[COLOR FF26B7BC]A[/COLOR]梦',
                '[COLOR FF26B7BC]阿[/COLOR]尔卑斯少女',
                '[COLOR FF26B7BC]阿[/COLOR]杜',
                '[COLOR FF26B7BC]阿[/COLOR]鹦爱说笑',
                '神奇[COLOR FF26B7BC]阿[/COLOR]哟',
                '匈奴王·[COLOR FF26B7BC]阿[/COLOR]提拉',
                '[COLOR FF26B7BC]阿[/COLOR]甘正传',
                '[COLOR FF26B7BC]阿[/COLOR]呆与阿瓜']
        else:
            dataSearchWord = [
                'A计划',
                '多啦A梦',
                '阿尔卑斯少女',
                '阿杜',
                '阿鹦爱说笑',
                '神奇阿哟',
                '匈奴王·阿提拉',
                '阿甘正传',
                '阿呆与阿瓜',
                'A计划',
                '多啦A梦',
                '阿尔卑斯少女',
                '阿杜',
                '阿鹦爱说笑',
                '神奇阿哟',
                '匈奴王·阿提拉',
                '阿甘正传',
                '阿呆与阿瓜']
        size = self.searchWordArr.size()
        for pos in range(size):
            item = self.searchWordArr.getListItem(pos)
            item.setLabel(dataSearchWord[pos])
        if not val:
            selectItem = self.searchWordArr.getListItem(self.searchWordArr.getSelectedPosition())
            selectItem.setLabel('[COLOR FF26B7BC]'+selectItem.getLabel()+'[/COLOR]')

    @ch.action("back", "*")
    def exit_script(self):
        self.close()

    @ch.action("up", "*")
    @ch.action("down", "*")
    def deal_down_pic_script(self):
        if self.control:
            mid = self.control.getId()
            if mid == self.ID_RESULT_CARTOON:
                if self.resultNum <= 6:
                    down = self.getControl(self.ID_DOWN_ICON)
                    down.setVisible(False)
                else:
                    pos = self.control.getSelectedPosition()
                    if pos != -1:
                        size = self.control.size()
                        if size > 0:
                            lastlineFirst = size - size % 3
                            down = self.getControl(self.ID_DOWN_ICON)
                            if pos >= lastlineFirst-1:
                                down.setVisible(False)
                            else:
                                down.setVisible(True)
            self.deal_keyboard_focus_down()

    @ch.action("left", "*")
    @ch.action("right", "*")
    def deal_keyboard_focus_down(self):
        id = self.control.getId()
        if id == self.ID_LETTER:
            letter = self.getControl(self.ID_LETTER_FOCUS)
            pos = self.control.getSelectedPosition()
            x = pos % 7 * 96 + 4
            y = pos / 7 * 110 + 172
            # print 'control_focus_pos ' + str(x) + '_' + str(y)
            letter.setPosition(x, y)
        elif id == self.ID_NUMBER:
            number = self.getControl(self.ID_NUMBER_FOCUS)
            pos = self.control.getSelectedPosition()
            x = pos * 65 + 18
            y = 653
            number.setPosition(x, y)

            self.window.setProperty("needMove", 'yes')
            # self.window.clearProperty("needMove")
            self.window.setProperty("moveX", str(x))
            self.window.setProperty("moveY", str(y))

    def onClick(self, control_id):
        super(SearchWindowUI, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(ID_LETTER)
    def click_keyboard_letter(self):
        xbmc.executebuiltin('CancelAlarm(clockLetter,silent)')
        self.window.setProperty('NeedAnimLetter', 'yes')
        xbmc.executebuiltin('AlarmClock(clockLetter,ClearProperty(NeedAnimLetter),00:01,silent)')
        self.dealKeyboard()

    @ch.click(ID_NUMBER)
    def click_keyboard_number(self):
        xbmc.executebuiltin('CancelAlarm(clockNumber,silent)')
        self.window.setProperty('NeedAnimNumber', 'yes')
        xbmc.executebuiltin('AlarmClock(clockNumber,ClearProperty(NeedAnimNumber),00:01,silent)')
        self.dealKeyboard()

    @ch.click(ID_SEARCH_WORD)
    def click_search_word(self):
        self.getSearchWord()
        self.getSearchResultList()

    @ch.click(ID_SEARCH_BG)
    def click_search_edit(self):
        self.setFocusId(self.ID_KEYBOARD)

    def dealKeyboard(self):
        label = self.listitem.getLabel()
        print('nenaTest_ onClick label', label)
        if label == self.VAL_DEL:
            print('nenaTest_ do del')
            editbox = self.getControl(self.ID_EDIT)
            self.searchKey = editbox.getLabel()
            self.searchKey = self.searchKey[0:-1]
            editbox.setLabel(self.searchKey)
        else:
            print('nenaTest_ do appendText')
            self.appendText(label)
        self.getSearchWordList()
        self.getSearchResultList()

    # append search key to show editbox content
    def appendText(self, char):
        print('nenaTest_ SearchWindowUI appendText')
        editbox = self.getControl(self.ID_EDIT)
        self.searchKey = editbox.getLabel() + char
        editbox.setLabel(self.searchKey)

    # get search word list now focus item label
    def getSearchWord(self):
        label = self.listitem.getLabel()
        self.searchWord = label
        print('nenaTest_ onClick self.searchWord', self.searchWord)

    # get search word list for key
    def getSearchWordList(self):
        print('nenaTest_ SearchWindowUI getSearchWordList: ', self.searchKey)
        dataSearchWord = [
            '[COLOR FF26B7BC]A[/COLOR]计划',
            '多啦[COLOR FF26B7BC]A[/COLOR]梦',
            '[COLOR FF26B7BC]阿[/COLOR]尔卑斯少女',
            '[COLOR FF26B7BC]阿[/COLOR]杜',
            '[COLOR FF26B7BC]阿[/COLOR]鹦爱说笑',
            '神奇[COLOR FF26B7BC]阿[/COLOR]哟',
            '匈奴王·[COLOR FF26B7BC]阿[/COLOR]提拉',
            '[COLOR FF26B7BC]阿[/COLOR]甘正传',
            '[COLOR FF26B7BC]阿[/COLOR]呆与阿瓜',
            '[COLOR FF26B7BC]A[/COLOR]计划',
            '多啦[COLOR FF26B7BC]A[/COLOR]梦',
            '[COLOR FF26B7BC]阿[/COLOR]尔卑斯少女',
            '[COLOR FF26B7BC]阿[/COLOR]杜',
            '[COLOR FF26B7BC]阿[/COLOR]鹦爱说笑',
            '神奇[COLOR FF26B7BC]阿[/COLOR]哟',
            '匈奴王·[COLOR FF26B7BC]阿[/COLOR]提拉',
            '[COLOR FF26B7BC]阿[/COLOR]甘正传',
            '[COLOR FF26B7BC]阿[/COLOR]呆与阿瓜']
        self.searchWord = dataSearchWord[0]
        self.searchWordArr = self.getControl(self.ID_SEARCH_WORD)
        self.searchWordArr.reset()
        for val in dataSearchWord:
            word = xbmcgui.ListItem(val)
            self.searchWordArr.addItem(word)
        lastWord = self.searchWordArr.getListItem(self.searchWordArr.size()-1)
        lastWord.setProperty('needntLine', 'right')

    # get search result list for word
    def getSearchResultList(self):
        print('nenaTest_ SearchWindowUI getSearchResultList: ', self.searchWord)
        title = self.getControl(self.ID_RESULT_SELECT_TITLE)
        title.setLabel(self.searchWord)
        self.resultNum = 0

        idMovie = 0
        idCartoon = 0
        idMovieLabel = 0
        idCartoonLabel = 0
        if self.TEXT_VAL:
            self.TEXT_VAL = False
            idMovie = self.ID_RESULT_MOVIE
            idCartoon = self.ID_RESULT_CARTOON
            idMovieLabel = self.ID_MOVIE_NUM
            idCartoonLabel = self.ID_CARTOON_NUM
        else:
            self.TEXT_VAL = True
            idMovie = self.ID_RESULT_CARTOON
            idCartoon = self.ID_RESULT_MOVIE
            idMovieLabel = self.ID_CARTOON_NUM
            idCartoonLabel = self.ID_MOVIE_NUM

        dataResultMovie = []
        dataResultMovie = [
            {'label': 'A', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': 'B', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': 'C', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': 'D', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': 'E', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': 'F', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': 'G', 'label2': '8.6分', 'icon': 'home/movie1.jpg'}]
        self.resultMovieArr = self.getControl(idMovie)
        self.resultMovieArr.reset()
        for val in dataResultMovie:
            info = xbmcgui.ListItem(val['label'])
            info.setLabel2(val['label2'])
            info.setIconImage(val['icon'])
            self.resultMovieArr.addItem(info)
        movieSize = self.resultMovieArr.size()
        movieTitle = self.getControl(idMovieLabel)
        if idMovieLabel == self.ID_MOVIE_NUM:
            movieTitle.setLabel("电影 " + str(movieSize))
        else:
            movieTitle.setLabel("动漫 " + str(movieSize))
        movieTitle.setVisible(movieSize != 0)
        self.resultNum += movieSize

        dataResultCartoon = []
        dataResultCartoon = [
            {'label': '1', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '2', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '3', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '4', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '5', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '6', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '7', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '8', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '9', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '10', 'label2': '8.6分', 'icon': 'home/movie1.jpg'},
            {'label': '11', 'label2': '8.6分', 'icon': 'home/movie1.jpg'}]
        self.resultCartoonArr = self.getControl(idCartoon)
        self.resultCartoonArr.reset()
        for val in dataResultCartoon:
            result = xbmcgui.ListItem(val['label'])
            result.setLabel2(val['label2'])
            result.setIconImage(val['icon'])
            self.resultCartoonArr.addItem(result)
        cartoonSize = self.resultCartoonArr.size()
        cartoonTitle = self.getControl(idCartoonLabel)
        if idCartoonLabel == self.ID_MOVIE_NUM:
            cartoonTitle.setLabel("电影 " + str(cartoonSize))
        else:
            cartoonTitle.setLabel("动漫 " + str(cartoonSize))
        cartoonTitle.setVisible(cartoonSize != 0)
        self.resultNum += cartoonSize

        lResultNum = self.getControl(self.ID_RESULT_NUM)
        lResultNum.setLabel('搜索结果:' + str(self.resultNum))

        down = self.getControl(self.ID_DOWN_ICON)
        if self.resultNum > 6:
            down.setVisible(True)
        else:
            down.setVisible(False)
