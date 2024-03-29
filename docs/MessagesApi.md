# hoprd_sdk.MessagesApi

All URIs are relative to */api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_delete_messages**](MessagesApi.md#messages_delete_messages) | **DELETE** /messages/ | 
[**messages_get_size**](MessagesApi.md#messages_get_size) | **GET** /messages/size | 
[**messages_peek_all_message**](MessagesApi.md#messages_peek_all_message) | **POST** /messages/peek-all | 
[**messages_peek_message**](MessagesApi.md#messages_peek_message) | **POST** /messages/peek | 
[**messages_pop_all_message**](MessagesApi.md#messages_pop_all_message) | **POST** /messages/pop-all | 
[**messages_pop_message**](MessagesApi.md#messages_pop_message) | **POST** /messages/pop | 
[**messages_send_message**](MessagesApi.md#messages_send_message) | **POST** /messages/ | 
[**messages_websocket**](MessagesApi.md#messages_websocket) | **GET** /messages/websocket | 

# **messages_delete_messages**
> messages_delete_messages(tag)



Delete messages from nodes message inbox. Does not return any data.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
tag = hoprd_sdk.MessageTag() # MessageTag | Tag used to filter target messages.

try:
    api_instance.messages_delete_messages(tag)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_delete_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**MessageTag**](.md)| Tag used to filter target messages. | 

### Return type

void (empty response body)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_get_size**
> InlineResponse2004 messages_get_size(tag)



Get size of filtered message inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
tag = hoprd_sdk.MessageTag() # MessageTag | Tag used to filter target messages.

try:
    api_response = api_instance.messages_get_size(tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_get_size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**MessageTag**](.md)| Tag used to filter target messages. | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_peek_all_message**
> InlineResponse2005 messages_peek_all_message(body=body)



Get list of messages currently present in the nodes message inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.MessagesPeekallBody() # MessagesPeekallBody |  (optional)

try:
    api_response = api_instance.messages_peek_all_message(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_peek_all_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagesPeekallBody**](MessagesPeekallBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_peek_message**
> ReceivedMessage messages_peek_message(body=body)



Get oldest message currently present in the nodes message inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.MessagesPeekBody() # MessagesPeekBody |  (optional)

try:
    api_response = api_instance.messages_peek_message(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_peek_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagesPeekBody**](MessagesPeekBody.md)|  | [optional] 

### Return type

[**ReceivedMessage**](ReceivedMessage.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_pop_all_message**
> InlineResponse2005 messages_pop_all_message(body=body)



Get list of messages currently present in the nodes message inbox. The messages are removed from the inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.MessagesPopallBody() # MessagesPopallBody |  (optional)

try:
    api_response = api_instance.messages_pop_all_message(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_pop_all_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagesPopallBody**](MessagesPopallBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_pop_message**
> ReceivedMessage messages_pop_message(body=body)



Get oldest message currently present in the nodes message inbox. The message is removed from the inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.MessagesPopBody() # MessagesPopBody |  (optional)

try:
    api_response = api_instance.messages_pop_message(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_pop_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagesPopBody**](MessagesPopBody.md)|  | [optional] 

### Return type

[**ReceivedMessage**](ReceivedMessage.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_send_message**
> str messages_send_message(body=body)



Send a message to another peer using a given path (list of node addresses that should relay our message through network). If no path is given, HOPR will attempt to find a path.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.MessagesBody() # MessagesBody |  (optional)

try:
    api_response = api_instance.messages_send_message(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagesBody**](MessagesBody.md)|  | [optional] 

### Return type

**str**

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_websocket**
> str messages_websocket()



This is a websocket endpoint which exposes a subset of message functions. Incoming messages from other nodes are sent to the websocket client. A client may also send message by sending the following data:   { cmd: \"sendmsg\", args: { peerId: \"SOME_PEER_ID\", path: [], hops: 1} } The command arguments follow the same semantics as in the dedicated API endpoint for sending messages.  The following messages may be sent by the server over the Websocket connection:    {     type: \"message\",     tag: 12,     body: \"my example message\"   }    {     type: \"message-ack\",     id: \"some challenge id\"   }    {     type: \"message-ack-challenge\",     id: \"some challenge id\"   }  Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/messages/websocket/?apiToken=myApiToken`

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = hoprd_sdk.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = hoprd_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))

try:
    api_response = api_instance.messages_websocket()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_websocket: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/text, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

