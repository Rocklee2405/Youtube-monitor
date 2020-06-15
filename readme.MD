# Monitor bbc channel youtube
```
Auto download audio from bbc channel
```

## Usage
Video on youtube have 3 format: mp4, m4a and webm.
Change format you want download in option.
Option
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

Run 
```
docker-compose up -d
```
