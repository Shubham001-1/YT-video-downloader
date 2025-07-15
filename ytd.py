from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL
app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    
    data = request.json
    urldoc = data.get('urldoc')
    formatdoc = data.get('formatdoc')
    qualitydoc = data.get('qualitydoc')
    print("Received data from JS backend:", data)
    quality_map = {
        "1080p": "bestvideo[height<=1080]+bestaudio/best",
        "720p": "bestvideo[height<=720]+bestaudio/best",
        "480p": "bestvideo[height<=480]+bestaudio/best",
        "360p": "bestvideo[height<=360]+bestaudio/best",
        "best": "best"
    }

    ytdlp_format = quality_map.get(qualitydoc, "best")
    if not urldoc:
        print("Received data from JS backend:")
        return jsonify({"error": "URL is required"}), 400

    try:
        
        options = {
    'format': 'best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    
       }

        with YoutubeDL(options) as ydl:
            ydl.download([urldoc])

        return jsonify({"status": "Downloaded successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)


