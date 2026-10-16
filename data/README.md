# Data availability and layout

The GitHub package intentionally does not upload original multi-GB CT RAW volumes,
individual cropped blocks, pore masks, or the >8,000 PNM Excel tables.

`source_rock_counts.csv` describes the per-rock 729 candidate 200³ crops (stride 100)
from 11 rocks (8,019 candidates). `master_column_names.csv` lists schema fields.

## Required local files

A full re-run requires **11 source CT volumes** and the digital rock data-generation
pipeline, or the saved **PNM pore/throat Excel files** and master table produced by the
pipeline. The author-supplied master CSV contains Windows-specific absolute file paths
and is NOT redistributed in this public-ready package. To use training notebooks, place
it at `data/DRP317_11sandstone_GNN_dataset_v3/summary/DRP317_11sandstone_GNN_dataset_v2_master.csv`,
and ensure referenced PNM Excel files are present. Resolve absolute path entries to
local PNM files using the built-in notebook filename fallback. Do not assume that
master CSV alone is sufficient to run graph training.

You can set `PMGNN_DATA_ROOT` to a separate disk path containing the original complete
generated dataset instead of copying large files into the repo.

External raw CT inputs can be supplied through `PMGNN_MINERAL_RAW`, `PMGNN_MTSIMON_RAW`,
`PMGNN_YULAI_RAW`, `PMGNN_EF78_RAW`, and (optional) `PMGNN_EF75_RAW`.

The original 11-sandstone source description cites the Digital Porous Media Portal
(DOI: 10.17612/F4H1-W124); verify individual dataset terms before redistribution.
