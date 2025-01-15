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

class UserPasswordPolicy(object):
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
        'minimum_length': 'int',
        'maximum_length': 'int',
        'minimum_uppercase_letters': 'int',
        'minimum_lowercase_letters': 'int',
        'minimum_digits': 'int',
        'minimum_special_characters': 'int',
        'allow_whitespaces': 'bool',
        'force_user_to_reset_password_if_not_valid': 'bool',
        'password_expiration_period_days': 'int',
        'password_reuse_frequency_days': 'int'
    }

    attribute_map = {
        'minimum_length': 'minimumLength',
        'maximum_length': 'maximumLength',
        'minimum_uppercase_letters': 'minimumUppercaseLetters',
        'minimum_lowercase_letters': 'minimumLowercaseLetters',
        'minimum_digits': 'minimumDigits',
        'minimum_special_characters': 'minimumSpecialCharacters',
        'allow_whitespaces': 'allowWhitespaces',
        'force_user_to_reset_password_if_not_valid': 'forceUserToResetPasswordIfNotValid',
        'password_expiration_period_days': 'passwordExpirationPeriodDays',
        'password_reuse_frequency_days': 'passwordReuseFrequencyDays'
    }

    def __init__(self, minimum_length=None, maximum_length=None, minimum_uppercase_letters=None, minimum_lowercase_letters=None, minimum_digits=None, minimum_special_characters=None, allow_whitespaces=None, force_user_to_reset_password_if_not_valid=None, password_expiration_period_days=None, password_reuse_frequency_days=None):  # noqa: E501
        """UserPasswordPolicy - a model defined in Swagger"""  # noqa: E501
        self._minimum_length = None
        self._maximum_length = None
        self._minimum_uppercase_letters = None
        self._minimum_lowercase_letters = None
        self._minimum_digits = None
        self._minimum_special_characters = None
        self._allow_whitespaces = None
        self._force_user_to_reset_password_if_not_valid = None
        self._password_expiration_period_days = None
        self._password_reuse_frequency_days = None
        self.discriminator = None
        if minimum_length is not None:
            self.minimum_length = minimum_length
        if maximum_length is not None:
            self.maximum_length = maximum_length
        if minimum_uppercase_letters is not None:
            self.minimum_uppercase_letters = minimum_uppercase_letters
        if minimum_lowercase_letters is not None:
            self.minimum_lowercase_letters = minimum_lowercase_letters
        if minimum_digits is not None:
            self.minimum_digits = minimum_digits
        if minimum_special_characters is not None:
            self.minimum_special_characters = minimum_special_characters
        if allow_whitespaces is not None:
            self.allow_whitespaces = allow_whitespaces
        if force_user_to_reset_password_if_not_valid is not None:
            self.force_user_to_reset_password_if_not_valid = force_user_to_reset_password_if_not_valid
        if password_expiration_period_days is not None:
            self.password_expiration_period_days = password_expiration_period_days
        if password_reuse_frequency_days is not None:
            self.password_reuse_frequency_days = password_reuse_frequency_days

    @property
    def minimum_length(self):
        """Gets the minimum_length of this UserPasswordPolicy.  # noqa: E501

        Minimum number of symbols in the password.  # noqa: E501

        :return: The minimum_length of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_length

    @minimum_length.setter
    def minimum_length(self, minimum_length):
        """Sets the minimum_length of this UserPasswordPolicy.

        Minimum number of symbols in the password.  # noqa: E501

        :param minimum_length: The minimum_length of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_length = minimum_length

    @property
    def maximum_length(self):
        """Gets the maximum_length of this UserPasswordPolicy.  # noqa: E501

        Maximum number of symbols in the password.  # noqa: E501

        :return: The maximum_length of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._maximum_length

    @maximum_length.setter
    def maximum_length(self, maximum_length):
        """Sets the maximum_length of this UserPasswordPolicy.

        Maximum number of symbols in the password.  # noqa: E501

        :param maximum_length: The maximum_length of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._maximum_length = maximum_length

    @property
    def minimum_uppercase_letters(self):
        """Gets the minimum_uppercase_letters of this UserPasswordPolicy.  # noqa: E501

        Minimum number of uppercase letters in the password.  # noqa: E501

        :return: The minimum_uppercase_letters of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_uppercase_letters

    @minimum_uppercase_letters.setter
    def minimum_uppercase_letters(self, minimum_uppercase_letters):
        """Sets the minimum_uppercase_letters of this UserPasswordPolicy.

        Minimum number of uppercase letters in the password.  # noqa: E501

        :param minimum_uppercase_letters: The minimum_uppercase_letters of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_uppercase_letters = minimum_uppercase_letters

    @property
    def minimum_lowercase_letters(self):
        """Gets the minimum_lowercase_letters of this UserPasswordPolicy.  # noqa: E501

        Minimum number of lowercase letters in the password.  # noqa: E501

        :return: The minimum_lowercase_letters of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_lowercase_letters

    @minimum_lowercase_letters.setter
    def minimum_lowercase_letters(self, minimum_lowercase_letters):
        """Sets the minimum_lowercase_letters of this UserPasswordPolicy.

        Minimum number of lowercase letters in the password.  # noqa: E501

        :param minimum_lowercase_letters: The minimum_lowercase_letters of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_lowercase_letters = minimum_lowercase_letters

    @property
    def minimum_digits(self):
        """Gets the minimum_digits of this UserPasswordPolicy.  # noqa: E501

        Minimum number of digits in the password.  # noqa: E501

        :return: The minimum_digits of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_digits

    @minimum_digits.setter
    def minimum_digits(self, minimum_digits):
        """Sets the minimum_digits of this UserPasswordPolicy.

        Minimum number of digits in the password.  # noqa: E501

        :param minimum_digits: The minimum_digits of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_digits = minimum_digits

    @property
    def minimum_special_characters(self):
        """Gets the minimum_special_characters of this UserPasswordPolicy.  # noqa: E501

        Minimum number of special in the password.  # noqa: E501

        :return: The minimum_special_characters of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._minimum_special_characters

    @minimum_special_characters.setter
    def minimum_special_characters(self, minimum_special_characters):
        """Sets the minimum_special_characters of this UserPasswordPolicy.

        Minimum number of special in the password.  # noqa: E501

        :param minimum_special_characters: The minimum_special_characters of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._minimum_special_characters = minimum_special_characters

    @property
    def allow_whitespaces(self):
        """Gets the allow_whitespaces of this UserPasswordPolicy.  # noqa: E501

        Allow whitespaces  # noqa: E501

        :return: The allow_whitespaces of this UserPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._allow_whitespaces

    @allow_whitespaces.setter
    def allow_whitespaces(self, allow_whitespaces):
        """Sets the allow_whitespaces of this UserPasswordPolicy.

        Allow whitespaces  # noqa: E501

        :param allow_whitespaces: The allow_whitespaces of this UserPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._allow_whitespaces = allow_whitespaces

    @property
    def force_user_to_reset_password_if_not_valid(self):
        """Gets the force_user_to_reset_password_if_not_valid of this UserPasswordPolicy.  # noqa: E501

        Force user to update password if existing one does not pass validation  # noqa: E501

        :return: The force_user_to_reset_password_if_not_valid of this UserPasswordPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._force_user_to_reset_password_if_not_valid

    @force_user_to_reset_password_if_not_valid.setter
    def force_user_to_reset_password_if_not_valid(self, force_user_to_reset_password_if_not_valid):
        """Sets the force_user_to_reset_password_if_not_valid of this UserPasswordPolicy.

        Force user to update password if existing one does not pass validation  # noqa: E501

        :param force_user_to_reset_password_if_not_valid: The force_user_to_reset_password_if_not_valid of this UserPasswordPolicy.  # noqa: E501
        :type: bool
        """

        self._force_user_to_reset_password_if_not_valid = force_user_to_reset_password_if_not_valid

    @property
    def password_expiration_period_days(self):
        """Gets the password_expiration_period_days of this UserPasswordPolicy.  # noqa: E501

        Password expiration period (days). Force expiration of the password.  # noqa: E501

        :return: The password_expiration_period_days of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._password_expiration_period_days

    @password_expiration_period_days.setter
    def password_expiration_period_days(self, password_expiration_period_days):
        """Sets the password_expiration_period_days of this UserPasswordPolicy.

        Password expiration period (days). Force expiration of the password.  # noqa: E501

        :param password_expiration_period_days: The password_expiration_period_days of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._password_expiration_period_days = password_expiration_period_days

    @property
    def password_reuse_frequency_days(self):
        """Gets the password_reuse_frequency_days of this UserPasswordPolicy.  # noqa: E501

        Password reuse frequency (days). Disallow to use the same password for the defined number of days  # noqa: E501

        :return: The password_reuse_frequency_days of this UserPasswordPolicy.  # noqa: E501
        :rtype: int
        """
        return self._password_reuse_frequency_days

    @password_reuse_frequency_days.setter
    def password_reuse_frequency_days(self, password_reuse_frequency_days):
        """Sets the password_reuse_frequency_days of this UserPasswordPolicy.

        Password reuse frequency (days). Disallow to use the same password for the defined number of days  # noqa: E501

        :param password_reuse_frequency_days: The password_reuse_frequency_days of this UserPasswordPolicy.  # noqa: E501
        :type: int
        """

        self._password_reuse_frequency_days = password_reuse_frequency_days

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
        if issubclass(UserPasswordPolicy, dict):
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
        if not isinstance(other, UserPasswordPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
