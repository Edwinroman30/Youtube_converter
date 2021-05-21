from pytube import YouTube
import sys

def toDownload_video(data_url):
    yt = YouTube(data_url)
    print('\nPlease wait while download... {}'.format(yt.title))

    print('Chosee a resolution:'.title())
    listresolution = yt.streams.filter(file_extension='mp4',progressive=True).order_by('resolution').desc()

    if(listresolution.get_by_resolution('360p')):
        print('1) 360p')
    if(listresolution.get_by_resolution('720p')):
        print('2) 720p')
    
    sencond_menu = int(input('=> '))
    try:
        if sencond_menu == 1:
            listresolution.get_by_resolution('360p').download()
        if sencond_menu == 2:
            listresolution.get_by_resolution('720p').download()
        if sencond_menu not in (1,2):
            print('That resolution is out of range. :/')
    except HTTPError as e:
        print('There was problem to access the video, it is Forbidden.')
   
def toDownload_audio(data_url):
    yt = YouTube(data_url)
    print('\nPlease wait while download... {}'.format(yt.title))

    print('Chossing the Quality: '.title())
    listresolution = yt.streams.filter(only_audio=True,progressive=False)
    
    if(listresolution.get_audio_only()):
        listresolution.get_audio_only().download()
  
try:

    url_yt = input('Type the url video: ')

    print('Welcome to PYtube: \n 1) To download video \n 2) To download audio \n 3) Just exit.'.title())
    first_menu = int(input('=> ')) 

    if first_menu == 1:
        toDownload_video(url_yt)
        
    if first_menu == 2:
        toDownload_audio(url_yt)
        
    if first_menu == 3:
        sys.exit()
        
    if first_menu not in (1,2,3):
        print('Sorry your choise is out of menu... :(')
        
except ValueError as e:
    print('May you are typing a letter instead a number in the menu range.')
    print('Something went wrong... Please communicate with the software provider -> Edwin Roman')
    print(e)
except NameError as e:
    print('Something went wrong... Please comunicate with the software provider -> Edwin Roman')
    print(e)