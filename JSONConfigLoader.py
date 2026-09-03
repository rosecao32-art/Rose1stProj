import json
import os

# Required fields for validation
REQUIRED_FIELDS = ["temperature", "pH"]

class ConfigError(Exception):
    """Custom exception for configuration-related errors."""
    pass


def load_config(file_path):
    """Load JSON configuration from a file with proper exception handling."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: '{file_path}'")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON format in '{file_path}': {e}")
    except Exception as e:
        raise ConfigError(f"Error reading file '{file_path}': {e}")


def validate_config(config_list):
    for config in config_list:
        missing = [f for f in REQUIRED_FIELDS if f not in config]
        if missing:
            raise ConfigError(f"Missing fields in entry {config.get('Name', '?')}: {missing}")

        if not isinstance(config["temperature"], (int, float)):
            raise ConfigError(f"Invalid temperature in {config.get('Name', '?')}")

        ph = config["pH"]
        if not isinstance(ph, (int, float)) or not (0 <= ph <= 14):
            raise ConfigError(f"Invalid pH in {config.get('Name', '?')}")


def print_summary(config_list):
    print("\n=== Configuration Summary ===")
    for config in config_list:
        print(f"Experiment: {config.get('Name', 'Unknown')}")
        for key, value in config.items():
            print(f"  {key:15}: {value}")
        print()
    print("=============================\n")


def main():
    try:
        config_data = load_config("data2.json")
        validate_config(config_data)
        print_summary(config_data)

    except (FileNotFoundError, ConfigError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
