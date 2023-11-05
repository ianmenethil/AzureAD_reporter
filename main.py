# Description: main.py contains the main flow all options. File Contents:
from pathlib import Path
import logging
import typer
from pandas import json_normalize  # pylint: disable=unused-import
from rich.logging import RichHandler
from rich.console import Console
from rich.traceback import install
from users import execute_order66
from seeker import execute_seeker
from Common import Choices
from FM import FileManager

creds_file = 'config/config.yaml'
console = Console()
install()
logging.basicConfig(level=logging.INFO, format="%(message)s", datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=False, tracebacks_show_locals=False)])
logger = logging.getLogger(__name__)
logs_dir = Path('logs')
logs_dir.mkdir(exist_ok=True)
file_handler = logging.FileHandler(logs_dir / 'applogs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(datefmt="%d-%m-%Y", fmt="%(asctime)s|%(message)s"))
logger.addHandler(file_handler)
def main(tenant: str = typer.Option(None, "--tenant", "-t"), client_id: str = typer.Option(None, "--client-id", "-c"), client_secret: str = typer.Option(None, "--secret", "-s")):
    """
    Main function to execute the application logic based on the user's choice.
    :param tenant: Tenant ID for the application.
    :param client_id: Client ID for the application.
    :param client_secret: Client secret for the application."""
    date_str, _, _ = FileManager.get_date_properties()
    creds = FileManager.load_creds(creds_file)

    if creds and isinstance(creds.get('app_config'), dict) and 'input_dir' in creds['app_config']:
        input_folder = Path(creds['app_config']['input_dir'])
    else:
        input_folder = Path('input')
        console.print(f"===========================================================\nConfig file is not setup. Fallback to default input folder \nJSON file will be saved in: '{input_folder}'\n===========================================================", style="bold red")

    input_folder.mkdir(exist_ok=True)
    json_file_path = input_folder / f'{date_str}_users.json'
    initial_choice = Choices.get_job(console)
    job_index = str(initial_choice)
    job_functions = {'0': execute_order66, '1': execute_seeker,}  # '2': execute_user_plans_and_licenses, # Not yet implemented

    job_to_execute = job_functions.get(job_index)

    if job_to_execute:
        job_to_execute(json_file_path, date_str, console, logger, creds_file, tenant, client_id, client_secret)
    else:
        console.print("Invalid choice. Exiting.", style="bold red")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    typer.run(main)
