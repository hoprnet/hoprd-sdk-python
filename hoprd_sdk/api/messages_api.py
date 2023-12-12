# coding: utf-8

"""
    HOPRd Rest API v3

    This Rest API enables developers to interact with a hoprd node programatically.  # noqa: E501

    OpenAPI spec version: 3.0.0
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

    def messages_delete_messages(self, tag, **kwargs):  # noqa: E501
        """messages_delete_messages  # noqa: E501

        Delete messages from nodes message inbox. Does not return any data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_delete_messages(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageTag tag: Tag used to filter target messages. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_delete_messages_with_http_info(tag, **kwargs)  # noqa: E501
        else:
            (data) = self.messages_delete_messages_with_http_info(tag, **kwargs)  # noqa: E501
            return data

    def messages_delete_messages_with_http_info(self, tag, **kwargs):  # noqa: E501
        """messages_delete_messages  # noqa: E501

        Delete messages from nodes message inbox. Does not return any data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_delete_messages_with_http_info(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageTag tag: Tag used to filter target messages. (required)
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
                    " to method messages_delete_messages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `messages_delete_messages`")  # noqa: E501

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
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/', 'DELETE',
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

    def messages_get_size(self, tag, **kwargs):  # noqa: E501
        """messages_get_size  # noqa: E501

        Get size of filtered message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_get_size(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageTag tag: Tag used to filter target messages. (required)
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_get_size_with_http_info(tag, **kwargs)  # noqa: E501
        else:
            (data) = self.messages_get_size_with_http_info(tag, **kwargs)  # noqa: E501
            return data

    def messages_get_size_with_http_info(self, tag, **kwargs):  # noqa: E501
        """messages_get_size  # noqa: E501

        Get size of filtered message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_get_size_with_http_info(tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageTag tag: Tag used to filter target messages. (required)
        :return: InlineResponse2004
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
                    " to method messages_get_size" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `messages_get_size`")  # noqa: E501

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
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/size', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_peek_all_message(self, **kwargs):  # noqa: E501
        """messages_peek_all_message  # noqa: E501

        Get list of messages currently present in the nodes message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_peek_all_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPeekallBody body:
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_peek_all_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_peek_all_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_peek_all_message_with_http_info(self, **kwargs):  # noqa: E501
        """messages_peek_all_message  # noqa: E501

        Get list of messages currently present in the nodes message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_peek_all_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPeekallBody body:
        :return: InlineResponse2005
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
                    " to method messages_peek_all_message" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/peek-all', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_peek_message(self, **kwargs):  # noqa: E501
        """messages_peek_message  # noqa: E501

        Get oldest message currently present in the nodes message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_peek_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPeekBody body:
        :return: ReceivedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_peek_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_peek_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_peek_message_with_http_info(self, **kwargs):  # noqa: E501
        """messages_peek_message  # noqa: E501

        Get oldest message currently present in the nodes message inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_peek_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPeekBody body:
        :return: ReceivedMessage
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
                    " to method messages_peek_message" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/peek', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReceivedMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_pop_all_message(self, **kwargs):  # noqa: E501
        """messages_pop_all_message  # noqa: E501

        Get list of messages currently present in the nodes message inbox. The messages are removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_pop_all_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPopallBody body:
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_pop_all_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_pop_all_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_pop_all_message_with_http_info(self, **kwargs):  # noqa: E501
        """messages_pop_all_message  # noqa: E501

        Get list of messages currently present in the nodes message inbox. The messages are removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_pop_all_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPopallBody body:
        :return: InlineResponse2005
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
                    " to method messages_pop_all_message" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/pop-all', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2005',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_pop_message(self, **kwargs):  # noqa: E501
        """messages_pop_message  # noqa: E501

        Get oldest message currently present in the nodes message inbox. The message is removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_pop_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPopBody body:
        :return: ReceivedMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_pop_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_pop_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_pop_message_with_http_info(self, **kwargs):  # noqa: E501
        """messages_pop_message  # noqa: E501

        Get oldest message currently present in the nodes message inbox. The message is removed from the inbox.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_pop_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesPopBody body:
        :return: ReceivedMessage
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
                    " to method messages_pop_message" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/pop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReceivedMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def messages_send_message(self, **kwargs):  # noqa: E501
        """messages_send_message  # noqa: E501

        Send a message to another peer using a given path (list of node addresses that should relay our message through network). If no path is given, HOPR will attempt to find a path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_send_message(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesBody body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_send_message_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_send_message_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_send_message_with_http_info(self, **kwargs):  # noqa: E501
        """messages_send_message  # noqa: E501

        Send a message to another peer using a given path (list of node addresses that should relay our message through network). If no path is given, HOPR will attempt to find a path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_send_message_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessagesBody body:
        :return: str
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
                    " to method messages_send_message" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/', 'POST',
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

    def messages_websocket(self, **kwargs):  # noqa: E501
        """messages_websocket  # noqa: E501

        This is a websocket endpoint which exposes a subset of message functions. Incoming messages from other nodes are sent to the websocket client. A client may also send message by sending the following data:   { cmd: \"sendmsg\", args: { peerId: \"SOME_PEER_ID\", path: [], hops: 1} } The command arguments follow the same semantics as in the dedicated API endpoint for sending messages.  The following messages may be sent by the server over the Websocket connection:    {     type: \"message\",     tag: 12,     body: \"my example message\"   }    {     type: \"message-ack\",     id: \"some challenge id\"   }    {     type: \"message-ack-challenge\",     id: \"some challenge id\"   }  Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/messages/websocket/?apiToken=myApiToken`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_websocket(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.messages_websocket_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.messages_websocket_with_http_info(**kwargs)  # noqa: E501
            return data

    def messages_websocket_with_http_info(self, **kwargs):  # noqa: E501
        """messages_websocket  # noqa: E501

        This is a websocket endpoint which exposes a subset of message functions. Incoming messages from other nodes are sent to the websocket client. A client may also send message by sending the following data:   { cmd: \"sendmsg\", args: { peerId: \"SOME_PEER_ID\", path: [], hops: 1} } The command arguments follow the same semantics as in the dedicated API endpoint for sending messages.  The following messages may be sent by the server over the Websocket connection:    {     type: \"message\",     tag: 12,     body: \"my example message\"   }    {     type: \"message-ack\",     id: \"some challenge id\"   }    {     type: \"message-ack-challenge\",     id: \"some challenge id\"   }  Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/messages/websocket/?apiToken=myApiToken`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.messages_websocket_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
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
                    " to method messages_websocket" % key
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
            ['application/text', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['keyScheme', 'passwordScheme']  # noqa: E501

        return self.api_client.call_api(
            '/messages/websocket', 'GET',
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
