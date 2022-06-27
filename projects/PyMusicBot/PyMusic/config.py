class PyMusicConfig:
    @staticmethod
    def buildPATH(file,path):
        return path+file

    class MPV:
        EXEC_PATH = ".\mpv\mpv.exe"
        ARGS = "--no-video"

    class Playlist:
        PATH = "./playlists/"
    
    class YT_DL:
        SEARCH_REG_EX = r"watch\?v=(\S{11})"
        SEARCH_RESULTS_URL = "https://www.youtube.com/results?"
        WATCH_URL = "https://www.youtube.com/watch?v="
        PROPERTY= "og:title"