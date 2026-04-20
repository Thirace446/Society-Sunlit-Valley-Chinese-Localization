import os
import json
from pathlib import Path
import datetime

# --- Configuration ---
VALLEY_DIR = "valley"
COBBLE_DIR = "cobblemon"
LOG_FILE = "log.md"
REPORT_FILE = "report.json"

def write_log(message, mode="a"):
    """Writes a message to the console and appends it to the log file."""
    with open(LOG_FILE, mode, encoding="utf-8") as f:
        f.write(message + "\n")

def load_json(path):
    """Safely loads a JSON file. Returns None if file is missing, or empty dict if invalid."""
    if not path.exists():
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except Exception:
        return {}

def compare_en_us_keys(data_v, data_c):
    """
    Compares two JSON dictionaries.
    Returns: (detailed_report_dict, has_differences_bool, list_of_diff_keys)
    """
    all_keys = sorted(set(data_v.keys()) | set(data_c.keys()))
    full_report = {}
    diff_keys = []

    for key in all_keys:
        val_v = data_v.get(key)
        val_c = data_c.get(key)

        if key in data_v and key in data_c:
            if val_v == val_c:
                status = "Identical"
            else:
                status = "Value Mismatch"
                diff_keys.append(key)
        elif key in data_v:
            status = "Unique to Valley"
            diff_keys.append(key)
        else:
            status = "Unique to Cobblemon"
            diff_keys.append(key)

        full_report[key] = {
            "status": status,
            "valley_value": val_v,
            "cobblemon_value": val_c
        }
        
    return full_report, len(diff_keys) > 0, diff_keys

def main():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_log(f"=== Module report ({timestamp}) ===\n", mode="w")

    p_valley = Path(VALLEY_DIR)
    p_cobble = Path(COBBLE_DIR)

    if not p_valley.exists() or not p_cobble.exists():
        print(f"Error: Required directories '{VALLEY_DIR}' or '{COBBLE_DIR}' not found.")
        return

    # Get folder sets
    mods_v = {d.name for d in p_valley.iterdir() if d.is_dir()}
    mods_c = {d.name for d in p_cobble.iterdir() if d.is_dir()}

    # 1. Identify missing folders
    only_in_valley = sorted(list(mods_v - mods_c))
    only_in_cobble = sorted(list(mods_c - mods_v))
    common_mods = sorted(list(mods_v & mods_c))

    # --- Perform Content Comparison (Only for Common Folders) ---
    report_data = {}
    mods_with_diffs = [] 
    identical_mods_count = 0

    print(f"Comparing common modules in '{VALLEY_DIR}' and '{COBBLE_DIR}'...")

    for mod in common_mods:
        file_v = p_valley / mod / "lang" / "en_us.json"
        file_c = p_cobble / mod / "lang" / "en_us.json"

        data_v = load_json(file_v)
        data_c = load_json(file_c)

        # Compare only if both JSON files exist
        if data_v is not None and data_c is not None:
            report, has_diff, diff_keys = compare_en_us_keys(data_v, data_c)
            report_data[mod] = report
            
            if has_diff:
                mods_with_diffs.append({"name": mod, "keys": diff_keys})
            else:
                identical_mods_count += 1
        else:
            # Handle cases where folder exists but en_us.json is missing
            missing_info = []
            if data_v is None: missing_info.append(f"Missing en_us.json in {VALLEY_DIR}")
            if data_c is None: missing_info.append(f"Missing en_us.json in {COBBLE_DIR}")
            mods_with_diffs.append({"name": mod, "keys": [f"File Error: {' & '.join(missing_info)}"]})

    # --- Writing to log.md ---
    # Section 1: Missing Folders (Names only)
    write_log("[1. Missing Module Folders]")
    if only_in_valley:
        write_log(f"▶ Folders found only in '{VALLEY_DIR}' (Missing in Cobblemon):")
        for m in only_in_valley: write_log(f"   - {m}")
    
    if only_in_cobble:
        write_log(f"\n▶ Folders found only in '{COBBLE_DIR}' (Missing in Valley):")
        for m in only_in_cobble: write_log(f"   - {m}")
        
    if not only_in_valley and not only_in_cobble:
        write_log("   (Folder lists match perfectly)")

    # Section 2: Content Differences (Key names only)
    write_log("\n[2. Content Differences in Common Modules]")
    if mods_with_diffs:
        for item in mods_with_diffs:
            write_log(f"▶ Module: {item['name']}")
            for k in item['keys']:
                write_log(f"   - {k}")
            write_log("-" * 50)
    else:
        write_log("   (No differences found in translation keys)")

    # Section 3: Summary
    write_log(f"\n[3. Statistics Summary]")
    write_log(f"   - Common Modules Total: {len(common_mods)}")
    write_log(f"   - Perfectly Matching Modules: {identical_mods_count}")
    write_log(f"   - Modules with Content Differences: {len(mods_with_diffs)}")

    # --- Writing to report.json ---
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)

    print(f"\nComparison complete!")
    print(f"- Summary of differences & missing folders: {LOG_FILE}")
    print(f"- Detailed key-value report: {REPORT_FILE}")

if __name__ == "__main__":
    main()