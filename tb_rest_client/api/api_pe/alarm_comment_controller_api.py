# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class AlarmCommentControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_alarm_comment_using_delete(self, alarm_id, comment_id, **kwargs):  # noqa: E501
        """Delete Alarm comment (deleteAlarmComment)  # noqa: E501

        Deletes the Alarm comment. Referencing non-existing Alarm comment Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alarm_comment_using_delete(alarm_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str comment_id: A string value representing the alarm comment id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_alarm_comment_using_delete_with_http_info(alarm_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_alarm_comment_using_delete_with_http_info(alarm_id, comment_id, **kwargs)  # noqa: E501
            return data

    def delete_alarm_comment_using_delete_with_http_info(self, alarm_id, comment_id, **kwargs):  # noqa: E501
        """Delete Alarm comment (deleteAlarmComment)  # noqa: E501

        Deletes the Alarm comment. Referencing non-existing Alarm comment Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_alarm_comment_using_delete_with_http_info(alarm_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str comment_id: A string value representing the alarm comment id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id', 'comment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_alarm_comment_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `delete_alarm_comment_using_delete`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if ('comment_id' not in params or
                params['comment_id'] is None):
            raise ValueError("Missing the required parameter `comment_id` when calling `delete_alarm_comment_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501
        if 'comment_id' in params:
            path_params['commentId'] = params['comment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTP login form']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{alarmId}/comment/{commentId}', 'DELETE',
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

    def get_alarm_comments_using_get(self, alarm_id, page_size, page, **kwargs):  # noqa: E501
        """Get Alarm comments (getAlarmComments)  # noqa: E501

        Returns a page of alarm comments for specified alarm. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alarm_comments_using_get(alarm_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataAlarmCommentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alarm_comments_using_get_with_http_info(alarm_id, page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alarm_comments_using_get_with_http_info(alarm_id, page_size, page, **kwargs)  # noqa: E501
            return data

    def get_alarm_comments_using_get_with_http_info(self, alarm_id, page_size, page, **kwargs):  # noqa: E501
        """Get Alarm comments (getAlarmComments)  # noqa: E501

        Returns a page of alarm comments for specified alarm. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alarm_comments_using_get_with_http_info(alarm_id, page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataAlarmCommentInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id', 'page_size', 'page', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alarm_comments_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `get_alarm_comments_using_get`")  # noqa: E501
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_alarm_comments_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_alarm_comments_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTP login form']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{alarmId}/comment?sortProperty=createdTime{&page,pageSize,sortOrder}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataAlarmCommentInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_alarm_comment_using_post(self, alarm_id, **kwargs):  # noqa: E501
        """Create or update Alarm Comment   # noqa: E501

        Creates or Updates the Alarm Comment. When creating comment, platform generates Alarm Comment Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm Comment id will be present in the response. Specify existing Alarm Comment id to update the alarm. Referencing non-existing Alarm Comment Id will cause 'Not Found' error.    To create new Alarm comment entity it is enough to specify 'comment' json element with 'text' node, for example: {\"comment\": { \"text\": \"my comment\"}}.    If comment type is not specified the default value 'OTHER' will be saved. If 'alarmId' or 'userId' specified in body it will be ignored.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_alarm_comment_using_post(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param AlarmComment body:
        :return: AlarmComment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_alarm_comment_using_post_with_http_info(alarm_id, **kwargs)  # noqa: E501
        else:
            (data) = self.save_alarm_comment_using_post_with_http_info(alarm_id, **kwargs)  # noqa: E501
            return data

    def save_alarm_comment_using_post_with_http_info(self, alarm_id, **kwargs):  # noqa: E501
        """Create or update Alarm Comment   # noqa: E501

        Creates or Updates the Alarm Comment. When creating comment, platform generates Alarm Comment Id as [time-based UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_1_(date-time_and_MAC_address)). The newly created Alarm Comment id will be present in the response. Specify existing Alarm Comment id to update the alarm. Referencing non-existing Alarm Comment Id will cause 'Not Found' error.    To create new Alarm comment entity it is enough to specify 'comment' json element with 'text' node, for example: {\"comment\": { \"text\": \"my comment\"}}.    If comment type is not specified the default value 'OTHER' will be saved. If 'alarmId' or 'userId' specified in body it will be ignored.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_alarm_comment_using_post_with_http_info(alarm_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str alarm_id: A string value representing the alarm id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param AlarmComment body:
        :return: AlarmComment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['alarm_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_alarm_comment_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'alarm_id' is set
        if ('alarm_id' not in params or
                params['alarm_id'] is None):
            raise ValueError("Missing the required parameter `alarm_id` when calling `save_alarm_comment_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'alarm_id' in params:
            path_params['alarmId'] = params['alarm_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['HTTP login form']  # noqa: E501

        return self.api_client.call_api(
            '/api/alarm/{alarmId}/comment', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlarmComment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
