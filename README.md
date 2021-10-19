# Overview

This repo provides example JSON body sections to enable and disable the CIS Benchmarks for Azure in Lacework when calling the PATCH method on *https://lacework-tenant.lacework.net/api/v1/external/recommendations/azure* API Endpoint via the Lacework CLI

# Script
## azure-cis-config.sh
This repo also includes an example script that can be used to perform the config, with a requirement of having curl and the Lacework CLI installed and configured.  Usage is:

`azure-cis-config.sh [disable_cis_10|disable_cis_12|enable_cis_12] [lacework-tenant]`

If the Lacework CLI is not configured to the same lacework-tenant provided in the ARGs the command will fail.

Where the first argument is the action you wish to perform, and the second argument is your lacework tenant (without the `.lacework.net`) eg. `dev5.dev5.corp`

## generate_checker_maps.py
This helper script can be used to generate updated versions of the checker maps based on the recommendations(checkers) deployed to the target environment.
This will update the json files in this repo