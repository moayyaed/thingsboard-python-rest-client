# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
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

class ServerSecurityConfig(object):
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
        'bootstrap_server_account_timeout': 'int',
        'bootstrap_server_is': 'bool',
        'client_hold_off_time': 'int',
        'host': 'str',
        'port': 'int',
        'security_host': 'str',
        'security_port': 'int',
        'server_id': 'int',
        'server_public_key': 'str'
    }

    attribute_map = {
        'bootstrap_server_account_timeout': 'bootstrapServerAccountTimeout',
        'bootstrap_server_is': 'bootstrapServerIs',
        'client_hold_off_time': 'clientHoldOffTime',
        'host': 'host',
        'port': 'port',
        'security_host': 'securityHost',
        'security_port': 'securityPort',
        'server_id': 'serverId',
        'server_public_key': 'serverPublicKey'
    }

    def __init__(self, bootstrap_server_account_timeout=None, bootstrap_server_is=None, client_hold_off_time=None, host=None, port=None, security_host=None, security_port=None, server_id=None, server_public_key=None):  # noqa: E501
        """ServerSecurityConfig - a model defined in Swagger"""  # noqa: E501
        self._bootstrap_server_account_timeout = None
        self._bootstrap_server_is = None
        self._client_hold_off_time = None
        self._host = None
        self._port = None
        self._security_host = None
        self._security_port = None
        self._server_id = None
        self._server_public_key = None
        self.discriminator = None
        if bootstrap_server_account_timeout is not None:
            self.bootstrap_server_account_timeout = bootstrap_server_account_timeout
        if bootstrap_server_is is not None:
            self.bootstrap_server_is = bootstrap_server_is
        if client_hold_off_time is not None:
            self.client_hold_off_time = client_hold_off_time
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if security_host is not None:
            self.security_host = security_host
        if security_port is not None:
            self.security_port = security_port
        if server_id is not None:
            self.server_id = server_id
        if server_public_key is not None:
            self.server_public_key = server_public_key

    @property
    def bootstrap_server_account_timeout(self):
        """Gets the bootstrap_server_account_timeout of this ServerSecurityConfig.  # noqa: E501


        :return: The bootstrap_server_account_timeout of this ServerSecurityConfig.  # noqa: E501
        :rtype: int
        """
        return self._bootstrap_server_account_timeout

    @bootstrap_server_account_timeout.setter
    def bootstrap_server_account_timeout(self, bootstrap_server_account_timeout):
        """Sets the bootstrap_server_account_timeout of this ServerSecurityConfig.


        :param bootstrap_server_account_timeout: The bootstrap_server_account_timeout of this ServerSecurityConfig.  # noqa: E501
        :type: int
        """

        self._bootstrap_server_account_timeout = bootstrap_server_account_timeout

    @property
    def bootstrap_server_is(self):
        """Gets the bootstrap_server_is of this ServerSecurityConfig.  # noqa: E501


        :return: The bootstrap_server_is of this ServerSecurityConfig.  # noqa: E501
        :rtype: bool
        """
        return self._bootstrap_server_is

    @bootstrap_server_is.setter
    def bootstrap_server_is(self, bootstrap_server_is):
        """Sets the bootstrap_server_is of this ServerSecurityConfig.


        :param bootstrap_server_is: The bootstrap_server_is of this ServerSecurityConfig.  # noqa: E501
        :type: bool
        """

        self._bootstrap_server_is = bootstrap_server_is

    @property
    def client_hold_off_time(self):
        """Gets the client_hold_off_time of this ServerSecurityConfig.  # noqa: E501


        :return: The client_hold_off_time of this ServerSecurityConfig.  # noqa: E501
        :rtype: int
        """
        return self._client_hold_off_time

    @client_hold_off_time.setter
    def client_hold_off_time(self, client_hold_off_time):
        """Sets the client_hold_off_time of this ServerSecurityConfig.


        :param client_hold_off_time: The client_hold_off_time of this ServerSecurityConfig.  # noqa: E501
        :type: int
        """

        self._client_hold_off_time = client_hold_off_time

    @property
    def host(self):
        """Gets the host of this ServerSecurityConfig.  # noqa: E501


        :return: The host of this ServerSecurityConfig.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ServerSecurityConfig.


        :param host: The host of this ServerSecurityConfig.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this ServerSecurityConfig.  # noqa: E501


        :return: The port of this ServerSecurityConfig.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerSecurityConfig.


        :param port: The port of this ServerSecurityConfig.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def security_host(self):
        """Gets the security_host of this ServerSecurityConfig.  # noqa: E501


        :return: The security_host of this ServerSecurityConfig.  # noqa: E501
        :rtype: str
        """
        return self._security_host

    @security_host.setter
    def security_host(self, security_host):
        """Sets the security_host of this ServerSecurityConfig.


        :param security_host: The security_host of this ServerSecurityConfig.  # noqa: E501
        :type: str
        """

        self._security_host = security_host

    @property
    def security_port(self):
        """Gets the security_port of this ServerSecurityConfig.  # noqa: E501


        :return: The security_port of this ServerSecurityConfig.  # noqa: E501
        :rtype: int
        """
        return self._security_port

    @security_port.setter
    def security_port(self, security_port):
        """Sets the security_port of this ServerSecurityConfig.


        :param security_port: The security_port of this ServerSecurityConfig.  # noqa: E501
        :type: int
        """

        self._security_port = security_port

    @property
    def server_id(self):
        """Gets the server_id of this ServerSecurityConfig.  # noqa: E501


        :return: The server_id of this ServerSecurityConfig.  # noqa: E501
        :rtype: int
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ServerSecurityConfig.


        :param server_id: The server_id of this ServerSecurityConfig.  # noqa: E501
        :type: int
        """

        self._server_id = server_id

    @property
    def server_public_key(self):
        """Gets the server_public_key of this ServerSecurityConfig.  # noqa: E501


        :return: The server_public_key of this ServerSecurityConfig.  # noqa: E501
        :rtype: str
        """
        return self._server_public_key

    @server_public_key.setter
    def server_public_key(self, server_public_key):
        """Sets the server_public_key of this ServerSecurityConfig.


        :param server_public_key: The server_public_key of this ServerSecurityConfig.  # noqa: E501
        :type: str
        """

        self._server_public_key = server_public_key

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
        if issubclass(ServerSecurityConfig, dict):
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
        if not isinstance(other, ServerSecurityConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
