from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# CONFIGURATION
UPLOAD_FOLDER = 'uploads/archive'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ---------------------------------------------------------
# ML SEARCH ENGINE LOCATION
# ---------------------------------------------------------
# Your Machine Learning search logic would be initialized here.
# It would hook into the 'search' route to compare user inputs 
# against the files in UPLOAD_FOLDER.
# ---------------------------------------------------------

@app.route('/')
def home():
    # This serves the HTML code provided above
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"status": "Archive Updated"}), 200

from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# This creates a folder named 'static/uploads' to store the photos
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16MB

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        # We save it to 'static/uploads' so the website can actually display it later
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        return jsonify({
            "message": "Item Archived",
            "url": f"/static/uploads/{filename}"
        }), 200

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
