# Channel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Channel can be either incomming or outgoing. Incomming means that other node can send messages using this node as relay. Outgoing means that this node can use other node to send message as realy. | [optional] 
**channel_id** | **str** | Channel ID that can be used in other calls, not to confuse with transaction hash. | [optional] 
**peer_id** | [**HoprAddress**](HoprAddress.md) |  | [optional] 
**status** | [**ChannelStatus**](ChannelStatus.md) |  | [optional] 
**balance** | [**HoprBalance**](HoprBalance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

