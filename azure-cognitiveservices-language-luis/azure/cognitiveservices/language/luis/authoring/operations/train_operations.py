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

from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError

from .. import models


class TrainOperations(object):
    """TrainOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self.config = config

    def train_version(
            self, app_id, version_id, custom_headers=None, raw=False, **operation_config):
        """Sends a training request for a version of a specified LUIS app. This
        POST request initiates a request asynchronously. To determine whether
        the training request is successful, submit a GET request to get
        training status. Note: The application version is not fully trained
        unless all the models (intents and entities) are trained successfully
        or are up to date. To verify training success, get the training status
        at least once after training is complete.

        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.train_version.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Ocp-Apim-Subscription-Key'] = self._serialize.header("self.config.ocp_apim_subscription_key", self.config.ocp_apim_subscription_key, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [202, 400, 401, 403, 409, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 202:
            deserialized = self._deserialize('EnqueueTrainingResponse', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 401:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 403:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 409:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 429:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    train_version.metadata = {'url': '/apps/{appId}/versions/{versionId}/train'}

    def get_status(
            self, app_id, version_id, custom_headers=None, raw=False, **operation_config):
        """Gets the training status of all models (intents and entities) for the
        specified LUIS app. You must call the train API to train the LUIS app
        before you call this API to get training status. "appID" specifies the
        LUIS app ID. "versionId" specifies the version number of the LUIS app.
        For example, "0.1".

        :param app_id: The application ID.
        :type app_id: str
        :param version_id: The version ID.
        :type version_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: object or ClientRawResponse if raw=true
        :rtype: object or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_status.metadata['url']
        path_format_arguments = {
            'Endpoint': self._serialize.url("self.config.endpoint", self.config.endpoint, 'str', skip_quote=True),
            'appId': self._serialize.url("app_id", app_id, 'str'),
            'versionId': self._serialize.url("version_id", version_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if custom_headers:
            header_parameters.update(custom_headers)
        header_parameters['Ocp-Apim-Subscription-Key'] = self._serialize.header("self.config.ocp_apim_subscription_key", self.config.ocp_apim_subscription_key, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 400, 401, 403, 429]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('[ModelTrainingInfo]', response)
        if response.status_code == 400:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 401:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 403:
            deserialized = self._deserialize('ErrorResponse', response)
        if response.status_code == 429:
            deserialized = self._deserialize('ErrorResponse', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_status.metadata = {'url': '/apps/{appId}/versions/{versionId}/train'}
