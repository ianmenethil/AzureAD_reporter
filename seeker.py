# Description: seeker.py contains the flow for option 1 from main.py. File Contents:
from pathlib import Path
import traceback
from prompt_toolkit import prompt
import typer
from Common import Choices
from MG_Graph import GraphAPI
from FM import FileManager

def execute_seeker(json_file_path, date_str, console, logger, credentials_file, tenant: str = typer.Option(None, "--tenant", "-t"), client_id: str = typer.Option(None, "--client-id", "-c"), client_secret: str = typer.Option(None, "--secret", "-s")):
    pass
#     creds = FileManager.load_creds(credentials_file)
#     if json_file_path.exists() and FileManager.check_json_content(json_file_path):
#         console.print("JSON file exists and contains data. Skipping API call.", style="bold green")
#     else:
#         if not all([tenant, client_id, client_secret]):
#             if creds:
#                 tenant = tenant or creds['credentials']['tenant_id']
#                 client_id = client_id or creds['credentials']['client_id']
#                 client_secret = client_secret or creds['credentials']['client_secret']
#             else:
#                 tenant = tenant or prompt("Enter tenant ID: ")  # Prompt for credentials if not found in the configuration file
#                 client_id = client_id or prompt("Enter client ID: ")
#                 client_secret = client_secret or prompt("Enter client secret: ")
#         if not all([tenant, client_id, client_secret]):  # Ensure all required credentials are provided before proceeding
#             console.print("Missing credentials. Please provide tenant ID, client ID, and client secret.", style="bold red")
#             raise typer.Exit(code=1)
#         # token = GraphAPI.mock_token(tenant, client_id, client_secret, console)  # NOTE Fetch token and data
#         token = GraphAPI.get_token(tenant, client_id, client_secret, console)  # NOTE Fetch token and data

#         if token:
#             console.print("Token successfully fetched.", style="bold green")
#             account_enabled = Choices.get_accountEnabled(console)
#             account_enabled_map = {0: 0, 1: 1}
#             account_enabled = account_enabled_map.get(account_enabled, 0) # Default to 0 (enabled accounts only) if not found
#             console.print(f"Accounts: {'Enabled Accounts Only' if account_enabled == 0 else 'All'}", style="bold blue")
#             console.print(f"Account enabled is {account_enabled}", style="bold red")

#             user_type_str = Choices.get_userType(console)
#             user_type_map = {0: 3, 1: 2, 2: 1}  # 0: 'All', 1: 'Guest', 2: 'Member'
#             user_type = user_type_map.get(user_type_str, 3)  # Default to 3 ('All') if not found
#             console.print(f"User type is {user_type}", style="bold red")

#             licenses = 0
#             dynamic_url = GraphAPI.construct_endpoint(console, user_type, account_enabled, licenses)  # NOTE
#             try:
#                 GraphAPI.get_data(token, json_file_path, dynamic_url, console)  # NOTE
#                 # GraphAPI.mock_data(token, json_file_path, dynamic_url, console)  # NOTE
#             except Exception:
#                 console.print("Failed to fetch data.", style="bold red")
#         else:
#             console.print("Failed to fetch token. Please check your credentials.", style="bold red")
#             raise typer.Exit(code=1)
#         if not all([tenant, client_id, client_secret]):
#             console.print("Missing credentials. Please provide tenant ID, client ID, and client secret.", style="bold red")
#             raise typer.Exit(code=1)

#     if creds and isinstance(creds.get('app_config'), dict) and 'output_dir' in creds['app_config']:
#         output_folder = Path(creds['app_config']['output_dir'])
#     else:
#         output_folder = Path("output")  # Use the default output folder if the condition is not met
#         console.print(f"===========================================================\nConfig file is not setup. Fallback to default output folder \nCSV/Excel files will be saved in: '{output_folder}'\n===========================================================", style="bold red")
#     output_folder.mkdir(exist_ok=True)

#     csv_file_path = FileManager.generate_filename(output_folder / f'{date_str}_compliant_users.csv')
#     filtered_csv_file_path = FileManager.generate_filename(output_folder / f'{date_str}_non_compliant_users.csv')
#     disabled_csv_file_path = FileManager.generate_filename(output_folder / f'{date_str}_disabled_accounts.csv')

#     try:
#         FileManager.json_to_csv(json_file_path, csv_file_path, filtered_csv_file_path, disabled_csv_file_path, logger)
#         if Path(csv_file_path).exists() and Path(filtered_csv_file_path).exists() and Path(disabled_csv_file_path).exists():
#             console.print("CSV files saved successfully.", style="bold green")
#             excel_file_path = FileManager.generate_filename(output_folder / f'{date_str}_UsersData.xlsx')
#             logger.info(f"file name generator returned {excel_file_path}")
#             try:
#                 FileManager.csv_to_excel(output_dir=output_folder, excel_filename=excel_file_path.name, logger=logger)
#                 if excel_file_path.exists():
#                     console.print("Excel file saved successfully.", style="bold green")
#                 else:
#                     console.print("Failed to save Excel file.", style="bold red")
#             except Exception as e:
#                 logger.info(f"An error occurred while saving the Excel file: {e}", exc_info=True)
#                 traceback.print_exc()
#         else:
#             console.print("Failed to save CSV files.", style="bold red")
#     except Exception as e:
#         logger.info(f"An error occurred while converting JSON to CSV: {e}", exc_info=True)
