SPEC=http://api.vedh.io/api/v1/swagger/?format=openapi 
# SPEC=http://localhost:8000/api/v1/swagger/?format=openapi 
openapi-generator generate -g python -i $SPEC --package-name veros_api
