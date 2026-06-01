#!/usr/bin/env python3
"""
fix_svg_ns.py
Uklanja neispravni svg: namespace prefiks koji je ET dodao.
Zamjenjuje: xmlns:svg="..." → xmlns="..."  i  <svg:TAG → <TAG  i  </svg:TAG → </TAG
"""
import glob
import re
import sys

pattern = 'assets/print/u*.svg'
files = sorted(glob.glob(pattern))

fixed = 0
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'svg:' not in content and 'xmlns:svg' not in content:
        continue  # nema problema

    original = content

    # 1. xmlns:svg="http://www.w3.org/2000/svg" -> xmlns="http://www.w3.org/2000/svg"
    content = content.replace('xmlns:svg="http://www.w3.org/2000/svg"', 'xmlns="http://www.w3.org/2000/svg"')

    # 2. <svg:TAG -> <TAG  (opening tags)
    content = re.sub(r'<svg:', '<', content)

    # 3. </svg:TAG -> </TAG  (closing tags)
    content = re.sub(r'</svg:', '</', content)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed += 1

print(f'Popravljeno {fixed} datoteka.')
