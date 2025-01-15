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

class NotificationInfo(object):
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
        'dashboard_id': 'DashboardId',
        'state_entity_id': 'EntityId',
        'type': 'str'
    }

    attribute_map = {
        'dashboard_id': 'dashboardId',
        'state_entity_id': 'stateEntityId',
        'type': 'type'
    }

    discriminator_value_class_map = {
              }

    def __init__(self, dashboard_id=None, state_entity_id=None, type=None):  # noqa: E501
        """NotificationInfo - a model defined in Swagger"""  # noqa: E501
        self._dashboard_id = None
        self._state_entity_id = None
        self._type = None
        self.discriminator = 'type'
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if state_entity_id is not None:
            self.state_entity_id = state_entity_id
        self.type = type

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this NotificationInfo.  # noqa: E501


        :return: The dashboard_id of this NotificationInfo.  # noqa: E501
        :rtype: DashboardId
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this NotificationInfo.


        :param dashboard_id: The dashboard_id of this NotificationInfo.  # noqa: E501
        :type: DashboardId
        """

        self._dashboard_id = dashboard_id

    @property
    def state_entity_id(self):
        """Gets the state_entity_id of this NotificationInfo.  # noqa: E501


        :return: The state_entity_id of this NotificationInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._state_entity_id

    @state_entity_id.setter
    def state_entity_id(self, state_entity_id):
        """Sets the state_entity_id of this NotificationInfo.


        :param state_entity_id: The state_entity_id of this NotificationInfo.  # noqa: E501
        :type: EntityId
        """

        self._state_entity_id = state_entity_id

    @property
    def type(self):
        """Gets the type of this NotificationInfo.  # noqa: E501


        :return: The type of this NotificationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NotificationInfo.


        :param type: The type of this NotificationInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(NotificationInfo, dict):
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
        if not isinstance(other, NotificationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
