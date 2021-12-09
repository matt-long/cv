#!/usr/bin/env python
from subprocess import check_call


with open('publications.bib') as fid:
    lines = fid.readlines()

keys = list(filter(lambda s: s[0] == '@', lines))
keys = [s.strip().replace(',', '').split('{')[1] for s in keys]

preamble = [
    r'\documentclass[11pt]{article}',
    r'\begin{document}',
]

post = [
    r'\bibliographystyle{agu-based-rev-num}',
    r'\bibliography{publications}',
    r'\end{document}',
]

with open('pubs.tex', 'w') as fid:
    for line in preamble:
        fid.write(f'{line}\n')
    for key in keys:
        fid.write(f'\\nocite{{{key}}}\n')
    for line in post:
        fid.write(f'{line}\n')

check_call(
    ['pandoc', '-s', '--bibliography', 'publications.bib',
    '--filter', 'pandoc-citeproc', 'pubs.tex', '-o', 'pubs.docx'
    ]
)
