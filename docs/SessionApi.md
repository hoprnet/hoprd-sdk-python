# hoprd_sdk.SessionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_client**](SessionApi.md#close_client) | **DELETE** /api/v3/session/{protocol}/{ip}/{port} | Closes an existing Session listener.
[**create_client**](SessionApi.md#create_client) | **POST** /api/v3/session/{protocol} | Creates a new client session returning the given session listening host and port over TCP or UDP.
[**list_clients**](SessionApi.md#list_clients) | **GET** /api/v3/session/{protocol} | Lists existing Session listeners for the given IP protocol.

# **close_client**
> close_client(protocol, ip, port)

Closes an existing Session listener.

The listener must've been previously created and bound for the given IP protocol. Once a listener is closed, no more socket connections can be made to it. If the passed port number is 0, listeners on all ports of the given listening IP and protocol will be closed.

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
api_instance = hoprd_sdk.SessionApi(hoprd_sdk.ApiClient(configuration))
protocol = hoprd_sdk.IpProtocol() # IpProtocol | 
ip = 'ip_example' # str | 
port = 56 # int | 

try:
    # Closes an existing Session listener.
    api_instance.close_client(protocol, ip, port)
except ApiException as e:
    print("Exception when calling SessionApi->close_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | [**IpProtocol**](.md)|  | 
 **ip** | **str**|  | 
 **port** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client**
> SessionClientResponse create_client(body, protocol)

Creates a new client session returning the given session listening host and port over TCP or UDP.

If no listening port is given in the request, the socket will be bound to a random free port and returned in the response. Different capabilities can be configured for the session, such as data segmentation or retransmission.  Once the host and port are bound, it is possible to use the socket for bidirectional read/write communication over the selected IP protocol and HOPR network routing with the given destination. The destination HOPR node forwards all the data to the given target over the selected IP protocol.  Various services require different types of socket communications: - services running over UDP usually do not require data retransmission, as it is already expected that UDP does not provide these and is therefore handled at the application layer. - On the contrary, services running over TCP *almost always* expect data segmentation and retransmission capabilities, so these should be configured while creating a session that passes TCP data.

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
api_instance = hoprd_sdk.SessionApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.SessionClientRequest() # SessionClientRequest | Creates a new client HOPR session that will start listening on a dedicated port. Once the port is bound, it is possible to use the socket for bidirectional read and write communication.
protocol = 'protocol_example' # str | IP transport protocol

try:
    # Creates a new client session returning the given session listening host and port over TCP or UDP.
    api_response = api_instance.create_client(body, protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionClientRequest**](SessionClientRequest.md)| Creates a new client HOPR session that will start listening on a dedicated port. Once the port is bound, it is possible to use the socket for bidirectional read and write communication. | 
 **protocol** | **str**| IP transport protocol | 

### Return type

[**SessionClientResponse**](SessionClientResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> list[SessionClientResponse] list_clients(protocol)

Lists existing Session listeners for the given IP protocol.

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
api_instance = hoprd_sdk.SessionApi(hoprd_sdk.ApiClient(configuration))
protocol = 'protocol_example' # str | IP transport protocol

try:
    # Lists existing Session listeners for the given IP protocol.
    api_response = api_instance.list_clients(protocol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SessionApi->list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocol** | **str**| IP transport protocol | 

### Return type

[**list[SessionClientResponse]**](SessionClientResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

