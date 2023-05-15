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

class TelemetryMappingConfiguration(object):
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
        'attribute': 'list[str]',
        'attribute_lwm2m': 'dict(str, ObjectAttributes)',
        'key_name': 'dict(str, str)',
        'observe': 'list[str]',
        'telemetry': 'list[str]'
    }

    attribute_map = {
        'attribute': 'attribute',
        'attribute_lwm2m': 'attributeLwm2m',
        'key_name': 'keyName',
        'observe': 'observe',
        'telemetry': 'telemetry'
    }

    def __init__(self, attribute=None, attribute_lwm2m=None, key_name=None, observe=None, telemetry=None):  # noqa: E501
        """TelemetryMappingConfiguration - a model defined in Swagger"""  # noqa: E501
        self._attribute = None
        self._attribute_lwm2m = None
        self._key_name = None
        self._observe = None
        self._telemetry = None
        self.discriminator = None
        if attribute is not None:
            self.attribute = attribute
        if attribute_lwm2m is not None:
            self.attribute_lwm2m = attribute_lwm2m
        if key_name is not None:
            self.key_name = key_name
        if observe is not None:
            self.observe = observe
        if telemetry is not None:
            self.telemetry = telemetry

    @property
    def attribute(self):
        """Gets the attribute of this TelemetryMappingConfiguration.  # noqa: E501


        :return: The attribute of this TelemetryMappingConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this TelemetryMappingConfiguration.


        :param attribute: The attribute of this TelemetryMappingConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._attribute = attribute

    @property
    def attribute_lwm2m(self):
        """Gets the attribute_lwm2m of this TelemetryMappingConfiguration.  # noqa: E501


        :return: The attribute_lwm2m of this TelemetryMappingConfiguration.  # noqa: E501
        :rtype: dict(str, ObjectAttributes)
        """
        return self._attribute_lwm2m

    @attribute_lwm2m.setter
    def attribute_lwm2m(self, attribute_lwm2m):
        """Sets the attribute_lwm2m of this TelemetryMappingConfiguration.


        :param attribute_lwm2m: The attribute_lwm2m of this TelemetryMappingConfiguration.  # noqa: E501
        :type: dict(str, ObjectAttributes)
        """

        self._attribute_lwm2m = attribute_lwm2m

    @property
    def key_name(self):
        """Gets the key_name of this TelemetryMappingConfiguration.  # noqa: E501


        :return: The key_name of this TelemetryMappingConfiguration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this TelemetryMappingConfiguration.


        :param key_name: The key_name of this TelemetryMappingConfiguration.  # noqa: E501
        :type: dict(str, str)
        """

        self._key_name = key_name

    @property
    def observe(self):
        """Gets the observe of this TelemetryMappingConfiguration.  # noqa: E501


        :return: The observe of this TelemetryMappingConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._observe

    @observe.setter
    def observe(self, observe):
        """Sets the observe of this TelemetryMappingConfiguration.


        :param observe: The observe of this TelemetryMappingConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._observe = observe

    @property
    def telemetry(self):
        """Gets the telemetry of this TelemetryMappingConfiguration.  # noqa: E501


        :return: The telemetry of this TelemetryMappingConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._telemetry

    @telemetry.setter
    def telemetry(self, telemetry):
        """Sets the telemetry of this TelemetryMappingConfiguration.


        :param telemetry: The telemetry of this TelemetryMappingConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._telemetry = telemetry

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
        if issubclass(TelemetryMappingConfiguration, dict):
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
        if not isinstance(other, TelemetryMappingConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
