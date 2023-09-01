# ChannelTopology

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | [**ChannelId**](ChannelId.md) |  | [optional] 
**source_peer_id** | [**HoprAddress**](HoprAddress.md) |  | [optional] 
**destination_peer_id** | [**HoprAddress**](HoprAddress.md) |  | [optional] 
**source_address** | [**NativeAddress**](NativeAddress.md) |  | [optional] 
**destination_address** | [**NativeAddress**](NativeAddress.md) |  | [optional] 
**balance** | [**HoprBalance**](HoprBalance.md) |  | [optional] 
**status** | [**ChannelStatus**](ChannelStatus.md) |  | [optional] 
**ticket_index** | **str** | Each ticket is labeled by an ongoing serial number named ticket index i and its current value is stored in the smart contract. | [optional] 
**channel_epoch** | **str** | Payment channels might run through multiple open and close sequences, this epoch tracks the sequence. | [optional] 
**closure_time** | **str** | Time when the channel can be closed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

