# PM-GNN: Physics-Motivated Pore-Network Graph Neural Network

Research code for the digital rock physics study predicting directional permeability
and effective **scalar-spring-network proxy** elastic modulus from extracted pore
networks. Four ablations are included, plus external-rock evaluation notebooks.

> **This repository package preserves the author's notebooks but is not a validated
> one-command end-to-end reproduction environment**: large CT volumes and PNM files
> were not supplied for redistributable hosting, and saved-checkpoint filename tags
> were not updated after the actual notebook split changed. Read
> [Known limitations](docs/KNOWN_LIMITATIONS.md) before reporting results.

## Contents

| Notebook | Purpose |
|---|---|
| `notebooks/00_build_11_sandstone_dataset.ipynb` | CT crop, binary pore segmentation, pore-network flow and scalar spring proxy labels; create master table |
| `notebooks/01_baseline_GNN.ipynb` | Baseline GNN |
| `notebooks/02_GNN_global_descriptors.ipynb` | GNN + global descriptors |
| `notebooks/03_GNN_flow_path_descriptors.ipynb` | GNN + flow path descriptors |
| `notebooks/04_PM_GNN_full.ipynb` | Full PM-GNN |
| `notebooks/05_external_mineral.ipynb` | External mineral sandstone |
| `notebooks/06_external_mtsimon.ipynb` | External Mt Simon sandstone |
| `notebooks/07_external_yulaiLR_SR.ipynb` | External yulaiLR-SR sandstone |
| `notebooks/08_external_EF_78_shale.ipynb` | EF-78 shale proof of transfer limits |
| `notebooks/09_optional_EF_75_not_in_manuscript.ipynb` | Additional exploratory EF-75 notebook; not a reported manuscript test |
| `checkpoints/` | Supplied saved models, scaler `.pkl` and small training histories, carrying stale `9train_2val` filename/config tags |
| `reproducibility/` | Recorded training time table, hash-based provenance, checkpoint manifest |
| `docs/KNOWN_LIMITATIONS.md` | Scientific, source and code caveats |

## Recommended setup

The original notebook metadata indicates **Python 3.9.19**, but does not reliably
record the exact original TensorFlow, OpenPNM, CUDA or driver versions.
The following is a **suggested clean environment**, not an exact historical lock:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

For **NVIDIA RTX 4070 Ti** on Windows, prefer **WSL2/Linux** for modern TensorFlow GPU
rather than assuming native Windows TensorFlow >=2.11 provides GPU support. Follow
TensorFlow's CUDA/driver installation guidance; on a supported Linux stack an optional
installation is `pip install 'tensorflow[and-cuda]==2.15.1'`.
Verify with `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`.
GPU availability and all dependency combinations have not been validated here.

Reported author machine: **Intel Core i9-13900K, NVIDIA RTX 4070 Ti, 128 GB RAM**.
OS, CUDA, cuDNN and exact library versions are not supplied.

## Data paths (no author-specific drive letters)

Run `jupyter lab` from the **repository root**. By default the notebooks look under
`data/` and write generated material to `data/DRP317_11sandstone_GNN_dataset_v3/`
and external output to `outputs/`.
To use your existing large dataset stored elsewhere:

```bash
export PMGNN_PROJECT_ROOT="$PWD"
export PMGNN_DATA_ROOT="/path/to/your/complete/rock-data-folder"
export PMGNN_MODEL_DIR="$PWD/checkpoints/PM-GNN_saved_tag_9train_2val"
export PMGNN_EF78_RAW="/path/to/EF-78.raw"
# Also available: PMGNN_MTSIMON_RAW, PMGNN_MINERAL_RAW, PMGNN_YULAI_RAW,
# PMGNN_EF75_RAW, PMGNN_OUTPUT_ROOT.
jupyter lab
```

Windows PowerShell example:

```powershell
$env:PMGNN_PROJECT_ROOT = (Get-Location).Path
$env:PMGNN_DATA_ROOT = 'D:\my-rock-data'
$env:PMGNN_EF78_RAW = 'D:\my-CT\EF-78.raw'
jupyter lab
```

The dataset builder uses **200³ voxel blocks with stride 100** and `PORE_MAX=60`.
The author-supplied builder notebook retains its **debug default**
`MAX_BLOCKS_PER_ROCK = 10`. Set this to `None` for a *full regeneration attempt*;
the historical full run setting is not independently recorded in the file.
The pore-network stage can be expensive in compute and memory. The original full
training dataset requires the master CSV **and** underlying PNM Excel graph files;
master CSV alone cannot reconstruct the models.

## Workflow

1. Obtain original 11 sandstone CT RAW files and prepare the complete local folder.
2. Configure `PMGNN_DATA_ROOT`, open `00_build_11_sandstone_dataset.ipynb`, confirm
   RAW names/shapes, crop stride, grayscale segmentation, and full-run settings.
3. Run the dataset generation notebook, inspect its quality summary, and retain
   the generated PNM Excel files.
4. Run notebooks `01`–`04` for the four model variants; note that they currently
   define a **3-rock validation** split, while supplied checkpoints still carry an old
   **2-rock validation** *filename label*. The executed notebook logs show 8-train/3-validation; this is a naming bug, not evidence of 9/2 training.
5. Configure external raw CT path(s) and the appropriate verified model checkpoint;
   run notebooks `05`–`08` as needed.
6. Run `python scripts/check_repository.py` as a fast static package audit.

## Core implementation details

Nodes describe pores; graph edges describe pore-throat connectivity. Graph message
passing uses neighbor mean aggregation (two layers, 64 hidden units) and graph
mean pooling. Global descriptors are appended to node inputs; the permeability
branch additionally uses 22 directional/path conductance summary descriptors.
Modulus targets are proxy properties calculated from a **scalar spring network**,
not experimental laboratory elastic moduli or an independently verified full
elasticity solution. SHAP analysis in the original training notebooks uses a
surrogate random forest to explain trained-model predictions.

## Recorded training cost

The four author-supplied runs reported the following **training-only** wall times:

| Model | Permeability (s) | Modulus (s) | Total (s) | Relative to GNN |
|---|---:|---:|---:|---:|
| GNN baseline | 319.84 | 336.13 | 655.97 | 1.00× |
| + global | 551.46 | 592.62 | 1,144.08 | 1.74× |
| + flow paths | 499.57 | 340.47 | 840.04 | 1.28× |
| PM-GNN | 1,647.55 | 914.84 | 2,562.39 | 3.91× |

**Do not interpret these values as inference benchmarks or end-to-end speedup over
physical solvers.** Early stopping epochs differ across runs. Details in
`reproducibility/recorded_training_times.csv`.

## Data availability / citation / license

Original CT volume arrays are **not** included. The 11-sandstone source was described
as Digital Porous Media Portal DOI **10.17612/F4H1-W124**. See
[data availability instructions](data/README.md). Check other dataset DOI/permissions
against original dataset records before publication.

**Repository license is not yet selected.** Add a real `LICENSE` after the code owner
has decided what permissions to grant. Do not claim this package is already a
peer-reviewed, independently reproduced open-source implementation.
