# hoprd_sdk.TicketsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_all_tickets**](TicketsApi.md#redeem_all_tickets) | **POST** /api/v3/tickets/redeem | 
[**show_all_tickets**](TicketsApi.md#show_all_tickets) | **GET** /api/v3/tickets | 
[**show_ticket_statistics**](TicketsApi.md#show_ticket_statistics) | **GET** /api/v3/tickets/statistics | 

# **redeem_all_tickets**
> redeem_all_tickets()



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
api_instance = hoprd_sdk.TicketsApi(hoprd_sdk.ApiClient(configuration))

try:
    api_instance.redeem_all_tickets()
except ApiException as e:
    print("Exception when calling TicketsApi->redeem_all_tickets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_all_tickets**
> list[ChannelTicket] show_all_tickets()



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
api_instance = hoprd_sdk.TicketsApi(hoprd_sdk.ApiClient(configuration))

try:
    api_response = api_instance.show_all_tickets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->show_all_tickets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChannelTicket]**](ChannelTicket.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_ticket_statistics**
> NodeTicketStatisticsResponse show_ticket_statistics()



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
api_instance = hoprd_sdk.TicketsApi(hoprd_sdk.ApiClient(configuration))

try:
    api_response = api_instance.show_ticket_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TicketsApi->show_ticket_statistics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeTicketStatisticsResponse**](NodeTicketStatisticsResponse.md)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

