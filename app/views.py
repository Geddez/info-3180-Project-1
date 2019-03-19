"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
import datetime
from app import app, db
from app.models import UserProfile
from flask import render_template, request, redirect, url_for, flash
from app.forms import RegisterForm
from werkzeug.utils import secure_filename
from pprint import pprint


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        location = form.location.data
        gender = form.gender.data
        biography = form.biography.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
        
        user_profile = UserProfile(firstname, lastname, gender, email, location, biography, filename)
        
        db.session.add(user_profile)
        db.session.commit()

        flash('Profile Created Successfully!', 'success')
        return redirect(url_for('profiles'))

    flash_errors(form)
    return render_template('profile.html', form=form)


@app.route('/profile/<userId>')
def userProfile(userId):
    user_profile = db.session.query(UserProfile).get(userId)
    return render_template('user_profile.html', profile=user_profile)
    
@app.route('/profiles')
def profiles():
    user_profiles = db.session.query(UserProfile).all()
    return render_template('profiles.html', user_profiles=user_profiles)


###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the {} field - {}".format(getattr(form, field).label.text, error), 'warning')


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
