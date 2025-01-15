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

class ResponseEntity(object):
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
        'body': 'object',
        'status_code': 'str',
        'status_code_value': 'int'
    }

    attribute_map = {
        'body': 'body',
        'status_code': 'statusCode',
        'status_code_value': 'statusCodeValue'
    }

    def __init__(self, body=None, status_code=None, status_code_value=None):  # noqa: E501
        """ResponseEntity - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._status_code = None
        self._status_code_value = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if status_code is not None:
            self.status_code = status_code
        if status_code_value is not None:
            self.status_code_value = status_code_value

    @property
    def body(self):
        """Gets the body of this ResponseEntity.  # noqa: E501


        :return: The body of this ResponseEntity.  # noqa: E501
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ResponseEntity.


        :param body: The body of this ResponseEntity.  # noqa: E501
        :type: object
        """

        self._body = body

    @property
    def status_code(self):
        """Gets the status_code of this ResponseEntity.  # noqa: E501


        :return: The status_code of this ResponseEntity.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ResponseEntity.


        :param status_code: The status_code of this ResponseEntity.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCEPTED", "ALREADY_REPORTED", "BAD_GATEWAY", "BAD_REQUEST", "BANDWIDTH_LIMIT_EXCEEDED", "CHECKPOINT", "CONFLICT", "CONTINUE", "CREATED", "DESTINATION_LOCKED", "EXPECTATION_FAILED", "FAILED_DEPENDENCY", "FORBIDDEN", "FOUND", "GATEWAY_TIMEOUT", "GONE", "HTTP_VERSION_NOT_SUPPORTED", "IM_USED", "INSUFFICIENT_SPACE_ON_RESOURCE", "INSUFFICIENT_STORAGE", "INTERNAL_SERVER_ERROR", "I_AM_A_TEAPOT", "LENGTH_REQUIRED", "LOCKED", "LOOP_DETECTED", "METHOD_FAILURE", "METHOD_NOT_ALLOWED", "MOVED_PERMANENTLY", "MOVED_TEMPORARILY", "MULTIPLE_CHOICES", "MULTI_STATUS", "NETWORK_AUTHENTICATION_REQUIRED", "NON_AUTHORITATIVE_INFORMATION", "NOT_ACCEPTABLE", "NOT_EXTENDED", "NOT_FOUND", "NOT_IMPLEMENTED", "NOT_MODIFIED", "NO_CONTENT", "OK", "PARTIAL_CONTENT", "PAYLOAD_TOO_LARGE", "PAYMENT_REQUIRED", "PERMANENT_REDIRECT", "PRECONDITION_FAILED", "PRECONDITION_REQUIRED", "PROCESSING", "PROXY_AUTHENTICATION_REQUIRED", "REQUESTED_RANGE_NOT_SATISFIABLE", "REQUEST_ENTITY_TOO_LARGE", "REQUEST_HEADER_FIELDS_TOO_LARGE", "REQUEST_TIMEOUT", "REQUEST_URI_TOO_LONG", "RESET_CONTENT", "SEE_OTHER", "SERVICE_UNAVAILABLE", "SWITCHING_PROTOCOLS", "TEMPORARY_REDIRECT", "TOO_EARLY", "TOO_MANY_REQUESTS", "UNAUTHORIZED", "UNAVAILABLE_FOR_LEGAL_REASONS", "UNPROCESSABLE_ENTITY", "UNSUPPORTED_MEDIA_TYPE", "UPGRADE_REQUIRED", "URI_TOO_LONG", "USE_PROXY", "VARIANT_ALSO_NEGOTIATES"]  # noqa: E501
        if status_code not in allowed_values:
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

    @property
    def status_code_value(self):
        """Gets the status_code_value of this ResponseEntity.  # noqa: E501


        :return: The status_code_value of this ResponseEntity.  # noqa: E501
        :rtype: int
        """
        return self._status_code_value

    @status_code_value.setter
    def status_code_value(self, status_code_value):
        """Sets the status_code_value of this ResponseEntity.


        :param status_code_value: The status_code_value of this ResponseEntity.  # noqa: E501
        :type: int
        """

        self._status_code_value = status_code_value

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
        if issubclass(ResponseEntity, dict):
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
        if not isinstance(other, ResponseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
