from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, Diary
from . import db
import json
from flask import jsonify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        diary = request.form.get('diary')

        if len(diary) < 1:
            flash('Name is too short!', category='error')
        else:
            new_diary = Diary(name=diary, user_id=current_user.id)
            db.session.add(new_diary)
            db.session.commit()
            flash('Diary added!', category='success')
    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['DELETE'])
def delete_note():
    if request.method == 'DELETE':
        try:
            note_data = request.get_json()  # Use get_json() to parse JSON data
            note_id = note_data['noteId']
            note = Note.query.get(note_id)

            if note:
                diary = Diary.query.get(note.diary_id)
                if diary and diary.user_id == current_user.id:
                    db.session.delete(note)
                    db.session.commit()
                    return jsonify({})

        except Exception as e:
            return jsonify({'error': f'Invalid request format: {str(e)}'}), 400

    return jsonify({'error': 'Invalid request method'}), 405


@views.route('/delete-diary/<int:diary_id>', methods=['DELETE'])
def delete_diary(diary_id):
    diary = Diary.query.get(diary_id)

    if diary:
        if diary.user_id == current_user.id:
            Note.query.filter_by(diary_id=diary_id).delete()

            db.session.delete(diary)
            db.session.commit()
            return jsonify({'success': True})

    return jsonify({'success': False, 'error': 'Diary not found or unauthorized access'})


@views.route('/diary-notes/edit/<int:note_id>', methods=['PUT'])
@login_required
def edit_note(note_id):
    note = Note.query.get(note_id)
    diary_id = note.diary_id
    new_note_text = request.form.get('editedNote')

    if new_note_text is None or len(new_note_text) < 1:
        flash('Note is too short!', category='error')
        return jsonify({'success': False, 'error': 'Note is too short'})

    note.data = new_note_text
    db.session.commit()

    diary = Diary.query.get(diary_id)

    flash('Note updated!', category='success')
    return render_template("diary_notes.html", user=current_user, diary=diary)

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

    if not diary or diary.user_id != current_user.id:
        flash('Diary not found or unauthorized access', category='error')
        return redirect(url_for('views.home'))

    return render_template("diary_notes.html", user=current_user, diary=diary)
