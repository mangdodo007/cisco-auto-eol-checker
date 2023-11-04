# Cisco Automate EOL Checkers

This tool is used to check Cisco End Of Life (EOL) information based on a serial number.

## Prerequisites

- You need to register for the EOX API at [Cisco API Console](https://apiconsole.cisco.com) to obtain a client ID and client secret.
- After you have both the client ID and client secret, you need to modify the code in `main.py`:

  ```python
  YOUR_CLIENT_ID = "xxx"
  YOUR_CLIENT_SECRET = "xxx"
- Install any required libraries using the following command:

  ```shell
  pip install -r requirements.txt

## How to Use
1. Run main.py.
2. Input a serial number.
3. After running, you will see information about EOL in JSON format, like this:
   ```json
    {
    "PaginationResponseRecord": {
        "PageIndex": 1,
        "LastIndex": 1,
        "TotalRecords": 1,
        "PageRecords": 1
    },
    "EOXRecord": [
        {
        "EOLProductID": "WS-C6506",
        "ProductIDDescription": "Cat 6506 Chassis, 6-slot, 12RU, No Power Supply, No Fan Tray",
        "ProductBulletinNumber": "3037",
        "LinkToProductBulletinURL": "http://www.cisco.com/en/US/products/hw/switches/ps708/prod_eol_notice0900aecd8035ece4.html",
        "EOXExternalAnnouncementDate": {
            "value": "2005-11-01",
            "dateFormat": "YYYY-MM-DD"
        },
        "EndOfSaleDate": {
            "value": "2006-11-01",
            "dateFormat": "YYYY-MM-DD"
        },
        "EndOfSWMaintenanceReleases": {
            "value": "2007-11-01",
            "dateFormat": "YYYY-MM-DD"
        },
        "EndOfSecurityVulnerabilitySupportDate": {
            "value": "",
            "dateFormat": "YYYY-MM-DD"
        },
        "EndOfRoutineFailureAnalysisDate": {
            "value": "2007-11-01",
            "dateFormat": "YYYY-MM-DD"
        },
        "EndOfServiceContractRenewal": {
            "value": "2012-08-01",
            "dateFormat": "YYYY-MM-DD"
        },
        "LastDateOfSupport": {
            "value": "2012-11-30",
            "dateFormat": "YYYY-MM-DD"
        },
        "EndOfSvcAttachDate": {
            "value": "2007-11-01",
            "dateFormat": "YYYY-MM-DD"
        },
        "UpdatedTimeStamp": {
            "value": "2011-10-28",
            "dateFormat": "YYYY-MM-DD"
        },
        "EOXMigrationDetails": {
            "PIDActiveFlag": "Y",
            "MigrationInformation": "Catalyst 6500 Enhanced 6-slot chassis, 12RU, no PS, no Fan Tray",
            "MigrationOption": "Enter PID(s)",
            "MigrationProductId": "WS-C6506-E",
            "MigrationProductName": "",
            "MigrationStrategy": "",
            "MigrationProductInfoURL": ""
        },
        "EOXInputType": "ShowEOXBySerialNumber",
        "EOXInputValue": "TBA03270652"
        }
    ]
    }
   ```
- yo're done!


## Note
This project is provided as a sample. If you need to adapt this code to your environment, you can edit and modify it. For example, you may want to change the input method to use an Excel or text file for checking multiple devices.
