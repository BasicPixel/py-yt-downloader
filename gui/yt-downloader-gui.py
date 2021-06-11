# Python Youtube video downloader
# YT tutorial: https://youtu.be/FVq6TYw9WjE
# pytube documentation: https://pytube.io/en/latest/

from pytube import YouTube, Playlist
import PySimpleGUI as sg
from os import getcwd

# Destination folder
dl_folder = getcwd()
folder_msg = 'Files are downloaded to: ' + dl_folder

# PySimpleGUI Initialization
sg.theme("DarkBlue") # sets theme

layout = [ # sets elements of the layout
    [sg.Text("Enter the link to the youtube video / playlist: ")],
    [sg.InputText(key='input', size=(100,1))],
    [sg.Button('Ok'), sg.Button('Cancel')],
    [sg.Text(key='data', size=(100, 5))],
    [sg.HorizontalSeparator()],
    [sg.Button('Download', disabled=True), sg.Text(folder_msg, key='folder')],
    [sg.Text('', key='downloading', size=(100,1))]
]

# Windows Definition
window = sg.Window('Python YouTube Downloader', layout, font=('Segoe UI', 11), element_padding=(5, 5))

# Main event loop
while True:
    # listen for events
    event, values = window.read()

    # breaks loop if windows is closed or if cancel button is clicked
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    # Section 1: get link, create object, get and display data
    # When OK button is clicked:
    elif event == 'Ok':
        try:
            data_correct = '\nIf the info above is correct, click download button below to start downloading'
            
            # get link value from input box
            link = values['input']
            
            # if the link is to a playlist:
            if link.startswith("https://www.youtube.com/playlist"):
                link_type = 'playlist'
                
                # create playlist object
                target = Playlist(link)
                
                # display data about playlist
                data = f'Plalist title: {target.title}\nPlaylist has {target.length} videos'
                window['data'].update(data + data_correct)
            else:
                link_type = 'video'
                target = YouTube(link)
                
                data = f'Video title: {target.title}\nVideo is {round(target.length / 60, 2)} minutes long\nVideo has {target.views} views'
                window['data'].update(data + data_correct)

            window['Download'].update(disabled=False)
            
        except:
            window['data'].update("Video / playlist link could not be found")

    # Section 2: download video / playlist
    elif event == 'Download':
        try:
            if link_type == 'playlist':
                # display 'downloading...' next to download button
                window['downloading'].update(f'Downloading videos from playlist "{target.title}"...')
                
                # iterate through videos in playlist
                for video in target.videos:
                    # find highest resolution stream + download it
                    video.streams.get_highest_resolution().download(dl_folder)
            else:
                window['downloading'].update(f'Downloading video "{target.title}"...')
                target.streams.get_highest_resolution().download(dl_folder)

            # Display 'download successful' upon completion
            target.register_on_complete_callback(window['downloading'].update(f'Download successful.'))
        except:
            window['downloading'].update(f'Could not download video / playlist.')
    
# closes window when loop is broken
window.close()