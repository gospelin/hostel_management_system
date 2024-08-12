from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class RoomForm(FlaskForm):
    room_number = StringField("Room Number", validators=[DataRequired()])
    capacity = IntegerField("Capacity", validators=[DataRequired()])
    submit = SubmitField("Add Room")


class BookingForm(FlaskForm):
    guest_name = StringField("Guest Name", validators=[DataRequired()])
    check_in = DateField(
        "Check-In Date", format="%Y-%m-%d", validators=[DataRequired()]
    )
    check_out = DateField(
        "Check-Out Date", format="%Y-%m-%d", validators=[DataRequired()]
    )
    room_id = IntegerField("Room ID", validators=[DataRequired()])
    submit = SubmitField("Book Room")
