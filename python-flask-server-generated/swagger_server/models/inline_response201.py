# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse201(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, diary_id: int=None):  # noqa: E501
        """InlineResponse201 - a model defined in Swagger

        :param diary_id: The diary_id of this InlineResponse201.  # noqa: E501
        :type diary_id: int
        """
        self.swagger_types = {
            'diary_id': int
        }

        self.attribute_map = {
            'diary_id': 'diary_id'
        }
        self._diary_id = diary_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse201':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_201 of this InlineResponse201.  # noqa: E501
        :rtype: InlineResponse201
        """
        return util.deserialize_model(dikt, cls)

    @property
    def diary_id(self) -> int:
        """Gets the diary_id of this InlineResponse201.


        :return: The diary_id of this InlineResponse201.
        :rtype: int
        """
        return self._diary_id

    @diary_id.setter
    def diary_id(self, diary_id: int):
        """Sets the diary_id of this InlineResponse201.


        :param diary_id: The diary_id of this InlineResponse201.
        :type diary_id: int
        """

        self._diary_id = diary_id
