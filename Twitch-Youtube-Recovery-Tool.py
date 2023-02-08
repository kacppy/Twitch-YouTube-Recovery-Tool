import re, os, requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL


class MyLogger:
    def debug(self, msg):
        if "Destination:" in msg:
            print(msg)

    def info(self, msg):
        if "Destination:" in msg:
            print(msg)

    def warning(self, msg):
        pass

    def error(self, msg):
        pass


def twitch_recovery(streamer, year, m_url):
    URLS = []

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}

    i=1
    url=m_url
    print("( + ) Fetching clips links (it may take a while, please be patient)")

    while True:
        try:
            r = requests.get(url, headers=header)
        except:
            print("( ! ) Connection error.")
            break

        soup = BeautifulSoup(r.content, 'html.parser')
        divs = soup.find_all('div', class_='conslug')

        url=m_url+"/"+str(i)
        i+=1

        for conslug_div in divs:
            for img in conslug_div.find_all("img", class_='conthumb'):
                data_original = img.get("data-original")
                new_url = re.sub("-preview.*$", ".mp4", data_original)
                URLS.append(new_url)

        if not divs:
            break

    ydl_opts = {
        'ignoreerrors': True,
        'outtmpl': '/'+streamer+'/'+str(year)+'/%(title)s.%(ext)s',
        "quiet": True,
        'logger': MyLogger(),
    }

    print("( + ) Found "+str(len(URLS))+" clips links")
    print("( + ) We are trying to recover the clips (many of old clips are no longer on the Twitch servers)")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)

    print("( + ) That's all I could do, there is no more clips on Twitch servers")


def youtube_channel_recovery(channel):
    print("( + ) Fetching video links (it may take a while, please be patient)")

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',}
    url = "https://www.noxinfluencer.com/youtube/channel/"+channel+"?tab=content"
    try:
        r = requests.get(url, headers=header)
    except:
        print("( ! ) Connection error.")

    soup = BeautifulSoup(r.content, 'html.parser')
    URLS = []

    for div in soup.find_all('a', class_='info-container'):
        video_link = div.get("href")
        video_id = re.sub(r'/youtube/video-analytics/', '', video_link)
        URLS.append("https://web.archive.org/https://www.youtube.com/watch?v="+video_id)

    ydl_opts = {
        'ignoreerrors': True,
        'outtmpl': '/'+channel+'/%(title)s.%(ext)s',
    }

    print("( + ) Found "+str(len(URLS))+" video links")
    print("( + ) We are trying to recover the videos (if video had more views it's higher chance to recover)")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)


def youtube_video_recovery(video):
    print("( + )Searching for video")

    URLS = []

    video_id = re.search(r'[\w-]+$', video).group(0)
    URLS.append("https://www.youtube.com/watch?v="+video_id)
    URLS.append("https://web.archive.org/https://www.youtube.com/watch?v="+video_id)

    ydl_opts = {
        'ignoreerrors': True,
    }

    print("( + )We are trying to recover the video")

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)


def main():
    print("Select Platform for recover:")
    print("1. Twitch")
    print("2. YouTube")

    choice = int(input("Select option: (1, 2): "))

    if choice == 1:
        print("( -------- ) Welcome in Twitch Clips Recovery Tool ( -------- )")
        link = input("( - ) Enter the link to Twitch streamer: ")
        year = int(input("( - ) Select the year from which you want clips (you can choose from 2017 to present): "))

        try:
            streamer = re.search(r"twitch\.tv/([^/]*)", link).group(1)
            print("( + ) Selected streamer: "+str(streamer))
        except:
            print('Oops, no streamer name found in that link!')
            main()

        m_url = "https://twitchstats.net/clips/streamer/"+streamer+"/"+str(year)
        twitch_recovery(streamer, year, m_url)

    elif choice == 2:
        print("( -------- ) Welcome in YouTube Videos Recovery Tool ( -------- )")

        print("Select what You want to do:")
        print("1. Try to Recover specific video (if you know link to that video)")
        print("2. Try to Recover videos from YouTube channel")

        choice_2 = int(input("Select option: (1, 2): "))
        if choice_2 == 1:
            video_link = input("( - ) Enter a YouTube video link: ")
            youtube_video_recovery(video_link)

        if choice_2 == 2:
            channel_id = input("( - ) Enter a YouTube Channel ID (see README file to learn how to get ChannelID): ")
            youtube_channel_recovery(channel_id)


if __name__ == '__main__':
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    main()