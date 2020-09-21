from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    title = StringField('Pitch Title')
    category = SelectField('Categories', choices=[('Product', 'Product'), ('Adverts', 'Adverts'),('Interview Pitch', 'Interview Pitch')], validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Post Comments')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')