# coding: utf-8

# flake8: noqa
"""
    FastReport Cloud

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from fastreport_cloud_sdk.models.admin_export_folder_create_vm import AdminExportFolderCreateVM
from fastreport_cloud_sdk.models.admin_folder_create_vm import AdminFolderCreateVM
from fastreport_cloud_sdk.models.admin_report_folder_create_vm import AdminReportFolderCreateVM
from fastreport_cloud_sdk.models.admin_subscription_vm import AdminSubscriptionVM
from fastreport_cloud_sdk.models.admin_template_folder_create_vm import AdminTemplateFolderCreateVM
from fastreport_cloud_sdk.models.api_key_vm import ApiKeyVM
from fastreport_cloud_sdk.models.api_keys_vm import ApiKeysVM
from fastreport_cloud_sdk.models.app_mixins import AppMixins
from fastreport_cloud_sdk.models.audit_action_vm import AuditActionVM
from fastreport_cloud_sdk.models.audit_actions_vm import AuditActionsVM
from fastreport_cloud_sdk.models.audit_file_property_changed_vm import AuditFilePropertyChangedVM
from fastreport_cloud_sdk.models.audit_subscription_action_vm import AuditSubscriptionActionVM
from fastreport_cloud_sdk.models.audit_type import AuditType
from fastreport_cloud_sdk.models.auth_config_vm import AuthConfigVM
from fastreport_cloud_sdk.models.breadcrumbs_model import BreadcrumbsModel
from fastreport_cloud_sdk.models.breadcrumbs_vm import BreadcrumbsVM
from fastreport_cloud_sdk.models.count_vm import CountVM
from fastreport_cloud_sdk.models.create_api_key_vm import CreateApiKeyVM
from fastreport_cloud_sdk.models.create_data_source_admin_vm import CreateDataSourceAdminVM
from fastreport_cloud_sdk.models.create_data_source_vm import CreateDataSourceVM
from fastreport_cloud_sdk.models.create_email_task_vm import CreateEmailTaskVM
from fastreport_cloud_sdk.models.create_endpoint_vm import CreateEndpointVM
from fastreport_cloud_sdk.models.create_export_report_task_vm import CreateExportReportTaskVM
from fastreport_cloud_sdk.models.create_export_template_task_vm import CreateExportTemplateTaskVM
from fastreport_cloud_sdk.models.create_fetch_task_vm import CreateFetchTaskVM
from fastreport_cloud_sdk.models.create_group_admin_vm import CreateGroupAdminVM
from fastreport_cloud_sdk.models.create_group_vm import CreateGroupVM
from fastreport_cloud_sdk.models.create_prepare_template_task_vm import CreatePrepareTemplateTaskVM
from fastreport_cloud_sdk.models.create_subscription_invite_vm import CreateSubscriptionInviteVM
from fastreport_cloud_sdk.models.create_task_base_vm import CreateTaskBaseVM
from fastreport_cloud_sdk.models.create_thumbnail_report_task_vm import CreateThumbnailReportTaskVM
from fastreport_cloud_sdk.models.create_thumbnail_template_task_vm import CreateThumbnailTemplateTaskVM
from fastreport_cloud_sdk.models.create_transform_task_base_vm import CreateTransformTaskBaseVM
from fastreport_cloud_sdk.models.create_transport_task_base_vm import CreateTransportTaskBaseVM
from fastreport_cloud_sdk.models.create_webhook_task_vm import CreateWebhookTaskVM
from fastreport_cloud_sdk.models.data_source_administrate import DataSourceAdministrate
from fastreport_cloud_sdk.models.data_source_connection_type import DataSourceConnectionType
from fastreport_cloud_sdk.models.data_source_create import DataSourceCreate
from fastreport_cloud_sdk.models.data_source_create_data_source_get_data_source_update_data_source_delete_data_source_execute_data_source_administrate_permission import DataSourceCreateDataSourceGetDataSourceUpdateDataSourceDeleteDataSourceExecuteDataSourceAdministratePermission
from fastreport_cloud_sdk.models.data_source_delete import DataSourceDelete
from fastreport_cloud_sdk.models.data_source_execute import DataSourceExecute
from fastreport_cloud_sdk.models.data_source_get import DataSourceGet
from fastreport_cloud_sdk.models.data_source_permission import DataSourcePermission
from fastreport_cloud_sdk.models.data_source_permission_data_source_create_data_source_get_data_source_update_data_source_delete_data_source_execute_data_source_administrate_permissions import DataSourcePermissionDataSourceCreateDataSourceGetDataSourceUpdateDataSourceDeleteDataSourceExecuteDataSourceAdministratePermissions
from fastreport_cloud_sdk.models.data_source_permissions import DataSourcePermissions
from fastreport_cloud_sdk.models.data_source_permissions_vm import DataSourcePermissionsVM
from fastreport_cloud_sdk.models.data_source_sorting import DataSourceSorting
from fastreport_cloud_sdk.models.data_source_status import DataSourceStatus
from fastreport_cloud_sdk.models.data_source_update import DataSourceUpdate
from fastreport_cloud_sdk.models.data_source_vm import DataSourceVM
from fastreport_cloud_sdk.models.data_sources_vm import DataSourcesVM
from fastreport_cloud_sdk.models.default_permissions_vm import DefaultPermissionsVM
from fastreport_cloud_sdk.models.delete_api_key_vm import DeleteApiKeyVM
from fastreport_cloud_sdk.models.email_task_vm import EmailTaskVM
from fastreport_cloud_sdk.models.endpoint_vm import EndpointVM
from fastreport_cloud_sdk.models.entity_vm import EntityVM
from fastreport_cloud_sdk.models.export_create_admin_vm import ExportCreateAdminVM
from fastreport_cloud_sdk.models.export_create_vm import ExportCreateVM
from fastreport_cloud_sdk.models.export_folder_create_vm import ExportFolderCreateVM
from fastreport_cloud_sdk.models.export_format import ExportFormat
from fastreport_cloud_sdk.models.export_report_task_vm import ExportReportTaskVM
from fastreport_cloud_sdk.models.export_report_vm import ExportReportVM
from fastreport_cloud_sdk.models.export_template_task_vm import ExportTemplateTaskVM
from fastreport_cloud_sdk.models.export_template_vm import ExportTemplateVM
from fastreport_cloud_sdk.models.export_vm import ExportVM
from fastreport_cloud_sdk.models.export_vm_files_vm_base import ExportVMFilesVMBase
from fastreport_cloud_sdk.models.exports_vm import ExportsVM
from fastreport_cloud_sdk.models.fetch_task_vm import FetchTaskVM
from fastreport_cloud_sdk.models.file_administrate import FileAdministrate
from fastreport_cloud_sdk.models.file_create import FileCreate
from fastreport_cloud_sdk.models.file_create_file_get_file_update_file_delete_file_execute_file_administrate_permission import FileCreateFileGetFileUpdateFileDeleteFileExecuteFileAdministratePermission
from fastreport_cloud_sdk.models.file_create_vm import FileCreateVM
from fastreport_cloud_sdk.models.file_delete import FileDelete
from fastreport_cloud_sdk.models.file_execute import FileExecute
from fastreport_cloud_sdk.models.file_get import FileGet
from fastreport_cloud_sdk.models.file_icon_vm import FileIconVM
from fastreport_cloud_sdk.models.file_kind import FileKind
from fastreport_cloud_sdk.models.file_permission import FilePermission
from fastreport_cloud_sdk.models.file_permission_file_create_file_get_file_update_file_delete_file_execute_file_administrate_permissions import FilePermissionFileCreateFileGetFileUpdateFileDeleteFileExecuteFileAdministratePermissions
from fastreport_cloud_sdk.models.file_permissions import FilePermissions
from fastreport_cloud_sdk.models.file_permissions_vm import FilePermissionsVM
from fastreport_cloud_sdk.models.file_rename_vm import FileRenameVM
from fastreport_cloud_sdk.models.file_sorting import FileSorting
from fastreport_cloud_sdk.models.file_status import FileStatus
from fastreport_cloud_sdk.models.file_status_reason import FileStatusReason
from fastreport_cloud_sdk.models.file_tags_update_vm import FileTagsUpdateVM
from fastreport_cloud_sdk.models.file_type import FileType
from fastreport_cloud_sdk.models.file_update import FileUpdate
from fastreport_cloud_sdk.models.file_vm import FileVM
from fastreport_cloud_sdk.models.file_vm_files_vm_base import FileVMFilesVMBase
from fastreport_cloud_sdk.models.files_vm import FilesVM
from fastreport_cloud_sdk.models.folder_create_vm import FolderCreateVM
from fastreport_cloud_sdk.models.folder_icon_vm import FolderIconVM
from fastreport_cloud_sdk.models.folder_rename_vm import FolderRenameVM
from fastreport_cloud_sdk.models.folder_tags_update_vm import FolderTagsUpdateVM
from fastreport_cloud_sdk.models.frontend_app import FrontendApp
from fastreport_cloud_sdk.models.group_administrate import GroupAdministrate
from fastreport_cloud_sdk.models.group_create import GroupCreate
from fastreport_cloud_sdk.models.group_create_group_get_group_update_group_delete_group_execute_group_administrate_permission import GroupCreateGroupGetGroupUpdateGroupDeleteGroupExecuteGroupAdministratePermission
from fastreport_cloud_sdk.models.group_delete import GroupDelete
from fastreport_cloud_sdk.models.group_execute import GroupExecute
from fastreport_cloud_sdk.models.group_get import GroupGet
from fastreport_cloud_sdk.models.group_permission import GroupPermission
from fastreport_cloud_sdk.models.group_permission_group_create_group_get_group_update_group_delete_group_execute_group_administrate_permissions import GroupPermissionGroupCreateGroupGetGroupUpdateGroupDeleteGroupExecuteGroupAdministratePermissions
from fastreport_cloud_sdk.models.group_permissions import GroupPermissions
from fastreport_cloud_sdk.models.group_permissions_vm import GroupPermissionsVM
from fastreport_cloud_sdk.models.group_update import GroupUpdate
from fastreport_cloud_sdk.models.group_user_vm import GroupUserVM
from fastreport_cloud_sdk.models.group_users_vm import GroupUsersVM
from fastreport_cloud_sdk.models.group_vm import GroupVM
from fastreport_cloud_sdk.models.groups_vm import GroupsVM
from fastreport_cloud_sdk.models.input_file_vm import InputFileVM
from fastreport_cloud_sdk.models.invited_user import InvitedUser
from fastreport_cloud_sdk.models.my_permissions_vm import MyPermissionsVM
from fastreport_cloud_sdk.models.output_file_vm import OutputFileVM
from fastreport_cloud_sdk.models.prepare_template_task_vm import PrepareTemplateTaskVM
from fastreport_cloud_sdk.models.prepare_template_vm import PrepareTemplateVM
from fastreport_cloud_sdk.models.problem_details import ProblemDetails
from fastreport_cloud_sdk.models.profile_visibility import ProfileVisibility
from fastreport_cloud_sdk.models.rename_data_source_vm import RenameDataSourceVM
from fastreport_cloud_sdk.models.rename_group_vm import RenameGroupVM
from fastreport_cloud_sdk.models.rename_subscription_vm import RenameSubscriptionVM
from fastreport_cloud_sdk.models.report_create_admin_vm import ReportCreateAdminVM
from fastreport_cloud_sdk.models.report_create_vm import ReportCreateVM
from fastreport_cloud_sdk.models.report_folder_create_vm import ReportFolderCreateVM
from fastreport_cloud_sdk.models.report_info import ReportInfo
from fastreport_cloud_sdk.models.report_vm import ReportVM
from fastreport_cloud_sdk.models.report_vm_files_vm_base import ReportVMFilesVMBase
from fastreport_cloud_sdk.models.reports_vm import ReportsVM
from fastreport_cloud_sdk.models.run_email_task_vm import RunEmailTaskVM
from fastreport_cloud_sdk.models.run_endpoint_vm import RunEndpointVM
from fastreport_cloud_sdk.models.run_export_report_task_vm import RunExportReportTaskVM
from fastreport_cloud_sdk.models.run_export_template_task_vm import RunExportTemplateTaskVM
from fastreport_cloud_sdk.models.run_fetch_task_vm import RunFetchTaskVM
from fastreport_cloud_sdk.models.run_input_file_vm import RunInputFileVM
from fastreport_cloud_sdk.models.run_prepare_template_task_vm import RunPrepareTemplateTaskVM
from fastreport_cloud_sdk.models.run_task_base_vm import RunTaskBaseVM
from fastreport_cloud_sdk.models.run_thumbnail_report_task_vm import RunThumbnailReportTaskVM
from fastreport_cloud_sdk.models.run_thumbnail_template_task_vm import RunThumbnailTemplateTaskVM
from fastreport_cloud_sdk.models.run_transform_task_base_vm import RunTransformTaskBaseVM
from fastreport_cloud_sdk.models.run_transport_task_base_vm import RunTransportTaskBaseVM
from fastreport_cloud_sdk.models.run_webhook_task_vm import RunWebhookTaskVM
from fastreport_cloud_sdk.models.save_mode import SaveMode
from fastreport_cloud_sdk.models.server_configuration_vm import ServerConfigurationVM
from fastreport_cloud_sdk.models.subscription_administrate import SubscriptionAdministrate
from fastreport_cloud_sdk.models.subscription_create import SubscriptionCreate
from fastreport_cloud_sdk.models.subscription_create_subscription_get_subscription_update_subscription_delete_subscription_execute_subscription_administrate_permission import SubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermission
from fastreport_cloud_sdk.models.subscription_delete import SubscriptionDelete
from fastreport_cloud_sdk.models.subscription_execute import SubscriptionExecute
from fastreport_cloud_sdk.models.subscription_folder import SubscriptionFolder
from fastreport_cloud_sdk.models.subscription_get import SubscriptionGet
from fastreport_cloud_sdk.models.subscription_invite_vm import SubscriptionInviteVM
from fastreport_cloud_sdk.models.subscription_invites_vm import SubscriptionInvitesVM
from fastreport_cloud_sdk.models.subscription_period_vm import SubscriptionPeriodVM
from fastreport_cloud_sdk.models.subscription_permission import SubscriptionPermission
from fastreport_cloud_sdk.models.subscription_permission_subscription_create_subscription_get_subscription_update_subscription_delete_subscription_execute_subscription_administrate_permissions import SubscriptionPermissionSubscriptionCreateSubscriptionGetSubscriptionUpdateSubscriptionDeleteSubscriptionExecuteSubscriptionAdministratePermissions
from fastreport_cloud_sdk.models.subscription_permissions import SubscriptionPermissions
from fastreport_cloud_sdk.models.subscription_permissions_vm import SubscriptionPermissionsVM
from fastreport_cloud_sdk.models.subscription_plan_vm import SubscriptionPlanVM
from fastreport_cloud_sdk.models.subscription_plans_vm import SubscriptionPlansVM
from fastreport_cloud_sdk.models.subscription_update import SubscriptionUpdate
from fastreport_cloud_sdk.models.subscription_user_vm import SubscriptionUserVM
from fastreport_cloud_sdk.models.subscription_users_vm import SubscriptionUsersVM
from fastreport_cloud_sdk.models.subscription_vm import SubscriptionVM
from fastreport_cloud_sdk.models.subscriptions_vm import SubscriptionsVM
from fastreport_cloud_sdk.models.task_administrate import TaskAdministrate
from fastreport_cloud_sdk.models.task_base_vm import TaskBaseVM
from fastreport_cloud_sdk.models.task_create import TaskCreate
from fastreport_cloud_sdk.models.task_create_task_get_task_update_task_delete_task_execute_task_administrate_permission import TaskCreateTaskGetTaskUpdateTaskDeleteTaskExecuteTaskAdministratePermission
from fastreport_cloud_sdk.models.task_delete import TaskDelete
from fastreport_cloud_sdk.models.task_execute import TaskExecute
from fastreport_cloud_sdk.models.task_get import TaskGet
from fastreport_cloud_sdk.models.task_permission import TaskPermission
from fastreport_cloud_sdk.models.task_permission_task_create_task_get_task_update_task_delete_task_execute_task_administrate_permissions import TaskPermissionTaskCreateTaskGetTaskUpdateTaskDeleteTaskExecuteTaskAdministratePermissions
from fastreport_cloud_sdk.models.task_permissions import TaskPermissions
from fastreport_cloud_sdk.models.task_permissions_vm import TaskPermissionsVM
from fastreport_cloud_sdk.models.task_settings_vm import TaskSettingsVM
from fastreport_cloud_sdk.models.task_type import TaskType
from fastreport_cloud_sdk.models.task_update import TaskUpdate
from fastreport_cloud_sdk.models.tasks_vm import TasksVM
from fastreport_cloud_sdk.models.template_create_admin_vm import TemplateCreateAdminVM
from fastreport_cloud_sdk.models.template_create_vm import TemplateCreateVM
from fastreport_cloud_sdk.models.template_folder_create_vm import TemplateFolderCreateVM
from fastreport_cloud_sdk.models.template_vm import TemplateVM
from fastreport_cloud_sdk.models.template_vm_files_vm_base import TemplateVMFilesVMBase
from fastreport_cloud_sdk.models.templates_vm import TemplatesVM
from fastreport_cloud_sdk.models.thumbnail_report_task_vm import ThumbnailReportTaskVM
from fastreport_cloud_sdk.models.thumbnail_template_task_vm import ThumbnailTemplateTaskVM
from fastreport_cloud_sdk.models.time_period_type import TimePeriodType
from fastreport_cloud_sdk.models.transform_task_base_vm import TransformTaskBaseVM
from fastreport_cloud_sdk.models.transport_task_base_vm import TransportTaskBaseVM
from fastreport_cloud_sdk.models.update_data_source_connection_string_vm import UpdateDataSourceConnectionStringVM
from fastreport_cloud_sdk.models.update_data_source_permissions_vm import UpdateDataSourcePermissionsVM
from fastreport_cloud_sdk.models.update_data_source_subscription_vm import UpdateDataSourceSubscriptionVM
from fastreport_cloud_sdk.models.update_default_permissions_vm import UpdateDefaultPermissionsVM
from fastreport_cloud_sdk.models.update_email_task_vm import UpdateEmailTaskVM
from fastreport_cloud_sdk.models.update_endpoint_vm import UpdateEndpointVM
from fastreport_cloud_sdk.models.update_export_report_task_vm import UpdateExportReportTaskVM
from fastreport_cloud_sdk.models.update_export_template_task_vm import UpdateExportTemplateTaskVM
from fastreport_cloud_sdk.models.update_fetch_task_vm import UpdateFetchTaskVM
from fastreport_cloud_sdk.models.update_file_content_vm import UpdateFileContentVM
from fastreport_cloud_sdk.models.update_file_permissions_vm import UpdateFilePermissionsVM
from fastreport_cloud_sdk.models.update_group_permissions_vm import UpdateGroupPermissionsVM
from fastreport_cloud_sdk.models.update_prepare_template_task_vm import UpdatePrepareTemplateTaskVM
from fastreport_cloud_sdk.models.update_subscription_locale_vm import UpdateSubscriptionLocaleVM
from fastreport_cloud_sdk.models.update_subscription_permissions_vm import UpdateSubscriptionPermissionsVM
from fastreport_cloud_sdk.models.update_task_base_vm import UpdateTaskBaseVM
from fastreport_cloud_sdk.models.update_task_permissions_vm import UpdateTaskPermissionsVM
from fastreport_cloud_sdk.models.update_thumbnail_report_task_vm import UpdateThumbnailReportTaskVM
from fastreport_cloud_sdk.models.update_thumbnail_template_task_vm import UpdateThumbnailTemplateTaskVM
from fastreport_cloud_sdk.models.update_transform_task_base_vm import UpdateTransformTaskBaseVM
from fastreport_cloud_sdk.models.update_transport_task_base_vm import UpdateTransportTaskBaseVM
from fastreport_cloud_sdk.models.update_user_profile_vm import UpdateUserProfileVM
from fastreport_cloud_sdk.models.update_user_settings_vm import UpdateUserSettingsVM
from fastreport_cloud_sdk.models.update_webhook_task_vm import UpdateWebhookTaskVM
from fastreport_cloud_sdk.models.user_profile_vm import UserProfileVM
from fastreport_cloud_sdk.models.user_settings_vm import UserSettingsVM
from fastreport_cloud_sdk.models.validation_problem_details import ValidationProblemDetails
from fastreport_cloud_sdk.models.webhook_task_vm import WebhookTaskVM
