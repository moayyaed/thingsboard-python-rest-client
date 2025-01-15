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

class Button(object):
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
        'enabled': 'bool',
        'text': 'str',
        'link_type': 'str',
        'link': 'str',
        'dashboard_id': 'str',
        'dashboard_state': 'str',
        'set_entity_id_in_state': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'text': 'text',
        'link_type': 'linkType',
        'link': 'link',
        'dashboard_id': 'dashboardId',
        'dashboard_state': 'dashboardState',
        'set_entity_id_in_state': 'setEntityIdInState'
    }

    def __init__(self, enabled=None, text=None, link_type=None, link=None, dashboard_id=None, dashboard_state=None, set_entity_id_in_state=None):  # noqa: E501
        """Button - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._text = None
        self._link_type = None
        self._link = None
        self._dashboard_id = None
        self._dashboard_state = None
        self._set_entity_id_in_state = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if text is not None:
            self.text = text
        if link_type is not None:
            self.link_type = link_type
        if link is not None:
            self.link = link
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if dashboard_state is not None:
            self.dashboard_state = dashboard_state
        if set_entity_id_in_state is not None:
            self.set_entity_id_in_state = set_entity_id_in_state

    @property
    def enabled(self):
        """Gets the enabled of this Button.  # noqa: E501


        :return: The enabled of this Button.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Button.


        :param enabled: The enabled of this Button.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def text(self):
        """Gets the text of this Button.  # noqa: E501


        :return: The text of this Button.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Button.


        :param text: The text of this Button.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def link_type(self):
        """Gets the link_type of this Button.  # noqa: E501


        :return: The link_type of this Button.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this Button.


        :param link_type: The link_type of this Button.  # noqa: E501
        :type: str
        """
        allowed_values = ["LINK", "DASHBOARD"]  # noqa: E501
        if link_type not in allowed_values:
            raise ValueError(
                "Invalid value for `link_type` ({0}), must be one of {1}"  # noqa: E501
                .format(link_type, allowed_values)
            )

        self._link_type = link_type

    @property
    def link(self):
        """Gets the link of this Button.  # noqa: E501


        :return: The link of this Button.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Button.


        :param link: The link of this Button.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this Button.  # noqa: E501


        :return: The dashboard_id of this Button.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this Button.


        :param dashboard_id: The dashboard_id of this Button.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def dashboard_state(self):
        """Gets the dashboard_state of this Button.  # noqa: E501


        :return: The dashboard_state of this Button.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_state

    @dashboard_state.setter
    def dashboard_state(self, dashboard_state):
        """Sets the dashboard_state of this Button.


        :param dashboard_state: The dashboard_state of this Button.  # noqa: E501
        :type: str
        """

        self._dashboard_state = dashboard_state

    @property
    def set_entity_id_in_state(self):
        """Gets the set_entity_id_in_state of this Button.  # noqa: E501


        :return: The set_entity_id_in_state of this Button.  # noqa: E501
        :rtype: bool
        """
        return self._set_entity_id_in_state

    @set_entity_id_in_state.setter
    def set_entity_id_in_state(self, set_entity_id_in_state):
        """Sets the set_entity_id_in_state of this Button.


        :param set_entity_id_in_state: The set_entity_id_in_state of this Button.  # noqa: E501
        :type: bool
        """

        self._set_entity_id_in_state = set_entity_id_in_state

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
        if issubclass(Button, dict):
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
        if not isinstance(other, Button):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
