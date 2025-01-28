# GraphExportQuery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_disconnected_components** | **bool** | If set, nodes that are not connected to this node (via open channels) will not be exported. This setting automatically implies &#x60;ignore_non_opened_channels&#x60;. | [optional] [default to False]
**ignore_non_opened_channels** | **bool** | Do not export channels that are not in the &#x60;Open&#x60; state. | [optional] [default to False]
**raw_graph** | **bool** | Export the entire graph in raw JSON format, that can be later used to load the graph into e.g. a unit test.  Note that &#x60;ignore_disconnected_components&#x60; and &#x60;ignore_non_opened_channels&#x60; are ignored. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

