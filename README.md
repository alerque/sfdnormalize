# SFD Normalize

[![Build](https://github.com/alerque/sfdnormalize/actions/workflows/build.yml/badge.svg)](https://github.com/alerque/sfdnormalize/actions/workflows/build.yml)

Normalize Spline Font Database (SFD) files by discarding GUI state information making them easier to track in version control without clutter and conflicts between users.

```console
$ sfdnormalize --help

usage: sfdnormalize [-h] [--replace] [--version] [--keep KEEP]
                    [--sfd-version VERSION]
                    input_file [output_file]
https://github.com/alerque/sfdnormalize
(For authors, see AUTHORS in source distribution.)

Normalize Spline Font Database (SFD) files

positional arguments:
  input_file            Input SFD before normalization
  output_file           Path to write normalized SFD (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --replace, -r         Replace in place (default: False)
  --version, -V         show program's version number and exit
  --keep KEEP, -k KEEP  Keep lines beginning with these even if they'd be
                        normally dropped. (Can provide multiple times.)
                        (default: None)
  --sfd-version VERSION, -s VERSION
                        By default, latest SFD revision known to this program
                        will be written, unless specified here (default: 3.2)
```

## History

This script started life in the DejaVu Font project written in Perl (and dedicated to the Public Domain). At some point somebody rewrote it in Python, although I was unable to find any history between the latest Perl version and the first Python version that showed up in the Libertinus Font project.
