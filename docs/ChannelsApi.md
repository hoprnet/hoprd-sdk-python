# hoprd_sdk.ChannelsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_tickets_in_channel**](ChannelsApi.md#aggregate_tickets_in_channel) | **POST** /api/v3/channels/{channelId}/tickets/aggregate | Starts aggregation of tickets in the given channel.
[**close_channel**](ChannelsApi.md#close_channel) | **DELETE** /api/v3/channels/{channelId} | Closes the given channel.
[**fund_channel**](ChannelsApi.md#fund_channel) | **POST** /api/v3/channels/{channelId}/fund | Funds the given channel with the given amount of HOPR tokens.
[**list_channels**](ChannelsApi.md#list_channels) | **GET** /api/v3/channels | Lists channels opened to/from this node. Alternatively, it can print all
[**open_channel**](ChannelsApi.md#open_channel) | **POST** /api/v3/channels | Opens a channel to the given on-chain address with the given initial stake of HOPR tokens.
[**redeem_tickets_in_channel**](ChannelsApi.md#redeem_tickets_in_channel) | **POST** /api/v3/channels/{channelId}/tickets/redeem | Starts redeeming all tickets in the given channel.
[**show_channel**](ChannelsApi.md#show_channel) | **GET** /api/v3/channels/{channelId} | Returns information about the given channel.
[**show_channel_tickets**](ChannelsApi.md#show_channel_tickets) | **GET** /api/v3/channels/{channelId}/tickets | Lists all tickets for the given channel  ID.

# **aggregate_tickets_in_channel**
> aggregate_tickets_in_channel(channel_id)

Starts aggregation of tickets in the given channel.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    # Starts aggregation of tickets in the given channel.
    api_instance.aggregate_tickets_in_channel(channel_id)
except ApiException as e:
    print("Exception when calling ChannelsApi->aggregate_tickets_in_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| ID of the channel. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_channel**
> CloseChannelResponse close_channel(channel_id)

Closes the given channel.

If the channel is currently `Open`, it will transition it to `PendingToClose`. If the channels is in `PendingToClose` and the channel closure period has elapsed, it will transition it to `Closed`.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    # Closes the given channel.
    api_response = api_instance.close_channel(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->close_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| ID of the channel. | 

### Return type

[**CloseChannelResponse**](CloseChannelResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fund_channel**
> str fund_channel(body, channel_id)

Funds the given channel with the given amount of HOPR tokens.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.FundBodyRequest() # FundBodyRequest | Specifies the amount of HOPR tokens to fund a channel with.
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    # Funds the given channel with the given amount of HOPR tokens.
    api_response = api_instance.fund_channel(body, channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->fund_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FundBodyRequest**](FundBodyRequest.md)| Specifies the amount of HOPR tokens to fund a channel with. | 
 **channel_id** | **str**| ID of the channel. | 

### Return type

**str**

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_channels**
> NodeChannelsResponse list_channels(including_closed=including_closed, full_topology=full_topology)

Lists channels opened to/from this node. Alternatively, it can print all

the channels in the network as this node sees them.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
including_closed = true # bool | Should be the closed channels included? (optional)
full_topology = true # bool | Should all channels (not only the ones concerning this node) be enumerated? (optional)

try:
    # Lists channels opened to/from this node. Alternatively, it can print all
    api_response = api_instance.list_channels(including_closed=including_closed, full_topology=full_topology)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->list_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **including_closed** | **bool**| Should be the closed channels included? | [optional] 
 **full_topology** | **bool**| Should all channels (not only the ones concerning this node) be enumerated? | [optional] 

### Return type

[**NodeChannelsResponse**](NodeChannelsResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_channel**
> OpenChannelResponse open_channel(body)

Opens a channel to the given on-chain address with the given initial stake of HOPR tokens.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.OpenChannelBodyRequest() # OpenChannelBodyRequest | Open channel request specification: on-chain address of the counterparty and the initial HOPR token stake.

try:
    # Opens a channel to the given on-chain address with the given initial stake of HOPR tokens.
    api_response = api_instance.open_channel(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->open_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenChannelBodyRequest**](OpenChannelBodyRequest.md)| Open channel request specification: on-chain address of the counterparty and the initial HOPR token stake. | 

### Return type

[**OpenChannelResponse**](OpenChannelResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_tickets_in_channel**
> redeem_tickets_in_channel(channel_id)

Starts redeeming all tickets in the given channel.

**WARNING:** this should almost **never** be used as it can issue a large number of on-chain transactions. The tickets should almost always be aggregated first.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    # Starts redeeming all tickets in the given channel.
    api_instance.redeem_tickets_in_channel(channel_id)
except ApiException as e:
    print("Exception when calling ChannelsApi->redeem_tickets_in_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| ID of the channel. | 

### Return type

void (empty response body)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_channel**
> ChannelInfoResponse show_channel(channel_id)

Returns information about the given channel.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    # Returns information about the given channel.
    api_response = api_instance.show_channel(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->show_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| ID of the channel. | 

### Return type

[**ChannelInfoResponse**](ChannelInfoResponse.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_channel_tickets**
> list[ChannelTicket] show_channel_tickets(channel_id)

Lists all tickets for the given channel  ID.

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
api_instance = hoprd_sdk.ChannelsApi(hoprd_sdk.ApiClient(configuration))
channel_id = 'channel_id_example' # str | ID of the channel.

try:
    # Lists all tickets for the given channel  ID.
    api_response = api_instance.show_channel_tickets(channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->show_channel_tickets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| ID of the channel. | 

### Return type

[**list[ChannelTicket]**](ChannelTicket.md)

### Authorization

[api_token](../README.md#api_token), [bearer_token](../README.md#bearer_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

