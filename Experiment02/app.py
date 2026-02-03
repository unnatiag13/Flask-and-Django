from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'darkmode'
app.config['WTF_CSRF_ENABLED'] = False   # CSRF REMOVED 🔥


class StudentForm(FlaskForm):
    name = StringField('Student Name', validators=[DataRequired(), Length(min=3, max=30)])

    contact = StringField('Contact Number', validators=[
        DataRequired(),
        Regexp(r'^[6-9]\d{9}$', message='Enter valid 10 digit mobile number')
    ])

    email = StringField('Email ID', validators=[DataRequired(), Email()])

    roll = StringField('University Roll No.', validators=[DataRequired(), Length(min=5, max=15)])

    father = StringField("Father's Name", validators=[DataRequired(), Length(min=3, max=30)])

    address = TextAreaField('Address', validators=[DataRequired(), Length(min=10, max=200)])

    semester = SelectField('Semester', choices=[
        ('1','1'),('2','2'),('3','3'),('4','4'),
        ('5','5'),('6','6'),('7','7'),('8','8')
    ])

    course = StringField('Course', validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route('/', methods=['GET','POST'])
def home():
    form = StudentForm()
    if form.validate_on_submit():
        return render_template('success.html', data=form.data)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
