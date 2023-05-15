# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_pe.entity_filter import EntityFilter  # noqa: F401,E501

class DeviceSearchQueryFilter(EntityFilter):
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
        'device_types': 'list[str]',
        'direction': 'str',
        'fetch_last_level_only': 'bool',
        'max_level': 'int',
        'relation_type': 'str',
        'root_entity': 'EntityId'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'device_types': 'deviceTypes',
        'direction': 'direction',
        'fetch_last_level_only': 'fetchLastLevelOnly',
        'max_level': 'maxLevel',
        'relation_type': 'relationType',
        'root_entity': 'rootEntity'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, device_types=None, direction=None, fetch_last_level_only=None, max_level=None, relation_type=None, root_entity=None, *args, **kwargs):  # noqa: E501
        """DeviceSearchQueryFilter - a model defined in Swagger"""  # noqa: E501
        self._device_types = None
        self._direction = None
        self._fetch_last_level_only = None
        self._max_level = None
        self._relation_type = None
        self._root_entity = None
        self.discriminator = None
        if device_types is not None:
            self.device_types = device_types
        if direction is not None:
            self.direction = direction
        if fetch_last_level_only is not None:
            self.fetch_last_level_only = fetch_last_level_only
        if max_level is not None:
            self.max_level = max_level
        if relation_type is not None:
            self.relation_type = relation_type
        if root_entity is not None:
            self.root_entity = root_entity
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def device_types(self):
        """Gets the device_types of this DeviceSearchQueryFilter.  # noqa: E501


        :return: The device_types of this DeviceSearchQueryFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._device_types

    @device_types.setter
    def device_types(self, device_types):
        """Sets the device_types of this DeviceSearchQueryFilter.


        :param device_types: The device_types of this DeviceSearchQueryFilter.  # noqa: E501
        :type: list[str]
        """

        self._device_types = device_types

    @property
    def direction(self):
        """Gets the direction of this DeviceSearchQueryFilter.  # noqa: E501


        :return: The direction of this DeviceSearchQueryFilter.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this DeviceSearchQueryFilter.


        :param direction: The direction of this DeviceSearchQueryFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["FROM", "TO"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def fetch_last_level_only(self):
        """Gets the fetch_last_level_only of this DeviceSearchQueryFilter.  # noqa: E501


        :return: The fetch_last_level_only of this DeviceSearchQueryFilter.  # noqa: E501
        :rtype: bool
        """
        return self._fetch_last_level_only

    @fetch_last_level_only.setter
    def fetch_last_level_only(self, fetch_last_level_only):
        """Sets the fetch_last_level_only of this DeviceSearchQueryFilter.


        :param fetch_last_level_only: The fetch_last_level_only of this DeviceSearchQueryFilter.  # noqa: E501
        :type: bool
        """

        self._fetch_last_level_only = fetch_last_level_only

    @property
    def max_level(self):
        """Gets the max_level of this DeviceSearchQueryFilter.  # noqa: E501


        :return: The max_level of this DeviceSearchQueryFilter.  # noqa: E501
        :rtype: int
        """
        return self._max_level

    @max_level.setter
    def max_level(self, max_level):
        """Sets the max_level of this DeviceSearchQueryFilter.


        :param max_level: The max_level of this DeviceSearchQueryFilter.  # noqa: E501
        :type: int
        """

        self._max_level = max_level

    @property
    def relation_type(self):
        """Gets the relation_type of this DeviceSearchQueryFilter.  # noqa: E501


        :return: The relation_type of this DeviceSearchQueryFilter.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this DeviceSearchQueryFilter.


        :param relation_type: The relation_type of this DeviceSearchQueryFilter.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

    @property
    def root_entity(self):
        """Gets the root_entity of this DeviceSearchQueryFilter.  # noqa: E501


        :return: The root_entity of this DeviceSearchQueryFilter.  # noqa: E501
        :rtype: EntityId
        """
        return self._root_entity

    @root_entity.setter
    def root_entity(self, root_entity):
        """Sets the root_entity of this DeviceSearchQueryFilter.


        :param root_entity: The root_entity of this DeviceSearchQueryFilter.  # noqa: E501
        :type: EntityId
        """

        self._root_entity = root_entity

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
        if issubclass(DeviceSearchQueryFilter, dict):
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
        if not isinstance(other, DeviceSearchQueryFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
