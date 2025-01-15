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

class IntegrationInfo(object):
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
        'id': 'IntegrationId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'name': 'str',
        'type': 'str',
        'debug_mode': 'bool',
        'enabled': 'bool',
        'allow_create_devices_or_assets': 'bool',
        'version': 'int',
        'status': 'object',
        'stats': 'ArrayNode',
        'edge_template': 'bool',
        'remote': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'name': 'name',
        'type': 'type',
        'debug_mode': 'debugMode',
        'enabled': 'enabled',
        'allow_create_devices_or_assets': 'allowCreateDevicesOrAssets',
        'version': 'version',
        'status': 'status',
        'stats': 'stats',
        'edge_template': 'edgeTemplate',
        'remote': 'remote'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, name=None, type=None, debug_mode=None, enabled=None, allow_create_devices_or_assets=None, version=None, status=None, stats=None, edge_template=None, remote=None):  # noqa: E501
        """IntegrationInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._name = None
        self._type = None
        self._debug_mode = None
        self._enabled = None
        self._allow_create_devices_or_assets = None
        self._version = None
        self._status = None
        self._stats = None
        self._edge_template = None
        self._remote = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.name = name
        self.type = type
        if debug_mode is not None:
            self.debug_mode = debug_mode
        if enabled is not None:
            self.enabled = enabled
        if allow_create_devices_or_assets is not None:
            self.allow_create_devices_or_assets = allow_create_devices_or_assets
        if version is not None:
            self.version = version
        if status is not None:
            self.status = status
        if stats is not None:
            self.stats = stats
        if edge_template is not None:
            self.edge_template = edge_template
        if remote is not None:
            self.remote = remote

    @property
    def id(self):
        """Gets the id of this IntegrationInfo.  # noqa: E501


        :return: The id of this IntegrationInfo.  # noqa: E501
        :rtype: IntegrationId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntegrationInfo.


        :param id: The id of this IntegrationInfo.  # noqa: E501
        :type: IntegrationId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this IntegrationInfo.  # noqa: E501

        Timestamp of the integration creation, in milliseconds  # noqa: E501

        :return: The created_time of this IntegrationInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this IntegrationInfo.

        Timestamp of the integration creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this IntegrationInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this IntegrationInfo.  # noqa: E501


        :return: The tenant_id of this IntegrationInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this IntegrationInfo.


        :param tenant_id: The tenant_id of this IntegrationInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this IntegrationInfo.  # noqa: E501

        Integration Name  # noqa: E501

        :return: The name of this IntegrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IntegrationInfo.

        Integration Name  # noqa: E501

        :param name: The name of this IntegrationInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this IntegrationInfo.  # noqa: E501

        The type of the integration  # noqa: E501

        :return: The type of this IntegrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntegrationInfo.

        The type of the integration  # noqa: E501

        :param type: The type of this IntegrationInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["OCEANCONNECT", "SIGFOX", "THINGPARK", "TPE", "CHIRPSTACK", "PARTICLE", "TMOBILE_IOT_CDP", "HTTP", "MQTT", "PUB_SUB", "AWS_IOT", "AWS_SQS", "AWS_KINESIS", "IBM_WATSON_IOT", "TTN", "TTI", "AZURE_EVENT_HUB", "OPC_UA", "CUSTOM", "UDP", "TCP", "KAFKA", "AZURE_IOT_HUB", "APACHE_PULSAR", "RABBITMQ", "LORIOT", "COAP", "TUYA", "AZURE_SERVICE_BUS", "KPN"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def debug_mode(self):
        """Gets the debug_mode of this IntegrationInfo.  # noqa: E501

        Boolean flag to enable/disable saving received messages as debug events  # noqa: E501

        :return: The debug_mode of this IntegrationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, debug_mode):
        """Sets the debug_mode of this IntegrationInfo.

        Boolean flag to enable/disable saving received messages as debug events  # noqa: E501

        :param debug_mode: The debug_mode of this IntegrationInfo.  # noqa: E501
        :type: bool
        """

        self._debug_mode = debug_mode

    @property
    def enabled(self):
        """Gets the enabled of this IntegrationInfo.  # noqa: E501

        Boolean flag to enable/disable the integration  # noqa: E501

        :return: The enabled of this IntegrationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IntegrationInfo.

        Boolean flag to enable/disable the integration  # noqa: E501

        :param enabled: The enabled of this IntegrationInfo.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def allow_create_devices_or_assets(self):
        """Gets the allow_create_devices_or_assets of this IntegrationInfo.  # noqa: E501

        Boolean flag to allow/disallow the integration to create devices or assets that send message and do not exist in the system yet  # noqa: E501

        :return: The allow_create_devices_or_assets of this IntegrationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._allow_create_devices_or_assets

    @allow_create_devices_or_assets.setter
    def allow_create_devices_or_assets(self, allow_create_devices_or_assets):
        """Sets the allow_create_devices_or_assets of this IntegrationInfo.

        Boolean flag to allow/disallow the integration to create devices or assets that send message and do not exist in the system yet  # noqa: E501

        :param allow_create_devices_or_assets: The allow_create_devices_or_assets of this IntegrationInfo.  # noqa: E501
        :type: bool
        """

        self._allow_create_devices_or_assets = allow_create_devices_or_assets

    @property
    def version(self):
        """Gets the version of this IntegrationInfo.  # noqa: E501


        :return: The version of this IntegrationInfo.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this IntegrationInfo.


        :param version: The version of this IntegrationInfo.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def status(self):
        """Gets the status of this IntegrationInfo.  # noqa: E501


        :return: The status of this IntegrationInfo.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IntegrationInfo.


        :param status: The status of this IntegrationInfo.  # noqa: E501
        :type: object
        """

        self._status = status

    @property
    def stats(self):
        """Gets the stats of this IntegrationInfo.  # noqa: E501


        :return: The stats of this IntegrationInfo.  # noqa: E501
        :rtype: ArrayNode
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this IntegrationInfo.


        :param stats: The stats of this IntegrationInfo.  # noqa: E501
        :type: ArrayNode
        """

        self._stats = stats

    @property
    def edge_template(self):
        """Gets the edge_template of this IntegrationInfo.  # noqa: E501

        Boolean flag that specifies that is regular or edge template integration  # noqa: E501

        :return: The edge_template of this IntegrationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._edge_template

    @edge_template.setter
    def edge_template(self, edge_template):
        """Sets the edge_template of this IntegrationInfo.

        Boolean flag that specifies that is regular or edge template integration  # noqa: E501

        :param edge_template: The edge_template of this IntegrationInfo.  # noqa: E501
        :type: bool
        """

        self._edge_template = edge_template

    @property
    def remote(self):
        """Gets the remote of this IntegrationInfo.  # noqa: E501

        Boolean flag to enable/disable the integration to be executed remotely. Remote integration is launched in a separate microservice. Local integration is executed by the platform core  # noqa: E501

        :return: The remote of this IntegrationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this IntegrationInfo.

        Boolean flag to enable/disable the integration to be executed remotely. Remote integration is launched in a separate microservice. Local integration is executed by the platform core  # noqa: E501

        :param remote: The remote of this IntegrationInfo.  # noqa: E501
        :type: bool
        """

        self._remote = remote

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
        if issubclass(IntegrationInfo, dict):
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
        if not isinstance(other, IntegrationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
