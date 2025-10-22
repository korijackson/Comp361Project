# COMP 361 – Project
This project uses the **UNSW-NB15 dataset**.  
## Phase 0: Initializing Project

#### Step 1: Clone the Repository

#### Step 2: Folder Setup

Make sure your folders look like this:
```
Comp361Project/
├── .gitignore
├── README.md
├── scripts/
│   └── merge_dataset.py
└── UNSW-NB15 DataSet/
    ├── NUSW-NB15_features.csv
    ├── UNSW-NB15_1.csv
    ├── UNSW-NB15_2.csv
    ├── UNSW-NB15_3.csv
    └── UNSW-NB15_4.csv
```
#### Step 3: Install Pandas and run scripts/merge_dataset.py
```
pip install pandas
python scripts/merge_dataset.py
```



The `merge_dataset.py` script combines the four raw parts into one full dataset creating:
- **UNSW-NB15_full.csv**
- **UNSW-NB15_sample_1k.csv**




