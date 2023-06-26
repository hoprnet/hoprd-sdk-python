# swagger_client.MessagesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**message_sign**](MessagesApi.md#message_sign) | **POST** /message/sign | 
[**messages_send_message**](MessagesApi.md#messages_send_message) | **POST** /messages/ | 
[**messages_sign**](MessagesApi.md#messages_sign) | **POST** /messages/sign | 
[**messages_websocket**](MessagesApi.md#messages_websocket) | **GET** /messages/websocket | 

# **message_sign**
> InlineResponse2004 message_sign(body=body)



Signs a message given using the node’s private key. Prefixes messsage with “HOPR Signed Message: ” before signing.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MessageSignBody() # MessageSignBody |  (optional)

try:
    api_response = api_instance.message_sign(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->message_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageSignBody**](MessageSignBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MessagesBody() # MessagesBody |  (optional)

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

# **messages_sign**
> InlineResponse2004 messages_sign(body=body)



Signs a message given using the node’s private key. Prefixes messsage with “HOPR Signed Message: ” before signing.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))
body = swagger_client.MessagesSignBody() # MessagesSignBody |  (optional)

try:
    api_response = api_instance.messages_sign(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_sign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagesSignBody**](MessagesSignBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_websocket**
> str messages_websocket()



This is a websocket endpoint which exposes a subset of message functions. Incoming messages from other nodes are sent to the websocket client in stringified Uint8Array instance of rlp-encoded data. A client may also send message by sending the following data:   { cmd: \"sendmsg\", args: { recipient: \"SOME_PEER_ID\", path: [], hops: 1} } The command arguments follow the same semantics as in the dedicated API endpoint for sending messages.  Authentication (if enabled) is done via either passing an `apiToken` parameter in the url or cookie `X-Auth-Token`. Connect to the endpoint by using a WS client. No preview available. Example: `ws://127.0.0.1:3001/api/v2/messages/websocket/?apiToken=myApiToken`

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: keyScheme
configuration = swagger_client.Configuration()
configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-auth-token'] = 'Bearer'# Configure HTTP basic authorization: passwordScheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MessagesApi(swagger_client.ApiClient(configuration))

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

