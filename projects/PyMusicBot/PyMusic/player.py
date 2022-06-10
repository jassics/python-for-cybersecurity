import re, requests,urllib
from PyMusic.logger import PyMusicLogger as logger
from PyMusic.config import PyMusicConfig
import youtube_dl
import os
import time

class PyMusicPlayer:
    def __init__(self):
        pass
    
    @staticmethod
    def getMusicURL(search_query):
        query_string = urllib.parse.urlencode({"search_query": search_query})
        formatUrl = urllib.request.urlopen(PyMusicConfig.YT_DL.SEARCH_RESULTS_URL + query_string)
        search_results = re.findall(PyMusicConfig.YT_DL.SEARCH_REG_EX, formatUrl.read().decode())
        url = PyMusicConfig.YT_DL.WATCH_URL + "{}".format(search_results[0])
        # logger.info(f"Song URl: {url}")
        return url


    @staticmethod
    def getRequest(url):
        clip = requests.get(url)
        return clip,url


    @staticmethod
    def getMusicInfo(clip_url):
        video_info = youtube_dl.YoutubeDL().extract_info(url = clip_url,download=False)
        # logger.info(f"Song Info: {video_info['title']}")
        return video_info['title']
    
    @staticmethod
    def playFromPlaylist(filename):
        playlist = [] 
        playlist_path = PyMusicConfig.buildPATH(filename,PyMusicConfig.Playlist.PATH)
        with open(playlist_path, "r") as f:
            playlist = f.readlines()
        f.close()

        for music in playlist:
            if "http" in music:
                PyMusicPlayer.playURL(music.split("\n")[0]) #splitting new lines at the end
            else:
                PyMusicPlayer.play(music)
            

    @staticmethod
    def getPlaylist():
        print("[ 2 ] Available Playlists")
        logger.printSpace()

        playlist_path =  os.listdir(PyMusicConfig.Playlist.PATH)
        if len(playlist_path) != 0:
            for idx,playlist in enumerate(playlist_path):
                name = playlist.split(".")[0]
                logger.info(f"[ {idx+1} ]  {name}")

        user_inp = int(input("Enter choice: "))
        if user_inp <=0 or user_inp > len(playlist_path):
            logger.error("Wrong input!!!")
        else:
            logger.playlist("Selected Playlist: {}".format(playlist_path[user_inp-1].split(".")[0]))
            PyMusicPlayer.playFromPlaylist(filename=playlist_path[user_inp-1])
            time.sleep(5)
            

    @staticmethod
    def execMPV(clip_url):
        os.system(".\mpv\mpv.exe {} --no-video".format(clip_url))

    @staticmethod
    def play(search_query):
        url = PyMusicPlayer.getMusicURL(search_query)
        _,clip_url = PyMusicPlayer.getRequest(url)
        musicInfo = PyMusicPlayer.getMusicInfo(clip_url)
        logger.playing("Now Playing: {}".format(musicInfo))
        PyMusicPlayer.execMPV(clip_url)

    def playURL(url):
        _,clip_url = PyMusicPlayer.getRequest(url)
        musicInfo = PyMusicPlayer.getMusicInfo(clip_url)
        logger.playing("Now Playing: {}".format(musicInfo))
        PyMusicPlayer.execMPV(clip_url)
