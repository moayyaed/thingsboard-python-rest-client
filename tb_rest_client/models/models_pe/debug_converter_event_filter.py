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

class DebugConverterEventFilter(EventFilter):
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
        'is_error': 'bool',
        'error_str': 'str',
        'type': 'str',
        '_in': 'str',
        'out': 'str',
        'metadata': 'str',
        'error': 'bool'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'server': 'server',
        'is_error': 'isError',
        'error_str': 'errorStr',
        'type': 'type',
        '_in': 'in',
        'out': 'out',
        'metadata': 'metadata',
        'error': 'error'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, server=None, is_error=None, error_str=None, type=None, _in=None, out=None, metadata=None, error=None, *args, **kwargs):  # noqa: E501
        """DebugConverterEventFilter - a model defined in Swagger"""  # noqa: E501
        self._server = None
        self._is_error = None
        self._error_str = None
        self._type = None
        self.__in = None
        self._out = None
        self._metadata = None
        self._error = None
        self.discriminator = None
        if server is not None:
            self.server = server
        if is_error is not None:
            self.is_error = is_error
        if error_str is not None:
            self.error_str = error_str
        if type is not None:
            self.type = type
        if _in is not None:
            self._in = _in
        if out is not None:
            self.out = out
        if metadata is not None:
            self.metadata = metadata
        if error is not None:
            self.error = error
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def server(self):
        """Gets the server of this DebugConverterEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this DebugConverterEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def is_error(self):
        """Gets the is_error of this DebugConverterEventFilter.  # noqa: E501


        :return: The is_error of this DebugConverterEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        """Sets the is_error of this DebugConverterEventFilter.


        :param is_error: The is_error of this DebugConverterEventFilter.  # noqa: E501
        :type: bool
        """

        self._is_error = is_error

    @property
    def error_str(self):
        """Gets the error_str of this DebugConverterEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :return: The error_str of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._error_str

    @error_str.setter
    def error_str(self, error_str):
        """Sets the error_str of this DebugConverterEventFilter.

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :param error_str: The error_str of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._error_str = error_str

    @property
    def type(self):
        """Gets the type of this DebugConverterEventFilter.  # noqa: E501


        :return: The type of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DebugConverterEventFilter.


        :param type: The type of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def _in(self):
        """Gets the _in of this DebugConverterEventFilter.  # noqa: E501


        :return: The _in of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self.__in

    @_in.setter
    def _in(self, _in):
        """Sets the _in of this DebugConverterEventFilter.


        :param _in: The _in of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self.__in = _in

    @property
    def out(self):
        """Gets the out of this DebugConverterEventFilter.  # noqa: E501


        :return: The out of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._out

    @out.setter
    def out(self, out):
        """Sets the out of this DebugConverterEventFilter.


        :param out: The out of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._out = out

    @property
    def metadata(self):
        """Gets the metadata of this DebugConverterEventFilter.  # noqa: E501


        :return: The metadata of this DebugConverterEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DebugConverterEventFilter.


        :param metadata: The metadata of this DebugConverterEventFilter.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def error(self):
        """Gets the error of this DebugConverterEventFilter.  # noqa: E501


        :return: The error of this DebugConverterEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DebugConverterEventFilter.


        :param error: The error of this DebugConverterEventFilter.  # noqa: E501
        :type: bool
        """

        self._error = error

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
        if issubclass(DebugConverterEventFilter, dict):
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
        if not isinstance(other, DebugConverterEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
