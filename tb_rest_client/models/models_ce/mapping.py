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

class Mapping(object):
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
        'columns': 'list[ColumnMapping]',
        'delimiter': 'str',
        'header': 'bool',
        'update': 'bool'
    }

    attribute_map = {
        'columns': 'columns',
        'delimiter': 'delimiter',
        'header': 'header',
        'update': 'update'
    }

    def __init__(self, columns=None, delimiter=None, header=None, update=None):  # noqa: E501
        """Mapping - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._delimiter = None
        self._header = None
        self._update = None
        self.discriminator = None
        if columns is not None:
            self.columns = columns
        if delimiter is not None:
            self.delimiter = delimiter
        if header is not None:
            self.header = header
        if update is not None:
            self.update = update

    @property
    def columns(self):
        """Gets the columns of this Mapping.  # noqa: E501


        :return: The columns of this Mapping.  # noqa: E501
        :rtype: list[ColumnMapping]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Mapping.


        :param columns: The columns of this Mapping.  # noqa: E501
        :type: list[ColumnMapping]
        """

        self._columns = columns

    @property
    def delimiter(self):
        """Gets the delimiter of this Mapping.  # noqa: E501


        :return: The delimiter of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this Mapping.


        :param delimiter: The delimiter of this Mapping.  # noqa: E501
        :type: str
        """

        self._delimiter = delimiter

    @property
    def header(self):
        """Gets the header of this Mapping.  # noqa: E501


        :return: The header of this Mapping.  # noqa: E501
        :rtype: bool
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Mapping.


        :param header: The header of this Mapping.  # noqa: E501
        :type: bool
        """

        self._header = header

    @property
    def update(self):
        """Gets the update of this Mapping.  # noqa: E501


        :return: The update of this Mapping.  # noqa: E501
        :rtype: bool
        """
        return self._update

    @update.setter
    def update(self, update):
        """Sets the update of this Mapping.


        :param update: The update of this Mapping.  # noqa: E501
        :type: bool
        """

        self._update = update

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
        if issubclass(Mapping, dict):
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
        if not isinstance(other, Mapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
