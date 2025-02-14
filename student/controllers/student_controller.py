from flask import render_template, request, redirect, url_for, session, flash
from models import db, bcrypt, Students as Student


def register():
    if request.method == 'POST':
        name = request.form['name']
        student_id = request.form['student_id']
        email = request.form['email']
        password = request.form['password']
        course = request.form['course']
        college = request.form['college']

        phone_number = request.form['phone_number']

        
        existing_student = Student.query.filter_by(student_id=student_id).first() or Student.query.filter_by(email=email).first()

        if existing_student:

            flash('Student ID or Email already registered.', 'danger')
            return redirect(url_for('register'))

     
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        
        new_student = Student(

            name=name, student_id=student_id, email=email,
            password=hashed_password, course=course,
            college=college, phone_number=phone_number
        )

        db.session.add(new_student)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


def login():
    if request.method == 'POST':

        student_id = request.form['student_id']

        password = request.form['password']

        existing_student = Student.query.filter_by(student_id=student_id).first()

        if existing_student and bcrypt.check_password_hash(existing_student.password, password):

            session['student_id'] = existing_student.id

            flash('Login successful!', 'success')
            return redirect(url_for('profile'))


        flash('Invalid credentials, try again.', 'danger')

    return render_template('login.html')


def show_profile():
    if 'student_id' not in session:
        return redirect(url_for('login'))

    student = Student.query.get(session['student_id'])
    return render_template('profile.html', student=student)


def edit():
    if 'student_id' not in session:
        return redirect(url_for('login'))

    student = Student.query.get(session['student_id'])

    if request.method == 'POST':

        student.name = request.form['name']
        student.email = request.form['email']
        student.course = request.form['course']
        student.college = request.form['college']
        student.phone_number = request.form['phone_number']

        if request.form['password']:
            
            student.password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('edit.html', student=student)


def delete():
    if 'student_id' not in session:
        return redirect(url_for('login'))

    student = Student.query.get(session['student_id'])
    db.session.delete(student)
    db.session.commit()

    session.pop('student_id', None)
    flash('Account deleted successfully.', 'success')
    return redirect(url_for('register'))


def logout():
    session.pop('student_id', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))
