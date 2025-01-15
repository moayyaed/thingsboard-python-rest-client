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

class EntityDataQuery(object):
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
        'entity_filter': 'OneOfEntityDataQueryEntityFilter',
        'key_filters': 'list[KeyFilter]',
        'page_link': 'EntityDataPageLink',
        'entity_fields': 'list[EntityKey]',
        'latest_values': 'list[EntityKey]'
    }

    attribute_map = {
        'entity_filter': 'entityFilter',
        'key_filters': 'keyFilters',
        'page_link': 'pageLink',
        'entity_fields': 'entityFields',
        'latest_values': 'latestValues'
    }

    def __init__(self, entity_filter=None, key_filters=None, page_link=None, entity_fields=None, latest_values=None):  # noqa: E501
        """EntityDataQuery - a model defined in Swagger"""  # noqa: E501
        self._entity_filter = None
        self._key_filters = None
        self._page_link = None
        self._entity_fields = None
        self._latest_values = None
        self.discriminator = None
        if entity_filter is not None:
            self.entity_filter = entity_filter
        if key_filters is not None:
            self.key_filters = key_filters
        if page_link is not None:
            self.page_link = page_link
        if entity_fields is not None:
            self.entity_fields = entity_fields
        if latest_values is not None:
            self.latest_values = latest_values

    @property
    def entity_filter(self):
        """Gets the entity_filter of this EntityDataQuery.  # noqa: E501


        :return: The entity_filter of this EntityDataQuery.  # noqa: E501
        :rtype: OneOfEntityDataQueryEntityFilter
        """
        return self._entity_filter

    @entity_filter.setter
    def entity_filter(self, entity_filter):
        """Sets the entity_filter of this EntityDataQuery.


        :param entity_filter: The entity_filter of this EntityDataQuery.  # noqa: E501
        :type: OneOfEntityDataQueryEntityFilter
        """

        self._entity_filter = entity_filter

    @property
    def key_filters(self):
        """Gets the key_filters of this EntityDataQuery.  # noqa: E501


        :return: The key_filters of this EntityDataQuery.  # noqa: E501
        :rtype: list[KeyFilter]
        """
        return self._key_filters

    @key_filters.setter
    def key_filters(self, key_filters):
        """Sets the key_filters of this EntityDataQuery.


        :param key_filters: The key_filters of this EntityDataQuery.  # noqa: E501
        :type: list[KeyFilter]
        """

        self._key_filters = key_filters

    @property
    def page_link(self):
        """Gets the page_link of this EntityDataQuery.  # noqa: E501


        :return: The page_link of this EntityDataQuery.  # noqa: E501
        :rtype: EntityDataPageLink
        """
        return self._page_link

    @page_link.setter
    def page_link(self, page_link):
        """Sets the page_link of this EntityDataQuery.


        :param page_link: The page_link of this EntityDataQuery.  # noqa: E501
        :type: EntityDataPageLink
        """

        self._page_link = page_link

    @property
    def entity_fields(self):
        """Gets the entity_fields of this EntityDataQuery.  # noqa: E501


        :return: The entity_fields of this EntityDataQuery.  # noqa: E501
        :rtype: list[EntityKey]
        """
        return self._entity_fields

    @entity_fields.setter
    def entity_fields(self, entity_fields):
        """Sets the entity_fields of this EntityDataQuery.


        :param entity_fields: The entity_fields of this EntityDataQuery.  # noqa: E501
        :type: list[EntityKey]
        """

        self._entity_fields = entity_fields

    @property
    def latest_values(self):
        """Gets the latest_values of this EntityDataQuery.  # noqa: E501


        :return: The latest_values of this EntityDataQuery.  # noqa: E501
        :rtype: list[EntityKey]
        """
        return self._latest_values

    @latest_values.setter
    def latest_values(self, latest_values):
        """Sets the latest_values of this EntityDataQuery.


        :param latest_values: The latest_values of this EntityDataQuery.  # noqa: E501
        :type: list[EntityKey]
        """

        self._latest_values = latest_values

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
        if issubclass(EntityDataQuery, dict):
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
        if not isinstance(other, EntityDataQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
