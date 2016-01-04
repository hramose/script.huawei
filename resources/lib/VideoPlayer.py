# -*- coding: utf8 -*-

import xbmc
import urllib2
import re
from WindowManager import wm
from Utils import *


class VideoPlayer(xbmc.Player):

    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__(self)
        self.stopped = False

    def onPlayBackEnded(self):
        self.stopped = True

    def onPlayBackStopped(self):
        self.stopped = True

    def onPlayBackStarted(self):
        self.stopped = False

    def play(self, url, listitem, window=False):
        if window and window.window_type == "dialog":
            wm.add_to_stack(window)
            window.close()
        super(VideoPlayer, self).play(item=url,
                                      listitem=listitem,
                                      windowed=False,
                                      startpos=-1)
        if window and window.window_type == "dialog":
            self.wait_for_video_end()
            wm.pop_stack()

    def wait_for_video_end(self):
        xbmc.sleep(500)
        while not self.stopped:
            xbmc.sleep(200)
        self.stopped = False
