# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.3.3-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from tb_rest_client.models.models_ce import EntityFilter


class EdgeTypeFilter(EntityFilter):
    """
    Do not edit the class manually.

    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'edge_name_filter': 'str',
        'edge_type': 'str'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'edge_name_filter': 'edgeNameFilter',
        'edge_type': 'edgeType'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, edge_name_filter=None, edge_type=None, *args, **kwargs):  # noqa: E501
        """EdgeTypeFilter - a model defined in Swagger"""  # noqa: E501
        self._edge_name_filter = None
        self._edge_type = None
        self.discriminator = None
        if edge_name_filter is not None:
            self.edge_name_filter = edge_name_filter
        if edge_type is not None:
            self.edge_type = edge_type
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def edge_name_filter(self):
        """Gets the edge_name_filter of this EdgeTypeFilter.  # noqa: E501


        :return: The edge_name_filter of this EdgeTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._edge_name_filter

    @edge_name_filter.setter
    def edge_name_filter(self, edge_name_filter):
        """Sets the edge_name_filter of this EdgeTypeFilter.


        :param edge_name_filter: The edge_name_filter of this EdgeTypeFilter.  # noqa: E501
        :type: str
        """

        self._edge_name_filter = edge_name_filter

    @property
    def edge_type(self):
        """Gets the edge_type of this EdgeTypeFilter.  # noqa: E501


        :return: The edge_type of this EdgeTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._edge_type

    @edge_type.setter
    def edge_type(self, edge_type):
        """Sets the edge_type of this EdgeTypeFilter.


        :param edge_type: The edge_type of this EdgeTypeFilter.  # noqa: E501
        :type: str
        """

        self._edge_type = edge_type

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
        if issubclass(EdgeTypeFilter, dict):
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
        if not isinstance(other, EdgeTypeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
