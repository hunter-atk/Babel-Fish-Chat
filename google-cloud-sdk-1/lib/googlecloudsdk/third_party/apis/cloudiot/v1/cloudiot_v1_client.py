"""Generated client library for cloudiot version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudiot.v1 import cloudiot_v1_messages as messages


class CloudiotV1(base_api.BaseApiClient):
  """Generated client library for service cloudiot version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudiot.googleapis.com/'

  _PACKAGE = u'cloudiot'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloudiot']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudiotV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudiot handle."""
    url = url or self.BASE_URL
    super(CloudiotV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_registries_devices_configVersions = self.ProjectsLocationsRegistriesDevicesConfigVersionsService(self)
    self.projects_locations_registries_devices_states = self.ProjectsLocationsRegistriesDevicesStatesService(self)
    self.projects_locations_registries_devices = self.ProjectsLocationsRegistriesDevicesService(self)
    self.projects_locations_registries_groups_devices_configVersions = self.ProjectsLocationsRegistriesGroupsDevicesConfigVersionsService(self)
    self.projects_locations_registries_groups_devices_states = self.ProjectsLocationsRegistriesGroupsDevicesStatesService(self)
    self.projects_locations_registries_groups_devices = self.ProjectsLocationsRegistriesGroupsDevicesService(self)
    self.projects_locations_registries_groups = self.ProjectsLocationsRegistriesGroupsService(self)
    self.projects_locations_registries = self.ProjectsLocationsRegistriesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsRegistriesDevicesConfigVersionsService(base_api.BaseApiService):
    """Service class for the projects_locations_registries_devices_configVersions resource."""

    _NAME = u'projects_locations_registries_devices_configVersions'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesDevicesConfigVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the last few versions of the device configuration in descending.
order (i.e.: newest first).

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesConfigVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeviceConfigVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices/{devicesId}/configVersions',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.devices.configVersions.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'numVersions'],
        relative_path=u'v1/{+name}/configVersions',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesConfigVersionsListRequest',
        response_type_name=u'ListDeviceConfigVersionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistriesDevicesStatesService(base_api.BaseApiService):
    """Service class for the projects_locations_registries_devices_states resource."""

    _NAME = u'projects_locations_registries_devices_states'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesDevicesStatesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the last few versions of the device state in descending order (i.e.:.
newest first).

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesStatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeviceStatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices/{devicesId}/states',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.devices.states.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'numStates'],
        relative_path=u'v1/{+name}/states',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesStatesListRequest',
        response_type_name=u'ListDeviceStatesResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistriesDevicesService(base_api.BaseApiService):
    """Service class for the projects_locations_registries_devices resource."""

    _NAME = u'projects_locations_registries_devices'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesDevicesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a device in a device registry.

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Device) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.devices.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/devices',
        request_field=u'device',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesCreateRequest',
        response_type_name=u'Device',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a device.

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices/{devicesId}',
        http_method=u'DELETE',
        method_id=u'cloudiot.projects.locations.registries.devices.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details about a device.

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Device) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices/{devicesId}',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.devices.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'fieldMask'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesGetRequest',
        response_type_name=u'Device',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List devices in a device registry.

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDevicesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.devices.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'deviceIds', u'deviceNumIds', u'fieldMask', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/devices',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesListRequest',
        response_type_name=u'ListDevicesResponse',
        supports_download=False,
    )

    def ModifyCloudToDeviceConfig(self, request, global_params=None):
      r"""Modifies the configuration for the device, which is eventually sent from.
the Cloud IoT Core servers. Returns the modified configuration version and
its metadata.

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesModifyCloudToDeviceConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceConfig) The response message.
      """
      config = self.GetMethodConfig('ModifyCloudToDeviceConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    ModifyCloudToDeviceConfig.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices/{devicesId}:modifyCloudToDeviceConfig',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.devices.modifyCloudToDeviceConfig',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:modifyCloudToDeviceConfig',
        request_field=u'modifyCloudToDeviceConfigRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesModifyCloudToDeviceConfigRequest',
        response_type_name=u'DeviceConfig',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a device.

      Args:
        request: (CloudiotProjectsLocationsRegistriesDevicesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Device) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/devices/{devicesId}',
        http_method=u'PATCH',
        method_id=u'cloudiot.projects.locations.registries.devices.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'device',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDevicesPatchRequest',
        response_type_name=u'Device',
        supports_download=False,
    )

  class ProjectsLocationsRegistriesGroupsDevicesConfigVersionsService(base_api.BaseApiService):
    """Service class for the projects_locations_registries_groups_devices_configVersions resource."""

    _NAME = u'projects_locations_registries_groups_devices_configVersions'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesGroupsDevicesConfigVersionsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the last few versions of the device configuration in descending.
order (i.e.: newest first).

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsDevicesConfigVersionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeviceConfigVersionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}/devices/{devicesId}/configVersions',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.groups.devices.configVersions.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'numVersions'],
        relative_path=u'v1/{+name}/configVersions',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsDevicesConfigVersionsListRequest',
        response_type_name=u'ListDeviceConfigVersionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistriesGroupsDevicesStatesService(base_api.BaseApiService):
    """Service class for the projects_locations_registries_groups_devices_states resource."""

    _NAME = u'projects_locations_registries_groups_devices_states'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesGroupsDevicesStatesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Lists the last few versions of the device state in descending order (i.e.:.
newest first).

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsDevicesStatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeviceStatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}/devices/{devicesId}/states',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.groups.devices.states.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'numStates'],
        relative_path=u'v1/{+name}/states',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsDevicesStatesListRequest',
        response_type_name=u'ListDeviceStatesResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistriesGroupsDevicesService(base_api.BaseApiService):
    """Service class for the projects_locations_registries_groups_devices resource."""

    _NAME = u'projects_locations_registries_groups_devices'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesGroupsDevicesService, self).__init__(client)
      self._upload_configs = {
          }

    def Delete(self, request, global_params=None):
      r"""Deletes a device.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsDevicesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}/devices/{devicesId}',
        http_method=u'DELETE',
        method_id=u'cloudiot.projects.locations.registries.groups.devices.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsDevicesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details about a device.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsDevicesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Device) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}/devices/{devicesId}',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.groups.devices.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'fieldMask'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsDevicesGetRequest',
        response_type_name=u'Device',
        supports_download=False,
    )

    def ModifyCloudToDeviceConfig(self, request, global_params=None):
      r"""Modifies the configuration for the device, which is eventually sent from.
the Cloud IoT Core servers. Returns the modified configuration version and
its metadata.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsDevicesModifyCloudToDeviceConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceConfig) The response message.
      """
      config = self.GetMethodConfig('ModifyCloudToDeviceConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    ModifyCloudToDeviceConfig.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}/devices/{devicesId}:modifyCloudToDeviceConfig',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.groups.devices.modifyCloudToDeviceConfig',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:modifyCloudToDeviceConfig',
        request_field=u'modifyCloudToDeviceConfigRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsDevicesModifyCloudToDeviceConfigRequest',
        response_type_name=u'DeviceConfig',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a device.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsDevicesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Device) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}/devices/{devicesId}',
        http_method=u'PATCH',
        method_id=u'cloudiot.projects.locations.registries.groups.devices.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'device',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsDevicesPatchRequest',
        response_type_name=u'Device',
        supports_download=False,
    )

  class ProjectsLocationsRegistriesGroupsService(base_api.BaseApiService):
    """Service class for the projects_locations_registries_groups resource."""

    _NAME = u'projects_locations_registries_groups'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesGroupsService, self).__init__(client)
      self._upload_configs = {
          }

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.groups.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.groups.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGroupsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}/groups/{groupsId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.groups.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGroupsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsRegistriesService(base_api.BaseApiService):
    """Service class for the projects_locations_registries resource."""

    _NAME = u'projects_locations_registries'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsRegistriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a device registry that contains devices.

      Args:
        request: (CloudiotProjectsLocationsRegistriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceRegistry) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1/{+parent}/registries',
        request_field=u'deviceRegistry',
        request_type_name=u'CloudiotProjectsLocationsRegistriesCreateRequest',
        response_type_name=u'DeviceRegistry',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a device registry configuration.

      Args:
        request: (CloudiotProjectsLocationsRegistriesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}',
        http_method=u'DELETE',
        method_id=u'cloudiot.projects.locations.registries.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a device registry configuration.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceRegistry) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGetRequest',
        response_type_name=u'DeviceRegistry',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (CloudiotProjectsLocationsRegistriesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}:getIamPolicy',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:getIamPolicy',
        request_field=u'getIamPolicyRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists device registries.

      Args:
        request: (CloudiotProjectsLocationsRegistriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeviceRegistriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries',
        http_method=u'GET',
        method_id=u'cloudiot.projects.locations.registries.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1/{+parent}/registries',
        request_field='',
        request_type_name=u'CloudiotProjectsLocationsRegistriesListRequest',
        response_type_name=u'ListDeviceRegistriesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a device registry configuration.

      Args:
        request: (CloudiotProjectsLocationsRegistriesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceRegistry) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}',
        http_method=u'PATCH',
        method_id=u'cloudiot.projects.locations.registries.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1/{+name}',
        request_field=u'deviceRegistry',
        request_type_name=u'CloudiotProjectsLocationsRegistriesPatchRequest',
        response_type_name=u'DeviceRegistry',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

      Args:
        request: (CloudiotProjectsLocationsRegistriesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

      Args:
        request: (CloudiotProjectsLocationsRegistriesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/projects/{projectsId}/locations/{locationsId}/registries/{registriesId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'cloudiot.projects.locations.registries.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'CloudiotProjectsLocationsRegistriesTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(CloudiotV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudiotV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
