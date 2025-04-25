from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')

# Simplified setup for videos - don't try to create directories in serverless
VIDEO_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static', 'videos')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sankey')
def sankey():
    return render_template('sankey.html')

@app.route('/video')
def video():
    try:
        # Safety check if directory exists
        if os.path.exists(VIDEO_FOLDER):
            video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith('.mp4')]
        else:
            video_files = []
        return render_template('video.html', video_files=video_files)
    except Exception as e:
        return str(e), 500  # Return error information for debugging

@app.route('/static/videos/<filename>')
def serve_video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)