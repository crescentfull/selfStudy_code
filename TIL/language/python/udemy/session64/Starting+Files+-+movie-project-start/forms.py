from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = StringField('Year', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    ranking = StringField('Ranking', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    img_url = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")