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

    print('Choosing the best Quality: '.title())
    listresolution = yt.streams.filter(only_audio=True,progressive=False)
    
    if(listresolution.get_audio_only()):
        listresolution.get_audio_only().download()

def extractSubtitle(data_url):
    yt = YouTube(data_url)
    
    print('Choose the Languege of Subtitle: '.title())
    captions = yt.captions
    
    
    # if  ('en' in captions.items()):
    #      print('1) English')    
    # elif ('a.en' in captions.items()):
    #     print('1) Autogenerate English')
    # else:
    #     print('-English subtitle is not defined.') 
            
    # if('es' in captions.items()):
    #     print('2) Spanish | Español')
    # if('a.es' in captions.items()):
    #     print('3) Español Autogenerado')
    
    print('4) Exit.')

    # third_menu = int(input('=> '))
    # try:
    #     if third_menu == 1:
    #         capt = captions.get_by_language_code('en').generate_srt_captions()
    #         print(capt)
    #     if third_menu == 2:
    #         capt = captions.get_by_language_code('es').generate_srt_captions()
    #         print(capt)
    #     if third_menu == 3:
    #         capt = captions.get_by_language_code('a.es').generate_srt_captions()
    #         print(capt)
    #     if third_menu == 4:
    #         sys.exit()
    #     if third_menu not in (1,2,3,4):
    #         print('That is out of range. :/')
    # except HTTPError as e:
    #     print('There was problem to access the video, it is Forbidden.')

#? -------------------------------- MAIN PROGRAM ------------------------------------------------------
  
try:

    url_yt = input('Type the url video: ')

    print('Welcome to PYtube: \n 1) To download video. \n 2) To download audio. \n 3) Extract Subtitle. \n 4) Just exit.'.title())
    first_menu = int(input('=> ')) 

    if first_menu == 1:
        toDownload_video(url_yt)
        
    if first_menu == 2:
        toDownload_audio(url_yt)
    
    if first_menu == 3:
        extractSubtitle(url_yt)
        
    if first_menu == 4:
        sys.exit()
        
    if first_menu not in (1,2,3,4):
        print('Sorry your choise is out of menu... :(')
        
except ValueError as e:
    print('May you are typing a letter instead of a number in the menu range.')
    print('Something went wrong... Please communicate with the software provider -> Edwin Roman')
    print(e)
except NameError as e:
    print('Something went wrong... Please comunicate with the software provider -> Edwin Roman')
    print(e)