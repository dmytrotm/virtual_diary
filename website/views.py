from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Diary, Shared, User
from . import db
import json
from flask import jsonify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        diary_name = request.form.get('diary')

        if len(diary_name) < 1:
            flash('Name is too short!', category='error')
        else:
            new_diary = Diary(name=diary_name, user_id=current_user.id)
            db.session.add(new_diary)
            db.session.commit()
            flash('Diary added!', category='success')

    # Retrieve user's diaries and shared diaries
    user_diaries = Diary.query.filter_by(user_id=current_user.id).all()
    shared_diaries = Shared.query.filter_by(user_id=current_user.id).all()
    return render_template('home.html', user=current_user, user_diaries=user_diaries, shared_diaries=shared_diaries)


@views.route('/delete-note', methods=['DELETE'])
def delete_note():
    if request.method == 'DELETE':
        note_data = json.loads(request.data)
        note_id = note_data['noteId']
        note = Note.query.get(note_id)

        if note:
            diary = Diary.query.get(note.diary_id)
            if diary and diary.user_id == current_user.id:
                db.session.delete(note)
                db.session.commit()
                return jsonify({})

    return jsonify({'error': 'Invalid request method'})

@views.route('/delete-diary/<int:diary_id>', methods=['DELETE'])
def delete_diary(diary_id):
    diary = Diary.query.get(diary_id)

    if diary:
        if diary.user_id == current_user.id:
            Note.query.filter_by(diary_id=diary_id).delete()
            Shared.query.filter_by(diary_id=diary_id).delete()

            db.session.delete(diary)
            db.session.commit()
            return jsonify({'success': True})

    return jsonify({'success': False, 'error': 'Diary not found or unauthorized access'})


from datetime import datetime

@views.route('/diary-notes/edit/<int:note_id>', methods=['PUT'])
@login_required
def edit_note(note_id):
    note = Note.query.get(note_id)
    diary_id = note.diary_id
    new_note_text = request.form.get('editedNote')

    if new_note_text is None or len(new_note_text) < 1:
        flash('Note is too short!', category='error')
        return jsonify({'success': False, 'error': 'Note is too short'})

    # Update note data and date
    note.data = new_note_text
    current_time = datetime.now().strftime('%H:%M:%S')
    note.date = datetime.combine(datetime.now().date(), datetime.strptime(current_time, '%H:%M:%S').time())
    note.edited = True
    
    db.session.commit()

    diary = Diary.query.get(diary_id)

    flash('Note updated!', category='success')
    return render_template("diary_notes_partial.html", diary=diary)


@views.route('/diary-notes/<int:diary_id>', methods=['GET', 'POST'])
@login_required
def diary_notes(diary_id):
    note_text = request.form.get('note')

    if note_text is None:
        pass
    else:
        if len(note_text) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note_text, diary_id=diary_id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    diary = Diary.query.get(diary_id)

    if not diary:
        flash('Diary not found', category='error')
        return redirect(url_for('views.home'))

    return render_template("diary_notes.html", user=current_user, diary=diary)

def get_shared_diaries(user_id):
    shared_diaries = Shared.query.filter_by(user_id=user_id).all()
    
    # Extracting diary_ids from shared_diaries
    diary_ids = [shared.diary_id for shared in shared_diaries]

    # Fetching the diary objects using the extracted diary_ids
    diaries = Diary.query.filter(Diary.id.in_(diary_ids)).all()

    return diaries

@views.route('/', methods=['GET'])
@login_required
def shared_diaries(user_id):
    shared_diaries = get_shared_diaries(user_id)
    
    # If there are no shared diaries or the user does not have access
    if not shared_diaries:
        flash('No shared diaries found or unauthorized access', category='error')
        return redirect(url_for('views.home'))

    return render_template("home.html", user=current_user, shared_diaries=shared_diaries)

@views.route('/share-diary/<int:diary_id>', methods=['POST'])
@login_required
def share_diary(diary_id):
    if request.method == 'POST':
        # Retrieve the email address of the user to share with from the form data
        recipient_email = request.form.get('recipient_email')

        # Check if the email exists in the User table
        recipient = User.query.filter_by(email=recipient_email).first()
        if not recipient:
            flash('User with the provided email does not exist', category='error')
            return redirect(url_for('views.home'))
        
         # Check if the recipient is the current user
        if recipient.email == current_user.email:
            flash('Cannot share the diary with yourself', category='error')
            return redirect(url_for('views.home'))

        # Check if the diary belongs to the current user
        diary = Diary.query.get(diary_id)
        if not diary or diary.user_id != current_user.id:
            flash('Diary not found or unauthorized access', category='error')
            return redirect(url_for('views.home'))

        # Check if the diary is already shared with the recipient
        shared_diary = Shared.query.filter_by(user_id=recipient.id, diary_id=diary_id).first()
        if shared_diary:
            flash(f'The diary is already shared with {recipient_email}', category='error')
            return redirect(url_for('views.home'))

        # Create a new shared diary association
        new_shared_diary = Shared(user_id=recipient.id, diary_id=diary_id)
        db.session.add(new_shared_diary)
        db.session.commit()
        
        flash(f'Diary shared with {recipient_email} successfully', category='success')
        return redirect(url_for('views.home'))

    # Redirect to the home page if the request method is not POST
    return redirect(url_for('views.home'))
