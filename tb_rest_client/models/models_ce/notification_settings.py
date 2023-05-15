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

class NotificationSettings(object):
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
        'delivery_methods_configs': 'dict(str, NotificationDeliveryMethodConfig)'
    }

    attribute_map = {
        'delivery_methods_configs': 'deliveryMethodsConfigs'
    }

    def __init__(self, delivery_methods_configs=None):  # noqa: E501
        """NotificationSettings - a model defined in Swagger"""  # noqa: E501
        self._delivery_methods_configs = None
        self.discriminator = None
        self.delivery_methods_configs = delivery_methods_configs

    @property
    def delivery_methods_configs(self):
        """Gets the delivery_methods_configs of this NotificationSettings.  # noqa: E501


        :return: The delivery_methods_configs of this NotificationSettings.  # noqa: E501
        :rtype: dict(str, NotificationDeliveryMethodConfig)
        """
        return self._delivery_methods_configs

    @delivery_methods_configs.setter
    def delivery_methods_configs(self, delivery_methods_configs):
        """Sets the delivery_methods_configs of this NotificationSettings.


        :param delivery_methods_configs: The delivery_methods_configs of this NotificationSettings.  # noqa: E501
        :type: dict(str, NotificationDeliveryMethodConfig)
        """
        if delivery_methods_configs is None:
            raise ValueError("Invalid value for `delivery_methods_configs`, must not be `None`")  # noqa: E501

        self._delivery_methods_configs = delivery_methods_configs

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
        if issubclass(NotificationSettings, dict):
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
        if not isinstance(other, NotificationSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
