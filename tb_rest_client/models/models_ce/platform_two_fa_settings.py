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

class PlatformTwoFaSettings(object):
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
        'providers': 'list[OneOfPlatformTwoFaSettingsProvidersItems]',
        'min_verification_code_send_period': 'int',
        'verification_code_check_rate_limit': 'str',
        'max_verification_failures_before_user_lockout': 'int',
        'total_allowed_time_for_verification': 'int'
    }

    attribute_map = {
        'providers': 'providers',
        'min_verification_code_send_period': 'minVerificationCodeSendPeriod',
        'verification_code_check_rate_limit': 'verificationCodeCheckRateLimit',
        'max_verification_failures_before_user_lockout': 'maxVerificationFailuresBeforeUserLockout',
        'total_allowed_time_for_verification': 'totalAllowedTimeForVerification'
    }

    def __init__(self, providers=None, min_verification_code_send_period=None, verification_code_check_rate_limit=None, max_verification_failures_before_user_lockout=None, total_allowed_time_for_verification=None):  # noqa: E501
        """PlatformTwoFaSettings - a model defined in Swagger"""  # noqa: E501
        self._providers = None
        self._min_verification_code_send_period = None
        self._verification_code_check_rate_limit = None
        self._max_verification_failures_before_user_lockout = None
        self._total_allowed_time_for_verification = None
        self.discriminator = None
        self.providers = providers
        self.min_verification_code_send_period = min_verification_code_send_period
        if verification_code_check_rate_limit is not None:
            self.verification_code_check_rate_limit = verification_code_check_rate_limit
        if max_verification_failures_before_user_lockout is not None:
            self.max_verification_failures_before_user_lockout = max_verification_failures_before_user_lockout
        self.total_allowed_time_for_verification = total_allowed_time_for_verification

    @property
    def providers(self):
        """Gets the providers of this PlatformTwoFaSettings.  # noqa: E501


        :return: The providers of this PlatformTwoFaSettings.  # noqa: E501
        :rtype: list[OneOfPlatformTwoFaSettingsProvidersItems]
        """
        return self._providers

    @providers.setter
    def providers(self, providers):
        """Sets the providers of this PlatformTwoFaSettings.


        :param providers: The providers of this PlatformTwoFaSettings.  # noqa: E501
        :type: list[OneOfPlatformTwoFaSettingsProvidersItems]
        """
        if providers is None:
            raise ValueError("Invalid value for `providers`, must not be `None`")  # noqa: E501

        self._providers = providers

    @property
    def min_verification_code_send_period(self):
        """Gets the min_verification_code_send_period of this PlatformTwoFaSettings.  # noqa: E501


        :return: The min_verification_code_send_period of this PlatformTwoFaSettings.  # noqa: E501
        :rtype: int
        """
        return self._min_verification_code_send_period

    @min_verification_code_send_period.setter
    def min_verification_code_send_period(self, min_verification_code_send_period):
        """Sets the min_verification_code_send_period of this PlatformTwoFaSettings.


        :param min_verification_code_send_period: The min_verification_code_send_period of this PlatformTwoFaSettings.  # noqa: E501
        :type: int
        """
        if min_verification_code_send_period is None:
            raise ValueError("Invalid value for `min_verification_code_send_period`, must not be `None`")  # noqa: E501

        self._min_verification_code_send_period = min_verification_code_send_period

    @property
    def verification_code_check_rate_limit(self):
        """Gets the verification_code_check_rate_limit of this PlatformTwoFaSettings.  # noqa: E501


        :return: The verification_code_check_rate_limit of this PlatformTwoFaSettings.  # noqa: E501
        :rtype: str
        """
        return self._verification_code_check_rate_limit

    @verification_code_check_rate_limit.setter
    def verification_code_check_rate_limit(self, verification_code_check_rate_limit):
        """Sets the verification_code_check_rate_limit of this PlatformTwoFaSettings.


        :param verification_code_check_rate_limit: The verification_code_check_rate_limit of this PlatformTwoFaSettings.  # noqa: E501
        :type: str
        """

        self._verification_code_check_rate_limit = verification_code_check_rate_limit

    @property
    def max_verification_failures_before_user_lockout(self):
        """Gets the max_verification_failures_before_user_lockout of this PlatformTwoFaSettings.  # noqa: E501


        :return: The max_verification_failures_before_user_lockout of this PlatformTwoFaSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_verification_failures_before_user_lockout

    @max_verification_failures_before_user_lockout.setter
    def max_verification_failures_before_user_lockout(self, max_verification_failures_before_user_lockout):
        """Sets the max_verification_failures_before_user_lockout of this PlatformTwoFaSettings.


        :param max_verification_failures_before_user_lockout: The max_verification_failures_before_user_lockout of this PlatformTwoFaSettings.  # noqa: E501
        :type: int
        """

        self._max_verification_failures_before_user_lockout = max_verification_failures_before_user_lockout

    @property
    def total_allowed_time_for_verification(self):
        """Gets the total_allowed_time_for_verification of this PlatformTwoFaSettings.  # noqa: E501


        :return: The total_allowed_time_for_verification of this PlatformTwoFaSettings.  # noqa: E501
        :rtype: int
        """
        return self._total_allowed_time_for_verification

    @total_allowed_time_for_verification.setter
    def total_allowed_time_for_verification(self, total_allowed_time_for_verification):
        """Sets the total_allowed_time_for_verification of this PlatformTwoFaSettings.


        :param total_allowed_time_for_verification: The total_allowed_time_for_verification of this PlatformTwoFaSettings.  # noqa: E501
        :type: int
        """
        if total_allowed_time_for_verification is None:
            raise ValueError("Invalid value for `total_allowed_time_for_verification`, must not be `None`")  # noqa: E501

        self._total_allowed_time_for_verification = total_allowed_time_for_verification

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
        if issubclass(PlatformTwoFaSettings, dict):
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
        if not isinstance(other, PlatformTwoFaSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
