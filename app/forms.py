# Define forms if needed (e.g., using Flask-WTF for form handling)

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MusicForm(FlaskForm):
    """
    Form for handling user input for generating music.
    """
    # File field for uploading audio files
    audio_file = FileField('Upload Audio File',
                           validators=[FileRequired(), FileAllowed(['mp3', 'wav'], 'Audio files only!')])
    
    # Text field for additional user input (e.g., style or genre)
    style_input = StringField('Music Style or Genre', validators=[DataRequired()])
    
    # Submit button
    submit = SubmitField('Generate Music')
