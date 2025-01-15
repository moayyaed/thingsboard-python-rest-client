# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0PE
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

class RuleChainMetaData(object):
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
        'rule_chain_id': 'RuleChainId',
        'version': 'int',
        'first_node_index': 'int',
        'nodes': 'list[RuleNode]',
        'connections': 'list[NodeConnectionInfo]',
        'rule_chain_connections': 'list[RuleChainConnectionInfo]'
    }

    attribute_map = {
        'rule_chain_id': 'ruleChainId',
        'version': 'version',
        'first_node_index': 'firstNodeIndex',
        'nodes': 'nodes',
        'connections': 'connections',
        'rule_chain_connections': 'ruleChainConnections'
    }

    def __init__(self, rule_chain_id=None, version=None, first_node_index=None, nodes=None, connections=None, rule_chain_connections=None):  # noqa: E501
        """RuleChainMetaData - a model defined in Swagger"""  # noqa: E501
        self._rule_chain_id = None
        self._version = None
        self._first_node_index = None
        self._nodes = None
        self._connections = None
        self._rule_chain_connections = None
        self.discriminator = None
        self.rule_chain_id = rule_chain_id
        if version is not None:
            self.version = version
        self.first_node_index = first_node_index
        self.nodes = nodes
        self.connections = connections
        self.rule_chain_connections = rule_chain_connections

    @property
    def rule_chain_id(self):
        """Gets the rule_chain_id of this RuleChainMetaData.  # noqa: E501


        :return: The rule_chain_id of this RuleChainMetaData.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._rule_chain_id

    @rule_chain_id.setter
    def rule_chain_id(self, rule_chain_id):
        """Sets the rule_chain_id of this RuleChainMetaData.


        :param rule_chain_id: The rule_chain_id of this RuleChainMetaData.  # noqa: E501
        :type: RuleChainId
        """
        if rule_chain_id is None:
            raise ValueError("Invalid value for `rule_chain_id`, must not be `None`")  # noqa: E501

        self._rule_chain_id = rule_chain_id

    @property
    def version(self):
        """Gets the version of this RuleChainMetaData.  # noqa: E501

        Version of the Rule Chain  # noqa: E501

        :return: The version of this RuleChainMetaData.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RuleChainMetaData.

        Version of the Rule Chain  # noqa: E501

        :param version: The version of this RuleChainMetaData.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def first_node_index(self):
        """Gets the first_node_index of this RuleChainMetaData.  # noqa: E501

        Index of the first rule node in the 'nodes' list  # noqa: E501

        :return: The first_node_index of this RuleChainMetaData.  # noqa: E501
        :rtype: int
        """
        return self._first_node_index

    @first_node_index.setter
    def first_node_index(self, first_node_index):
        """Sets the first_node_index of this RuleChainMetaData.

        Index of the first rule node in the 'nodes' list  # noqa: E501

        :param first_node_index: The first_node_index of this RuleChainMetaData.  # noqa: E501
        :type: int
        """
        if first_node_index is None:
            raise ValueError("Invalid value for `first_node_index`, must not be `None`")  # noqa: E501

        self._first_node_index = first_node_index

    @property
    def nodes(self):
        """Gets the nodes of this RuleChainMetaData.  # noqa: E501

        List of rule node JSON objects  # noqa: E501

        :return: The nodes of this RuleChainMetaData.  # noqa: E501
        :rtype: list[RuleNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this RuleChainMetaData.

        List of rule node JSON objects  # noqa: E501

        :param nodes: The nodes of this RuleChainMetaData.  # noqa: E501
        :type: list[RuleNode]
        """
        if nodes is None:
            raise ValueError("Invalid value for `nodes`, must not be `None`")  # noqa: E501

        self._nodes = nodes

    @property
    def connections(self):
        """Gets the connections of this RuleChainMetaData.  # noqa: E501

        List of JSON objects that represent connections between rule nodes  # noqa: E501

        :return: The connections of this RuleChainMetaData.  # noqa: E501
        :rtype: list[NodeConnectionInfo]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this RuleChainMetaData.

        List of JSON objects that represent connections between rule nodes  # noqa: E501

        :param connections: The connections of this RuleChainMetaData.  # noqa: E501
        :type: list[NodeConnectionInfo]
        """
        if connections is None:
            raise ValueError("Invalid value for `connections`, must not be `None`")  # noqa: E501

        self._connections = connections

    @property
    def rule_chain_connections(self):
        """Gets the rule_chain_connections of this RuleChainMetaData.  # noqa: E501

        List of JSON objects that represent connections between rule nodes and other rule chains.  # noqa: E501

        :return: The rule_chain_connections of this RuleChainMetaData.  # noqa: E501
        :rtype: list[RuleChainConnectionInfo]
        """
        return self._rule_chain_connections

    @rule_chain_connections.setter
    def rule_chain_connections(self, rule_chain_connections):
        """Sets the rule_chain_connections of this RuleChainMetaData.

        List of JSON objects that represent connections between rule nodes and other rule chains.  # noqa: E501

        :param rule_chain_connections: The rule_chain_connections of this RuleChainMetaData.  # noqa: E501
        :type: list[RuleChainConnectionInfo]
        """
        if rule_chain_connections is None:
            raise ValueError("Invalid value for `rule_chain_connections`, must not be `None`")  # noqa: E501

        self._rule_chain_connections = rule_chain_connections

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
        if issubclass(RuleChainMetaData, dict):
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
        if not isinstance(other, RuleChainMetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
