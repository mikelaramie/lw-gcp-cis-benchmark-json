# Overview

This repo provides example JSON body sections to enable and disable the CIS Benchmarks for GCP in Lacework when calling the PATCH method on *https://lacework-tenant.lacework.net/api/v1/external/recommendations/gcp* API Endpoint

# Script
This repo also includes an example script that can be used to perform the config, with a requirement of having curl and the Lacework CLI installed.  Usage is:

`gcp-cis-config.sh [disable_cis_10|disable_cis_12|enable_cis_12] [lacework-tenant] [lacework-subaccount]`

Where the first argument is the action you wish to perform, the second argument is your lacework tenant (without the `.lacework.net`) and the third argument is the subaccount where the GCP for Lacework is configured.

# Further information

`lacework-tenant` If you are in the Frankfurt datacenter you need to specify this as `tenant.fra`

`lacework-subaccount` If you Lacework tenant is enrolled in an organization then you need to specify the name of the subaccount. If this is not the case then ignore the third argument.
