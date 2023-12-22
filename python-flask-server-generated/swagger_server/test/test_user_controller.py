# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.inline_response2011 import InlineResponse2011  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_user_user_id_delete(self):
        """Test case for user_user_id_delete

        Delete user by ID
        """
        response = self.client.open(
            '/api/user/{userId}'.format(user_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_get(self):
        """Test case for user_user_id_get

        Get user by ID
        """
        response = self.client.open(
            '/api/user/{userId}'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_post(self):
        """Test case for user_user_id_post

        Create user
        """
        body = User()
        response = self.client.open(
            '/api/user/{userId}'.format(user_id=56),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_id_put(self):
        """Test case for user_user_id_put

        Update user by ID
        """
        body = User()
        response = self.client.open(
            '/api/user/{userId}'.format(user_id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
