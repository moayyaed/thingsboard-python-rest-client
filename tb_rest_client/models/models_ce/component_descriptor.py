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

class ComponentDescriptor(object):
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
        'id': 'ComponentDescriptorId',
        'created_time': 'int',
        'type': 'str',
        'scope': 'str',
        'clustering_mode': 'str',
        'name': 'str',
        'clazz': 'str',
        'configuration_version': 'int',
        'actions': 'str',
        'has_queue_name': 'bool',
        'configuration_descriptor': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'type': 'type',
        'scope': 'scope',
        'clustering_mode': 'clusteringMode',
        'name': 'name',
        'clazz': 'clazz',
        'configuration_version': 'configurationVersion',
        'actions': 'actions',
        'has_queue_name': 'hasQueueName',
        'configuration_descriptor': 'configurationDescriptor'
    }

    def __init__(self, id=None, created_time=None, type=None, scope=None, clustering_mode=None, name=None, clazz=None, configuration_version=None, actions=None, has_queue_name=None, configuration_descriptor=None):  # noqa: E501
        """ComponentDescriptor - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._type = None
        self._scope = None
        self._clustering_mode = None
        self._name = None
        self._clazz = None
        self._configuration_version = None
        self._actions = None
        self._has_queue_name = None
        self._configuration_descriptor = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if type is not None:
            self.type = type
        if scope is not None:
            self.scope = scope
        if clustering_mode is not None:
            self.clustering_mode = clustering_mode
        if name is not None:
            self.name = name
        if clazz is not None:
            self.clazz = clazz
        if configuration_version is not None:
            self.configuration_version = configuration_version
        if actions is not None:
            self.actions = actions
        if has_queue_name is not None:
            self.has_queue_name = has_queue_name
        if configuration_descriptor is not None:
            self.configuration_descriptor = configuration_descriptor

    @property
    def id(self):
        """Gets the id of this ComponentDescriptor.  # noqa: E501


        :return: The id of this ComponentDescriptor.  # noqa: E501
        :rtype: ComponentDescriptorId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentDescriptor.


        :param id: The id of this ComponentDescriptor.  # noqa: E501
        :type: ComponentDescriptorId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this ComponentDescriptor.  # noqa: E501

        Timestamp of the descriptor creation, in milliseconds  # noqa: E501

        :return: The created_time of this ComponentDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this ComponentDescriptor.

        Timestamp of the descriptor creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this ComponentDescriptor.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def type(self):
        """Gets the type of this ComponentDescriptor.  # noqa: E501

        Type of the Rule Node  # noqa: E501

        :return: The type of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComponentDescriptor.

        Type of the Rule Node  # noqa: E501

        :param type: The type of this ComponentDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENRICHMENT", "FILTER", "TRANSFORMATION", "ACTION", "EXTERNAL", "FLOW"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def scope(self):
        """Gets the scope of this ComponentDescriptor.  # noqa: E501

        Scope of the Rule Node. Always set to 'TENANT', since no rule chains on the 'SYSTEM' level yet.  # noqa: E501

        :return: The scope of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ComponentDescriptor.

        Scope of the Rule Node. Always set to 'TENANT', since no rule chains on the 'SYSTEM' level yet.  # noqa: E501

        :param scope: The scope of this ComponentDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["TENANT"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"  # noqa: E501
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def clustering_mode(self):
        """Gets the clustering_mode of this ComponentDescriptor.  # noqa: E501

        Clustering mode of the RuleNode. This mode represents the ability to start Rule Node in multiple microservices.  # noqa: E501

        :return: The clustering_mode of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._clustering_mode

    @clustering_mode.setter
    def clustering_mode(self, clustering_mode):
        """Sets the clustering_mode of this ComponentDescriptor.

        Clustering mode of the RuleNode. This mode represents the ability to start Rule Node in multiple microservices.  # noqa: E501

        :param clustering_mode: The clustering_mode of this ComponentDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER_PREFERENCE", "ENABLED", "SINGLETON"]  # noqa: E501
        if clustering_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `clustering_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(clustering_mode, allowed_values)
            )

        self._clustering_mode = clustering_mode

    @property
    def name(self):
        """Gets the name of this ComponentDescriptor.  # noqa: E501

        Name of the Rule Node. Taken from the @RuleNode annotation.  # noqa: E501

        :return: The name of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentDescriptor.

        Name of the Rule Node. Taken from the @RuleNode annotation.  # noqa: E501

        :param name: The name of this ComponentDescriptor.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def clazz(self):
        """Gets the clazz of this ComponentDescriptor.  # noqa: E501

        Full name of the Java class that implements the Rule Engine Node interface.  # noqa: E501

        :return: The clazz of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._clazz

    @clazz.setter
    def clazz(self, clazz):
        """Sets the clazz of this ComponentDescriptor.

        Full name of the Java class that implements the Rule Engine Node interface.  # noqa: E501

        :param clazz: The clazz of this ComponentDescriptor.  # noqa: E501
        :type: str
        """

        self._clazz = clazz

    @property
    def configuration_version(self):
        """Gets the configuration_version of this ComponentDescriptor.  # noqa: E501

        Rule node configuration version. By default, this value is 0. If the rule node is a versioned node, this value might be greater than 0.  # noqa: E501

        :return: The configuration_version of this ComponentDescriptor.  # noqa: E501
        :rtype: int
        """
        return self._configuration_version

    @configuration_version.setter
    def configuration_version(self, configuration_version):
        """Sets the configuration_version of this ComponentDescriptor.

        Rule node configuration version. By default, this value is 0. If the rule node is a versioned node, this value might be greater than 0.  # noqa: E501

        :param configuration_version: The configuration_version of this ComponentDescriptor.  # noqa: E501
        :type: int
        """

        self._configuration_version = configuration_version

    @property
    def actions(self):
        """Gets the actions of this ComponentDescriptor.  # noqa: E501

        Rule Node Actions. Deprecated. Always null.  # noqa: E501

        :return: The actions of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ComponentDescriptor.

        Rule Node Actions. Deprecated. Always null.  # noqa: E501

        :param actions: The actions of this ComponentDescriptor.  # noqa: E501
        :type: str
        """

        self._actions = actions

    @property
    def has_queue_name(self):
        """Gets the has_queue_name of this ComponentDescriptor.  # noqa: E501

        Indicates that the RuleNode supports queue name configuration.  # noqa: E501

        :return: The has_queue_name of this ComponentDescriptor.  # noqa: E501
        :rtype: bool
        """
        return self._has_queue_name

    @has_queue_name.setter
    def has_queue_name(self, has_queue_name):
        """Sets the has_queue_name of this ComponentDescriptor.

        Indicates that the RuleNode supports queue name configuration.  # noqa: E501

        :param has_queue_name: The has_queue_name of this ComponentDescriptor.  # noqa: E501
        :type: bool
        """

        self._has_queue_name = has_queue_name

    @property
    def configuration_descriptor(self):
        """Gets the configuration_descriptor of this ComponentDescriptor.  # noqa: E501


        :return: The configuration_descriptor of this ComponentDescriptor.  # noqa: E501
        :rtype: JsonNode
        """
        return self._configuration_descriptor

    @configuration_descriptor.setter
    def configuration_descriptor(self, configuration_descriptor):
        """Sets the configuration_descriptor of this ComponentDescriptor.


        :param configuration_descriptor: The configuration_descriptor of this ComponentDescriptor.  # noqa: E501
        :type: JsonNode
        """

        self._configuration_descriptor = configuration_descriptor

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
        if issubclass(ComponentDescriptor, dict):
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
        if not isinstance(other, ComponentDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
