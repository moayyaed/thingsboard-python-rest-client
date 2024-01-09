# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.2PE
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

class TbResource(object):
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
        'descriptor': 'JsonNode',
        'link': 'str',
        'name': 'str',
        'preview': 'str',
        'public': 'bool',
        'public_link': 'str',
        'public_resource_key': 'str',
        'id': 'TbResourceId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'title': 'str',
        'resource_type': 'str',
        'resource_key': 'str',
        'etag': 'str',
        'file_name': 'str',
        'data': 'str'
    }

    attribute_map = {
        'descriptor': 'descriptor',
        'link': 'link',
        'name': 'name',
        'preview': 'preview',
        'public': 'public',
        'public_link': 'publicLink',
        'public_resource_key': 'publicResourceKey',
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'title': 'title',
        'resource_type': 'resourceType',
        'resource_key': 'resourceKey',
        'etag': 'etag',
        'file_name': 'fileName',
        'data': 'data'
    }

    def __init__(self, descriptor=None, link=None, name=None, preview=None, public=None, public_link=None, public_resource_key=None, id=None, created_time=None, tenant_id=None, customer_id=None, title=None, resource_type=None, resource_key=None, etag=None, file_name=None, data=None):  # noqa: E501
        """TbResource - a model defined in Swagger"""  # noqa: E501
        self._descriptor = None
        self._link = None
        self._name = None
        self._preview = None
        self._public = None
        self._public_link = None
        self._public_resource_key = None
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._title = None
        self._resource_type = None
        self._resource_key = None
        self._etag = None
        self._file_name = None
        self._data = None
        self.discriminator = None
        if descriptor is not None:
            self.descriptor = descriptor
        if link is not None:
            self.link = link
        if name is not None:
            self.name = name
        if preview is not None:
            self.preview = preview
        if public is not None:
            self.public = public
        if public_link is not None:
            self.public_link = public_link
        if public_resource_key is not None:
            self.public_resource_key = public_resource_key
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        if title is not None:
            self.title = title
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_key is not None:
            self.resource_key = resource_key
        if etag is not None:
            self.etag = etag
        if file_name is not None:
            self.file_name = file_name
        if data is not None:
            self.data = data

    @property
    def descriptor(self):
        """Gets the descriptor of this TbResource.  # noqa: E501


        :return: The descriptor of this TbResource.  # noqa: E501
        :rtype: JsonNode
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor):
        """Sets the descriptor of this TbResource.


        :param descriptor: The descriptor of this TbResource.  # noqa: E501
        :type: JsonNode
        """

        self._descriptor = descriptor

    @property
    def link(self):
        """Gets the link of this TbResource.  # noqa: E501


        :return: The link of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this TbResource.


        :param link: The link of this TbResource.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def name(self):
        """Gets the name of this TbResource.  # noqa: E501


        :return: The name of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TbResource.


        :param name: The name of this TbResource.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def preview(self):
        """Gets the preview of this TbResource.  # noqa: E501


        :return: The preview of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this TbResource.


        :param preview: The preview of this TbResource.  # noqa: E501
        :type: str
        """

        self._preview = preview

    @property
    def public(self):
        """Gets the public of this TbResource.  # noqa: E501


        :return: The public of this TbResource.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this TbResource.


        :param public: The public of this TbResource.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def public_link(self):
        """Gets the public_link of this TbResource.  # noqa: E501


        :return: The public_link of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._public_link

    @public_link.setter
    def public_link(self, public_link):
        """Sets the public_link of this TbResource.


        :param public_link: The public_link of this TbResource.  # noqa: E501
        :type: str
        """

        self._public_link = public_link

    @property
    def public_resource_key(self):
        """Gets the public_resource_key of this TbResource.  # noqa: E501


        :return: The public_resource_key of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._public_resource_key

    @public_resource_key.setter
    def public_resource_key(self, public_resource_key):
        """Sets the public_resource_key of this TbResource.


        :param public_resource_key: The public_resource_key of this TbResource.  # noqa: E501
        :type: str
        """

        self._public_resource_key = public_resource_key

    @property
    def id(self):
        """Gets the id of this TbResource.  # noqa: E501


        :return: The id of this TbResource.  # noqa: E501
        :rtype: TbResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TbResource.


        :param id: The id of this TbResource.  # noqa: E501
        :type: TbResourceId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this TbResource.  # noqa: E501

        Timestamp of the resource creation, in milliseconds  # noqa: E501

        :return: The created_time of this TbResource.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this TbResource.

        Timestamp of the resource creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this TbResource.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this TbResource.  # noqa: E501


        :return: The tenant_id of this TbResource.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this TbResource.


        :param tenant_id: The tenant_id of this TbResource.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this TbResource.  # noqa: E501


        :return: The customer_id of this TbResource.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this TbResource.


        :param customer_id: The customer_id of this TbResource.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def title(self):
        """Gets the title of this TbResource.  # noqa: E501

        Resource title.  # noqa: E501

        :return: The title of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TbResource.

        Resource title.  # noqa: E501

        :param title: The title of this TbResource.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def resource_type(self):
        """Gets the resource_type of this TbResource.  # noqa: E501

        Resource type.  # noqa: E501

        :return: The resource_type of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this TbResource.

        Resource type.  # noqa: E501

        :param resource_type: The resource_type of this TbResource.  # noqa: E501
        :type: str
        """
        allowed_values = ["IMAGE", "JKS", "JS_MODULE", "LWM2M_MODEL", "PKCS_12"]  # noqa: E501
        if resource_type not in allowed_values:
            raise ValueError(
                "Invalid value for `resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(resource_type, allowed_values)
            )

        self._resource_type = resource_type

    @property
    def resource_key(self):
        """Gets the resource_key of this TbResource.  # noqa: E501

        Resource key.  # noqa: E501

        :return: The resource_key of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._resource_key

    @resource_key.setter
    def resource_key(self, resource_key):
        """Sets the resource_key of this TbResource.

        Resource key.  # noqa: E501

        :param resource_key: The resource_key of this TbResource.  # noqa: E501
        :type: str
        """

        self._resource_key = resource_key

    @property
    def etag(self):
        """Gets the etag of this TbResource.  # noqa: E501

        Resource etag.  # noqa: E501

        :return: The etag of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """Sets the etag of this TbResource.

        Resource etag.  # noqa: E501

        :param etag: The etag of this TbResource.  # noqa: E501
        :type: str
        """

        self._etag = etag

    @property
    def file_name(self):
        """Gets the file_name of this TbResource.  # noqa: E501

        Resource file name.  # noqa: E501

        :return: The file_name of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this TbResource.

        Resource file name.  # noqa: E501

        :param file_name: The file_name of this TbResource.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def data(self):
        """Gets the data of this TbResource.  # noqa: E501

        Resource data.  # noqa: E501

        :return: The data of this TbResource.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TbResource.

        Resource data.  # noqa: E501

        :param data: The data of this TbResource.  # noqa: E501
        :type: str
        """

        self._data = data

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
        if issubclass(TbResource, dict):
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
        if not isinstance(other, TbResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
