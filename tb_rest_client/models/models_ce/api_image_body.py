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

class ApiImageBody(object):
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
        'file': 'str',
        'title': 'str',
        'image_sub_type': 'str'
    }

    attribute_map = {
        'file': 'file',
        'title': 'title',
        'image_sub_type': 'imageSubType'
    }

    def __init__(self, file=None, title=None, image_sub_type=None):  # noqa: E501
        """ApiImageBody - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._title = None
        self._image_sub_type = None
        self.discriminator = None
        self.file = file
        if title is not None:
            self.title = title
        if image_sub_type is not None:
            self.image_sub_type = image_sub_type

    @property
    def file(self):
        """Gets the file of this ApiImageBody.  # noqa: E501


        :return: The file of this ApiImageBody.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ApiImageBody.


        :param file: The file of this ApiImageBody.  # noqa: E501
        :type: str
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def title(self):
        """Gets the title of this ApiImageBody.  # noqa: E501


        :return: The title of this ApiImageBody.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ApiImageBody.


        :param title: The title of this ApiImageBody.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def image_sub_type(self):
        """Gets the image_sub_type of this ApiImageBody.  # noqa: E501


        :return: The image_sub_type of this ApiImageBody.  # noqa: E501
        :rtype: str
        """
        return self._image_sub_type

    @image_sub_type.setter
    def image_sub_type(self, image_sub_type):
        """Sets the image_sub_type of this ApiImageBody.


        :param image_sub_type: The image_sub_type of this ApiImageBody.  # noqa: E501
        :type: str
        """

        self._image_sub_type = image_sub_type

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
        if issubclass(ApiImageBody, dict):
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
        if not isinstance(other, ApiImageBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
