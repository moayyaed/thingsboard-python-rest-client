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
from tb_rest_client.models.models_pe.event_filter import EventFilter  # noqa: F401,E501

class LifeCycleEventFilter(EventFilter):
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
        'not_empty': 'bool',
        'event_type': 'str',
        'server': 'str',
        'event': 'str',
        'status': 'str',
        'error_str': 'str'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'not_empty': 'notEmpty',
        'event_type': 'eventType',
        'server': 'server',
        'event': 'event',
        'status': 'status',
        'error_str': 'errorStr'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, not_empty=None, event_type=None, server=None, event=None, status=None, error_str=None, *args, **kwargs):  # noqa: E501
        """LifeCycleEventFilter - a model defined in Swagger"""  # noqa: E501
        self._not_empty = None
        self._event_type = None
        self._server = None
        self._event = None
        self._status = None
        self._error_str = None
        self.discriminator = None
        if not_empty is not None:
            self.not_empty = not_empty
        self.event_type = event_type
        if server is not None:
            self.server = server
        if event is not None:
            self.event = event
        if status is not None:
            self.status = status
        if error_str is not None:
            self.error_str = error_str
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def not_empty(self):
        """Gets the not_empty of this LifeCycleEventFilter.  # noqa: E501


        :return: The not_empty of this LifeCycleEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._not_empty

    @not_empty.setter
    def not_empty(self, not_empty):
        """Sets the not_empty of this LifeCycleEventFilter.


        :param not_empty: The not_empty of this LifeCycleEventFilter.  # noqa: E501
        :type: bool
        """

        self._not_empty = not_empty

    @property
    def event_type(self):
        """Gets the event_type of this LifeCycleEventFilter.  # noqa: E501

        String value representing the event type  # noqa: E501

        :return: The event_type of this LifeCycleEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this LifeCycleEventFilter.

        String value representing the event type  # noqa: E501

        :param event_type: The event_type of this LifeCycleEventFilter.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEBUG_CONVERTER", "DEBUG_INTEGRATION", "DEBUG_RULE_CHAIN", "DEBUG_RULE_NODE", "ERROR", "LC_EVENT", "RAW_DATA", "STATS"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def server(self):
        """Gets the server of this LifeCycleEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this LifeCycleEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this LifeCycleEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this LifeCycleEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def event(self):
        """Gets the event of this LifeCycleEventFilter.  # noqa: E501

        String value representing the lifecycle event type  # noqa: E501

        :return: The event of this LifeCycleEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this LifeCycleEventFilter.

        String value representing the lifecycle event type  # noqa: E501

        :param event: The event of this LifeCycleEventFilter.  # noqa: E501
        :type: str
        """

        self._event = event

    @property
    def status(self):
        """Gets the status of this LifeCycleEventFilter.  # noqa: E501

        String value representing status of the lifecycle event  # noqa: E501

        :return: The status of this LifeCycleEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LifeCycleEventFilter.

        String value representing status of the lifecycle event  # noqa: E501

        :param status: The status of this LifeCycleEventFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["Failure", "Success"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def error_str(self):
        """Gets the error_str of this LifeCycleEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :return: The error_str of this LifeCycleEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._error_str

    @error_str.setter
    def error_str(self, error_str):
        """Sets the error_str of this LifeCycleEventFilter.

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :param error_str: The error_str of this LifeCycleEventFilter.  # noqa: E501
        :type: str
        """

        self._error_str = error_str

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
        if issubclass(LifeCycleEventFilter, dict):
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
        if not isinstance(other, LifeCycleEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
