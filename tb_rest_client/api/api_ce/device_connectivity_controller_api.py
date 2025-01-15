# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0
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

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class DeviceConnectivityControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_gateway_docker_compose_using_get(self, device_id, **kwargs):  # noqa: E501
        """Download generated docker-compose.yml file for gateway (downloadGatewayDockerCompose)  # noqa: E501

        Download generated docker-compose.yml for gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_gateway_docker_compose_using_get(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: Resource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_gateway_docker_compose_using_get_with_http_info(device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_gateway_docker_compose_using_get_with_http_info(device_id, **kwargs)  # noqa: E501
            return data

    def download_gateway_docker_compose_using_get_with_http_info(self, device_id, **kwargs):  # noqa: E501
        """Download generated docker-compose.yml file for gateway (downloadGatewayDockerCompose)  # noqa: E501

        Download generated docker-compose.yml for gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_gateway_docker_compose_using_get_with_http_info(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: Resource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_gateway_docker_compose_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `download_gateway_docker_compose_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/device-connectivity/gateway-launch/{deviceId}/docker-compose/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Resource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_server_certificate_using_get(self, protocol, **kwargs):  # noqa: E501
        """Download server certificate using file path defined in device.connectivity properties (downloadServerCertificate)  # noqa: E501

        Download server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_server_certificate_using_get(protocol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protocol: A string value representing the device connectivity protocol. Possible values: 'mqtt', 'mqtts', 'http', 'https', 'coap', 'coaps' (required)
        :return: Resource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_server_certificate_using_get_with_http_info(protocol, **kwargs)  # noqa: E501
        else:
            (data) = self.download_server_certificate_using_get_with_http_info(protocol, **kwargs)  # noqa: E501
            return data

    def download_server_certificate_using_get_with_http_info(self, protocol, **kwargs):  # noqa: E501
        """Download server certificate using file path defined in device.connectivity properties (downloadServerCertificate)  # noqa: E501

        Download server certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_server_certificate_using_get_with_http_info(protocol, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str protocol: A string value representing the device connectivity protocol. Possible values: 'mqtt', 'mqtts', 'http', 'https', 'coap', 'coaps' (required)
        :return: Resource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['protocol']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_server_certificate_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'protocol' is set
        if ('protocol' not in params or
                params['protocol'] is None):
            raise ValueError("Missing the required parameter `protocol` when calling `download_server_certificate_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'protocol' in params:
            path_params['protocol'] = params['protocol']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/device-connectivity/{protocol}/certificate/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Resource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_device_publish_telemetry_commands_using_get(self, device_id, **kwargs):  # noqa: E501
        """Get commands to publish device telemetry (getDevicePublishTelemetryCommands)  # noqa: E501

        Fetch the list of commands to publish device telemetry based on device profile If the user has the authority of 'Tenant Administrator', the server checks that the device is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the device is assigned to the same customer.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_publish_telemetry_commands_using_get(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: JsonNode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_publish_telemetry_commands_using_get_with_http_info(device_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_device_publish_telemetry_commands_using_get_with_http_info(device_id, **kwargs)  # noqa: E501
            return data

    def get_device_publish_telemetry_commands_using_get_with_http_info(self, device_id, **kwargs):  # noqa: E501
        """Get commands to publish device telemetry (getDevicePublishTelemetryCommands)  # noqa: E501

        Fetch the list of commands to publish device telemetry based on device profile If the user has the authority of 'Tenant Administrator', the server checks that the device is owned by the same tenant. If the user has the authority of 'Customer User', the server checks that the device is assigned to the same customer.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_publish_telemetry_commands_using_get_with_http_info(device_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str device_id: A string value representing the device id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: JsonNode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_publish_telemetry_commands_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params or
                params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `get_device_publish_telemetry_commands_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/device-connectivity/{deviceId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonNode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
