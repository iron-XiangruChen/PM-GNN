# Evidence from the provided PM-GNN executed notebook

The author-provided full PM-GNN notebook, in the output of the rock-level split cell,
prints:

```text
数据划分方式: rock_group_8train_3val
训练集数量: 5777
验证集数量: 2081
训练集岩样数: 8
验证集岩样数: 3
```

The original source code, however, declared `SPLIT_MODE = "rock_group_9train_2val"`
near its start and only assigned the true `split_method` later, without updating
`SPLIT_MODE`. Hence the archived checkpoint filenames and config are stale **labels**.
The original notebook is listed in the provenance CSV by code SHA256, and the
provided result archive filenames remain unchanged. See KNOWN_LIMITATIONS.md.
