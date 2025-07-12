from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from models.models import db, Advisor

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        advisor = Advisor.query.filter_by(username=username).first()
        if advisor and check_password_hash(advisor.password, password):
            session['advisor_id'] = advisor.id
            session['batch_id'] = advisor.batch_id
            flash('Login successful!', 'success')
            return redirect(url_for('attendance.dashboard'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
