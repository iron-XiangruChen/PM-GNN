#!/usr/bin/env python3
"""Standard-library validation that GitHub notebook JSON exists, has no outputs,
and local path settings do not contain the original drive-specific paths."""
import ast, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
notebooks=list((ROOT/'notebooks').glob('*.ipynb'))
errors=[]
for path in sorted(notebooks):
    try:
        nb=json.loads(path.read_text(encoding='utf-8'))
        if nb.get('nbformat') != 4:errors.append(f'{path.name}: unexpected nbformat')
        for idx,c in enumerate(nb['cells']):
            if c['cell_type']!='code':continue
            if c.get('outputs'):errors.append(f'{path.name} cell {idx}: outputs not stripped')
            code=''.join(c.get('source',[]))
            if re.search(r'[A-Z]:\\(?:Deepl_Project|Doctor)',code):
                errors.append(f'{path.name} cell {idx}: private drive path remains')
            if not re.search(r'^\s*(?:%|!|\?)(?!\w+\s*=)',code,flags=re.M):
                try:ast.parse(code)
                except SyntaxError as exc:errors.append(f'{path.name} cell {idx}: Python syntax: {exc}')
    except Exception as exc:errors.append(f'{path.name}: {exc}')
if len(notebooks)!=10:errors.append(f'Expected 10 notebooks, found {len(notebooks)}')
if errors:
    print('FAILED:',*errors,sep='\n - ');sys.exit(1)
print(f'OK: {len(notebooks)} notebooks parse cleanly; all code cells have no outputs.')
print('Note: this is NOT a TensorFlow/PNM runtime reproduction test.')
