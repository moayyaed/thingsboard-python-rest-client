# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3PAAS-RC1
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from tb_rest_client.models.models_pe import DeviceProfileTransportConfiguration


class SnmpDeviceProfileTransportConfiguration(DeviceProfileTransportConfiguration):
    """
    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'communication_configs': 'list[SnmpCommunicationConfig]',
        'retries': 'int',
        'timeout_ms': 'int'
    }
    if hasattr(DeviceProfileTransportConfiguration, "swagger_types"):
        swagger_types.update(DeviceProfileTransportConfiguration.swagger_types)

    attribute_map = {
        'communication_configs': 'communicationConfigs',
        'retries': 'retries',
        'timeout_ms': 'timeoutMs'
    }
    if hasattr(DeviceProfileTransportConfiguration, "attribute_map"):
        attribute_map.update(DeviceProfileTransportConfiguration.attribute_map)

    def __init__(self, communication_configs=None, retries=None, timeout_ms=None, *args, **kwargs):  # noqa: E501
        """SnmpDeviceProfileTransportConfiguration - a model defined in Swagger"""  # noqa: E501
        self._communication_configs = None
        self._retries = None
        self._timeout_ms = None
        self.discriminator = None
        if communication_configs is not None:
            self.communication_configs = communication_configs
        if retries is not None:
            self.retries = retries
        if timeout_ms is not None:
            self.timeout_ms = timeout_ms
        DeviceProfileTransportConfiguration.__init__(self, *args, **kwargs)

    @property
    def communication_configs(self):
        """Gets the communication_configs of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The communication_configs of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: list[SnmpCommunicationConfig]
        """
        return self._communication_configs

    @communication_configs.setter
    def communication_configs(self, communication_configs):
        """Sets the communication_configs of this SnmpDeviceProfileTransportConfiguration.


        :param communication_configs: The communication_configs of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501
        :type: list[SnmpCommunicationConfig]
        """

        self._communication_configs = communication_configs

    @property
    def retries(self):
        """Gets the retries of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The retries of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this SnmpDeviceProfileTransportConfiguration.


        :param retries: The retries of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def timeout_ms(self):
        """Gets the timeout_ms of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The timeout_ms of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._timeout_ms

    @timeout_ms.setter
    def timeout_ms(self, timeout_ms):
        """Sets the timeout_ms of this SnmpDeviceProfileTransportConfiguration.


        :param timeout_ms: The timeout_ms of this SnmpDeviceProfileTransportConfiguration.  # noqa: E501
        :type: int
        """

        self._timeout_ms = timeout_ms

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
        if issubclass(SnmpDeviceProfileTransportConfiguration, dict):
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
        if not isinstance(other, SnmpDeviceProfileTransportConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
