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

from .default_device_profile_transport_configuration import DefaultDeviceProfileTransportConfiguration
from .json_node import JsonNode
from .merged_user_permissions import MergedUserPermissions
from .page_data_edge import PageDataEdge
from .tenant_solution_template_info import TenantSolutionTemplateInfo
from .admin_settings_id import AdminSettingsId
from .entity_data import EntityData
from .login_response import LoginResponse
from .event_id import EventId
from .scheduler_event_info import SchedulerEventInfo
from .test_sms_request import TestSmsRequest
from .ota_package import OtaPackage
from .group_permission import GroupPermission
from .user import User
from .o_auth2_mobile_info import OAuth2MobileInfo
from .numeric_filter_predicate import NumericFilterPredicate
from .device_profile_alarm import DeviceProfileAlarm
from .ota_package_info import OtaPackageInfo
from .alarm_data import AlarmData
from .entity_id import EntityId
from .complex_filter_predicate import ComplexFilterPredicate
from .edge_id import EdgeId
from .device_profile_data import DeviceProfileData
from .allowed_permissions_info import AllowedPermissionsInfo
from .device_group_ota_package import DeviceGroupOtaPackage
from .login_white_labeling_params import LoginWhiteLabelingParams
from .sign_up_request import SignUpRequest
from .share_group_request import ShareGroupRequest
from .save_ota_package_info_request import SaveOtaPackageInfoRequest
from .mqtt_device_transport_configuration import MqttDeviceTransportConfiguration
from .bulk_import_result_device import BulkImportResultDevice
from .device_search_query_filter import DeviceSearchQueryFilter
from .byte_buffer import ByteBuffer
from .edge import Edge
from .scheduler_event_with_customer_info import SchedulerEventWithCustomerInfo
from .entity_relations_query import EntityRelationsQuery
from .sms_provider_configuration import SmsProviderConfiguration
from .entity_relation_info import EntityRelationInfo
from .component_descriptor import ComponentDescriptor
from .short_customer_info import ShortCustomerInfo
from .duration_alarm_condition_spec import DurationAlarmConditionSpec
from .group_permission_id import GroupPermissionId
from .o_auth2_registration_info import OAuth2RegistrationInfo
from .twilio_sms_provider_configuration import TwilioSmsProviderConfiguration
from .page_data_converter import PageDataConverter
from .lw_m2m_resource_observe import LwM2mResourceObserve
from .default_tenant_profile_configuration import DefaultTenantProfileConfiguration
from .role_id import RoleId
from .check_pre_provisioned_devices_device_profile_provision_configuration import \
    CheckPreProvisionedDevicesDeviceProfileProvisionConfiguration
from .alarm_info import AlarmInfo
from .debug_converter_event_filter import DebugConverterEventFilter
from .o_auth2_client_info import OAuth2ClientInfo
from .boolean_filter_predicate import BooleanFilterPredicate
from .rule_chain_id import RuleChainId
from .admin_settings import AdminSettings
from .o_auth2_client_registration_template import OAuth2ClientRegistrationTemplate
from .rule_node import RuleNode
from .other_configuration import OtherConfiguration
from .device_data import DeviceData
from .page_data_integration import PageDataIntegration
from .proto_transport_payload_configuration import ProtoTransportPayloadConfiguration
from .dashboard_id import DashboardId
from .change_password_request import ChangePasswordRequest
from .tenant_profile_data import TenantProfileData
from .shared_attributes_setting_snmp_communication_config import SharedAttributesSettingSnmpCommunicationConfig
from .sign_up_self_registration_params import SignUpSelfRegistrationParams
from .report_config import ReportConfig
from .o_auth2_custom_mapper_config import OAuth2CustomMapperConfig
from .update_message import UpdateMessage
from .power_saving_configuration import PowerSavingConfiguration
from .entity_group_filter import EntityGroupFilter
from .ota_package_id import OtaPackageId
from .error_event_filter import ErrorEventFilter
from .page_data_short_entity_view import PageDataShortEntityView
from .alarm_schedule import AlarmSchedule
from .user_id import UserId
from .entity_group_list_filter import EntityGroupListFilter
from .integration_id import IntegrationId
from .asset_type_filter import AssetTypeFilter
from .statistics_event_filter import StatisticsEventFilter
from .page_data_entity_group_info import PageDataEntityGroupInfo
from .api_usage_state_filter import ApiUsageStateFilter
from .merged_group_permission_info import MergedGroupPermissionInfo
from .widgets_bundle_id import WidgetsBundleId
from .atomic_integer import AtomicInteger
from .security_settings import SecuritySettings
from .event_filter import EventFilter
from .lw_m2m_object import LwM2mObject
from .edge_search_query import EdgeSearchQuery
from .page_data_scheduler_event_info import PageDataSchedulerEventInfo
from .state_entity_owner_filter import StateEntityOwnerFilter
from .o_auth2_params_info import OAuth2ParamsInfo
from .entity_view_id import EntityViewId
from .alarm_condition_filter_key import AlarmConditionFilterKey
from .merged_group_type_permission_info import MergedGroupTypePermissionInfo
from .device_transport_configuration import DeviceTransportConfiguration
from .page_data_role import PageDataRole
from .alarm_condition_filter import AlarmConditionFilter
from .alarm import Alarm
from .attributes_entity_view import AttributesEntityView
from .login_request import LoginRequest
from .device_profile_provision_configuration import DeviceProfileProvisionConfiguration
from .specific_time_schedule import SpecificTimeSchedule
from .favicon import Favicon
from .o_auth2_info import OAuth2Info
from .activate_user_request import ActivateUserRequest
from .converter import Converter
from .resource import Resource
from .subscription_usage import SubscriptionUsage
from .default_device_transport_configuration import DefaultDeviceTransportConfiguration
from .entity_group_id import EntityGroupId
from .telemetry_mapping_configuration import TelemetryMappingConfiguration
from .default_device_profile_configuration import DefaultDeviceProfileConfiguration
from .any_time_schedule import AnyTimeSchedule
from .allow_create_new_devices_device_profile_provision_configuration import \
    AllowCreateNewDevicesDeviceProfileProvisionConfiguration
from .to_device_rpc_request_snmp_communication_config import ToDeviceRpcRequestSnmpCommunicationConfig
from .default_device_configuration import DefaultDeviceConfiguration
from .widget_type_info import WidgetTypeInfo
from .entity_name_filter import EntityNameFilter
from .tb_resource_id import TbResourceId
from .efento_coap_device_type_configuration import EfentoCoapDeviceTypeConfiguration
from .edge_event import EdgeEvent
from .page_data_rule_chain import PageDataRuleChain
from .customer_id import CustomerId
from .snmp_device_transport_configuration import SnmpDeviceTransportConfiguration
from .short_entity_view import ShortEntityView
from .alarm_rule import AlarmRule
from .key_filter import KeyFilter
from .client_attributes_querying_snmp_communication_config import ClientAttributesQueryingSnmpCommunicationConfig
from .rule_chain_import_result import RuleChainImportResult
from .custom_menu_item import CustomMenuItem
from .role import Role
from .entity_group_info import EntityGroupInfo
from .input_stream import InputStream
from .edge_type_filter import EdgeTypeFilter
from .palette import Palette
from .object_node import ObjectNode
from .device_configuration import DeviceConfiguration
from .entity_subtype import EntitySubtype
from .entity_key import EntityKey
from .integration import Integration
from .device_type_filter import DeviceTypeFilter
from .edge_search_query_filter import EdgeSearchQueryFilter
from .save_device_with_credentials_request import SaveDeviceWithCredentialsRequest
from .bulk_import_result_edge import BulkImportResultEdge
from .lwm2m_device_transport_configuration import Lwm2mDeviceTransportConfiguration
from .palette_settings import PaletteSettings
from .response_entity import ResponseEntity
from .entity_list_filter import EntityListFilter
from .entity_type_filter import EntityTypeFilter
from .custom_time_schedule import CustomTimeSchedule
from .tenant_solution_template_instructions import TenantSolutionTemplateInstructions
from .snmp_communication_config import SnmpCommunicationConfig
from .rule_chain_meta_data import RuleChainMetaData
from .bulk_import_result_asset import BulkImportResultAsset
from .edge_event_id import EdgeEventId
from .column_mapping import ColumnMapping
from .claim_request import ClaimRequest
from .widget_type_id import WidgetTypeId
from .custom_menu import CustomMenu
from .relations_search_parameters import RelationsSearchParameters
from .thingsboard_credentials_expired_response import ThingsboardCredentialsExpiredResponse
from .o_auth2_basic_mapper_config import OAuth2BasicMapperConfig
from .simple_alarm_condition_spec import SimpleAlarmConditionSpec
from .rpc import Rpc
from .group_permission_info import GroupPermissionInfo
from .rpc_id import RpcId
from .default_rule_chain_create_request import DefaultRuleChainCreateRequest
from .transport_payload_type_configuration import TransportPayloadTypeConfiguration
from .entity_group import EntityGroup
from .ts_value import TsValue
from .solution_install_response import SolutionInstallResponse
from .telemetry_querying_snmp_communication_config import TelemetryQueryingSnmpCommunicationConfig
from .device_profile_configuration import DeviceProfileConfiguration
from .entity_group_name_filter import EntityGroupNameFilter
from .entity_data_query import EntityDataQuery
from .custom_translation import CustomTranslation
from .entity_count_query import EntityCountQuery
from .entity_view_search_query import EntityViewSearchQuery
from .o_auth2_domain_info import OAuth2DomainInfo
from .bulk_import_request import BulkImportRequest
from .node_connection_info import NodeConnectionInfo
from .entity_data_page_link import EntityDataPageLink
from .thingsboard_error_response import ThingsboardErrorResponse
from .coap_device_transport_configuration import CoapDeviceTransportConfiguration
from .string_filter_predicate import StringFilterPredicate
from .snmp_mapping import SnmpMapping
from .mqtt_device_profile_transport_configuration import MqttDeviceProfileTransportConfiguration
from .telemetry_entity_view import TelemetryEntityView
from .single_entity_filter import SingleEntityFilter
from .entity_view_search_query_filter import EntityViewSearchQueryFilter
from .disabled_device_profile_provision_configuration import DisabledDeviceProfileProvisionConfiguration
from .asset_search_query import AssetSearchQuery
from .entity_filter import EntityFilter
from .debug_integration_event_filter import DebugIntegrationEventFilter
from .entity_view_type_filter import EntityViewTypeFilter
from .tenant_profile_configuration import TenantProfileConfiguration
from .device_profile_transport_configuration import DeviceProfileTransportConfiguration
from .object_attributes import ObjectAttributes
from .relation_entity_type_filter import RelationEntityTypeFilter
from .asset_search_query_filter import AssetSearchQueryFilter
from .reset_password_email_request import ResetPasswordEmailRequest
from .tenant_solution_template_details import TenantSolutionTemplateDetails
from .tenant_profile_id import TenantProfileId
from .blob_entity_id import BlobEntityId
from .key_filter_predicate import KeyFilterPredicate
from .o_auth2_mapper_config import OAuth2MapperConfig
from .default_coap_device_type_configuration import DefaultCoapDeviceTypeConfiguration
from .snmp_device_profile_transport_configuration import SnmpDeviceProfileTransportConfiguration
from .life_cycle_event_filter import LifeCycleEventFilter
from .blob_entity_with_customer_info import BlobEntityWithCustomerInfo
from .relations_query_filter import RelationsQueryFilter
from .alarm_condition import AlarmCondition
from .self_registration_params import SelfRegistrationParams
from .rule_chain_data import RuleChainData
from .lw_m2m_instance import LwM2mInstance
from .repeating_alarm_condition_spec import RepeatingAlarmConditionSpec
from .custom_time_schedule_item import CustomTimeScheduleItem
from .mapping import Mapping
from .user_password_policy import UserPasswordPolicy
from .page_data_edge_event import PageDataEdgeEvent
from .device_id import DeviceId
from .converter_id import ConverterId
from .aws_sns_sms_provider_configuration import AwsSnsSmsProviderConfiguration
from .scheduler_event import SchedulerEvent
from .lwm2m_device_profile_transport_configuration import Lwm2mDeviceProfileTransportConfiguration
from .page_data_blob_entity_with_customer_info import PageDataBlobEntityWithCustomerInfo
from .component_descriptor_id import ComponentDescriptorId
from .o_auth2_client_registration_template_id import OAuth2ClientRegistrationTemplateId
from .alarm_id import AlarmId
from .audit_log import AuditLog
from .scheduler_event_id import SchedulerEventId
from .alarm_data_page_link import AlarmDataPageLink
from .device_search_query import DeviceSearchQuery
from .alarm_data_query import AlarmDataQuery
from .alarm_condition_spec import AlarmConditionSpec
from .coap_device_type_configuration import CoapDeviceTypeConfiguration
from .reset_password_request import ResetPasswordRequest
from .white_labeling_params import WhiteLabelingParams
from .asset_id import AssetId
from .tb_resource import TbResource
from .blob_entity_info import BlobEntityInfo
from .device_credentials_id import DeviceCredentialsId
from .rule_node_id import RuleNodeId
from .rule_chain_connection_info import RuleChainConnectionInfo
from .audit_log_id import AuditLogId
from .device_profile_id import DeviceProfileId
from .coap_device_profile_transport_configuration import CoapDeviceProfileTransportConfiguration
from .json_transport_payload_configuration import JsonTransportPayloadConfiguration
from .entity_data_sort_order import EntityDataSortOrder
from .page_data_ota_package_info import PageDataOtaPackageInfo
from .page_data_contact_basedobject import PageDataContactBasedobject
from .rule_chain import RuleChain
from .entities_by_group_name_filter import EntitiesByGroupNameFilter
from .version_create_request import VersionCreateRequest
from .two_fa_provider_config import TwoFaProviderConfig
from .version_load_request import VersionLoadRequest
from .lw_m2_m_bootstrap_server_credential import LwM2MBootstrapServerCredential
from .two_fa_account_config import TwoFaAccountConfig
from .version_load_result import VersionLoadResult
from .deferred_result_list_branch_info import DeferredResultListBranchInfo
from .deferred_result_page_data_entity_version import DeferredResultPageDataEntityVersion
from .deferred_result_entity_data_info import DeferredResultEntityDataInfo
from .version_creation_result import VersionCreationResult
from .deferred_result_list_versioned_entity_info import DeferredResultListVersionedEntityInfo
from .deferred_result_entity_data_diff import DeferredResultEntityDataDiff
from .entity_version import EntityVersion
from .entity_type_load_result import EntityTypeLoadResult
from .complex_version_create_request import ComplexVersionCreateRequest
from .version_load_config import VersionLoadConfig
from .single_entity_version_load_request import SingleEntityVersionLoadRequest
from .entity_type_version_load_request import EntityTypeVersionLoadRequest
from .version_create_config import VersionCreateConfig
from .single_entity_version_create_request import SingleEntityVersionCreateRequest
from .entity_type_version_create_config import EntityTypeVersionCreateConfig
from .entity_type_version_load_config import EntityTypeVersionLoadConfig
from .repository_settings import RepositorySettings
from .deferred_result_repository_settings import DeferredResultRepositorySettings
from .deferred_result_void import DeferredResultVoid
from .auto_version_create_config import AutoVersionCreateConfig
from .platform_two_fa_settings import PlatformTwoFaSettings
from .account_two_fa_settings import AccountTwoFaSettings
from .two_fa_account_config_update_request import TwoFaAccountConfigUpdateRequest
from .two_fa_provider_info import TwoFaProviderInfo
from .entity_load_error import EntityLoadError
from .array_node import ArrayNode
from .integration_info import IntegrationInfo
from .page_data_integration_info import PageDataIntegrationInfo
from .raw_data_event_filter import RawDataEventFilter
from .rule_node_debug_event_filter import RuleNodeDebugEventFilter
from .scheduler_event_filter import SchedulerEventFilter
from .affected_tenant_administrators_filter import AffectedTenantAdministratorsFilter
from .affected_user_filter import AffectedUserFilter
from .alarm_assignee import AlarmAssignee
from .alarm_assignment_notification_rule_trigger_config import AlarmAssignmentNotificationRuleTriggerConfig
from .alarm_comment import AlarmComment
from .alarm_comment_id import AlarmCommentId
from .alarm_comment_info import AlarmCommentInfo
from .alarm_comment_notification_rule_trigger_config import AlarmCommentNotificationRuleTriggerConfig
from .alarm_count_query import AlarmCountQuery
from .alarm_comment_notification_rule_trigger_config import AlarmCommentNotificationRuleTriggerConfig
from .all_users_filter import AllUsersFilter
from .api_usage_limit_notification_rule_trigger_config import ApiUsageLimitNotificationRuleTriggerConfig
from .asset_info import AssetInfo
from .asset_profile_id import AssetProfileId
from .clear_rule import ClearRule
from .comparison_ts_value import ComparisonTsValue
from .customer_info import CustomerInfo
from .customer_users_filter import CustomerUsersFilter
from .delivery_method_notification_template import DeliveryMethodNotificationTemplate
from .device_activity_notification_rule_trigger_config import DeviceActivityNotificationRuleTriggerConfig
from .device_info import DeviceInfo
from .edge_info import EdgeInfo
from .email_delivery_method_notification_template import EmailDeliveryMethodNotificationTemplate
from .entities_limit_notification_rule_trigger_config import EntitiesLimitNotificationRuleTriggerConfig
from .entity_action_notification_rule_trigger_config import EntityActionNotificationRuleTriggerConfig
from .entity_view_info import EntityViewInfo
from .escalated_notification_rule_recipients_config import EscalatedNotificationRuleRecipientsConfig
from .event_info import EventInfo
from .features_info import FeaturesInfo
from .integration_lifecycle_event_notification_rule_trigger_config import IntegrationLifecycleEventNotificationRuleTriggerConfig  # noqa: E501
from .last_visited_dashboard_info import LastVisitedDashboardInfo
from .license_usage_info import LicenseUsageInfo
from .new_platform_version_notification_rule_trigger_config import NewPlatformVersionNotificationRuleTriggerConfig
from .notification import Notification
from .notification_delivery_method_config import NotificationDeliveryMethodConfig
from .notification_id import NotificationId
from .notification_info import NotificationInfo
from .notification_request import NotificationRequest
from .notification_request_config import NotificationRequestConfig
from .notification_request_id import NotificationRequestId
from .notification_request_preview import NotificationRequestPreview
from .notification_request_stats import NotificationRequestStats
from .notification_rule_config import NotificationRuleConfig
from .notification_rule_id import NotificationRuleId
from .notification_rule_recipients_config import NotificationRuleRecipientsConfig
from .notification_template_config import NotificationTemplateConfig
from .notification_template_id import NotificationTemplateId
from .originator_entity_owner_users_filter import OriginatorEntityOwnerUsersFilter
from .page_data_customer_info import PageDataCustomerInfo
from .page_data_edge_info import PageDataEdgeInfo
from .page_data_entity_view_info import PageDataEntityViewInfo
from .page_data_event_info import PageDataEventInfo
from .page_data_user_email_info import PageDataUserEmailInfo
from .page_data_user_info import PageDataUserInfo
from .platform_users_notification_target_config import PlatformUsersNotificationTargetConfig
from .psklw_m2_m_bootstrap_server_credential import PSKLwM2MBootstrapServerCredential
from .repository_settings import RepositorySettings
from .rpklw_m2_m_bootstrap_server_credential import RPKLwM2MBootstrapServerCredential
from .rule_chain_debug_event_filter import RuleChainDebugEventFilter
from .rule_engine_component_lifecycle_event_notification_rule_trigger_config import RuleEngineComponentLifecycleEventNotificationRuleTriggerConfig  # noqa: E501
from .slack_conversation import SlackConversation
from .slack_delivery_method_notification_template import SlackDeliveryMethodNotificationTemplate
from .slack_notification_delivery_method_config import SlackNotificationDeliveryMethodConfig
from .slack_notification_target_config import SlackNotificationTargetConfig
from .sms_delivery_method_notification_template import SmsDeliveryMethodNotificationTemplate
from .starred_dashboard_info import StarredDashboardInfo
from .system_administrators_filter import SystemAdministratorsFilter
from .system_info import SystemInfo
from .system_info_data import SystemInfoData
from .tenant_administrators_filter import TenantAdministratorsFilter
from .user_dashboards_info import UserDashboardsInfo
from .user_email_info import UserEmailInfo
from .user_group_list_filter import UserGroupListFilter
from .user_info import UserInfo
from .user_list_filter import UserListFilter
from .user_role_filter import UserRoleFilter
from .users_filter import UsersFilter
from .web_delivery_method_notification_template import WebDeliveryMethodNotificationTemplate
from .x509_certificate_chain_provision_configuration import X509CertificateChainProvisionConfiguration
from .contact_based_object import ContactBasedObject
from .locale_code_upload_body import LocaleCodeUploadBody
from .mobile_app_settings_id import MobileAppSettingsId
from .translation_info import TranslationInfo
from .alarm_notification_rule_trigger_config import AlarmNotificationRuleTriggerConfig
from .converters_info import ConvertersInfo
from .custom_menu_info import CustomMenuInfo
from .custom_menu_delete_result import CustomMenuDeleteResult
from .custom_menu_id import CustomMenuId
from .custom_menu_config import CustomMenuConfig
from .default_menu_item import DefaultMenuItem
from .home_menu_item import HomeMenuItem
from .integration_converters_info import IntegrationConvertersInfo
from .menu_item import MenuItem
from .model import Model
from .captcha_params import CaptchaParams
from .default_dashboard_params import DefaultDashboardParams
from .enterprise_captcha_params import EnterpriseCaptchaParams
from .entity_export_data_object import EntityExportDataObject
from .mobile_self_registration_params import MobileSelfRegistrationParams
from .mobile_redirect_params import MobileRedirectParams
from .notification_rule_trigger_config import NotificationRuleTriggerConfig
from .sign_up_field import SignUpField
from .task_processing_failure_notification_rule_trigger_config import TaskProcessingFailureNotificationRuleTriggerConfig
from .v2_captcha_params import V2CaptchaParams
from .v3_captcha_params import V3CaptchaParams
from .web_self_registration_params import WebSelfRegistrationParams
