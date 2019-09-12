SPEC=http://api.vedh.io/api/v1/swagger/?format=openapi 
openapi-generator generate -g python -i $SPEC --package-name api
