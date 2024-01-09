# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.2
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
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

class EdgeEvent(object):
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
        'action': 'str',
        'body': 'JsonNode',
        'created_time': 'int',
        'edge_id': 'EdgeId',
        'entity_id': 'str',
        'id': 'EdgeEventId',
        'seq_id': 'int',
        'tenant_id': 'TenantId',
        'type': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'action': 'action',
        'body': 'body',
        'created_time': 'createdTime',
        'edge_id': 'edgeId',
        'entity_id': 'entityId',
        'id': 'id',
        'seq_id': 'seqId',
        'tenant_id': 'tenantId',
        'type': 'type',
        'uid': 'uid'
    }

    def __init__(self, action=None, body=None, created_time=None, edge_id=None, entity_id=None, id=None, seq_id=None, tenant_id=None, type=None, uid=None):  # noqa: E501
        """EdgeEvent - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._body = None
        self._created_time = None
        self._edge_id = None
        self._entity_id = None
        self._id = None
        self._seq_id = None
        self._tenant_id = None
        self._type = None
        self._uid = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if body is not None:
            self.body = body
        if created_time is not None:
            self.created_time = created_time
        if edge_id is not None:
            self.edge_id = edge_id
        if entity_id is not None:
            self.entity_id = entity_id
        if id is not None:
            self.id = id
        if seq_id is not None:
            self.seq_id = seq_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid

    @property
    def action(self):
        """Gets the action of this EdgeEvent.  # noqa: E501


        :return: The action of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this EdgeEvent.


        :param action: The action of this EdgeEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADDED", "ALARM_ACK", "ALARM_ASSIGNED", "ALARM_CLEAR", "ALARM_UNASSIGNED", "ASSIGNED_TO_CUSTOMER", "ASSIGNED_TO_EDGE", "ATTRIBUTES_DELETED", "ATTRIBUTES_UPDATED", "CREDENTIALS_REQUEST", "CREDENTIALS_UPDATED", "DELETED", "ENTITY_MERGE_REQUEST", "POST_ATTRIBUTES", "RELATION_ADD_OR_UPDATE", "RELATION_DELETED", "RPC_CALL", "TIMESERIES_UPDATED", "UNASSIGNED_FROM_CUSTOMER", "UNASSIGNED_FROM_EDGE", "UPDATED"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def body(self):
        """Gets the body of this EdgeEvent.  # noqa: E501


        :return: The body of this EdgeEvent.  # noqa: E501
        :rtype: JsonNode
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EdgeEvent.


        :param body: The body of this EdgeEvent.  # noqa: E501
        :type: JsonNode
        """

        self._body = body

    @property
    def created_time(self):
        """Gets the created_time of this EdgeEvent.  # noqa: E501


        :return: The created_time of this EdgeEvent.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EdgeEvent.


        :param created_time: The created_time of this EdgeEvent.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def edge_id(self):
        """Gets the edge_id of this EdgeEvent.  # noqa: E501


        :return: The edge_id of this EdgeEvent.  # noqa: E501
        :rtype: EdgeId
        """
        return self._edge_id

    @edge_id.setter
    def edge_id(self, edge_id):
        """Sets the edge_id of this EdgeEvent.


        :param edge_id: The edge_id of this EdgeEvent.  # noqa: E501
        :type: EdgeId
        """

        self._edge_id = edge_id

    @property
    def entity_id(self):
        """Gets the entity_id of this EdgeEvent.  # noqa: E501


        :return: The entity_id of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EdgeEvent.


        :param entity_id: The entity_id of this EdgeEvent.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def id(self):
        """Gets the id of this EdgeEvent.  # noqa: E501


        :return: The id of this EdgeEvent.  # noqa: E501
        :rtype: EdgeEventId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeEvent.


        :param id: The id of this EdgeEvent.  # noqa: E501
        :type: EdgeEventId
        """

        self._id = id

    @property
    def seq_id(self):
        """Gets the seq_id of this EdgeEvent.  # noqa: E501


        :return: The seq_id of this EdgeEvent.  # noqa: E501
        :rtype: int
        """
        return self._seq_id

    @seq_id.setter
    def seq_id(self, seq_id):
        """Sets the seq_id of this EdgeEvent.


        :param seq_id: The seq_id of this EdgeEvent.  # noqa: E501
        :type: int
        """

        self._seq_id = seq_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EdgeEvent.  # noqa: E501


        :return: The tenant_id of this EdgeEvent.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EdgeEvent.


        :param tenant_id: The tenant_id of this EdgeEvent.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this EdgeEvent.  # noqa: E501


        :return: The type of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EdgeEvent.


        :param type: The type of this EdgeEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADMIN_SETTINGS", "ALARM", "ASSET", "ASSET_PROFILE", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_VIEW", "OTA_PACKAGE", "QUEUE", "RELATION", "RULE_CHAIN", "RULE_CHAIN_METADATA", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this EdgeEvent.  # noqa: E501


        :return: The uid of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EdgeEvent.


        :param uid: The uid of this EdgeEvent.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(EdgeEvent, dict):
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
        if not isinstance(other, EdgeEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
