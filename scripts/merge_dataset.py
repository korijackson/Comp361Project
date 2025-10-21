from pathlib import Path
import pandas as pd
import glob
import sys

def load_features_csv(feature_path: Path) -> list[str]:
    """Read the feature-name file with robust encoding handling and return list of names."""
    # Try UTF-8, then latin1, then replace errors
    for enc in ("utf-8", "latin1"):
        try:
            features_df = pd.read_csv(feature_path, encoding=enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        features_df = pd.read_csv(feature_path, encoding_errors="replace")

    # Normalize the name column (common variants)
    if 'Name' not in features_df.columns:
        for alt in ('name', 'Feature', 'feature', 'Column', 'column'):
            if alt in features_df.columns:
                features_df.rename(columns={alt: 'Name'}, inplace=True)
                break

    # Fallback: assume first column is names
    if 'Name' not in features_df.columns:
        features_df.columns = ['Name'] + list(features_df.columns[1:])

    names = features_df['Name'].astype(str).tolist()
    if not names:
        sys.exit("❌ Could not extract feature names from the features file.")
    return names

def main():
    # 1) Point to the data folder (one level up from /scripts)
    DATA_DIR = Path("../UNSW-NB15 DataSet").resolve()
    if not DATA_DIR.exists():
        sys.exit(f"❌ Data folder not found: {DATA_DIR}")

    # 2) Find ONLY the four raw parts (avoid picking up *_full or *_sample)
    pattern = str(DATA_DIR / "UNSW-NB15_*.csv")
    all_matches = sorted(glob.glob(pattern))
    files = [p for p in all_matches if Path(p).stem in {
        "UNSW-NB15_1", "UNSW-NB15_2", "UNSW-NB15_3", "UNSW-NB15_4"
    }]
    if not files:
        sys.exit(f"❌ Found matches {all_matches}, but not the 4 raw parts. Check filenames.")

    print("🔎 Found files (merge order):")
    for f in files:
        print(" •", Path(f).name)

    # 3) Read feature names from the *features* file (note: NUSW spelling is correct in many releases)
    feature_path = DATA_DIR / "NUSW-NB15_features.csv"
    if not feature_path.exists():
        sys.exit(f"❌ Feature file not found: {feature_path}")
    feature_names = load_features_csv(feature_path)

    # Optional sanity: UNSW-NB15 has 49 features + labels; if your file lists more/less, we still proceed
    print(f"\n🧩 Loaded {len(feature_names)} feature names from: {feature_path.name}")
    print("   First 10:", feature_names[:10])

    # 4) Load each data part *without* trusting its header; apply official feature names
    dataframes = []
    for f in files:
        df_part = pd.read_csv(f, header=None, names=feature_names, low_memory=False)
        dataframes.append(df_part)

    # 5) Merge all parts
    df = pd.concat(dataframes, ignore_index=True)
    print("\n✅ Combined shape:", df.shape)
    print("   Example columns:", list(df.columns)[:10], "...")

    # 6) Quick sanity prints if present
    for col in ("label", "attack_cat"):
        if col in df.columns:
            print(f"\n📊 Value counts for '{col}':")
            print(df[col].value_counts(dropna=False).head(20))

    # 7) Save merged dataset (and a 1k-row sample)
    out_path = DATA_DIR / "UNSW-NB15_full.csv"
    df.to_csv(out_path, index=False)
    print(f"\n💾 Saved merged file to: {out_path}")

    sample_path = DATA_DIR / "UNSW-NB15_sample_1k.csv"
    df.sample(n=min(1000, len(df)), random_state=42).to_csv(sample_path, index=False)
    print(f"🧪 Saved 1k-row sample to: {sample_path}")

if __name__ == "__main__":
    main()