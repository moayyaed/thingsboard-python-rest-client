# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class QueueStatsControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_queue_stats_by_id(self, queue_stats_id, **kwargs):  # noqa: E501
        """Get Queue stats entity by id (getQueueStatsById)  # noqa: E501

        Fetch the Queue stats object based on the provided Queue stats id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_stats_by_id(queue_stats_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_stats_id: A string value representing the queue stats id. For example, '687f294c-42b6-435a-983c-b7beff2784f9' (required)
        :return: QueueStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_queue_stats_by_id_with_http_info(queue_stats_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_queue_stats_by_id_with_http_info(queue_stats_id, **kwargs)  # noqa: E501
            return data

    def get_queue_stats_by_id_with_http_info(self, queue_stats_id, **kwargs):  # noqa: E501
        """Get Queue stats entity by id (getQueueStatsById)  # noqa: E501

        Fetch the Queue stats object based on the provided Queue stats id.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_stats_by_id_with_http_info(queue_stats_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_stats_id: A string value representing the queue stats id. For example, '687f294c-42b6-435a-983c-b7beff2784f9' (required)
        :return: QueueStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_stats_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_queue_stats_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'queue_stats_id' is set
        if ('queue_stats_id' not in params or
                params['queue_stats_id'] is None):
            raise ValueError("Missing the required parameter `queue_stats_id` when calling `get_queue_stats_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'queue_stats_id' in params:
            path_params['queueStatsId'] = params['queue_stats_id']  # noqa: E501

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
            '/api/queueStats/{queueStatsId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueueStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_queue_stats_by_ids(self, queue_stats_ids, **kwargs):  # noqa: E501
        """Get QueueStats By Ids (getQueueStatsByIds)  # noqa: E501

        Fetch the Queue stats objects based on the provided ids.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_stats_by_ids(queue_stats_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_stats_ids: A list of queue stats ids, separated by comma ',' (required)
        :return: list[QueueStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_queue_stats_by_ids_with_http_info(queue_stats_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_queue_stats_by_ids_with_http_info(queue_stats_ids, **kwargs)  # noqa: E501
            return data

    def get_queue_stats_by_ids_with_http_info(self, queue_stats_ids, **kwargs):  # noqa: E501
        """Get QueueStats By Ids (getQueueStatsByIds)  # noqa: E501

        Fetch the Queue stats objects based on the provided ids.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_queue_stats_by_ids_with_http_info(queue_stats_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str queue_stats_ids: A list of queue stats ids, separated by comma ',' (required)
        :return: list[QueueStats]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['queue_stats_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_queue_stats_by_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'queue_stats_ids' is set
        if ('queue_stats_ids' not in params or
                params['queue_stats_ids'] is None):
            raise ValueError("Missing the required parameter `queue_stats_ids` when calling `get_queue_stats_by_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'queue_stats_ids' in params:
            query_params.append(('queueStatsIds', params['queue_stats_ids']))  # noqa: E501
            collection_formats['queueStatsIds'] = 'multi'  # noqa: E501

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
            '/api/queueStats{?queueStatsIds}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[QueueStats]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tenant_queue_stats(self, page_size, page, **kwargs):  # noqa: E501
        """Get Queue Stats entities (getTenantQueueStats)  # noqa: E501

        Returns a page of queue stats objects that are designed to collect queue statistics for every service. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_queue_stats(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'substring' filter based on the queue name or service id.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataQueueStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tenant_queue_stats_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tenant_queue_stats_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_tenant_queue_stats_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """Get Queue Stats entities (getTenantQueueStats)  # noqa: E501

        Returns a page of queue stats objects that are designed to collect queue statistics for every service. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tenant_queue_stats_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: The case insensitive 'substring' filter based on the queue name or service id.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :return: PageDataQueueStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'text_search', 'sort_property', 'sort_order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tenant_queue_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_tenant_queue_stats`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_tenant_queue_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
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
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/queueStats{?pageSize,page,textSearch,sortProperty,sortOrder}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataQueueStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
