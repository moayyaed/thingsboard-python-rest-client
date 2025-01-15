# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2025. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pprint
import re  # noqa: F401

import six

class EntityExportDataObject(object):
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
        'entity_type': 'str',
        'entity': 'object',
        'relations': 'list[EntityRelation]',
        'attributes': 'dict(str, list[AttributeExportData])'
    }

    attribute_map = {
        'entity_type': 'entityType',
        'entity': 'entity',
        'relations': 'relations',
        'attributes': 'attributes'
    }

    discriminator_value_class_map = {
          'RuleChainExportData': 'RuleChainExportData',
'WidgetTypeExportData': 'WidgetTypeExportData',
'DeviceExportData': 'DeviceExportData',
'WidgetsBundleExportData': 'WidgetsBundleExportData'    }

    def __init__(self, entity_type=None, entity=None, relations=None, attributes=None):  # noqa: E501
        """EntityExportDataObject - a model defined in Swagger"""  # noqa: E501
        self._entity_type = None
        self._entity = None
        self._relations = None
        self._attributes = None
        self.discriminator = 'entityType'
        if entity_type is not None:
            self.entity_type = entity_type
        if entity is not None:
            self.entity = entity
        if relations is not None:
            self.relations = relations
        if attributes is not None:
            self.attributes = attributes

    @property
    def entity_type(self):
        """Gets the entity_type of this EntityExportDataObject.  # noqa: E501


        :return: The entity_type of this EntityExportDataObject.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EntityExportDataObject.


        :param entity_type: The entity_type of this EntityExportDataObject.  # noqa: E501
        :type: str
        """
        allowed_values = ["TENANT", "CUSTOMER", "USER", "DASHBOARD", "ASSET", "DEVICE", "ALARM", "RULE_CHAIN", "RULE_NODE", "ENTITY_VIEW", "WIDGETS_BUNDLE", "WIDGET_TYPE", "TENANT_PROFILE", "DEVICE_PROFILE", "ASSET_PROFILE", "API_USAGE_STATE", "TB_RESOURCE", "OTA_PACKAGE", "EDGE", "RPC", "QUEUE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "NOTIFICATION_REQUEST", "NOTIFICATION", "NOTIFICATION_RULE", "QUEUE_STATS", "OAUTH2_CLIENT", "DOMAIN", "MOBILE_APP"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def entity(self):
        """Gets the entity of this EntityExportDataObject.  # noqa: E501


        :return: The entity of this EntityExportDataObject.  # noqa: E501
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this EntityExportDataObject.


        :param entity: The entity of this EntityExportDataObject.  # noqa: E501
        :type: object
        """

        self._entity = entity

    @property
    def relations(self):
        """Gets the relations of this EntityExportDataObject.  # noqa: E501


        :return: The relations of this EntityExportDataObject.  # noqa: E501
        :rtype: list[EntityRelation]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        """Sets the relations of this EntityExportDataObject.


        :param relations: The relations of this EntityExportDataObject.  # noqa: E501
        :type: list[EntityRelation]
        """

        self._relations = relations

    @property
    def attributes(self):
        """Gets the attributes of this EntityExportDataObject.  # noqa: E501


        :return: The attributes of this EntityExportDataObject.  # noqa: E501
        :rtype: dict(str, list[AttributeExportData])
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EntityExportDataObject.


        :param attributes: The attributes of this EntityExportDataObject.  # noqa: E501
        :type: dict(str, list[AttributeExportData])
        """

        self._attributes = attributes

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(EntityExportDataObject, dict):
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
        if not isinstance(other, EntityExportDataObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
