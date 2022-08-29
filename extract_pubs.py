#!/usr/bin/env python
from subprocess import check_call

bibfile = "publications-2021.bib"

with open(bibfile) as fid:
    lines = fid.readlines()

keys = list(filter(lambda s: s[0] == "@", lines))
keys = [s.strip().replace(",", "").split("{")[1] for s in keys]

preamble = [
    r"\documentclass[11pt]{article}",
    r"\begin{document}",
]

post = [
    r"\bibliographystyle{agu-based-rev-num}",
    r"\bibliography{publications}",
    r"\end{document}",
]

with open("pubs.tex", "w") as fid:
    for line in preamble:
        fid.write(f"{line}\n")
    for key in keys:
        fid.write(f"\\nocite{{{key}}}\n")
    for line in post:
        fid.write(f"{line}\n")

docxfile = bibfile.replace(".bib", ".docx")

check_call(
    [
        "pandoc",
        "-s",
        "--bibliography",
        bibfile,
        "--citeproc",
        "pubs.tex",
        "-o",
        docxfile,
    ]
)
check_call(["rm", "-f", "pubs.tex"])
