# SRComp Validate Action

A GitHub Action to validate a compstate.

## Usage

This action aims to be a fully self-contained validator for Compstate repos. Usage is therefore very simple:

``` yaml
name: Validate

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: PeterJCLaw/srcomp-validate-action@v0.3
```
