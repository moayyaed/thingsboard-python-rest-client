# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2025. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pprint
import re  # noqa: F401

import six

class EntityVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'timestamp': 'int',
        'id': 'str',
        'name': 'str',
        'author': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'id': 'id',
        'name': 'name',
        'author': 'author'
    }

    def __init__(self, timestamp=None, id=None, name=None, author=None):  # noqa: E501
        """EntityVersion - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self._id = None
        self._name = None
        self._author = None
        self.discriminator = None
        if timestamp is not None:
            self.timestamp = timestamp
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if author is not None:
            self.author = author

    @property
    def timestamp(self):
        """Gets the timestamp of this EntityVersion.  # noqa: E501


        :return: The timestamp of this EntityVersion.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this EntityVersion.


        :param timestamp: The timestamp of this EntityVersion.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this EntityVersion.  # noqa: E501


        :return: The id of this EntityVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityVersion.


        :param id: The id of this EntityVersion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EntityVersion.  # noqa: E501


        :return: The name of this EntityVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityVersion.


        :param name: The name of this EntityVersion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def author(self):
        """Gets the author of this EntityVersion.  # noqa: E501


        :return: The author of this EntityVersion.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this EntityVersion.


        :param author: The author of this EntityVersion.  # noqa: E501
        :type: str
        """

        self._author = author

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EntityVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EntityVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
