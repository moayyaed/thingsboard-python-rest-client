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

class UserInfo(object):
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
        'id': 'UserId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'email': 'str',
        'name': 'str',
        'authority': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'phone': 'str',
        'additional_info': 'JsonNode',
        'owner_id': 'EntityId',
        'owner_name': 'str',
        'groups': 'list[EntityInfo]'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'email': 'email',
        'name': 'name',
        'authority': 'authority',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'phone': 'phone',
        'additional_info': 'additionalInfo',
        'owner_id': 'ownerId',
        'owner_name': 'ownerName',
        'groups': 'groups'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, customer_id=None, email=None, name=None, authority=None, first_name=None, last_name=None, phone=None, additional_info=None, owner_id=None, owner_name=None, groups=None):  # noqa: E501
        """UserInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._email = None
        self._name = None
        self._authority = None
        self._first_name = None
        self._last_name = None
        self._phone = None
        self._additional_info = None
        self._owner_id = None
        self._owner_name = None
        self._groups = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.email = email
        if name is not None:
            self.name = name
        self.authority = authority
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if phone is not None:
            self.phone = phone
        if additional_info is not None:
            self.additional_info = additional_info
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if groups is not None:
            self.groups = groups

    @property
    def id(self):
        """Gets the id of this UserInfo.  # noqa: E501


        :return: The id of this UserInfo.  # noqa: E501
        :rtype: UserId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserInfo.


        :param id: The id of this UserInfo.  # noqa: E501
        :type: UserId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this UserInfo.  # noqa: E501

        Timestamp of the user creation, in milliseconds  # noqa: E501

        :return: The created_time of this UserInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this UserInfo.

        Timestamp of the user creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this UserInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UserInfo.  # noqa: E501


        :return: The tenant_id of this UserInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UserInfo.


        :param tenant_id: The tenant_id of this UserInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this UserInfo.  # noqa: E501


        :return: The customer_id of this UserInfo.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this UserInfo.


        :param customer_id: The customer_id of this UserInfo.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def email(self):
        """Gets the email of this UserInfo.  # noqa: E501

        Email of the user  # noqa: E501

        :return: The email of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInfo.

        Email of the user  # noqa: E501

        :param email: The email of this UserInfo.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def name(self):
        """Gets the name of this UserInfo.  # noqa: E501

        Duplicates the email of the user, readonly  # noqa: E501

        :return: The name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserInfo.

        Duplicates the email of the user, readonly  # noqa: E501

        :param name: The name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def authority(self):
        """Gets the authority of this UserInfo.  # noqa: E501

        Authority  # noqa: E501

        :return: The authority of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this UserInfo.

        Authority  # noqa: E501

        :param authority: The authority of this UserInfo.  # noqa: E501
        :type: str
        """
        if authority is None:
            raise ValueError("Invalid value for `authority`, must not be `None`")  # noqa: E501
        allowed_values = ["CUSTOMER_USER", "PRE_VERIFICATION_TOKEN", "REFRESH_TOKEN", "SYS_ADMIN", "TENANT_ADMIN"]  # noqa: E501
        if authority not in allowed_values:
            raise ValueError(
                "Invalid value for `authority` ({0}), must be one of {1}"  # noqa: E501
                .format(authority, allowed_values)
            )

        self._authority = authority

    @property
    def first_name(self):
        """Gets the first_name of this UserInfo.  # noqa: E501

        First name of the user  # noqa: E501

        :return: The first_name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserInfo.

        First name of the user  # noqa: E501

        :param first_name: The first_name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserInfo.  # noqa: E501

        Last name of the user  # noqa: E501

        :return: The last_name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserInfo.

        Last name of the user  # noqa: E501

        :param last_name: The last_name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def phone(self):
        """Gets the phone of this UserInfo.  # noqa: E501

        Phone number of the user  # noqa: E501

        :return: The phone of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserInfo.

        Phone number of the user  # noqa: E501

        :param phone: The phone of this UserInfo.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def additional_info(self):
        """Gets the additional_info of this UserInfo.  # noqa: E501


        :return: The additional_info of this UserInfo.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this UserInfo.


        :param additional_info: The additional_info of this UserInfo.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def owner_id(self):
        """Gets the owner_id of this UserInfo.  # noqa: E501


        :return: The owner_id of this UserInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this UserInfo.


        :param owner_id: The owner_id of this UserInfo.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def owner_name(self):
        """Gets the owner_name of this UserInfo.  # noqa: E501

        Owner name  # noqa: E501

        :return: The owner_name of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this UserInfo.

        Owner name  # noqa: E501

        :param owner_name: The owner_name of this UserInfo.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def groups(self):
        """Gets the groups of this UserInfo.  # noqa: E501

        Groups  # noqa: E501

        :return: The groups of this UserInfo.  # noqa: E501
        :rtype: list[EntityInfo]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserInfo.

        Groups  # noqa: E501

        :param groups: The groups of this UserInfo.  # noqa: E501
        :type: list[EntityInfo]
        """

        self._groups = groups

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
        if issubclass(UserInfo, dict):
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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
