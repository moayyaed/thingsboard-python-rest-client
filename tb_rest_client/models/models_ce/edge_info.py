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

class EdgeInfo(object):
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
        'id': 'EdgeId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'root_rule_chain_id': 'RuleChainId',
        'name': 'str',
        'type': 'str',
        'label': 'str',
        'routing_key': 'str',
        'secret': 'str',
        'version': 'int',
        'customer_title': 'str',
        'customer_is_public': 'bool',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'root_rule_chain_id': 'rootRuleChainId',
        'name': 'name',
        'type': 'type',
        'label': 'label',
        'routing_key': 'routingKey',
        'secret': 'secret',
        'version': 'version',
        'customer_title': 'customerTitle',
        'customer_is_public': 'customerIsPublic',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, root_rule_chain_id=None, name=None, type=None, label=None, routing_key=None, secret=None, version=None, customer_title=None, customer_is_public=None, additional_info=None):  # noqa: E501
        """EdgeInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._root_rule_chain_id = None
        self._name = None
        self._type = None
        self._label = None
        self._routing_key = None
        self._secret = None
        self._version = None
        self._customer_title = None
        self._customer_is_public = None
        self._additional_info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if root_rule_chain_id is not None:
            self.root_rule_chain_id = root_rule_chain_id
        self.name = name
        self.type = type
        if label is not None:
            self.label = label
        self.routing_key = routing_key
        self.secret = secret
        if version is not None:
            self.version = version
        if customer_title is not None:
            self.customer_title = customer_title
        if customer_is_public is not None:
            self.customer_is_public = customer_is_public
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this EdgeInfo.  # noqa: E501


        :return: The id of this EdgeInfo.  # noqa: E501
        :rtype: EdgeId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeInfo.


        :param id: The id of this EdgeInfo.  # noqa: E501
        :type: EdgeId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EdgeInfo.  # noqa: E501

        Timestamp of the edge creation, in milliseconds  # noqa: E501

        :return: The created_time of this EdgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EdgeInfo.

        Timestamp of the edge creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this EdgeInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EdgeInfo.  # noqa: E501


        :return: The tenant_id of this EdgeInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EdgeInfo.


        :param tenant_id: The tenant_id of this EdgeInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this EdgeInfo.  # noqa: E501


        :return: The customer_id of this EdgeInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this EdgeInfo.


        :param customer_id: The customer_id of this EdgeInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def root_rule_chain_id(self):
        """Gets the root_rule_chain_id of this EdgeInfo.  # noqa: E501


        :return: The root_rule_chain_id of this EdgeInfo.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._root_rule_chain_id

    @root_rule_chain_id.setter
    def root_rule_chain_id(self, root_rule_chain_id):
        """Sets the root_rule_chain_id of this EdgeInfo.


        :param root_rule_chain_id: The root_rule_chain_id of this EdgeInfo.  # noqa: E501
        :type: RuleChainId
        """

        self._root_rule_chain_id = root_rule_chain_id

    @property
    def name(self):
        """Gets the name of this EdgeInfo.  # noqa: E501

        Unique Edge Name in scope of Tenant  # noqa: E501

        :return: The name of this EdgeInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeInfo.

        Unique Edge Name in scope of Tenant  # noqa: E501

        :param name: The name of this EdgeInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this EdgeInfo.  # noqa: E501

        Edge type  # noqa: E501

        :return: The type of this EdgeInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EdgeInfo.

        Edge type  # noqa: E501

        :param type: The type of this EdgeInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def label(self):
        """Gets the label of this EdgeInfo.  # noqa: E501

        Label that may be used in widgets  # noqa: E501

        :return: The label of this EdgeInfo.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this EdgeInfo.

        Label that may be used in widgets  # noqa: E501

        :param label: The label of this EdgeInfo.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def routing_key(self):
        """Gets the routing_key of this EdgeInfo.  # noqa: E501

        Edge routing key ('username') to authorize on cloud  # noqa: E501

        :return: The routing_key of this EdgeInfo.  # noqa: E501
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        """Sets the routing_key of this EdgeInfo.

        Edge routing key ('username') to authorize on cloud  # noqa: E501

        :param routing_key: The routing_key of this EdgeInfo.  # noqa: E501
        :type: str
        """
        if routing_key is None:
            raise ValueError("Invalid value for `routing_key`, must not be `None`")  # noqa: E501

        self._routing_key = routing_key

    @property
    def secret(self):
        """Gets the secret of this EdgeInfo.  # noqa: E501

        Edge secret ('password') to authorize on cloud  # noqa: E501

        :return: The secret of this EdgeInfo.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this EdgeInfo.

        Edge secret ('password') to authorize on cloud  # noqa: E501

        :param secret: The secret of this EdgeInfo.  # noqa: E501
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

    @property
    def version(self):
        """Gets the version of this EdgeInfo.  # noqa: E501


        :return: The version of this EdgeInfo.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EdgeInfo.


        :param version: The version of this EdgeInfo.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def customer_title(self):
        """Gets the customer_title of this EdgeInfo.  # noqa: E501


        :return: The customer_title of this EdgeInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_title

    @customer_title.setter
    def customer_title(self, customer_title):
        """Sets the customer_title of this EdgeInfo.


        :param customer_title: The customer_title of this EdgeInfo.  # noqa: E501
        :type: str
        """

        self._customer_title = customer_title

    @property
    def customer_is_public(self):
        """Gets the customer_is_public of this EdgeInfo.  # noqa: E501


        :return: The customer_is_public of this EdgeInfo.  # noqa: E501
        :rtype: bool
        """
        return self._customer_is_public

    @customer_is_public.setter
    def customer_is_public(self, customer_is_public):
        """Sets the customer_is_public of this EdgeInfo.


        :param customer_is_public: The customer_is_public of this EdgeInfo.  # noqa: E501
        :type: bool
        """

        self._customer_is_public = customer_is_public

    @property
    def additional_info(self):
        """Gets the additional_info of this EdgeInfo.  # noqa: E501


        :return: The additional_info of this EdgeInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this EdgeInfo.


        :param additional_info: The additional_info of this EdgeInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

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
        if issubclass(EdgeInfo, dict):
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
        if not isinstance(other, EdgeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
