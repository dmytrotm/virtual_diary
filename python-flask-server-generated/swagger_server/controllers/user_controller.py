import connexion
import six

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.inline_response2011 import InlineResponse2011  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def user_user_id_delete(user_id):  # noqa: E501
    """Delete user by ID

    Deletes a specific user. # noqa: E501

    :param user_id: ID of the user to delete
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def user_user_id_get(user_id):  # noqa: E501
    """Get user by ID

    Returns information about a specific user. # noqa: E501

    :param user_id: ID of the user to retrieve
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'


def user_user_id_post(body, user_id):  # noqa: E501
    """Create user

    Creates a new user. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: ID of the user to create
    :type user_id: int

    :rtype: InlineResponse2011
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_user_id_put(body, user_id):  # noqa: E501
    """Update user by ID

    Updates information about a specific user. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: ID of the user to update
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
