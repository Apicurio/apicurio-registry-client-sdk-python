## Service Registry SDK Examples

Examples for APIcurio service registry.

## Perequisites

1. Create .env file
```
touch .env
```
2. Open file and add url to the service registry.
For example when using Managed Service Registry Service 
```
SERVICE_REGISTRY_URL=https://3.serviceregistry.rhcloud.com/t/f21a297d-e6ea-49de-99b9-2a231018b7c5/apis/registry/v2
```

> NOTE: Please note that URL requires `apis/registry/v2` suffix to perform API calls

3. If you are using service registy instance that requires authentication you need to specify
username and password for authentication:

```
SERVICE_ACCOUNT_CLIENT_ID=srvc-acct-0
SERVICE_ACCOUNT_CLIENT_SECRET=b288da06-57ee-46c0-b708
```

## Examples

### Artifacts downloader

Artifacts downloader example shows how to 
download all artifacts from into your local file system

To run example execute: 
```
python3 api/example_artifacts_downloader.py 
```

> NOTE: please consider changing group_id variable to point to different artifact group.

Example will create all artifact files in `./temp` folder. 
 
### JSON Validator

Artifacts JSON validator example showcases end to end JSON schema validation
based on the artifacts stored in the Apicurio registry.

To run example execute:

```
python3 api/example_json_validator.py  
```

> NOTE: Example uses default group and will create new `message` artifact in your registry.

Example uses `artifact_validator.py` module that can be reused in other projects to provide 
out of the box validation for JSON Schemas.

