# Description: MG_Graph.py contains Common classes used in python files. Contents:
import json
import requests

class GraphAPI:
    @staticmethod
    def get_token(tenant, client_id, client_secret, console):
        url = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': 'https://graph.microsoft.com/.default'}
        console.print(f"Tenant ID: {tenant} | Client ID: {client_id}", style="bold red")
        console.print(f"Auth Endpoint: {url}", style="bold yellow")
        response = requests.post(url, data=data, timeout=30)
        console.print(f"Response status code: {response.status_code}", style="bold green")
        if response.status_code != 200:
            console.print("Failed to get a token. Check the credentials and try again.", style="bold red")
            console.print(f"Response text: {response.text}", style="bold red")
            return None
        json_response = response.json()
        return json_response.get("access_token", None)

    @staticmethod
    def get_data(token, json_fp, url, console):
        headers = {"Authorization": f"Bearer {token}"}
        all_users = []
        try:
            while url:
                response = requests.get(url, headers=headers, timeout=30)
                if response.status_code != 200:
                    console.print(f"Failed to fetch data. Status code: {response.status_code}", style="bold red")
                    response.raise_for_status()
                data = response.json()
                all_users.extend(data.get('value', []))
                console.print(f"Total users fetched: {len(all_users)}", style="bold blue")
                url = data.get('@odata.nextLink', None)
            with open(json_fp, 'w', encoding='utf-8') as f:
                json.dump(all_users, f)
            console.print("Data successfully fetched and saved.", style="bold green")
        except requests.exceptions.RequestException as e:
            console.print(f"Request exception: {e}", style="bold red")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")

    @staticmethod
    def construct_endpoint(console, utype=3, accounts=0, licenses=0):
        base_url = "https://graph.microsoft.com/v1.0/users"
        base_params = "?$count=true&$select=displayName,mail,userPrincipalName,createdDateTime,usageLocation,userType,externalUserState,externalUserStateChangeDateTime,onPremisesSamAccountName,onPremisesSecurityIdentifier,onPremisesSyncEnabled,onPremisesUserPrincipalName,otherMails,passwordPolicies,onPremisesDistinguishedName,onPremisesDomainName,onPremisesLastSyncDateTime,refreshTokensValidFromDateTime,securityIdentifier,signInSessionsValidFromDateTime,id,passwordProfile,identities,signInActivity,accountEnabled"
        user_types = {1: 'member', 2: 'guest', 3: 'all'}  # Map the numeric choice to user_type
        user_type = user_types.get(utype)
        filters = []
        if accounts == 0:  # If 0 pass filter for accountEnabled
            filters.append("accountEnabled eq true")
        if user_type in ['member', 'guest']:  # Append userType filter if user_type is 'member' or 'guest'
            filters.append(f"userType eq '{user_type}'")
        filter_query = "&$filter=" + " and ".join(filters) if filters else ""  # Join filters to create the filter query parameter
        plans_and_licenses = ",assignedPlans,assignedLicenses" if licenses == 1 else ""  # NOTE not used right now, hardcoded.
        final_params = f"{base_params}{plans_and_licenses}{filter_query}"
        url = f"{base_url}{final_params}"
        console.print("\n====================Endpoint Constructed====================\n", style="bold red")
        console.print(f"{url}", style="bold yellow")
        console.print("\n============================================================\n", style="bold red")
        return url

    @staticmethod
    def mock_token(tenant, client_id, _, console):
        console.print(f"Mock API Call: Tenant ID: {tenant} | Client ID: {client_id}", style="bold red")
        return "mock_access_token"  # Instead of making an API call, return a mock token

    @staticmethod
    def mock_data(token, json_fp, _, console):
        console.print(f"Mock API Call: Bearer {token}", style="bold blue")
        _ = [{"id": "1", "name": "Elliot Alderson"}, {"id": "2", "name": "Cae Menethil"}]  # Simulate a response with dummy data
        try:
            # pass
            # with open(json_fp, 'w', encoding='utf-8') as f:
            #     # json.dump(all_users, f)
            console.print(f"Mock data saved to {json_fp}", style="bold green")
        except Exception as e:
            console.print(f"An error occurred: {e}", style="bold red")
