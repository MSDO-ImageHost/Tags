# API Reference

## General
### Access control
Any request to Tags must contain a valid jwt in the header fields.

### Metadata
A response from Tags will contain some metadata, accessible via the properties of the response message. The properties will include correlation_id and content_type fields, along with a header field. The header field looks as follows:
```json
{
  "status_code": "<http status code>",
  "message": "<message describing the status code>"
}
```

## Tags

### ConfirmTagCreation
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/CreateTag
```json
{
  "tag_name": "<Tag name>",
  "tag_desc": "<Tag desc>",
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ConfirmTagCreation](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagCreation) 
```json
{
  "tag_id": "<TAG_ID>",
  "created_at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
### ConfirmTagUpdate
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/UpdateTag
```json
{
  "tag_id": "<TAG_ID>",
  "tag_name": "<New_Tag-name> OR NULL",
  "tag_desc": "<New_Tag-desc> OR NULL" 
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
  "tag_id": "<Tag-ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ConfirmTagDelete](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagDelete) 
```json
{
  "deleted_at": "<ISO8601 timestamp>"
}
```
[HTTP status code](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

### ConfirmAddedTag
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/AddTagToPost
```json
{
  "tag_id": "<Tag-ID>",
  "post_id": "<Tag-ID>",
  "post_author": "<User-ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ConfirmAddedTag](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmAddedTag)
```json
{
  "tag_id": "<Tag-ID>",
  "post_id": "<Post-ID>"
}
```

### ConfirmTagRemoval
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/RemoveTagFromPost
```json
{
  "tag_id": "<Tag-ID>",
  "post_id": "<Tag-ID>",
  "post_author": "<User-ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ConfirmTagRemoval](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ConfirmTagRemoval)
```json
{
  "removed_at": "<ISO8601 timestamp>"
}
```

### ReturnTag
Request: [Gateway](https://github.com/MSDO-ImageHost/Gateway)/RequestTag
```json
{
  "tag_id": "<Tag-ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ReturnTag](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ReturnTag) 
```json
{
  "tag_id": "<Tag-ID>",
  "author": "<User ID>",
  "tag_name": "<Tag-name>",
  "tag_desc": "<Tag-desc>",
  "created_at": "<ISO8601 timestamp>",
  "updated_at": "<ISO8601 timestamp>"
}
```
### ReturnTagsForPost
Request: [Posts](https://github.com/MSDO-ImageHost/Posts)/RequestTagsForPost
```json
{
  "post_id": "<Post_ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ReturnTagsForPost](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ReturnTagsForPost) 
```json
[
  {
    "tag_id": "<Tag-ID>",
    "author": "<User ID>",
    "tag_name": "<Tag-name>",
    "tag_desc": "<Tag-desc>",
    "created_at": "<ISO8601 timestamp>",
    "updated_at": "<ISO8601 timestamp>"
  }
  ...
]
```

### ReturnPostsForTag
Request: [Posts](https://github.com/MSDO-ImageHost/Posts)/RequestTagsForPost
```json
{
  "tag_id": "<Tag-ID>"
}
```
Response: [Tags](https://github.com/MSDO-ImageHost/Tags)/[ReturnTagsForPost](https://github.com/MSDO-ImageHost/Tags/blob/main/docs/api-spec.md#ReturnTagsForPost) 
```json
[
  {
    "post_id": "<Post-ID>"
  }
  ...
]
```

