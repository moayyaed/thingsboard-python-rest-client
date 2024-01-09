# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.2PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
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

class AlarmCondition(object):
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
        'condition': 'list[AlarmConditionFilter]',
        'spec': 'AlarmConditionSpec'
    }

    attribute_map = {
        'condition': 'condition',
        'spec': 'spec'
    }

    def __init__(self, condition=None, spec=None):  # noqa: E501
        """AlarmCondition - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self._spec = None
        self.discriminator = None
        if condition is not None:
            self.condition = condition
        if spec is not None:
            self.spec = spec

    @property
    def condition(self):
        """Gets the condition of this AlarmCondition.  # noqa: E501

        JSON array of alarm condition filters  # noqa: E501

        :return: The condition of this AlarmCondition.  # noqa: E501
        :rtype: list[AlarmConditionFilter]
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this AlarmCondition.

        JSON array of alarm condition filters  # noqa: E501

        :param condition: The condition of this AlarmCondition.  # noqa: E501
        :type: list[AlarmConditionFilter]
        """

        self._condition = condition

    @property
    def spec(self):
        """Gets the spec of this AlarmCondition.  # noqa: E501


        :return: The spec of this AlarmCondition.  # noqa: E501
        :rtype: AlarmConditionSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this AlarmCondition.


        :param spec: The spec of this AlarmCondition.  # noqa: E501
        :type: AlarmConditionSpec
        """

        self._spec = spec

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
        if issubclass(AlarmCondition, dict):
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
        if not isinstance(other, AlarmCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
