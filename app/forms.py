from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, SubmitField, SelectField, RadioField

class WorldForm(FlaskForm):
    class Meta:
        csrf = False
    title = StringField('World Title', [validators.input_required(), validators.length(min=2, max=32)], render_kw={'placeholder': 'World Title'})
    descr = TextAreaField('World Description', render_kw={'placeholder': 'World Description', 'rows': '5'})
    story = TextAreaField('World Story', render_kw={'placeholder': 'World Story', 'rows': '10'})
    submit = SubmitField('Submit')

class AddBoxesForm(FlaskForm):
    submit = SubmitField('Add')