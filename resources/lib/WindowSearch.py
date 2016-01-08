#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
from dialogs.DialogBaseInfo import DialogBaseInfo
from OnClickHandler import OnClickHandler
ch = OnClickHandler()

class SearchWindowUI(xbmcgui.WindowXML, DialogBaseInfo):

    ID_EDIT  = 9201
    ID_LETTER  = 9202
    ID_NUMBER  = 9203
    ID_DEAFAULT_INFO = 9220
    ID_HOT_SEARCH  = 9221
    ID_SEARCH_WORD  = 9231
    ID_RESULT_MOVIE  = 9241
    ID_RESULT_CARTOON  = 9251
    ID_RESULT_SELECT_TITLE = 9252
    ID_RESULT_NUM = 9253
    ID_MOVIE_NUM = 9242
    ID_CARTOON_NUM = 9255
    ID_RESULT_PAGE = 9233
    ID_SEARCH_BG = 9211
    ID_KEYBOARD = 9212
    
    VAL_DEL = 'del'

    def __init__(self, *args, **kwargs):
        print('nenaTest_ SearchWindowUI __init__: ')

    def onInit(self):
        print('nenaTest_ SearchWindowUI onInit: ')
        self.searchKey = ''
        self.searchWord = ''
        self.TEXT_VAL = True
        print('nenaTest_ SearchWindowUI onInit: ', self.TEXT_VAL)
        self.addData()
        self.setFocusId(self.ID_LETTER)

    # add data of keyboard and hot search list
    def addData(self):
        print('nenaTest_ SearchWindowUI addData: ')
        dataLetter = []
        dataLetter = [
        'A','B','C','D','E','F','G',
        'H','I','J','K','L','M','N',
        'O','P','Q','R','S','T',self.VAL_DEL,
        'U','V','W','X','Y','Z']
        self.letters = self.getControl(self.ID_LETTER)
        self.letters.reset()
        for val in dataLetter:
            letter = xbmcgui.ListItem(val)
            self.letters.addItem(letter)

        dataNumber = []
        dataNumber = ['1','2','3','4','5','6','7','8','9','0']
        self.numbers = self.getControl(self.ID_NUMBER)
        self.numbers.reset()
        for val in dataNumber:
            number = xbmcgui.ListItem(val)
            self.numbers.addItem(number)

        dataHotSearch = []
        dataHotSearch = [
        {'label':u'杜拉拉追婚记', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'克拉恋人', 'label2':u'7.4分', 'icon':'home/movie1.jpg'},
        {'label':u'盗墓笔记', 'label2':u'7.9分', 'icon':'home/movie1.jpg'}]
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

    @ch.action("back", "*")
    def exit_script(self):
        self.close()

    def onClick(self, control_id):
        super(Channel, self).onClick(control_id)
        ch.serve(control_id, self)

    @ch.click(ID_LETTER)
    def click_keyboard_letter(self):
        self.dealKeyboard(self.ID_LETTER)

    @ch.click(ID_NUMBER)
    def click_keyboard_number(self):
        self.dealKeyboard(self.ID_NUMBER)

    @ch.click(ID_SEARCH_WORD)
    def click_channel(self):
        self.getSearchWord()
        self.getSearchResultList()
        self.setFocusId(self.ID_RESULT_MOVIE)

    @ch.click(ID_SEARCH_BG)
    def click_channel(self):
        self.setFocusId(self.ID_KEYBOARD)

    def dealKeyboard(self, controlId):
        control = self.getControl(controlId)
        item = control.getSelectedItem()
        label = item.getLabel()
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
        control = self.getControl(self.ID_SEARCH_WORD)
        item = control.getSelectedItem()
        label = item.getLabel()
        self.searchWord = label
        print('nenaTest_ onClick self.searchWord', self.searchWord)

    # get search word list for key
    def getSearchWordList(self):
        print('nenaTest_ SearchWindowUI getSearchWordList: ', self.searchKey)
        dataSearchWord = [
        'A计划','多啦A梦',
        '阿尔卑斯少女','阿杜',
        '阿鹦爱说笑','神奇阿哟',
        '匈奴王·阿提拉','阿甘正传',
        '阿呆与阿瓜',
        'A计划','多啦A梦',
        '阿尔卑斯少女','阿杜',
        '阿鹦爱说笑','神奇阿哟',
        '匈奴王·阿提拉','阿甘正传',
        '阿呆与阿瓜']
        self.searchWord = dataSearchWord[0]
        self.searchWordArr = self.getControl(self.ID_SEARCH_WORD)
        self.searchWordArr.reset()
        for val in dataSearchWord:
            word = xbmcgui.ListItem(val)
            self.searchWordArr.addItem(word)

    # get search result list for word
    def getSearchResultList(self):
        print('nenaTest_ SearchWindowUI getSearchResultList: ', self.searchWord)
        
        title = self.getControl(self.ID_RESULT_SELECT_TITLE)
        title.setLabel(self.searchWord)
        resultNum = 0

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
        {'label':u'A', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'B', 'label2':u'7.4分', 'icon':'home/movie1.jpg'},
        {'label':u'C', 'label2':u'7.9分', 'icon':'home/movie1.jpg'},
        {'label':u'D', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'E', 'label2':u'7.4分', 'icon':'home/movie1.jpg'},
        {'label':u'F', 'label2':u'7.9分', 'icon':'home/movie1.jpg'},
        {'label':u'G', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'H', 'label2':u'7.4分', 'icon':'home/movie1.jpg'}]
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
        resultNum += movieSize

        dataResultCartoon = []
        dataResultCartoon = [
        {'label':u'1', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'2', 'label2':u'7.4分', 'icon':'home/movie1.jpg'},
        {'label':u'3', 'label2':u'7.9分', 'icon':'home/movie1.jpg'},
        {'label':u'4', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'5', 'label2':u'7.4分', 'icon':'home/movie1.jpg'},
        {'label':u'6', 'label2':u'7.9分', 'icon':'home/movie1.jpg'},
        {'label':u'7', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'8', 'label2':u'7.4分', 'icon':'home/movie1.jpg'},
        {'label':u'9', 'label2':u'7.9分', 'icon':'home/movie1.jpg'},
        {'label':u'10', 'label2':u'8.6分', 'icon':'home/movie1.jpg'},
        {'label':u'11', 'label2':u'7.4分', 'icon':'home/movie1.jpg'},
        {'label':u'12', 'label2':u'7.9分', 'icon':'home/movie1.jpg'},
        {'label':u'13', 'label2':u'7.9分', 'icon':'home/movie1.jpg'}]
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
        resultNum += cartoonSize

        lResultNum = self.getControl(self.ID_RESULT_NUM)
        lResultNum.setLabel('搜索结果:' + str(resultNum))
        