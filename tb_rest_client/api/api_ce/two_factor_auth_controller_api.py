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


class TwoFactorAuthControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def check_two_fa_verification_code_using_post(self, provider_type, verification_code, **kwargs):  # noqa: E501
        """Check 2FA verification code (checkTwoFaVerificationCode)  # noqa: E501

        Checks 2FA verification code, and if it is correct the method returns a regular access and refresh token pair.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings), and also will block a user after X unsuccessful verification attempts if such behavior is configured (in TwoFactorAuthSettings).  Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_two_fa_verification_code_using_post(provider_type, verification_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_type: providerType (required)
        :param str verification_code: verificationCode (required)
        :return: JwtPair
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.check_two_fa_verification_code_using_post_with_http_info(provider_type, verification_code, **kwargs)  # noqa: E501
        else:
            (data) = self.check_two_fa_verification_code_using_post_with_http_info(provider_type, verification_code, **kwargs)  # noqa: E501
            return data

    def check_two_fa_verification_code_using_post_with_http_info(self, provider_type, verification_code, **kwargs):  # noqa: E501
        """Check 2FA verification code (checkTwoFaVerificationCode)  # noqa: E501

        Checks 2FA verification code, and if it is correct the method returns a regular access and refresh token pair.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings), and also will block a user after X unsuccessful verification attempts if such behavior is configured (in TwoFactorAuthSettings).  Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_two_fa_verification_code_using_post_with_http_info(provider_type, verification_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_type: providerType (required)
        :param str verification_code: verificationCode (required)
        :return: JwtPair
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_type', 'verification_code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_two_fa_verification_code_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_type' is set
        if ('provider_type' not in params or
                params['provider_type'] is None):
            raise ValueError("Missing the required parameter `provider_type` when calling `check_two_fa_verification_code_using_post`")  # noqa: E501
        # verify the required parameter 'verification_code' is set
        if ('verification_code' not in params or
                params['verification_code'] is None):
            raise ValueError("Missing the required parameter `verification_code` when calling `check_two_fa_verification_code_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider_type' in params:
            query_params.append(('providerType', params['provider_type']))  # noqa: E501
        if 'verification_code' in params:
            query_params.append(('verificationCode', params['verification_code']))  # noqa: E501

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
            '/api/auth/2fa/verification/check{?providerType,verificationCode}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JwtPair',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_available_two_fa_providers_using_get1(self, **kwargs):  # noqa: E501
        """Get available 2FA providers (getAvailableTwoFaProviders)  # noqa: E501

        Get the list of 2FA provider infos available for user to use. Example: ``` [   {     \"type\": \"EMAIL\",     \"default\": true,     \"contact\": \"ab*****ko@gmail.com\"   },   {     \"type\": \"TOTP\",     \"default\": false,     \"contact\": null   },   {     \"type\": \"SMS\",     \"default\": false,     \"contact\": \"+38********12\"   } ] ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_two_fa_providers_using_get1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TwoFaProviderInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_available_two_fa_providers_using_get1_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_available_two_fa_providers_using_get1_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_available_two_fa_providers_using_get1_with_http_info(self, **kwargs):  # noqa: E501
        """Get available 2FA providers (getAvailableTwoFaProviders)  # noqa: E501

        Get the list of 2FA provider infos available for user to use. Example: ``` [   {     \"type\": \"EMAIL\",     \"default\": true,     \"contact\": \"ab*****ko@gmail.com\"   },   {     \"type\": \"TOTP\",     \"default\": false,     \"contact\": null   },   {     \"type\": \"SMS\",     \"default\": false,     \"contact\": \"+38********12\"   } ] ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_two_fa_providers_using_get1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[TwoFaProviderInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_two_fa_providers_using_get1" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/auth/2fa/providers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TwoFaProviderInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def request_two_fa_verification_code_using_post(self, provider_type, **kwargs):  # noqa: E501
        """Request 2FA verification code (requestTwoFaVerificationCode)  # noqa: E501

        Request 2FA verification code.  To make a request to this endpoint, you need an access token with the scope of PRE_VERIFICATION_TOKEN, which is issued on username/password auth if 2FA is enabled.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings). Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_two_fa_verification_code_using_post(provider_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_type: providerType (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.request_two_fa_verification_code_using_post_with_http_info(provider_type, **kwargs)  # noqa: E501
        else:
            (data) = self.request_two_fa_verification_code_using_post_with_http_info(provider_type, **kwargs)  # noqa: E501
            return data

    def request_two_fa_verification_code_using_post_with_http_info(self, provider_type, **kwargs):  # noqa: E501
        """Request 2FA verification code (requestTwoFaVerificationCode)  # noqa: E501

        Request 2FA verification code.  To make a request to this endpoint, you need an access token with the scope of PRE_VERIFICATION_TOKEN, which is issued on username/password auth if 2FA is enabled.  The API method is rate limited (using rate limit config from TwoFactorAuthSettings). Will return a Bad Request error if provider is not configured for usage, and Too Many Requests error if rate limits are exceeded.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.request_two_fa_verification_code_using_post_with_http_info(provider_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provider_type: providerType (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['provider_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method request_two_fa_verification_code_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'provider_type' is set
        if ('provider_type' not in params or
                params['provider_type'] is None):
            raise ValueError("Missing the required parameter `provider_type` when calling `request_two_fa_verification_code_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'provider_type' in params:
            query_params.append(('providerType', params['provider_type']))  # noqa: E501

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
            '/api/auth/2fa/verification/send{?providerType}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
