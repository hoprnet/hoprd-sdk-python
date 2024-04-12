# hoprd-sdk
API server using the hopr-lib created HOPR node and exposing it using a HTTP REST API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.2.1
- Package version: 2.1.0-rc.3
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import hoprd_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hoprd_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get node's HOPR and native addresses.
    api_response = api_instance.addresses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->addresses: %s\n" % e)

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))

try:
    # Get node's and associated Safe's HOPR and native balances as the allowance for HOPR
    api_response = api_instance.balances()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->balances: %s\n" % e)

# Configure API key authorization: api_token
configuration = hoprd_sdk.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = hoprd_sdk.AccountApi(hoprd_sdk.ApiClient(configuration))
body = hoprd_sdk.WithdrawBodyRequest() # WithdrawBodyRequest | 

try:
    # Withdraw funds from this node to the ethereum wallet address.
    api_response = api_instance.withdraw(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->withdraw: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**addresses**](docs/AccountApi.md#addresses) | **GET** /api/v3/account/addresses | Get node&#x27;s HOPR and native addresses.
*AccountApi* | [**balances**](docs/AccountApi.md#balances) | **GET** /api/v3/account/balances | Get node&#x27;s and associated Safe&#x27;s HOPR and native balances as the allowance for HOPR
*AccountApi* | [**withdraw**](docs/AccountApi.md#withdraw) | **POST** /api/v3/account/withdraw | Withdraw funds from this node to the ethereum wallet address.
*AliasApi* | [**aliases**](docs/AliasApi.md#aliases) | **GET** /api/v3/aliases | Get each previously set alias and its corresponding PeerId
*AliasApi* | [**delete_alias**](docs/AliasApi.md#delete_alias) | **DELETE** /api/v3/aliases/{alias} | Delete an alias.
*AliasApi* | [**get_alias**](docs/AliasApi.md#get_alias) | **GET** /api/v3/aliases/{alias} | Get alias for the PeerId (Hopr address) that have this alias assigned to it.
*AliasApi* | [**set_alias**](docs/AliasApi.md#set_alias) | **POST** /api/v3/aliases | Set alias for a peer with a specific PeerId.
*ChannelsApi* | [**aggregate_tickets_in_channel**](docs/ChannelsApi.md#aggregate_tickets_in_channel) | **POST** /api/v3/channels/{channelId}/tickets/aggregate | Starts aggregation of tickets in the given channel.
*ChannelsApi* | [**close_channel**](docs/ChannelsApi.md#close_channel) | **DELETE** /api/v3/channels/{channelId} | Closes the given channel.
*ChannelsApi* | [**fund_channel**](docs/ChannelsApi.md#fund_channel) | **POST** /api/v3/channels/{channelId}/fund | Funds the given channel with the given amount of HOPR tokens.
*ChannelsApi* | [**list_channels**](docs/ChannelsApi.md#list_channels) | **GET** /api/v3/channels | Lists channels opened to/from this node. Alternatively, it can print all
*ChannelsApi* | [**open_channel**](docs/ChannelsApi.md#open_channel) | **POST** /api/v3/channels | Opens a channel to the given on-chain address with the given initial stake of HOPR tokens.
*ChannelsApi* | [**redeem_tickets_in_channel**](docs/ChannelsApi.md#redeem_tickets_in_channel) | **POST** /api/v3/channels/{channelId}/tickets/redeem | Starts redeeming all tickets in the given channel.
*ChannelsApi* | [**show_channel**](docs/ChannelsApi.md#show_channel) | **GET** /api/v3/channels/{channelId} | Returns information about the given channel.
*ChannelsApi* | [**show_channel_tickets**](docs/ChannelsApi.md#show_channel_tickets) | **GET** /api/v3/channels/{channelId}/tickets | Lists all tickets for the given channel  ID.
*ChecksApi* | [**healthyz**](docs/ChecksApi.md#healthyz) | **GET** /healthyz | Check whether the node is healthy
*ChecksApi* | [**readyz**](docs/ChecksApi.md#readyz) | **GET** /readyz | Check whether the node is ready to accept connections.
*ChecksApi* | [**startedz**](docs/ChecksApi.md#startedz) | **GET** /startedz | Check whether the node is started.
*ConfigurationApi* | [**configuration**](docs/ConfigurationApi.md#configuration) | **GET** /api/v3/node/configuration | Get the configuration of the running node.
*MessagesApi* | [**delete_messages**](docs/MessagesApi.md#delete_messages) | **DELETE** /api/v3/messages | Delete messages from nodes message inbox.
*MessagesApi* | [**peek**](docs/MessagesApi.md#peek) | **POST** /api/v3/messages/peek | Peek the oldest message currently present in the nodes message inbox.
*MessagesApi* | [**peek_all**](docs/MessagesApi.md#peek_all) | **POST** /api/v3/messages/peek-all | Peek the list of messages currently present in the nodes message inbox, filtered by tag,
*MessagesApi* | [**pop**](docs/MessagesApi.md#pop) | **POST** /api/v3/messages/pop | Get the oldest message currently present in the nodes message inbox.
*MessagesApi* | [**pop_all**](docs/MessagesApi.md#pop_all) | **POST** /api/v3/messages/pop-all | Get the list of messages currently present in the nodes message inbox.
*MessagesApi* | [**send_message**](docs/MessagesApi.md#send_message) | **POST** /api/v3/messages | Send a message to another peer using the given path.
*MessagesApi* | [**size**](docs/MessagesApi.md#size) | **GET** /api/v3/messages/size | Get size of filtered message inbox for a specific tag
*NetworkApi* | [**price**](docs/NetworkApi.md#price) | **GET** /api/v3/network/price | Obtains the current ticket price.
*NodeApi* | [**entry_nodes**](docs/NodeApi.md#entry_nodes) | **GET** /api/v3/node/entryNodes | List all known entry nodes with multiaddrs and eligibility.
*NodeApi* | [**info**](docs/NodeApi.md#info) | **GET** /api/v3/node/info | Get information about this HOPR Node.
*NodeApi* | [**metrics**](docs/NodeApi.md#metrics) | **GET** /api/v3/node/metrics | Retrieve Prometheus metrics from the running node.
*NodeApi* | [**peers**](docs/NodeApi.md#peers) | **GET** /api/v3/node/peers | Lists information for &#x60;connected peers&#x60; and &#x60;announced peers&#x60;.
*NodeApi* | [**version**](docs/NodeApi.md#version) | **GET** /api/v3/node/version | Get release version of the running node.
*PeersApi* | [**ping_peer**](docs/PeersApi.md#ping_peer) | **POST** /api/v3/peers/{peerId}/ping | Directly pings the given peer.
*PeersApi* | [**show_peer_info**](docs/PeersApi.md#show_peer_info) | **GET** /api/v3/peers/{peerId} | Returns transport-related information about the given peer.
*TicketsApi* | [**redeem_all_tickets**](docs/TicketsApi.md#redeem_all_tickets) | **POST** /api/v3/tickets/redeem | Starts redeeming of all tickets in all channels.
*TicketsApi* | [**show_all_tickets**](docs/TicketsApi.md#show_all_tickets) | **GET** /api/v3/tickets | Returns all the tickets in all the channels.
*TicketsApi* | [**show_ticket_statistics**](docs/TicketsApi.md#show_ticket_statistics) | **GET** /api/v3/tickets/statistics | Returns current complete statistics on tickets.

## Documentation For Models

 - [AccountAddressesResponse](docs/AccountAddressesResponse.md)
 - [AccountBalancesResponse](docs/AccountBalancesResponse.md)
 - [AliasPeerIdBodyRequest](docs/AliasPeerIdBodyRequest.md)
 - [AnnouncedPeer](docs/AnnouncedPeer.md)
 - [ApiError](docs/ApiError.md)
 - [ChannelInfoResponse](docs/ChannelInfoResponse.md)
 - [ChannelTicket](docs/ChannelTicket.md)
 - [ChannelsQueryRequest](docs/ChannelsQueryRequest.md)
 - [CloseChannelResponse](docs/CloseChannelResponse.md)
 - [EntryNode](docs/EntryNode.md)
 - [FundBodyRequest](docs/FundBodyRequest.md)
 - [GetMessageBodyRequest](docs/GetMessageBodyRequest.md)
 - [HeartbeatInfo](docs/HeartbeatInfo.md)
 - [MessagePopAllResponse](docs/MessagePopAllResponse.md)
 - [MessagePopResponse](docs/MessagePopResponse.md)
 - [NodeChannel](docs/NodeChannel.md)
 - [NodeChannelsResponse](docs/NodeChannelsResponse.md)
 - [NodeInfoResponse](docs/NodeInfoResponse.md)
 - [NodePeerInfoResponse](docs/NodePeerInfoResponse.md)
 - [NodePeersQueryRequest](docs/NodePeersQueryRequest.md)
 - [NodePeersResponse](docs/NodePeersResponse.md)
 - [NodeTicketStatisticsResponse](docs/NodeTicketStatisticsResponse.md)
 - [NodeVersionResponse](docs/NodeVersionResponse.md)
 - [OpenChannelBodyRequest](docs/OpenChannelBodyRequest.md)
 - [OpenChannelResponse](docs/OpenChannelResponse.md)
 - [PeerIdResponse](docs/PeerIdResponse.md)
 - [PeerInfo](docs/PeerInfo.md)
 - [PingResponse](docs/PingResponse.md)
 - [SendMessageBodyRequest](docs/SendMessageBodyRequest.md)
 - [SendMessageResponse](docs/SendMessageResponse.md)
 - [SizeResponse](docs/SizeResponse.md)
 - [TagQueryRequest](docs/TagQueryRequest.md)
 - [TicketPriceResponse](docs/TicketPriceResponse.md)
 - [WithdrawBodyRequest](docs/WithdrawBodyRequest.md)

## Documentation For Authorization


## api_token

- **Type**: API key
- **API key parameter name**: X-Auth-Token
- **Location**: HTTP header

## bearer_token



## Author

tech@hoprnet.org
