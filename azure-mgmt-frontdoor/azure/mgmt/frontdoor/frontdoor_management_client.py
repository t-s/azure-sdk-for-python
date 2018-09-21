# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling
import uuid
from .operations.front_doors_operations import FrontDoorsOperations
from .operations.routing_rules_operations import RoutingRulesOperations
from .operations.health_probe_settings_operations import HealthProbeSettingsOperations
from .operations.load_balancing_settings_operations import LoadBalancingSettingsOperations
from .operations.backend_pools_operations import BackendPoolsOperations
from .operations.frontend_endpoints_operations import FrontendEndpointsOperations
from .operations.endpoints_operations import EndpointsOperations
from .operations.policies_operations import PoliciesOperations
from . import models


class FrontdoorManagementClientConfiguration(AzureConfiguration):
    """Configuration for FrontdoorManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(FrontdoorManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-frontdoor/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class FrontdoorManagementClient(SDKClient):
    """Frontdoor Client

    :ivar config: Configuration for client.
    :vartype config: FrontdoorManagementClientConfiguration

    :ivar front_doors: FrontDoors operations
    :vartype front_doors: azure.mgmt.frontdoor.operations.FrontDoorsOperations
    :ivar routing_rules: RoutingRules operations
    :vartype routing_rules: azure.mgmt.frontdoor.operations.RoutingRulesOperations
    :ivar health_probe_settings: HealthProbeSettings operations
    :vartype health_probe_settings: azure.mgmt.frontdoor.operations.HealthProbeSettingsOperations
    :ivar load_balancing_settings: LoadBalancingSettings operations
    :vartype load_balancing_settings: azure.mgmt.frontdoor.operations.LoadBalancingSettingsOperations
    :ivar backend_pools: BackendPools operations
    :vartype backend_pools: azure.mgmt.frontdoor.operations.BackendPoolsOperations
    :ivar frontend_endpoints: FrontendEndpoints operations
    :vartype frontend_endpoints: azure.mgmt.frontdoor.operations.FrontendEndpointsOperations
    :ivar endpoints: Endpoints operations
    :vartype endpoints: azure.mgmt.frontdoor.operations.EndpointsOperations
    :ivar policies: Policies operations
    :vartype policies: azure.mgmt.frontdoor.operations.PoliciesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = FrontdoorManagementClientConfiguration(credentials, subscription_id, base_url)
        super(FrontdoorManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.front_doors = FrontDoorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.routing_rules = RoutingRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.health_probe_settings = HealthProbeSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.load_balancing_settings = LoadBalancingSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backend_pools = BackendPoolsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.frontend_endpoints = FrontendEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)

    def check_front_door_name_availability(
            self, name, type, custom_headers=None, raw=False, **operation_config):
        """Check the availability of a Front Door resource name.

        :param name: The resource name to validate.
        :type name: str
        :param type: The type of the resource whose name is to be validated.
         Possible values include: 'Microsoft.Network/frontDoors',
         'Microsoft.Network/frontDoors/frontendEndpoints'
        :type type: str or ~azure.mgmt.frontdoor.models.ResourceType
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityOutput or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.frontdoor.models.CheckNameAvailabilityOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        check_front_door_name_availability_input = models.CheckNameAvailabilityInput(name=name, type=type)

        api_version = "2018-08-01"

        # Construct URL
        url = self.check_front_door_name_availability.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(check_front_door_name_availability_input, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_front_door_name_availability.metadata = {'url': '/providers/Microsoft.Network/checkFrontDoorNameAvailability'}

    def check_front_door_name_availability_with_subscription(
            self, name, type, custom_headers=None, raw=False, **operation_config):
        """Check the availability of a Front Door subdomain.

        :param name: The resource name to validate.
        :type name: str
        :param type: The type of the resource whose name is to be validated.
         Possible values include: 'Microsoft.Network/frontDoors',
         'Microsoft.Network/frontDoors/frontendEndpoints'
        :type type: str or ~azure.mgmt.frontdoor.models.ResourceType
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckNameAvailabilityOutput or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.frontdoor.models.CheckNameAvailabilityOutput or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.frontdoor.models.ErrorResponseException>`
        """
        check_front_door_name_availability_input = models.CheckNameAvailabilityInput(name=name, type=type)

        api_version = "2018-08-01"

        # Construct URL
        url = self.check_front_door_name_availability_with_subscription.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(check_front_door_name_availability_input, 'CheckNameAvailabilityInput')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('CheckNameAvailabilityOutput', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    check_front_door_name_availability_with_subscription.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Network/checkFrontDoorNameAvailability'}
