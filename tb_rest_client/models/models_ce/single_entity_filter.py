# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from tb_rest_client.models.models_ce.entity_filter import EntityFilter  # noqa: F401,E501

class SingleEntityFilter(EntityFilter):
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
        'single_entity': 'EntityId'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'single_entity': 'singleEntity'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, single_entity=None, *args, **kwargs):  # noqa: E501
        """SingleEntityFilter - a model defined in Swagger"""  # noqa: E501
        self._single_entity = None
        self.discriminator = None
        if single_entity is not None:
            self.single_entity = single_entity
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def single_entity(self):
        """Gets the single_entity of this SingleEntityFilter.  # noqa: E501


        :return: The single_entity of this SingleEntityFilter.  # noqa: E501
        :rtype: EntityId
        """
        return self._single_entity

    @single_entity.setter
    def single_entity(self, single_entity):
        """Sets the single_entity of this SingleEntityFilter.


        :param single_entity: The single_entity of this SingleEntityFilter.  # noqa: E501
        :type: EntityId
        """

        self._single_entity = single_entity

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
        if issubclass(SingleEntityFilter, dict):
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
        if not isinstance(other, SingleEntityFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
