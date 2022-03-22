rm -Rf ./openapi
wget https://raw.githubusercontent.com/Apicurio/apicurio-registry/master/app/src/main/resources-unfiltered/META-INF/resources/api-specifications/registry/v2/openapi.json -P ./openapi
rm -Rf ./apicurioregistryclient

echo "applying diff to enable basic auth - might need some manual changes"
git apply ./openapi/openapi.diff ./openapi/openapi.json

echo "Generating SDK"
npx @openapitools/openapi-generator-cli generate -g python \
    -i openapi/openapi.json -p "packageName=apicurioregistryclient" \
    --ignore-file-override=.openapi-generator-ignore \
    --git-user-id=Apicurio \
    --git-repo-id=apicurio-registry-client-sdk-python \
    -t .github/templates

    