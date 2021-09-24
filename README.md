# Overview

This repo provides example JSON body sections to enable and disable the CIS Benchmarks for GCP in Lacework when calling the PATCH method on *https://lacework-tenant.lacework.net/api/v1/external/recommendations/gcp* API Endpoint

# Script
This repo also includes an example script that can be used to perform the config, with a requirement of having curl and the Lacework CLI installed.  Usage is:

`gcp-cis-config.sh [disable_cis_10|disable_cis_12|enable_cis_12] [lacework-tenant]`

Where the first argument is the action you wish to perform, and the second argument is your lacework tenant (without the `.lacework.net`)
