# InlineResponse2002

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | Name of the network the node is running on. | [optional] 
**announced_address** | **list[str]** |  | [optional] 
**listening_address** | **list[str]** |  | [optional] 
**chain** | **str** | Name of the Hopr network this node connects to. | [optional] 
**hopr_token** | **str** | Contract address of the Hopr token on the ethereum chain. | [optional] 
**hopr_channels** | **str** | Contract address of the HoprChannels smart contract on ethereum chain. This smart contract is used to open payment channels between nodes on blockchain. | [optional] 
**hopr_network_registry_address** | **str** | Contract address of the contract that allows to control the number of nodes in the network | [optional] 
**connectivity_status** | **str** | Indicates how good is the connectivity of this node to the HOPR network: either RED, ORANGE, YELLOW or GREEN | [optional] 
**is_eligible** | **bool** | Determines whether the staking account associated with this node is eligible for accessing the HOPR network. Always true if network registry is disabled. | [optional] 
**channel_closure_period** | **float** | Time (in minutes) that this node needs in order to clean up before closing the channel. When requesting to close the channel each node needs some time to make sure that channel can be closed securely and cleanly. After this channelClosurePeriod passes the second request for closing channel will close the channel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

