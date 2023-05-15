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

class NotificationTarget(object):
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
        'configuration': 'NotificationTargetConfig',
        'created_time': 'int',
        'id': 'NotificationTargetId',
        'name': 'str',
        'tenant_id': 'TenantId'
    }

    attribute_map = {
        'configuration': 'configuration',
        'created_time': 'createdTime',
        'id': 'id',
        'name': 'name',
        'tenant_id': 'tenantId'
    }

    def __init__(self, configuration=None, created_time=None, id=None, name=None, tenant_id=None):  # noqa: E501
        """NotificationTarget - a model defined in Swagger"""  # noqa: E501
        self._configuration = None
        self._created_time = None
        self._id = None
        self._name = None
        self._tenant_id = None
        self.discriminator = None
        self.configuration = configuration
        if created_time is not None:
            self.created_time = created_time
        if id is not None:
            self.id = id
        self.name = name
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def configuration(self):
        """Gets the configuration of this NotificationTarget.  # noqa: E501


        :return: The configuration of this NotificationTarget.  # noqa: E501
        :rtype: NotificationTargetConfig
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this NotificationTarget.


        :param configuration: The configuration of this NotificationTarget.  # noqa: E501
        :type: NotificationTargetConfig
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def created_time(self):
        """Gets the created_time of this NotificationTarget.  # noqa: E501


        :return: The created_time of this NotificationTarget.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this NotificationTarget.


        :param created_time: The created_time of this NotificationTarget.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def id(self):
        """Gets the id of this NotificationTarget.  # noqa: E501


        :return: The id of this NotificationTarget.  # noqa: E501
        :rtype: NotificationTargetId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationTarget.


        :param id: The id of this NotificationTarget.  # noqa: E501
        :type: NotificationTargetId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NotificationTarget.  # noqa: E501


        :return: The name of this NotificationTarget.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationTarget.


        :param name: The name of this NotificationTarget.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this NotificationTarget.  # noqa: E501


        :return: The tenant_id of this NotificationTarget.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this NotificationTarget.


        :param tenant_id: The tenant_id of this NotificationTarget.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

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
        if issubclass(NotificationTarget, dict):
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
        if not isinstance(other, NotificationTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
