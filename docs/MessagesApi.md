# hoprd_sdk.MessagesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_messages**](MessagesApi.md#delete_messages) | **DELETE** /api/v3/messages | Delete messages from nodes message inbox.
[**peek**](MessagesApi.md#peek) | **POST** /api/v3/messages/peek | Peek the oldest message currently present in the nodes message inbox.
[**peek_all**](MessagesApi.md#peek_all) | **POST** /api/v3/messages/peek-all | Peek the list of messages currently present in the nodes message inbox, filtered by tag,
[**pop**](MessagesApi.md#pop) | **POST** /api/v3/messages/pop | Get the oldest message currently present in the nodes message inbox.
[**pop_all**](MessagesApi.md#pop_all) | **POST** /api/v3/messages/pop-all | Get the list of messages currently present in the nodes message inbox.
[**send_message**](MessagesApi.md#send_message) | **POST** /api/v3/messages | Send a message to another peer using the given path.
[**size**](MessagesApi.md#size) | **GET** /api/v3/messages/size | Get size of filtered message inbox for a specific tag

# **delete_messages**
> delete_messages(tag=tag)

Delete messages from nodes message inbox.

Delete messages from nodes message inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
tag = 56 # int |  (optional)

try:
    # Delete messages from nodes message inbox.
    api_instance.delete_messages(tag=tag)
except ApiException as e:
    print("Exception when calling MessagesApi->delete_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peek**
> MessagePopResponse peek(body)

Peek the oldest message currently present in the nodes message inbox.

Peek the oldest message currently present in the nodes message inbox.  The message is not removed from the inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.TagQueryRequest() # TagQueryRequest | Tag of message queue to peek from

try:
    # Peek the oldest message currently present in the nodes message inbox.
    api_response = api_instance.peek(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->peek: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagQueryRequest**](TagQueryRequest.md)| Tag of message queue to peek from | 

### Return type

[**MessagePopResponse**](MessagePopResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peek_all**
> MessagePopAllResponse peek_all(body)

Peek the list of messages currently present in the nodes message inbox, filtered by tag,

Peek the list of messages currently present in the nodes message inbox, filtered by tag, and optionally by timestamp (epoch in milliseconds). The messages are not removed from the inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.GetMessageBodyRequest() # GetMessageBodyRequest | Tag of message queue and optionally a timestamp since from to start peeking. When an empty object or an object with a `tag: 0` is provided, it fetches all the messages.

try:
    # Peek the list of messages currently present in the nodes message inbox, filtered by tag,
    api_response = api_instance.peek_all(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->peek_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetMessageBodyRequest**](GetMessageBodyRequest.md)| Tag of message queue and optionally a timestamp since from to start peeking. When an empty object or an object with a &#x60;tag: 0&#x60; is provided, it fetches all the messages. | 

### Return type

[**MessagePopAllResponse**](MessagePopAllResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pop**
> MessagePopResponse pop(body)

Get the oldest message currently present in the nodes message inbox.

Get the oldest message currently present in the nodes message inbox.  The message is removed from the inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.TagQueryRequest() # TagQueryRequest | Tag of message queue to pop from

try:
    # Get the oldest message currently present in the nodes message inbox.
    api_response = api_instance.pop(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->pop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagQueryRequest**](TagQueryRequest.md)| Tag of message queue to pop from | 

### Return type

[**MessagePopResponse**](MessagePopResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pop_all**
> MessagePopAllResponse pop_all(body)

Get the list of messages currently present in the nodes message inbox.

Get the list of messages currently present in the nodes message inbox.  The messages are removed from the inbox.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.TagQueryRequest() # TagQueryRequest | Tag of message queue to pop from. When an empty object or an object with a `tag: 0` is provided, it lists and removes all the messages.

try:
    # Get the list of messages currently present in the nodes message inbox.
    api_response = api_instance.pop_all(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->pop_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TagQueryRequest**](TagQueryRequest.md)| Tag of message queue to pop from. When an empty object or an object with a &#x60;tag: 0&#x60; is provided, it lists and removes all the messages. | 

### Return type

[**MessagePopAllResponse**](MessagePopAllResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> SendMessageResponse send_message(body)

Send a message to another peer using the given path.

Send a message to another peer using the given path.  The message can be sent either over a specified path or using a specified number of HOPS, if no path is given.

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.SendMessageBodyRequest() # SendMessageBodyRequest | Body of a message to send

try:
    # Send a message to another peer using the given path.
    api_response = api_instance.send_message(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendMessageBodyRequest**](SendMessageBodyRequest.md)| Body of a message to send | 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **size**
> SizeResponse size(tag=tag)

Get size of filtered message inbox for a specific tag

Get size of filtered message inbox for a specific tag

### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.MessagesApi(hoprd_sdk.ApiClient(configuration))
tag = 56 # int |  (optional)

try:
    # Get size of filtered message inbox for a specific tag
    api_response = api_instance.size(tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->size: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **int**|  | [optional] 

### Return type

[**SizeResponse**](SizeResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

