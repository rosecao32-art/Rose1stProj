import json
import csv
from statistics import mean

class ConfigError(Exception):
    """Custom exception for JSON structure issues."""
    pass


def load_json(path):
    """Load a JSON file with error handling."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise ConfigError(f"File not found: {path}")
    except json.JSONDecodeError as e:
        raise ConfigError(f"Invalid JSON format: {e}")


def extract_trial_info(data):
    """Extract trial IDs and average measurements from nested JSON."""
    try:
        trials = data["experiment"]["trials"]
    except KeyError:
        raise ConfigError("JSON missing required structure: experiment → trials")

    results = []

    for trial in trials:
        trial_id = trial.get("trial_id")
        measurements = trial.get("measurements")

        if trial_id is None:
            raise ConfigError("A trial is missing 'trial_id'")

        if not isinstance(measurements, list) or len(measurements) == 0:
            raise ConfigError(f"Trial {trial_id} has invalid or empty measurements")

        avg = mean(measurements)

        results.append({
            "trial_id": trial_id,
            "average_measurement": avg
        })

    return results


def write_json(path, data):
    """Write results to a new JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def write_csv(path, data):
    """Flatten results into CSV."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["trial_id", "average_measurement"])
        writer.writeheader()
        writer.writerows(data)


def main():
    try:
        raw = load_json("JSONdata3.json")
        results = extract_trial_info(raw)

        write_json("JSONtrial_summary.json", results)
        write_csv("CSVtrial_summary.csv", results)

        print("Processing complete. JSON and CSV files written.")

    except ConfigError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
