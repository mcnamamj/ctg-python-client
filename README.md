# What is this?

This repo runs [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) against the CTG (ClinicalTrials.gov) OpenAPI spec to create a generic python library for interacting with the new API endpoint.

# How to update?

If you want to update the downloaded specification with the latest version from clinicaltrials.gov, use: 

```
curl https://clinicaltrials.gov/api/oas/v2 > ctg-openapi-specification.yaml
git add ctg-openapi-specification.yaml
```

Then you'll load in that specification and the local settings via:

```
openapi-python-client update --path ctg-openapi-specification.yaml --config openapi-settings.yaml
```
