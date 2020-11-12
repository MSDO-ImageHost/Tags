# API Reference
## ConfirmTagCreation
Response: [ConfirmTagCreation](TagsLink#ConfirmTagCreation) 
```json
{
  "Tag_ID": "<TAG_ID>",
  "Create_status": "True/False"
}
```
Request: [Gateway](GatewayLink)/[GatewayCreateTag](GatewayLink#CreateTag)
## ConfirmTagUpdate
Response: [ConfirmTagUpdate](TagsLink#ConfirmTagUpdate) 
```json
{
  "Tag_ID": "<TAG_ID>",
  "Change_status": "True/False"
}
```
Request: [UpdateTag](GatewayLink#UpdateTag)
```json
{
  "Tag_ID": "<TAG_ID>",
  "Tag_name": "<New_Tag-name> OR NULL",
  "Tag_desc": "<New_Tag-desc> OR NULL" 
}
```
## ConfirmTagDelete
Response: [ConfirmTagDelete](TagsDocLink#ConfirmTagDelete) 
```json
{
  "Delete_status": "True/False"
}
```
Request: [DeleteTag](GatewayDocLink#DeleteTag)
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
## ReturnTag
Response: [ReturnTag](TagsDocLink#ReturnTag) 
```json
{
  "Tag_Name": "<Tag-name>",
  "Tag_Desc": "<Tag-desc>",
}
```
Request: [RequestTag](GatewayDocLink#RequestTag)
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
## ReturnTagsForPost
Response: [ReturnTagsForPost](TagsLink#ReturnTagsForPost)
```json
{
  "Tag_IDs": "[<Tag-ID1>, <Tag-ID2>, ...]"
}
```
Request: [RequestTagsForPost](GatewayLink#RequestTagsForPost)
```json
{
  "Post_ID": "<Post_ID>"
}
```
