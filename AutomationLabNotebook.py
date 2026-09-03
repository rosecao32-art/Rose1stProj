from datetime import datetime

# -----------------------------
# 1. Data structure: the notebook
# -----------------------------
notebook = []

# -----------------------------
# 2. Function to add entries
# -----------------------------
def add_entry(notebook, sample, mass_g, temperature_C, notes=""):
    entry = {
        "id": len(notebook) + 1,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "sample": sample,
        "mass_g": mass_g,
        "temperature_C": temperature_C,
        "notes": notes
    }
    notebook.append(entry)

# -----------------------------
# 3. Summary function
# -----------------------------
def summarize(notebook):
    print("\n=== LAB NOTEBOOK SUMMARY ===")
    for entry in notebook:
        print(
            f"ID {entry['id']} | {entry['date']} | Sample: {entry['sample']} | "
            f"Mass: {entry['mass_g']} g | Temp: {entry['temperature_C']} °C"
        )
    print("============================\n")

# -----------------------------
# 4. Filtering function
# -----------------------------
def filter_by_sample(notebook, sample_name):
    return [entry for entry in notebook if entry["sample"] == sample_name]

# -----------------------------
# 5. Test the automation
# -----------------------------
add_entry(notebook, "Si Nanowire", 2.5, 450, "Growth run #1")
add_entry(notebook, "Si Nanowire", 2.7, 455, "Growth run #2")
add_entry(notebook, "GaN Film", 1.2, 600, "Annealing test")

summarize(notebook)

filtered = filter_by_sample(notebook, "Si Nanowire")
print("Filtered entries for Si Nanowire:")
for f in filtered:
    print(f)
