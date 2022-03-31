## Service Registry SDK Examples

Examples for APIcurio service registry.

## Prerequisites

1. Install package locally

```
pip install .
pip install jsonschema python-dotenv
```

2. Create .env file
```
cd examples
touch .env
```

3. Open file and add url to the service registry.
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

> NOTE: For managed version of Registry please follow [official guide for creating service accounts](https://github.com/redhat-developer/app-services-guides/blob/main/docs/registry/rhoas-cli-getting-started-registry/README.adoc#proc-creating-service-registry-account_getting-started-rhoas-service-registry) 

## Examples

### Artifacts downloader

Artifacts downloader example shows how to 
download all artifacts from into your local file system

To run example execute: 
```
python3 api/example_artifacts_downloader.py <optional-group-id>
```

If `<optional-group-id>` is not passed, "default" will be used.

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

Example also includes protobuf file that can be used to generate Python code for parsing GRPC requests.
For more information see: https://developers.google.com/protocol-buffers/docs/pythontutorial

