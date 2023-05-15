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

class ReportConfig(object):
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
        'base_url': 'str',
        'dashboard_id': 'str',
        'name_pattern': 'str',
        'state': 'str',
        'timewindow': 'JsonNode',
        'timezone': 'str',
        'type': 'str',
        'use_current_user_credentials': 'bool',
        'use_dashboard_timewindow': 'bool',
        'user_id': 'str'
    }

    attribute_map = {
        'base_url': 'baseUrl',
        'dashboard_id': 'dashboardId',
        'name_pattern': 'namePattern',
        'state': 'state',
        'timewindow': 'timewindow',
        'timezone': 'timezone',
        'type': 'type',
        'use_current_user_credentials': 'useCurrentUserCredentials',
        'use_dashboard_timewindow': 'useDashboardTimewindow',
        'user_id': 'userId'
    }

    def __init__(self, base_url=None, dashboard_id=None, name_pattern=None, state=None, timewindow=None, timezone=None, type=None, use_current_user_credentials=None, use_dashboard_timewindow=None, user_id=None):  # noqa: E501
        """ReportConfig - a model defined in Swagger"""  # noqa: E501
        self._base_url = None
        self._dashboard_id = None
        self._name_pattern = None
        self._state = None
        self._timewindow = None
        self._timezone = None
        self._type = None
        self._use_current_user_credentials = None
        self._use_dashboard_timewindow = None
        self._user_id = None
        self.discriminator = None
        if base_url is not None:
            self.base_url = base_url
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if name_pattern is not None:
            self.name_pattern = name_pattern
        if state is not None:
            self.state = state
        if timewindow is not None:
            self.timewindow = timewindow
        if timezone is not None:
            self.timezone = timezone
        if type is not None:
            self.type = type
        if use_current_user_credentials is not None:
            self.use_current_user_credentials = use_current_user_credentials
        if use_dashboard_timewindow is not None:
            self.use_dashboard_timewindow = use_dashboard_timewindow
        if user_id is not None:
            self.user_id = user_id

    @property
    def base_url(self):
        """Gets the base_url of this ReportConfig.  # noqa: E501


        :return: The base_url of this ReportConfig.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this ReportConfig.


        :param base_url: The base_url of this ReportConfig.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this ReportConfig.  # noqa: E501


        :return: The dashboard_id of this ReportConfig.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this ReportConfig.


        :param dashboard_id: The dashboard_id of this ReportConfig.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def name_pattern(self):
        """Gets the name_pattern of this ReportConfig.  # noqa: E501


        :return: The name_pattern of this ReportConfig.  # noqa: E501
        :rtype: str
        """
        return self._name_pattern

    @name_pattern.setter
    def name_pattern(self, name_pattern):
        """Sets the name_pattern of this ReportConfig.


        :param name_pattern: The name_pattern of this ReportConfig.  # noqa: E501
        :type: str
        """

        self._name_pattern = name_pattern

    @property
    def state(self):
        """Gets the state of this ReportConfig.  # noqa: E501


        :return: The state of this ReportConfig.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ReportConfig.


        :param state: The state of this ReportConfig.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def timewindow(self):
        """Gets the timewindow of this ReportConfig.  # noqa: E501


        :return: The timewindow of this ReportConfig.  # noqa: E501
        :rtype: JsonNode
        """
        return self._timewindow

    @timewindow.setter
    def timewindow(self, timewindow):
        """Sets the timewindow of this ReportConfig.


        :param timewindow: The timewindow of this ReportConfig.  # noqa: E501
        :type: JsonNode
        """

        self._timewindow = timewindow

    @property
    def timezone(self):
        """Gets the timezone of this ReportConfig.  # noqa: E501


        :return: The timezone of this ReportConfig.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ReportConfig.


        :param timezone: The timezone of this ReportConfig.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def type(self):
        """Gets the type of this ReportConfig.  # noqa: E501


        :return: The type of this ReportConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReportConfig.


        :param type: The type of this ReportConfig.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def use_current_user_credentials(self):
        """Gets the use_current_user_credentials of this ReportConfig.  # noqa: E501


        :return: The use_current_user_credentials of this ReportConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_current_user_credentials

    @use_current_user_credentials.setter
    def use_current_user_credentials(self, use_current_user_credentials):
        """Sets the use_current_user_credentials of this ReportConfig.


        :param use_current_user_credentials: The use_current_user_credentials of this ReportConfig.  # noqa: E501
        :type: bool
        """

        self._use_current_user_credentials = use_current_user_credentials

    @property
    def use_dashboard_timewindow(self):
        """Gets the use_dashboard_timewindow of this ReportConfig.  # noqa: E501


        :return: The use_dashboard_timewindow of this ReportConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_dashboard_timewindow

    @use_dashboard_timewindow.setter
    def use_dashboard_timewindow(self, use_dashboard_timewindow):
        """Sets the use_dashboard_timewindow of this ReportConfig.


        :param use_dashboard_timewindow: The use_dashboard_timewindow of this ReportConfig.  # noqa: E501
        :type: bool
        """

        self._use_dashboard_timewindow = use_dashboard_timewindow

    @property
    def user_id(self):
        """Gets the user_id of this ReportConfig.  # noqa: E501


        :return: The user_id of this ReportConfig.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ReportConfig.


        :param user_id: The user_id of this ReportConfig.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(ReportConfig, dict):
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
        if not isinstance(other, ReportConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
