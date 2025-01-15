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

class DynamicValueBoolean(object):
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
        'source_type': 'str',
        'source_attribute': 'str',
        'inherit': 'bool'
    }

    attribute_map = {
        'source_type': 'sourceType',
        'source_attribute': 'sourceAttribute',
        'inherit': 'inherit'
    }

    def __init__(self, source_type=None, source_attribute=None, inherit=None):  # noqa: E501
        """DynamicValueBoolean - a model defined in Swagger"""  # noqa: E501
        self._source_type = None
        self._source_attribute = None
        self._inherit = None
        self.discriminator = None
        if source_type is not None:
            self.source_type = source_type
        if source_attribute is not None:
            self.source_attribute = source_attribute
        if inherit is not None:
            self.inherit = inherit

    @property
    def source_type(self):
        """Gets the source_type of this DynamicValueBoolean.  # noqa: E501


        :return: The source_type of this DynamicValueBoolean.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DynamicValueBoolean.


        :param source_type: The source_type of this DynamicValueBoolean.  # noqa: E501
        :type: str
        """
        allowed_values = ["CURRENT_TENANT", "CURRENT_CUSTOMER", "CURRENT_USER", "CURRENT_DEVICE"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def source_attribute(self):
        """Gets the source_attribute of this DynamicValueBoolean.  # noqa: E501


        :return: The source_attribute of this DynamicValueBoolean.  # noqa: E501
        :rtype: str
        """
        return self._source_attribute

    @source_attribute.setter
    def source_attribute(self, source_attribute):
        """Sets the source_attribute of this DynamicValueBoolean.


        :param source_attribute: The source_attribute of this DynamicValueBoolean.  # noqa: E501
        :type: str
        """

        self._source_attribute = source_attribute

    @property
    def inherit(self):
        """Gets the inherit of this DynamicValueBoolean.  # noqa: E501


        :return: The inherit of this DynamicValueBoolean.  # noqa: E501
        :rtype: bool
        """
        return self._inherit

    @inherit.setter
    def inherit(self, inherit):
        """Sets the inherit of this DynamicValueBoolean.


        :param inherit: The inherit of this DynamicValueBoolean.  # noqa: E501
        :type: bool
        """

        self._inherit = inherit

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
        if issubclass(DynamicValueBoolean, dict):
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
        if not isinstance(other, DynamicValueBoolean):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
