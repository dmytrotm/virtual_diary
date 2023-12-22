# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.diary import Diary  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.views_body import ViewsBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDiaryController(BaseTestCase):
    """DiaryController integration test stubs"""

    def test_views_diary_notes_diary_id_delete(self):
        """Test case for views_diary_notes_diary_id_delete

        Delete diary by ID
        """
        response = self.client.open(
            '/api/views/diary-notes/{diary_id}'.format(diary_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_views_diary_notes_diary_id_get(self):
        """Test case for views_diary_notes_diary_id_get

        Get diary by ID
        """
        response = self.client.open(
            '/api/views/diary-notes/{diary_id}'.format(diary_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_views_post(self):
        """Test case for views_post

        Create diary
        """
        body = ViewsBody()
        response = self.client.open(
            '/api/views',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
