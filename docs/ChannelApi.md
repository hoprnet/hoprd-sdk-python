# hoprd_sdk.ChannelApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_tickets_in_channel**](ChannelApi.md#aggregate_tickets_in_channel) | **POST** /api/v3/channels/{channelId}/tickets/aggregate | 
[**redeem_tickets_in_channel**](ChannelApi.md#redeem_tickets_in_channel) | **POST** /api/v3/channels/{channelId}/tickets/redeem | 

# **aggregate_tickets_in_channel**
> aggregate_tickets_in_channel(channel_id)



### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = hoprd_sdk.ChannelApi(hoprd_sdk.ApiClient(configuration))
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    api_instance.aggregate_tickets_in_channel(channel_id)
except ApiException as e:
    print("Exception when calling ChannelApi->aggregate_tickets_in_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| ID of the channel. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_tickets_in_channel**
> redeem_tickets_in_channel(channel_id)



### Example
```python
from __future__ import print_function
import time
import hoprd_sdk
from hoprd_sdk.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = hoprd_sdk.ChannelApi(hoprd_sdk.ApiClient(configuration))
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    api_instance.redeem_tickets_in_channel(channel_id)
except ApiException as e:
    print("Exception when calling ChannelApi->redeem_tickets_in_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| ID of the channel. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

