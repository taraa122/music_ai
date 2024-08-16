from flask import Blueprint, render_template, request, jsonify
from model.model_utils import predict_with_model

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/result', methods=['POST'])
def result():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and file.filename.endswith('.mp3'):
        file_path = 'temp.mp3'
        file.save(file_path)
        predictions = predict_with_model(file_path)
        return render_template('result.html', predictions=predictions.tolist())
    else:
        return jsonify({'error': 'Invalid file format'})
