# coding: utf-8

"""
    hoprd-api

    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501

    OpenAPI spec version: 0.1.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hoprd_sdk.api_client import ApiClient


class ChannelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def aggregate_tickets_in_channel(self, channel_id, **kwargs):  # noqa: E501
        """aggregate_tickets_in_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_tickets_in_channel(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.aggregate_tickets_in_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.aggregate_tickets_in_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def aggregate_tickets_in_channel_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """aggregate_tickets_in_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.aggregate_tickets_in_channel_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aggregate_tickets_in_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params or
                params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `aggregate_tickets_in_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels/{channelId}/tickets/aggregate', 'POST',
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

    def close_channel(self, channel_id, **kwargs):  # noqa: E501
        """close_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_channel(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: CloseChannelReceipt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.close_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.close_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def close_channel_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """close_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_channel_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: CloseChannelReceipt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method close_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params or
                params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `close_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels/{channelId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloseChannelReceipt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fund_channel(self, body, channel_id, **kwargs):  # noqa: E501
        """fund_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fund_channel(body, channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FundRequest body: Amount of HOPR to fund the channel (required)
        :param str channel_id: ID of the channel. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fund_channel_with_http_info(body, channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.fund_channel_with_http_info(body, channel_id, **kwargs)  # noqa: E501
            return data

    def fund_channel_with_http_info(self, body, channel_id, **kwargs):  # noqa: E501
        """fund_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fund_channel_with_http_info(body, channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FundRequest body: Amount of HOPR to fund the channel (required)
        :param str channel_id: ID of the channel. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fund_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `fund_channel`")  # noqa: E501
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params or
                params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `fund_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels/{channelId}/fund', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_channels(self, **kwargs):  # noqa: E501
        """list_channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_channels(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool including_closed:
        :param bool full_topology:
        :return: NodeChannels
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_channels_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_channels_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_channels_with_http_info(self, **kwargs):  # noqa: E501
        """list_channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_channels_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool including_closed:
        :param bool full_topology:
        :return: NodeChannels
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['including_closed', 'full_topology']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_channels" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'including_closed' in params:
            query_params.append(('includingClosed', params['including_closed']))  # noqa: E501
        if 'full_topology' in params:
            query_params.append(('fullTopology', params['full_topology']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeChannels',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def open_channel(self, body, **kwargs):  # noqa: E501
        """open_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_channel(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OpenChannelRequest body: Open channel request specification (required)
        :return: OpenChannelReceipt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_channel_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.open_channel_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def open_channel_with_http_info(self, body, **kwargs):  # noqa: E501
        """open_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_channel_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OpenChannelRequest body: Open channel request specification (required)
        :return: OpenChannelReceipt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `open_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OpenChannelReceipt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def redeem_tickets_in_channel(self, channel_id, **kwargs):  # noqa: E501
        """redeem_tickets_in_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.redeem_tickets_in_channel(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.redeem_tickets_in_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.redeem_tickets_in_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def redeem_tickets_in_channel_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """redeem_tickets_in_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.redeem_tickets_in_channel_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method redeem_tickets_in_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params or
                params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `redeem_tickets_in_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels/{channelId}/tickets/redeem', 'POST',
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

    def show_channel(self, channel_id, **kwargs):  # noqa: E501
        """show_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_channel(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: NodeTopologyChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.show_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.show_channel_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def show_channel_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """show_channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_channel_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: NodeTopologyChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_channel" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params or
                params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `show_channel`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels/{channelId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NodeTopologyChannel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def show_channel_tickets(self, channel_id, **kwargs):  # noqa: E501
        """show_channel_tickets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_channel_tickets(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: list[ChannelTicket]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.show_channel_tickets_with_http_info(channel_id, **kwargs)  # noqa: E501
        else:
            (data) = self.show_channel_tickets_with_http_info(channel_id, **kwargs)  # noqa: E501
            return data

    def show_channel_tickets_with_http_info(self, channel_id, **kwargs):  # noqa: E501
        """show_channel_tickets  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.show_channel_tickets_with_http_info(channel_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str channel_id: ID of the channel. (required)
        :return: list[ChannelTicket]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method show_channel_tickets" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params or
                params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `show_channel_tickets`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channelId'] = params['channel_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_token']  # noqa: E501

        return self.api_client.call_api(
            '/api/v3/channels/{channelId}/tickets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ChannelTicket]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
