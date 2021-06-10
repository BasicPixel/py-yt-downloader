# Python Youtube video downloader
# YT tutorial: https://youtu.be/FVq6TYw9WjE
# pytube documentation: https://pytube.io/en/latest/

from pytube import YouTube, Playlist

print('   Python Video Downloader   '.center(60, '-'))
video = ""
link_type = "Video"

try:
    # gets link from user, then creates youtube object from it
    link = input("Enter the link to the youtube video / playlist: ")
    if link.startswith("https://www.youtube.com/playlist"):
        link_type = "Playlist"
        video = Playlist(link)
    else:
        video = YouTube(link)
except KeyboardInterrupt:
    # quit on ctrl-c
    quit()
except:
    print("Video URL could not be found.")
    quit()

# display data about the video
print(f"{link_type} title is:\n{video.title}")
# print(f"{link_type} rating is {video.rating}")
if link_type == "Playlist":
    print(f"{link_type} has {video.length} videos")
else:
    print(f"{link_type} is {round(video.length / 60, 2)} minutes long")
    print(f"{link_type} has {int(float(video.views))} views")
print("-----------------------------------------")

# cancel and quit program on ctrl-c, continue to download otherwise
try:
    input("if the info above is correct, press enter to proceed with the download, or Ctrl-C to cancel.")
except:
    quit()

if link_type == "Playlist":
    print(f'Downloading videos from playlist "{video.title}"...')
else:
    print(f'Downloading Video "{video.title}"...')

try:
    # downloads highest resoulution stream that has audio and video
    
    if link_type == "Playlist":
        # iterate over videos in playlists
        for video in video.videos:
            video.streams.get_highest_resolution().download(r"D:\User\Downloads")
    else:
        video.streams.get_highest_resolution().download(r"D:\User\Downloads")
except:
    print(f"could not download video")

video.register_on_complete_callback(input(f'{link_type} download successful. Press enter to exit.'))