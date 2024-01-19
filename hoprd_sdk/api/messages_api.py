# coding: utf-8

"""
    hoprd-api

    API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API  # noqa: E501

    OpenAPI spec version: 0.2.0
    Contact: tech@hoprnet.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hoprd_sdk.api_client import ApiClient


class MessagesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_messages(self, **kwargs):  # noqa: E501
        """Delete messages from nodes message inbox.  # noqa: E501

        Delete messages from nodes message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_messages(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_messages_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_messages_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_messages_with_http_info(self, **kwargs):  # noqa: E501
        """Delete messages from nodes message inbox.  # noqa: E501

        Delete messages from nodes message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_messages_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_messages" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

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
            '/api/v3/messages', 'DELETE',
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

    def peek(self, body, **kwargs):  # noqa: E501
        """Peek the oldest message currently present in the nodes message inbox.  # noqa: E501

        Peek the oldest message currently present in the nodes message inbox.  The message is not removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peek(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagQuery body: Tag of message queue to peek from (required)
        :return: MessagePopRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peek_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.peek_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def peek_with_http_info(self, body, **kwargs):  # noqa: E501
        """Peek the oldest message currently present in the nodes message inbox.  # noqa: E501

        Peek the oldest message currently present in the nodes message inbox.  The message is not removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peek_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagQuery body: Tag of message queue to peek from (required)
        :return: MessagePopRes
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
                    " to method peek" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `peek`")  # noqa: E501

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
            '/api/v3/messages/peek', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessagePopRes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def peek_all(self, body, **kwargs):  # noqa: E501
        """Peek the list of messages currently present in the nodes message inbox, filtered by tag,  # noqa: E501

        Peek the list of messages currently present in the nodes message inbox, filtered by tag, and optionally by timestamp (epoch in milliseconds). The messages are not removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peek_all(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetMessageReq body: Tag of message queue and optionally a timestamp since from to start peeking (required)
        :return: InboxMessagesRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peek_all_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.peek_all_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def peek_all_with_http_info(self, body, **kwargs):  # noqa: E501
        """Peek the list of messages currently present in the nodes message inbox, filtered by tag,  # noqa: E501

        Peek the list of messages currently present in the nodes message inbox, filtered by tag, and optionally by timestamp (epoch in milliseconds). The messages are not removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peek_all_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetMessageReq body: Tag of message queue and optionally a timestamp since from to start peeking (required)
        :return: InboxMessagesRes
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
                    " to method peek_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `peek_all`")  # noqa: E501

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
            '/api/v3/messages/peek-all', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InboxMessagesRes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pop(self, body, **kwargs):  # noqa: E501
        """Get the oldest message currently present in the nodes message inbox.  # noqa: E501

        Get the oldest message currently present in the nodes message inbox.  The message is removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pop(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagQuery body: Tag of message queue to pop from (required)
        :return: MessagePopRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pop_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.pop_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def pop_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get the oldest message currently present in the nodes message inbox.  # noqa: E501

        Get the oldest message currently present in the nodes message inbox.  The message is removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pop_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagQuery body: Tag of message queue to pop from (required)
        :return: MessagePopRes
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
                    " to method pop" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `pop`")  # noqa: E501

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
            '/api/v3/messages/pop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessagePopRes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pop_all(self, body, **kwargs):  # noqa: E501
        """Get the list of messages currently present in the nodes message inbox.  # noqa: E501

        Get the list of messages currently present in the nodes message inbox.  The messages are removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pop_all(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagQuery body: Tag of message queue to pop from (required)
        :return: InboxMessagesRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pop_all_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.pop_all_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def pop_all_with_http_info(self, body, **kwargs):  # noqa: E501
        """Get the list of messages currently present in the nodes message inbox.  # noqa: E501

        Get the list of messages currently present in the nodes message inbox.  The messages are removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pop_all_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TagQuery body: Tag of message queue to pop from (required)
        :return: InboxMessagesRes
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
                    " to method pop_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `pop_all`")  # noqa: E501

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
            '/api/v3/messages/pop-all', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InboxMessagesRes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_message(self, body, **kwargs):  # noqa: E501
        """Send a message to another peer using a given path.  # noqa: E501

        Send a message to another peer using a given path.  The message can be sent either over a specified path or using a specified number of HOPS, if no path is given.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendMessageReq body: Body of a message to send (required)
        :return: SendMessageRes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.send_message_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_message_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def send_message_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send a message to another peer using a given path.  # noqa: E501

        Send a message to another peer using a given path.  The message can be sent either over a specified path or using a specified number of HOPS, if no path is given.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.send_message_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SendMessageReq body: Body of a message to send (required)
        :return: SendMessageRes
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
                    " to method send_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_message`")  # noqa: E501

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
            '/api/v3/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SendMessageRes',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def size(self, **kwargs):  # noqa: E501
        """Get size of filtered message inbox for a specific tag  # noqa: E501

        Get size of filtered message inbox for a specific tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.size(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag:
        :return: Size
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.size_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.size_with_http_info(**kwargs)  # noqa: E501
            return data

    def size_with_http_info(self, **kwargs):  # noqa: E501
        """Get size of filtered message inbox for a specific tag  # noqa: E501

        Get size of filtered message inbox for a specific tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.size_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int tag:
        :return: Size
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method size" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501

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
            '/api/v3/messages/size', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Size',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
