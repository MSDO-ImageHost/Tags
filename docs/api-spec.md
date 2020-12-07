# API Reference

## General
### Access control
Any request to Tags must contain a valid jwt in the header fields.

### Metadata
A response from Tags will contain some metadata, accessible via the properties of the response message. The properties will include correlation_id and content_type fields, along with a header field. The header field looks as follows:
```json
{
  "jwt": "<jwt token>",
  "status_code": "<http status code>",
  "message": "<message describing the status code>"
}
```

## Tags

### ConfirmTagCreation
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/CreateTag
```json
{
  "Tag_Name": "<Tag name>",
  "Tag_Desc": "<Tag desc>",
  "Post_ID": "<POST_ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ConfirmTagCreation](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagCreation) 
```json
{
  "Tag_ID": "<TAG_ID>",
  "Created_at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
### ConfirmTagUpdate
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/UpdateTag
```json
{
  "Tag_ID": "<TAG_ID>",
  "Tag_name": "<New_Tag-name> OR NULL",
  "Tag_desc": "<New_Tag-desc> OR NULL" 
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ConfirmTagUpdate](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagUpdate) 
```json
{
  "Updated_at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
### ConfirmTagDelete
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/DeleteTag
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ConfirmTagDelete](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagDelete) 
```json
{
  "deleted_at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
### ReturnTag
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/RequestTag
```json
{
  "Tag_ID": "<Tag-ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ReturnTag](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ReturnTag) 
```json
{
  "Tag_ID": "<Tag-ID>",
  "Post_ID": "<POST_ID>",
  "Author": "<User ID>",
  "Tag_Name": "<Tag-name>",
  "Tag_Desc": "<Tag-desc>",
  "Created_at": "<ISO8601 timestamp>",
  "Updated_at": "<ISO8601 timestamp>"
}
```
### ReturnTagsForPost
Request: [Posts](https://github.com/MSDO-ImageHost/Posts)/RequestTagsForPost
```json
{
  "Post_ID": "<Post_ID>"
}
```
List of tags 
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ReturnTagsForPost](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ReturnTagsForPost) 
```json
{
  [
    "Tag_ID": "<Tag-ID>",
    "Post_ID": "<POST_ID>",
    "Author": "<User ID>",
    "Tag_Name": "<Tag-name>",
    "Tag_Desc": "<Tag-desc>",
    "Created_at": "<ISO8601 timestamp>",
    "Updated_at": "<ISO8601 timestamp>"
  ]
  ...
}
```
