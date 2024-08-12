from app import app, db
from app.models import Room, Booking
from app.forms import RoomForm, BookingForm
from flask import render_template, redirect, url_for, request


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/manage_rooms", methods=["GET", "POST"])
def manage_rooms():
    form = RoomForm()
    if form.validate_on_submit():
        room = Room(room_number=form.room_number.data, capacity=form.capacity.data)
        db.session.add(room)
        db.session.commit()
        return redirect(url_for("manage_rooms"))
    rooms = Room.query.all()
    return render_template("manage_rooms.html", form=form, rooms=rooms)


@app.route("/view_bookings", methods=["GET", "POST"])
def view_bookings():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking(
            guest_name=form.guest_name.data,
            check_in=form.check_in.data,
            check_out=form.check_out.data,
            room_id=form.room_id.data,
        )
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for("view_bookings"))
    bookings = Booking.query.all()
    return render_template("view_bookings.html", form=form, bookings=bookings)
