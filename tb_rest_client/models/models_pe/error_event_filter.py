# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0PE
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
from tb_rest_client.models.models_pe.event_filter import EventFilter  # noqa: F401,E501

class ErrorEventFilter(EventFilter):
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
        'server': 'str',
        'method': 'str',
        'error_str': 'str'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'server': 'server',
        'method': 'method',
        'error_str': 'errorStr'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, server=None, method=None, error_str=None, *args, **kwargs):  # noqa: E501
        """ErrorEventFilter - a model defined in Swagger"""  # noqa: E501
        self._server = None
        self._method = None
        self._error_str = None
        self.discriminator = None
        if server is not None:
            self.server = server
        if method is not None:
            self.method = method
        if error_str is not None:
            self.error_str = error_str
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def server(self):
        """Gets the server of this ErrorEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this ErrorEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this ErrorEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this ErrorEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def method(self):
        """Gets the method of this ErrorEventFilter.  # noqa: E501

        String value representing the method name when the error happened  # noqa: E501

        :return: The method of this ErrorEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ErrorEventFilter.

        String value representing the method name when the error happened  # noqa: E501

        :param method: The method of this ErrorEventFilter.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def error_str(self):
        """Gets the error_str of this ErrorEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :return: The error_str of this ErrorEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._error_str

    @error_str.setter
    def error_str(self, error_str):
        """Sets the error_str of this ErrorEventFilter.

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :param error_str: The error_str of this ErrorEventFilter.  # noqa: E501
        :type: str
        """

        self._error_str = error_str

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
        if issubclass(ErrorEventFilter, dict):
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
        if not isinstance(other, ErrorEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
