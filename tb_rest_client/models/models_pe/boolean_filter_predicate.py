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
from tb_rest_client.models.models_pe.key_filter_predicate import KeyFilterPredicate  # noqa: F401,E501

class BooleanFilterPredicate(KeyFilterPredicate):
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
        'operation': 'str',
        'value': 'FilterPredicateValueboolean'
    }
    if hasattr(KeyFilterPredicate, "swagger_types"):
        swagger_types.update(KeyFilterPredicate.swagger_types)

    attribute_map = {
        'operation': 'operation',
        'value': 'value'
    }
    if hasattr(KeyFilterPredicate, "attribute_map"):
        attribute_map.update(KeyFilterPredicate.attribute_map)

    def __init__(self, operation=None, value=None, *args, **kwargs):  # noqa: E501
        """BooleanFilterPredicate - a model defined in Swagger"""  # noqa: E501
        self._operation = None
        self._value = None
        self.discriminator = None
        if operation is not None:
            self.operation = operation
        if value is not None:
            self.value = value
        KeyFilterPredicate.__init__(self, *args, **kwargs)

    @property
    def operation(self):
        """Gets the operation of this BooleanFilterPredicate.  # noqa: E501


        :return: The operation of this BooleanFilterPredicate.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this BooleanFilterPredicate.


        :param operation: The operation of this BooleanFilterPredicate.  # noqa: E501
        :type: str
        """
        allowed_values = ["EQUAL", "NOT_EQUAL"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def value(self):
        """Gets the value of this BooleanFilterPredicate.  # noqa: E501


        :return: The value of this BooleanFilterPredicate.  # noqa: E501
        :rtype: FilterPredicateValueboolean
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BooleanFilterPredicate.


        :param value: The value of this BooleanFilterPredicate.  # noqa: E501
        :type: FilterPredicateValueboolean
        """

        self._value = value

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
        if issubclass(BooleanFilterPredicate, dict):
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
        if not isinstance(other, BooleanFilterPredicate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
