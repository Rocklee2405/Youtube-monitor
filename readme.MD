# Monitor bbc channel youtube

```
Auto download audio from bbc channel
```

## Usage

Video on youtube have 3 format: mp4, m4a and webm.
Change format you want download in option.
Option:

```
options = {
            'continue' : 'continue',
            'ignoreerrors': True,
            'nooverwrites' : 'nooverwrites',
            'outtmpl' : '/temp' + '/%(id)s.%(ext)s',
            'format' : 'bestaudio[ext=webm]',
            'merge_ouput_format': 'webm',
        }
```

Change channel url you want to monitor:

```
version: '3'
services:
  bbc:
    image: bbc-monitor
    build: .
    volumes:
      - ./bbc.py:/bbc.py
      - ./main.py:/main.py
    environment:
      TZ: Asia/Saigon
      LINK: https://www.youtube.com/user/BBCVietnamese/videos 
```

Run 

```
docker-compose up -d
```
