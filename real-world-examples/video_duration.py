import moviepy.editor # pip install moviepy, need it for movie duration
import mimetypes # to guess file type, if it's a video file or not
import os # path, file and directory
import sys # to get the argument

# Converts duration into human readable format
def get_duration(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    hours    = "0"+str(hours) if(hours<10) else str(hours)
    minutes  = "0"+str(minutes) if(minutes<10) else str(minutes)
    seconds  = "0"+str(seconds) if(seconds<10) else str(seconds)
    return hours, minutes, seconds

# Display video(s) duration for given directory
def display_video_duration(videos_list):
    for video_file in videos_list:
        video_file_path = dir_path+"/"+video_file

        # check if video_file is of video type
        try:
            if mimetypes.guess_type(video_file_path)[0].startswith('video'):
                # Create an object by passing the location of a video file
                video = moviepy.editor.VideoFileClip(video_file_path)

                # Contains the duration of the video in terms of seconds
                video_duration = int(video.duration) # video length output is in seconds
                hours, minutes, seconds = get_duration(video_duration) #convert into human readable duration format

                print(f"{video_file}: {hours}:{minutes}:{seconds}")
        except AttributeError:
            pass

if (len(sys.argv) != 2):
    exit("It needs video file list to work")

dir_path = ""
if(os.path.isdir(sys.argv[1])):
    dir_path = sys.argv[1] # first argument as video list directory

# list to store vodeo files
videos = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        videos.append(path)

display_video_duration(videos)


# If you want to check the given file is a video file
#if mimetypes.guess_type(path)[0].startswith('video'):
#   print('It is a video')
