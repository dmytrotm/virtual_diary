import connexion
import six

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.note import Note  # noqa: E501
from swagger_server import util


def views_diary_notes_diary_id_notes_edit_note_id_put(body, diary_id, note_id):  # noqa: E501
    """Update note by ID

    Updates information about a specific note. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param diary_id: ID of the diary containing the note
    :type diary_id: int
    :param note_id: ID of the note to update
    :type note_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def views_diary_notes_diary_id_post(body, diary_id):  # noqa: E501
    """Create a new note for a diary

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param diary_id: ID of the diary
    :type diary_id: int

    :rtype: Note
    """
    if connexion.request.is_json:
        body = Note.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
