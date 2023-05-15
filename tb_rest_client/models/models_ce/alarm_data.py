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

class AlarmData(object):
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
        'entity_id': 'EntityId',
        'latest': 'dict(str, object)',
        'id': 'AlarmId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'name': 'str',
        'type': 'str',
        'originator': 'EntityId',
        'severity': 'str',
        'acknowledged': 'bool',
        'cleared': 'bool',
        'assignee_id': 'UserId',
        'start_ts': 'int',
        'end_ts': 'int',
        'ack_ts': 'int',
        'clear_ts': 'int',
        'assign_ts': 'int',
        'details': 'JsonNode',
        'propagate': 'bool',
        'originator_name': 'str',
        'propagate_to_owner': 'bool',
        'originator_label': 'str',
        'propagate_to_tenant': 'bool',
        'assignee': 'AlarmAssignee',
        'propagate_relation_types': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'latest': 'latest',
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'type': 'type',
        'originator': 'originator',
        'severity': 'severity',
        'acknowledged': 'acknowledged',
        'cleared': 'cleared',
        'assignee_id': 'assigneeId',
        'start_ts': 'startTs',
        'end_ts': 'endTs',
        'ack_ts': 'ackTs',
        'clear_ts': 'clearTs',
        'assign_ts': 'assignTs',
        'details': 'details',
        'propagate': 'propagate',
        'originator_name': 'originatorName',
        'propagate_to_owner': 'propagateToOwner',
        'originator_label': 'originatorLabel',
        'propagate_to_tenant': 'propagateToTenant',
        'assignee': 'assignee',
        'propagate_relation_types': 'propagateRelationTypes',
        'status': 'status'
    }

    def __init__(self, entity_id=None, latest=None, id=None, created_time=None, tenant_id=None, customer_id=None, name=None, type=None, originator=None, severity=None, acknowledged=None, cleared=None, assignee_id=None, start_ts=None, end_ts=None, ack_ts=None, clear_ts=None, assign_ts=None, details=None, propagate=None, originator_name=None, propagate_to_owner=None, originator_label=None, propagate_to_tenant=None, assignee=None, propagate_relation_types=None, status=None):  # noqa: E501
        """AlarmData - a model defined in Swagger"""  # noqa: E501
        self._entity_id = None
        self._latest = None
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._type = None
        self._originator = None
        self._severity = None
        self._acknowledged = None
        self._cleared = None
        self._assignee_id = None
        self._start_ts = None
        self._end_ts = None
        self._ack_ts = None
        self._clear_ts = None
        self._assign_ts = None
        self._details = None
        self._propagate = None
        self._originator_name = None
        self._propagate_to_owner = None
        self._originator_label = None
        self._propagate_to_tenant = None
        self._assignee = None
        self._propagate_relation_types = None
        self._status = None
        self.discriminator = None
        if entity_id is not None:
            self.entity_id = entity_id
        if latest is not None:
            self.latest = latest
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.name = name
        self.type = type
        self.originator = originator
        self.severity = severity
        self.acknowledged = acknowledged
        self.cleared = cleared
        if assignee_id is not None:
            self.assignee_id = assignee_id
        if start_ts is not None:
            self.start_ts = start_ts
        if end_ts is not None:
            self.end_ts = end_ts
        if ack_ts is not None:
            self.ack_ts = ack_ts
        if clear_ts is not None:
            self.clear_ts = clear_ts
        if assign_ts is not None:
            self.assign_ts = assign_ts
        if details is not None:
            self.details = details
        if propagate is not None:
            self.propagate = propagate
        if originator_name is not None:
            self.originator_name = originator_name
        if propagate_to_owner is not None:
            self.propagate_to_owner = propagate_to_owner
        if originator_label is not None:
            self.originator_label = originator_label
        if propagate_to_tenant is not None:
            self.propagate_to_tenant = propagate_to_tenant
        if assignee is not None:
            self.assignee = assignee
        if propagate_relation_types is not None:
            self.propagate_relation_types = propagate_relation_types
        self.status = status

    @property
    def entity_id(self):
        """Gets the entity_id of this AlarmData.  # noqa: E501


        :return: The entity_id of this AlarmData.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this AlarmData.


        :param entity_id: The entity_id of this AlarmData.  # noqa: E501
        :type: EntityId
        """

        self._entity_id = entity_id

    @property
    def latest(self):
        """Gets the latest of this AlarmData.  # noqa: E501


        :return: The latest of this AlarmData.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """Sets the latest of this AlarmData.


        :param latest: The latest of this AlarmData.  # noqa: E501
        :type: dict(str, object)
        """

        self._latest = latest

    @property
    def id(self):
        """Gets the id of this AlarmData.  # noqa: E501


        :return: The id of this AlarmData.  # noqa: E501
        :rtype: AlarmId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlarmData.


        :param id: The id of this AlarmData.  # noqa: E501
        :type: AlarmId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this AlarmData.  # noqa: E501

        Timestamp of the alarm creation, in milliseconds  # noqa: E501

        :return: The created_time of this AlarmData.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AlarmData.

        Timestamp of the alarm creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this AlarmData.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AlarmData.  # noqa: E501


        :return: The tenant_id of this AlarmData.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AlarmData.


        :param tenant_id: The tenant_id of this AlarmData.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this AlarmData.  # noqa: E501


        :return: The customer_id of this AlarmData.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AlarmData.


        :param customer_id: The customer_id of this AlarmData.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this AlarmData.  # noqa: E501

        representing type of the Alarm  # noqa: E501

        :return: The name of this AlarmData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlarmData.

        representing type of the Alarm  # noqa: E501

        :param name: The name of this AlarmData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this AlarmData.  # noqa: E501

        representing type of the Alarm  # noqa: E501

        :return: The type of this AlarmData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlarmData.

        representing type of the Alarm  # noqa: E501

        :param type: The type of this AlarmData.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def originator(self):
        """Gets the originator of this AlarmData.  # noqa: E501


        :return: The originator of this AlarmData.  # noqa: E501
        :rtype: EntityId
        """
        return self._originator

    @originator.setter
    def originator(self, originator):
        """Sets the originator of this AlarmData.


        :param originator: The originator of this AlarmData.  # noqa: E501
        :type: EntityId
        """
        if originator is None:
            raise ValueError("Invalid value for `originator`, must not be `None`")  # noqa: E501

        self._originator = originator

    @property
    def severity(self):
        """Gets the severity of this AlarmData.  # noqa: E501

        Alarm severity  # noqa: E501

        :return: The severity of this AlarmData.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this AlarmData.

        Alarm severity  # noqa: E501

        :param severity: The severity of this AlarmData.  # noqa: E501
        :type: str
        """
        if severity is None:
            raise ValueError("Invalid value for `severity`, must not be `None`")  # noqa: E501
        allowed_values = ["CRITICAL", "INDETERMINATE", "MAJOR", "MINOR", "WARNING"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def acknowledged(self):
        """Gets the acknowledged of this AlarmData.  # noqa: E501

        Acknowledged  # noqa: E501

        :return: The acknowledged of this AlarmData.  # noqa: E501
        :rtype: bool
        """
        return self._acknowledged

    @acknowledged.setter
    def acknowledged(self, acknowledged):
        """Sets the acknowledged of this AlarmData.

        Acknowledged  # noqa: E501

        :param acknowledged: The acknowledged of this AlarmData.  # noqa: E501
        :type: bool
        """
        if acknowledged is None:
            raise ValueError("Invalid value for `acknowledged`, must not be `None`")  # noqa: E501

        self._acknowledged = acknowledged

    @property
    def cleared(self):
        """Gets the cleared of this AlarmData.  # noqa: E501

        Cleared  # noqa: E501

        :return: The cleared of this AlarmData.  # noqa: E501
        :rtype: bool
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this AlarmData.

        Cleared  # noqa: E501

        :param cleared: The cleared of this AlarmData.  # noqa: E501
        :type: bool
        """
        if cleared is None:
            raise ValueError("Invalid value for `cleared`, must not be `None`")  # noqa: E501

        self._cleared = cleared

    @property
    def assignee_id(self):
        """Gets the assignee_id of this AlarmData.  # noqa: E501


        :return: The assignee_id of this AlarmData.  # noqa: E501
        :rtype: UserId
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        """Sets the assignee_id of this AlarmData.


        :param assignee_id: The assignee_id of this AlarmData.  # noqa: E501
        :type: UserId
        """

        self._assignee_id = assignee_id

    @property
    def start_ts(self):
        """Gets the start_ts of this AlarmData.  # noqa: E501

        Timestamp of the alarm start time, in milliseconds  # noqa: E501

        :return: The start_ts of this AlarmData.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this AlarmData.

        Timestamp of the alarm start time, in milliseconds  # noqa: E501

        :param start_ts: The start_ts of this AlarmData.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this AlarmData.  # noqa: E501

        Timestamp of the alarm end time(last time update), in milliseconds  # noqa: E501

        :return: The end_ts of this AlarmData.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this AlarmData.

        Timestamp of the alarm end time(last time update), in milliseconds  # noqa: E501

        :param end_ts: The end_ts of this AlarmData.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def ack_ts(self):
        """Gets the ack_ts of this AlarmData.  # noqa: E501

        Timestamp of the alarm acknowledgement, in milliseconds  # noqa: E501

        :return: The ack_ts of this AlarmData.  # noqa: E501
        :rtype: int
        """
        return self._ack_ts

    @ack_ts.setter
    def ack_ts(self, ack_ts):
        """Sets the ack_ts of this AlarmData.

        Timestamp of the alarm acknowledgement, in milliseconds  # noqa: E501

        :param ack_ts: The ack_ts of this AlarmData.  # noqa: E501
        :type: int
        """

        self._ack_ts = ack_ts

    @property
    def clear_ts(self):
        """Gets the clear_ts of this AlarmData.  # noqa: E501

        Timestamp of the alarm clearing, in milliseconds  # noqa: E501

        :return: The clear_ts of this AlarmData.  # noqa: E501
        :rtype: int
        """
        return self._clear_ts

    @clear_ts.setter
    def clear_ts(self, clear_ts):
        """Sets the clear_ts of this AlarmData.

        Timestamp of the alarm clearing, in milliseconds  # noqa: E501

        :param clear_ts: The clear_ts of this AlarmData.  # noqa: E501
        :type: int
        """

        self._clear_ts = clear_ts

    @property
    def assign_ts(self):
        """Gets the assign_ts of this AlarmData.  # noqa: E501

        Timestamp of the alarm assignment, in milliseconds  # noqa: E501

        :return: The assign_ts of this AlarmData.  # noqa: E501
        :rtype: int
        """
        return self._assign_ts

    @assign_ts.setter
    def assign_ts(self, assign_ts):
        """Sets the assign_ts of this AlarmData.

        Timestamp of the alarm assignment, in milliseconds  # noqa: E501

        :param assign_ts: The assign_ts of this AlarmData.  # noqa: E501
        :type: int
        """

        self._assign_ts = assign_ts

    @property
    def details(self):
        """Gets the details of this AlarmData.  # noqa: E501


        :return: The details of this AlarmData.  # noqa: E501
        :rtype: JsonNode
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AlarmData.


        :param details: The details of this AlarmData.  # noqa: E501
        :type: JsonNode
        """

        self._details = details

    @property
    def propagate(self):
        """Gets the propagate of this AlarmData.  # noqa: E501

        Propagation flag to specify if alarm should be propagated to parent entities of alarm originator  # noqa: E501

        :return: The propagate of this AlarmData.  # noqa: E501
        :rtype: bool
        """
        return self._propagate

    @propagate.setter
    def propagate(self, propagate):
        """Sets the propagate of this AlarmData.

        Propagation flag to specify if alarm should be propagated to parent entities of alarm originator  # noqa: E501

        :param propagate: The propagate of this AlarmData.  # noqa: E501
        :type: bool
        """

        self._propagate = propagate

    @property
    def originator_name(self):
        """Gets the originator_name of this AlarmData.  # noqa: E501

        Alarm originator name  # noqa: E501

        :return: The originator_name of this AlarmData.  # noqa: E501
        :rtype: str
        """
        return self._originator_name

    @originator_name.setter
    def originator_name(self, originator_name):
        """Sets the originator_name of this AlarmData.

        Alarm originator name  # noqa: E501

        :param originator_name: The originator_name of this AlarmData.  # noqa: E501
        :type: str
        """

        self._originator_name = originator_name

    @property
    def propagate_to_owner(self):
        """Gets the propagate_to_owner of this AlarmData.  # noqa: E501

        Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator  # noqa: E501

        :return: The propagate_to_owner of this AlarmData.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_to_owner

    @propagate_to_owner.setter
    def propagate_to_owner(self, propagate_to_owner):
        """Sets the propagate_to_owner of this AlarmData.

        Propagation flag to specify if alarm should be propagated to the owner (tenant or customer) of alarm originator  # noqa: E501

        :param propagate_to_owner: The propagate_to_owner of this AlarmData.  # noqa: E501
        :type: bool
        """

        self._propagate_to_owner = propagate_to_owner

    @property
    def originator_label(self):
        """Gets the originator_label of this AlarmData.  # noqa: E501

        Alarm originator label  # noqa: E501

        :return: The originator_label of this AlarmData.  # noqa: E501
        :rtype: str
        """
        return self._originator_label

    @originator_label.setter
    def originator_label(self, originator_label):
        """Sets the originator_label of this AlarmData.

        Alarm originator label  # noqa: E501

        :param originator_label: The originator_label of this AlarmData.  # noqa: E501
        :type: str
        """

        self._originator_label = originator_label

    @property
    def propagate_to_tenant(self):
        """Gets the propagate_to_tenant of this AlarmData.  # noqa: E501

        Propagation flag to specify if alarm should be propagated to the tenant entity  # noqa: E501

        :return: The propagate_to_tenant of this AlarmData.  # noqa: E501
        :rtype: bool
        """
        return self._propagate_to_tenant

    @propagate_to_tenant.setter
    def propagate_to_tenant(self, propagate_to_tenant):
        """Sets the propagate_to_tenant of this AlarmData.

        Propagation flag to specify if alarm should be propagated to the tenant entity  # noqa: E501

        :param propagate_to_tenant: The propagate_to_tenant of this AlarmData.  # noqa: E501
        :type: bool
        """

        self._propagate_to_tenant = propagate_to_tenant

    @property
    def assignee(self):
        """Gets the assignee of this AlarmData.  # noqa: E501


        :return: The assignee of this AlarmData.  # noqa: E501
        :rtype: AlarmAssignee
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this AlarmData.


        :param assignee: The assignee of this AlarmData.  # noqa: E501
        :type: AlarmAssignee
        """

        self._assignee = assignee

    @property
    def propagate_relation_types(self):
        """Gets the propagate_relation_types of this AlarmData.  # noqa: E501

        JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored.  # noqa: E501

        :return: The propagate_relation_types of this AlarmData.  # noqa: E501
        :rtype: list[str]
        """
        return self._propagate_relation_types

    @propagate_relation_types.setter
    def propagate_relation_types(self, propagate_relation_types):
        """Sets the propagate_relation_types of this AlarmData.

        JSON array of relation types that should be used for propagation. By default, 'propagateRelationTypes' array is empty which means that the alarm will be propagated based on any relation type to parent entities. This parameter should be used only in case when 'propagate' parameter is set to true, otherwise, 'propagateRelationTypes' array will be ignored.  # noqa: E501

        :param propagate_relation_types: The propagate_relation_types of this AlarmData.  # noqa: E501
        :type: list[str]
        """

        self._propagate_relation_types = propagate_relation_types

    @property
    def status(self):
        """Gets the status of this AlarmData.  # noqa: E501

        status of the Alarm  # noqa: E501

        :return: The status of this AlarmData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AlarmData.

        status of the Alarm  # noqa: E501

        :param status: The status of this AlarmData.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE_ACK", "ACTIVE_UNACK", "CLEARED_ACK", "CLEARED_UNACK"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(AlarmData, dict):
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
        if not isinstance(other, AlarmData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
