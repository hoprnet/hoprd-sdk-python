# SessionClientRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**list[SessionCapability]**](SessionCapability.md) | Capabilities for the Session protocol.  Defaults to &#x60;Segmentation&#x60; and &#x60;Retransmission&#x60; for TCP and nothing for UDP. | [optional] 
**destination** | **str** | Peer ID of the Exit node. | 
**listen_host** | **str** | Listen host (&#x60;ip:port&#x60;) for the Session socket at the Entry node.  Supports also partial specification (only &#x60;ip&#x60; or only &#x60;:port&#x60;) with the respective part replaced by the node&#x27;s configured default. | [optional] 
**path** | [**RoutingOptions**](RoutingOptions.md) |  | 
**target** | [**SessionTargetSpec**](SessionTargetSpec.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

