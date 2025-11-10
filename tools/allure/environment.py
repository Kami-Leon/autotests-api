import sys
import platform

from config import settings


def create_allure_environment_file():
    os_info = f'{platform.system()}, {platform.release()}'
    python_version = sys.version

    environment_data = {
        "os_info": os_info,
        "python_version": python_version,
        **settings.model_dump()
    }

    items = [f'{key}={value}' for key, value in environment_data.items()]
    properties = '\n'.join(items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
