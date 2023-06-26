# swagger_client.TicketsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tickets_get_statistics**](TicketsApi.md#tickets_get_statistics) | **GET** /tickets/statistics | 
[**tickets_get_tickets**](TicketsApi.md#tickets_get_tickets) | **GET** /tickets/ | 
[**tickets_redeem_tickets**](TicketsApi.md#tickets_redeem_tickets) | **POST** /tickets/redeem | 

# **tickets_get_statistics**
> InlineResponse200 tickets_get_statistics()



Get statistics regarding all your tickets. Node gets a ticket everytime it relays data packet in channel.

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.tickets_get_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_get_statistics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickets_get_tickets**
> list[Ticket] tickets_get_tickets()



Get all tickets earned by relaying data packets by your node from every channel.

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.tickets_get_tickets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_get_tickets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Ticket]**](Ticket.md)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tickets_redeem_tickets**
> tickets_redeem_tickets()



Redeems all tickets from all the channels and exchanges them for Hopr tokens. Every ticket have a chance to be winning one, rewarding you with Hopr tokens.

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
api_instance = swagger_client.TicketsApi(swagger_client.ApiClient(configuration))

try:
    api_instance.tickets_redeem_tickets()
except ApiException as e:
    print("Exception when calling TicketsApi->tickets_redeem_tickets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[keyScheme](../README.md#keyScheme), [passwordScheme](../README.md#passwordScheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

