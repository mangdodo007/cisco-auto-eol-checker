import requests
import urllib3
import json
from colorama import Fore, Style, init

#  disable certificate warning
urllib3.disable_warnings()

# setup for color terminal printing
init()
print_success_terminal = f"{Fore.GREEN}SUCCESS:{Style.RESET_ALL}"
print_error_terminal = f"{Fore.RED}ERROR:{Style.RESET_ALL}"
print_info_terminal = f"{Fore.CYAN}INFO:{Style.RESET_ALL}"

# change your client id and client secret
URL_API_KEY = "https://id.cisco.com/oauth2/default/v1/token"
URL_EOX_API = "https://apix.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/1/<serial-number>"
YOUR_CLIENT_ID = "xxx"
YOUR_CLIENT_SECRET = "xxx"


def _parse_apikey(json_data):
    
    try:
        api_key = json_data["access_token"]
        return api_key
    except KeyError:
        return None

def print_cyan(data):

    return f"{Fore.CYAN}{data}{Style.RESET_ALL}"

def get_apikey():

    params = {
        "grant_type": "client_credentials",
        "client_id": YOUR_CLIENT_ID,
        "client_secret": YOUR_CLIENT_SECRET
    }
    
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    
    try:   
        response = requests.post(url=URL_API_KEY, headers=header, params=params, verify=False) # create request for get api key
        
        if response.status_code == 200:
            api_key = _parse_apikey(response.json()) # parse response to get api key
            
            print(f"{print_success_terminal} Get Api Key is Success")

            return api_key
        else:
            print(f"{print_error_terminal} Get Api Key is Failed, status code: {response.status_code}, reason: {response.reason}")
            return None
    except Exception as error:
        print(f"{print_error_terminal} Get Api Key is Failed cause Unknown Error, msg: {error}")
        return None

def get_eox_data(api_key, serial_number):

    url = URL_EOX_API.replace("<serial-number>", serial_number)
    
    header = {
        "Authorization": f"Bearer {api_key}"
    }
    
    params = {
        "responseencoding": "json",
    }
    
    
    try:
        # Get Data EOX
        response = requests.get(url=url, headers=header, params=params, verify=False)
        if response.status_code == 200:
            result = response.json()
            print(f"{print_success_terminal} Get EOX data for SN: {print_cyan(serial_number)} is Success")
            # Log the success for the system and user

            if result == "":
                result = "N/A"
                
            return result
        
        else:
            print(f"{print_error_terminal} Get EOX data for SN: {print_cyan(serial_number)} is Failed, status code: {print_cyan(response.status_code)}, reason: {print_cyan(response.reason)}")
            # Log the failure for the user
            return None

    except Exception as error:
        print(f"{print_error_terminal} Get EOX data for SN: {print_cyan(serial_number)} is Failed, Cause: Unknown Error, msg: {error}")
        # Log the failure for the user
        return None


def run_app():
    print(f"{'-' * 10} Cisco EOL Tools {'-' * 10}")
    print()
    serial_number = str(input("Please input Serial Number: ")).strip()
    
    
    api_key = get_apikey()
    result = get_eox_data(api_key, serial_number)
    formated_result = json.dumps(result, indent=2)
    print(formated_result)

if __name__ == "__main__":
    run_app()