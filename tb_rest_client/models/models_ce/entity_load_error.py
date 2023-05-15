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

class EntityLoadError(object):
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
        'message': 'str',
        'source': 'EntityId',
        'target': 'EntityId',
        'type': 'str'
    }

    attribute_map = {
        'message': 'message',
        'source': 'source',
        'target': 'target',
        'type': 'type'
    }

    def __init__(self, message=None, source=None, target=None, type=None):  # noqa: E501
        """EntityLoadError - a model defined in Swagger"""  # noqa: E501
        self._message = None
        self._source = None
        self._target = None
        self._type = None
        self.discriminator = None
        if message is not None:
            self.message = message
        if source is not None:
            self.source = source
        if target is not None:
            self.target = target
        if type is not None:
            self.type = type

    @property
    def message(self):
        """Gets the message of this EntityLoadError.  # noqa: E501


        :return: The message of this EntityLoadError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EntityLoadError.


        :param message: The message of this EntityLoadError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def source(self):
        """Gets the source of this EntityLoadError.  # noqa: E501


        :return: The source of this EntityLoadError.  # noqa: E501
        :rtype: EntityId
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this EntityLoadError.


        :param source: The source of this EntityLoadError.  # noqa: E501
        :type: EntityId
        """

        self._source = source

    @property
    def target(self):
        """Gets the target of this EntityLoadError.  # noqa: E501


        :return: The target of this EntityLoadError.  # noqa: E501
        :rtype: EntityId
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this EntityLoadError.


        :param target: The target of this EntityLoadError.  # noqa: E501
        :type: EntityId
        """

        self._target = target

    @property
    def type(self):
        """Gets the type of this EntityLoadError.  # noqa: E501


        :return: The type of this EntityLoadError.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityLoadError.


        :param type: The type of this EntityLoadError.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(EntityLoadError, dict):
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
        if not isinstance(other, EntityLoadError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
