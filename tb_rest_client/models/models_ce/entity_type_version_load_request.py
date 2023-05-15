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
from tb_rest_client.models.models_ce.version_load_request import VersionLoadRequest  # noqa: F401,E501

class EntityTypeVersionLoadRequest(VersionLoadRequest):
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
        'entity_types': 'dict(str, EntityTypeVersionLoadConfig)',
        'type': 'str',
        'version_id': 'str'
    }
    if hasattr(VersionLoadRequest, "swagger_types"):
        swagger_types.update(VersionLoadRequest.swagger_types)

    attribute_map = {
        'entity_types': 'entityTypes',
        'type': 'type',
        'version_id': 'versionId'
    }
    if hasattr(VersionLoadRequest, "attribute_map"):
        attribute_map.update(VersionLoadRequest.attribute_map)

    def __init__(self, entity_types=None, type=None, version_id=None, *args, **kwargs):  # noqa: E501
        """EntityTypeVersionLoadRequest - a model defined in Swagger"""  # noqa: E501
        self._entity_types = None
        self._type = None
        self._version_id = None
        self.discriminator = None
        if entity_types is not None:
            self.entity_types = entity_types
        if type is not None:
            self.type = type
        if version_id is not None:
            self.version_id = version_id
        VersionLoadRequest.__init__(self, *args, **kwargs)

    @property
    def entity_types(self):
        """Gets the entity_types of this EntityTypeVersionLoadRequest.  # noqa: E501


        :return: The entity_types of this EntityTypeVersionLoadRequest.  # noqa: E501
        :rtype: dict(str, EntityTypeVersionLoadConfig)
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """Sets the entity_types of this EntityTypeVersionLoadRequest.


        :param entity_types: The entity_types of this EntityTypeVersionLoadRequest.  # noqa: E501
        :type: dict(str, EntityTypeVersionLoadConfig)
        """

        self._entity_types = entity_types

    @property
    def type(self):
        """Gets the type of this EntityTypeVersionLoadRequest.  # noqa: E501


        :return: The type of this EntityTypeVersionLoadRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityTypeVersionLoadRequest.


        :param type: The type of this EntityTypeVersionLoadRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENTITY_TYPE", "SINGLE_ENTITY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version_id(self):
        """Gets the version_id of this EntityTypeVersionLoadRequest.  # noqa: E501


        :return: The version_id of this EntityTypeVersionLoadRequest.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this EntityTypeVersionLoadRequest.


        :param version_id: The version_id of this EntityTypeVersionLoadRequest.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

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
        if issubclass(EntityTypeVersionLoadRequest, dict):
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
        if not isinstance(other, EntityTypeVersionLoadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
