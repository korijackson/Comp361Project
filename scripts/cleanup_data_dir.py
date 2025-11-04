from pathlib import Path
import shutil

# === Path setup (relative to project root) ===
# This script lives in /scripts, so we move one level up to find /data
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ARCHIVE = DATA / "old"
ARCHIVE.mkdir(exist_ok=True)

# === Files you want to KEEP ===
keep = {
    "minmax_scaler.pkl",
    "rf_model.pkl",
    "NUSW-NB15_features.csv",
    "UNSW-NB15_1.csv",
    "UNSW-NB15_2.csv",
    "UNSW-NB15_3.csv",
    "UNSW-NB15_4.csv",
    "UNSW-NB15_cleaned.csv",
    "UNSW-NB15_feature_importances.csv",
    "UNSW-NB15_rf_top15.png",
    "UNSW-NB15_selected_features.txt",
    "UNSW-NB15_top15.csv",
}

# === Move obsolete files into /data/old ===
moved = []
for file in DATA.iterdir():
    if file.is_file() and file.name not in keep:
        shutil.move(str(file), ARCHIVE / file.name)
        moved.append(file.name)

# === Reporting ===
if moved:
    print("✅ Moved obsolete files to /data/old/:")
    for f in moved:
        print(f"   - {f}")
else:
    print("No old files found. Your /data directory is already clean!")

print("\nRemaining files in /data/:")
for f in sorted(DATA.iterdir()):
    print(f"   - {f.name}")
