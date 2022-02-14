from flask import Flask,current_app,request
app = Flask(__name__)
import youtube_dl

@app.route('/')
def hello_world():
    return current_app.send_static_file('index.htm')
@app.route('/g')
def g():
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})
    video = ""
    yt_url = request.args.get('u')
    with ydl:
        result = ydl.extract_info \
        (yt_url,
        download=False) #We just want to extract the info

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries']

            #loops entries to grab each video_url
            for i, item in enumerate(video):
                video = result['entries'][i]
                print(video)
    return video

if __name__ == '__main__':
    app.run()