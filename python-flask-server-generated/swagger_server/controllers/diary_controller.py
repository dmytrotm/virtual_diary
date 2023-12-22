import connexion
import six

from swagger_server.models.diary import Diary  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.views_body import ViewsBody  # noqa: E501
from swagger_server import util


def views_diary_notes_diary_id_delete(diary_id):  # noqa: E501
    """Delete diary by ID

    Cancels a specific diary and restores the item to the inventory. # noqa: E501

    :param diary_id: ID of the diary
    :type diary_id: int

    :rtype: None
    """
    return 'do some magic!'


def views_diary_notes_diary_id_get(diary_id):  # noqa: E501
    """Get diary by ID

    Returns detailed information about a specific diary. # noqa: E501

    :param diary_id: ID of the diary
    :type diary_id: int

    :rtype: Diary
    """
    return 'do some magic!'


def views_post(body):  # noqa: E501
    """Create diary

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = ViewsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
