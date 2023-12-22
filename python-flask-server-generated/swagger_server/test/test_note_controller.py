# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.note import Note  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNoteController(BaseTestCase):
    """NoteController integration test stubs"""

    def test_views_diary_notes_diary_id_notes_edit_note_id_put(self):
        """Test case for views_diary_notes_diary_id_notes_edit_note_id_put

        Update note by ID
        """
        body = Note()
        response = self.client.open(
            '/api/views/diary-notes/{diary_id}/notes/edit/{note_id}'.format(diary_id=56, note_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_views_diary_notes_diary_id_post(self):
        """Test case for views_diary_notes_diary_id_post

        Create a new note for a diary
        """
        body = Note()
        response = self.client.open(
            '/api/views/diary-notes/{diary_id}'.format(diary_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
