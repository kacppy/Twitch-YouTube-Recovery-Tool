# Twitch Clips/YouTube Videos Recovery Tool

This script is not endorsed or supported by any of the services provided in any way. 
Any trademarks used belong to their owning companies and organisations.

Also I'm not associated with any of 3rd party services I used in my script.

## Why did I create this script?

Many old clips, although they are marked as deleted, still exist on the Twitch server. 

Additionally, many videos from "empty" YouTube channels can be recovered thanks to web.archive.org.

## My goals while creating this tool

- I don't wanna use any API from Twitch or Google
- I wanna develop solution as easy as possible

## What does it do?

- Script try to find Twitch streamer clips links and direct download clips from Twitch servers
- Script try to find Youtube videos links from provided channel and search if videos are available in web.archive

# Interface
![Interface](https://i.imgur.com/Q4tKf4k.png)

# Usage

## Instalation

1. Download repository
2. Install all requrements using:
```
pip install -r requirements.txt
```
3. Run script using python, depending on the system you use, for example:
```
python3 Twitch-Youtube-Recovery-Tool.py
```


## Twitch module

1. We need to provide direct link to Twitch streamer, for example:
```
https://www.twitch.tv/xqc
https://www.twitch.tv/xqc/videos
twitch.tv/xqc
```

2. Then we can select which year the script should try to find clips from, ranging from 2017 to the current year.

### Known bugs

Sometimes if the streamer was not streaming in the year you selected, an error may occur that causes all clips from the current year to be downloaded!



## YouTube module

1. If you want to recover a specific video and you know the link to that video, you can simply pass the link, e.g.:
```
https://youtu.be/keEPpwUpVX4
https://www.youtube.com/watch?v=keEPpwUpVX4
youtu.be/keEPpwUpVX4
```

2. If you don't know links to videos, you can try to recover all videos from selected channel, in that case you need to pass a YouTube channelID:
- To obtain the channel id, you must find on YouTube channel you want to recover (sometimes channel is already empty), then you can view the source code of the channel page and search (Ctrl+F) for value:
```
externalId
``` 
![ChannelID example](https://i.imgur.com/m7MtRC9.png)

- Alternatively, you can use a third-party website to get ChannelID, for example: https://commentpicker.com/youtube-channel-id.php


### Known bugs

Currently, you can only recover links to the last 24 videos from the channel. 
(Hopefully, there will be an update with a fix in the future ;3 )



# Roadmap
- Fix the YouTube module (to gather more than the last 24 videos links)
- Add more functionality (e.g.: search for unlisted videos, or recover deleted videos from YouTube playlists)

I have a lot of work recently, so an update with all fixes/functionality may not appear soon from me (or never XD)
# License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

