# 🧠 COMP 361 – Network Intrusion Detection Project

This project replicates and extends the methodology of *Vibhute et al. (2024)* using the **UNSW-NB15 dataset** for network intrusion detection.  
All steps are implemented in Python using **pandas**, **scikit-learn**, and **joblib**.

---

## 📁 Project Overview
This project processes, cleans, and analyzes the UNSW-NB15 dataset in multiple phases:

| Phase | Description | Main Output |
|--------|--------------|--------------|
| **0** | Dataset setup & merge | `UNSW-NB15_full.csv`, `UNSW-NB15_sample_1k.csv` |
| **1** | Preprocessing & cleaning | `UNSW-NB15_cleaned.csv` |
| **2** | Feature selection with Random Forest | `UNSW-NB15_top15.csv`, plots, and model artifacts |
