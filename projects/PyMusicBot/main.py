from PyMusic.player import PyMusicPlayer
from PyMusic.logger import PyMusicLogger as logger

def main():
    logger.printSpace()
    print("PyMusic Player Menu: ")
    logger.printSpace()
    print("[ 1 ]. Search music [🔍]  ")
    print("[ 2 ]. Play from Playlist [🎶]  ")
    print("[ 3 ]. Play from URL [🌐]  ")
    print("[ Q/q ] To Exit")

    user_inp = input("Enter choice: ")
    if user_inp == "1":
        logger.printSpace()
        music_name = input("[1] Search music [🔍]  ")
        PyMusicPlayer.play(search_query=music_name)
        
    elif user_inp == "2":
        logger.printSpace()
        PyMusicPlayer.getPlaylist()
    
    elif user_inp == "3":
        logger.printSpace()
        url = input("[3] Enter URL [🌐]  ")
        PyMusicPlayer.playURL(url)

    elif user_inp == "Q" or user_inp == "q":
        logger.info("Exiting the program")

    else:
        logger.error("Wrong input!!!")

if __name__ == "__main__":
    main()