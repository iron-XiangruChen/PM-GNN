# What the packaging process changed (and did NOT change)

- Ten original Jupyter notebooks were copied from user-provided sources.
- Removed executed cell outputs, execution counts, and transient notebook metadata
  to reduce upload size and avoid exposing old traces/file paths.
- Changed only existing path-assignment lines (`DATA_ROOT`, `RAW_PATH`, `MODEL_DIR`,
  `BASE_OUT`) to use environment variables or repository paths. No automatic simulation, threshold, model structure, batch size or validation split
  changes. In the four training notebooks, an additional metadata-only statement
  `SPLIT_MODE = split_method` was inserted after actual 8/3 rock grouping to correct
  stale saved-filename/config 9/2 labels. Existing checkpoint filenames remain untouched.
- Copied compact model checkpoints/scalers/historical training logs from four
  submitted result ZIPs into **saved-tag-labelled** folders. Figure outputs and full CSVs
  from result ZIPs were excluded, as were very large CT arrays and PNM Excel files.
- Data `source_rock_counts.csv` and `master_column_names.csv` generated from author-
  supplied `DRP317_11sandstone_GNN_dataset_v2_master.csv`; the unsanitized full master
  was omitted due to machine-specific paths and missing dependent PNM tables.
- Notebook-to-source code SHA256 hashes and path modification details are in
  `reproducibility/notebook_provenance.csv`.

* `00_build_11_sandstone_dataset.ipynb`: DATA_ROOT: absolute Windows path -> PMGNN_DATA_ROOT or repo/data
* `01_baseline_GNN.ipynb`: DATA_ROOT: absolute Windows path -> PMGNN_DATA_ROOT or repo/data
* `02_GNN_global_descriptors.ipynb`: DATA_ROOT: absolute Windows path -> PMGNN_DATA_ROOT or repo/data
* `03_GNN_flow_path_descriptors.ipynb`: DATA_ROOT: absolute Windows path -> PMGNN_DATA_ROOT or repo/data
* `04_PM_GNN_full.ipynb`: DATA_ROOT: absolute Windows path -> PMGNN_DATA_ROOT or repo/data
* `05_external_mineral.ipynb`: BASE_OUT: local disk -> PMGNN_OUTPUT_ROOT or repo/outputs/; MODEL_DIR: local disk -> PMGNN_MODEL_DIR or archived PM-GNN checkpoints; RAW_PATH: absolute Windows path -> PMGNN_MINERAL_RAW or repo/data/external
* `06_external_mtsimon.ipynb`: BASE_OUT: local disk -> PMGNN_OUTPUT_ROOT or repo/outputs/; MODEL_DIR: local disk -> PMGNN_MODEL_DIR or archived PM-GNN checkpoints; RAW_PATH: absolute Windows path -> PMGNN_MTSIMON_RAW or repo/data/external
* `07_external_yulaiLR_SR.ipynb`: BASE_OUT: local disk -> PMGNN_OUTPUT_ROOT or repo/outputs/; MODEL_DIR: local disk -> PMGNN_MODEL_DIR or archived PM-GNN checkpoints; RAW_PATH: absolute Windows path -> PMGNN_YULAI_RAW or repo/data/external
* `08_external_EF_78_shale.ipynb`: BASE_OUT: local disk -> PMGNN_OUTPUT_ROOT or repo/outputs/; MODEL_DIR: local disk -> PMGNN_MODEL_DIR or archived PM-GNN checkpoints; RAW_PATH: absolute Windows path -> PMGNN_EF78_RAW or repo/data/external
* `09_optional_EF_75_not_in_manuscript.ipynb`: BASE_OUT: local disk -> PMGNN_OUTPUT_ROOT or repo/outputs/; MODEL_DIR: local disk -> PMGNN_MODEL_DIR or archived PM-GNN checkpoints; RAW_PATH: absolute Windows path -> PMGNN_EF75_RAW or repo/data/external
