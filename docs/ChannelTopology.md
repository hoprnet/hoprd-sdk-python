# ChannelTopology

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_id** | **str** | Channel ID that can be used in other calls, not to confuse with transaction hash. | [optional] 
**source_peer_id** | [**HoprAddress**](HoprAddress.md) |  | [optional] 
**destination_peer_id** | [**HoprAddress**](HoprAddress.md) |  | [optional] 
**source_address** | [**NativeAddress**](NativeAddress.md) |  | [optional] 
**destination_address** | [**NativeAddress**](NativeAddress.md) |  | [optional] 
**balance** | [**HoprBalance**](HoprBalance.md) |  | [optional] 
**status** | [**ChannelStatus**](ChannelStatus.md) |  | [optional] 
**commitment** | **str** | Redeemed commitment | [optional] 
**ticket_epoch** | **str** | Ticket redemption relies on providing the value opening to a series of commitments that have previously been stored on-chain by the ticket recipient. | [optional] 
**ticket_index** | **str** | Each ticket is labeled by an ongoing serial number named ticket index i and its current value is stored in the smart contract. | [optional] 
**channel_epoch** | **str** | Payment channels might run through multiple open and close sequences, this epoch tracks the sequence. | [optional] 
**closure_time** | **str** | Time when the channel can be closed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

