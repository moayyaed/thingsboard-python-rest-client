# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TenantSolutionTemplateDetails(object):
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
        'description': 'str',
        'highlights': 'str',
        'image_urls': 'list[str]',
        'installed': 'bool',
        'id': 'str',
        'title': 'str',
        'level': 'str',
        'install_timeout_ms': 'int',
        'tenant_telemetry_keys': 'list[str]',
        'tenant_attribute_keys': 'list[str]'
    }

    attribute_map = {
        'description': 'description',
        'highlights': 'highlights',
        'image_urls': 'imageUrls',
        'installed': 'installed',
        'id': 'id',
        'title': 'title',
        'level': 'level',
        'install_timeout_ms': 'installTimeoutMs',
        'tenant_telemetry_keys': 'tenantTelemetryKeys',
        'tenant_attribute_keys': 'tenantAttributeKeys'
    }

    def __init__(self, description=None, highlights=None, image_urls=None, installed=None, id=None, title=None, level=None, install_timeout_ms=None, tenant_telemetry_keys=None, tenant_attribute_keys=None):  # noqa: E501
        """TenantSolutionTemplateDetails - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._highlights = None
        self._image_urls = None
        self._installed = None
        self._id = None
        self._title = None
        self._level = None
        self._install_timeout_ms = None
        self._tenant_telemetry_keys = None
        self._tenant_attribute_keys = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if highlights is not None:
            self.highlights = highlights
        if image_urls is not None:
            self.image_urls = image_urls
        if installed is not None:
            self.installed = installed
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if level is not None:
            self.level = level
        if install_timeout_ms is not None:
            self.install_timeout_ms = install_timeout_ms
        if tenant_telemetry_keys is not None:
            self.tenant_telemetry_keys = tenant_telemetry_keys
        if tenant_attribute_keys is not None:
            self.tenant_attribute_keys = tenant_attribute_keys

    @property
    def description(self):
        """Gets the description of this TenantSolutionTemplateDetails.  # noqa: E501


        :return: The description of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TenantSolutionTemplateDetails.


        :param description: The description of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def highlights(self):
        """Gets the highlights of this TenantSolutionTemplateDetails.  # noqa: E501


        :return: The highlights of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: str
        """
        return self._highlights

    @highlights.setter
    def highlights(self, highlights):
        """Sets the highlights of this TenantSolutionTemplateDetails.


        :param highlights: The highlights of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: str
        """

        self._highlights = highlights

    @property
    def image_urls(self):
        """Gets the image_urls of this TenantSolutionTemplateDetails.  # noqa: E501


        :return: The image_urls of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._image_urls

    @image_urls.setter
    def image_urls(self, image_urls):
        """Sets the image_urls of this TenantSolutionTemplateDetails.


        :param image_urls: The image_urls of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: list[str]
        """

        self._image_urls = image_urls

    @property
    def installed(self):
        """Gets the installed of this TenantSolutionTemplateDetails.  # noqa: E501


        :return: The installed of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        """Sets the installed of this TenantSolutionTemplateDetails.


        :param installed: The installed of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: bool
        """

        self._installed = installed

    @property
    def id(self):
        """Gets the id of this TenantSolutionTemplateDetails.  # noqa: E501

        ID of the solution template  # noqa: E501

        :return: The id of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantSolutionTemplateDetails.

        ID of the solution template  # noqa: E501

        :param id: The id of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TenantSolutionTemplateDetails.  # noqa: E501

        Template Title  # noqa: E501

        :return: The title of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TenantSolutionTemplateDetails.

        Template Title  # noqa: E501

        :param title: The title of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def level(self):
        """Gets the level of this TenantSolutionTemplateDetails.  # noqa: E501

        Level of the subscription that is required to unlock the template  # noqa: E501

        :return: The level of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this TenantSolutionTemplateDetails.

        Level of the subscription that is required to unlock the template  # noqa: E501

        :param level: The level of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["MAKER", "PROTOTYPE", "STARTUP"]  # noqa: E501
        if level not in allowed_values:
            raise ValueError(
                "Invalid value for `level` ({0}), must be one of {1}"  # noqa: E501
                .format(level, allowed_values)
            )

        self._level = level

    @property
    def install_timeout_ms(self):
        """Gets the install_timeout_ms of this TenantSolutionTemplateDetails.  # noqa: E501

        Timeout for the installation UI to wait while template is installing  # noqa: E501

        :return: The install_timeout_ms of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: int
        """
        return self._install_timeout_ms

    @install_timeout_ms.setter
    def install_timeout_ms(self, install_timeout_ms):
        """Sets the install_timeout_ms of this TenantSolutionTemplateDetails.

        Timeout for the installation UI to wait while template is installing  # noqa: E501

        :param install_timeout_ms: The install_timeout_ms of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: int
        """

        self._install_timeout_ms = install_timeout_ms

    @property
    def tenant_telemetry_keys(self):
        """Gets the tenant_telemetry_keys of this TenantSolutionTemplateDetails.  # noqa: E501

        What keys to delete during template uninstall  # noqa: E501

        :return: The tenant_telemetry_keys of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_telemetry_keys

    @tenant_telemetry_keys.setter
    def tenant_telemetry_keys(self, tenant_telemetry_keys):
        """Sets the tenant_telemetry_keys of this TenantSolutionTemplateDetails.

        What keys to delete during template uninstall  # noqa: E501

        :param tenant_telemetry_keys: The tenant_telemetry_keys of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: list[str]
        """

        self._tenant_telemetry_keys = tenant_telemetry_keys

    @property
    def tenant_attribute_keys(self):
        """Gets the tenant_attribute_keys of this TenantSolutionTemplateDetails.  # noqa: E501

        What attributes to delete during template uninstall  # noqa: E501

        :return: The tenant_attribute_keys of this TenantSolutionTemplateDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenant_attribute_keys

    @tenant_attribute_keys.setter
    def tenant_attribute_keys(self, tenant_attribute_keys):
        """Sets the tenant_attribute_keys of this TenantSolutionTemplateDetails.

        What attributes to delete during template uninstall  # noqa: E501

        :param tenant_attribute_keys: The tenant_attribute_keys of this TenantSolutionTemplateDetails.  # noqa: E501
        :type: list[str]
        """

        self._tenant_attribute_keys = tenant_attribute_keys

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
        if issubclass(TenantSolutionTemplateDetails, dict):
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
        if not isinstance(other, TenantSolutionTemplateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
