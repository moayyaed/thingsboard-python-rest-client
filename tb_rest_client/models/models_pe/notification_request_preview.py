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

class NotificationRequestPreview(object):
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
        'processed_templates': 'dict(str, object)',
        'total_recipients_count': 'int',
        'recipients_count_by_target': 'dict(str, int)',
        'recipients_preview': 'list[str]'
    }

    attribute_map = {
        'processed_templates': 'processedTemplates',
        'total_recipients_count': 'totalRecipientsCount',
        'recipients_count_by_target': 'recipientsCountByTarget',
        'recipients_preview': 'recipientsPreview'
    }

    def __init__(self, processed_templates=None, total_recipients_count=None, recipients_count_by_target=None, recipients_preview=None):  # noqa: E501
        """NotificationRequestPreview - a model defined in Swagger"""  # noqa: E501
        self._processed_templates = None
        self._total_recipients_count = None
        self._recipients_count_by_target = None
        self._recipients_preview = None
        self.discriminator = None
        if processed_templates is not None:
            self.processed_templates = processed_templates
        if total_recipients_count is not None:
            self.total_recipients_count = total_recipients_count
        if recipients_count_by_target is not None:
            self.recipients_count_by_target = recipients_count_by_target
        if recipients_preview is not None:
            self.recipients_preview = recipients_preview

    @property
    def processed_templates(self):
        """Gets the processed_templates of this NotificationRequestPreview.  # noqa: E501


        :return: The processed_templates of this NotificationRequestPreview.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._processed_templates

    @processed_templates.setter
    def processed_templates(self, processed_templates):
        """Sets the processed_templates of this NotificationRequestPreview.


        :param processed_templates: The processed_templates of this NotificationRequestPreview.  # noqa: E501
        :type: dict(str, object)
        """

        self._processed_templates = processed_templates

    @property
    def total_recipients_count(self):
        """Gets the total_recipients_count of this NotificationRequestPreview.  # noqa: E501


        :return: The total_recipients_count of this NotificationRequestPreview.  # noqa: E501
        :rtype: int
        """
        return self._total_recipients_count

    @total_recipients_count.setter
    def total_recipients_count(self, total_recipients_count):
        """Sets the total_recipients_count of this NotificationRequestPreview.


        :param total_recipients_count: The total_recipients_count of this NotificationRequestPreview.  # noqa: E501
        :type: int
        """

        self._total_recipients_count = total_recipients_count

    @property
    def recipients_count_by_target(self):
        """Gets the recipients_count_by_target of this NotificationRequestPreview.  # noqa: E501


        :return: The recipients_count_by_target of this NotificationRequestPreview.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._recipients_count_by_target

    @recipients_count_by_target.setter
    def recipients_count_by_target(self, recipients_count_by_target):
        """Sets the recipients_count_by_target of this NotificationRequestPreview.


        :param recipients_count_by_target: The recipients_count_by_target of this NotificationRequestPreview.  # noqa: E501
        :type: dict(str, int)
        """

        self._recipients_count_by_target = recipients_count_by_target

    @property
    def recipients_preview(self):
        """Gets the recipients_preview of this NotificationRequestPreview.  # noqa: E501


        :return: The recipients_preview of this NotificationRequestPreview.  # noqa: E501
        :rtype: list[str]
        """
        return self._recipients_preview

    @recipients_preview.setter
    def recipients_preview(self, recipients_preview):
        """Sets the recipients_preview of this NotificationRequestPreview.


        :param recipients_preview: The recipients_preview of this NotificationRequestPreview.  # noqa: E501
        :type: list[str]
        """

        self._recipients_preview = recipients_preview

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
        if issubclass(NotificationRequestPreview, dict):
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
        if not isinstance(other, NotificationRequestPreview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
