# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Updated `README.md`

## [0.1.0] - 2024-04-25

### Added

When using the `mpl_ascii` backend then `plt.show()` will print the plot as a string consisting of basic ASCII characters. This is supported for:

    - Bar charts
    - Horizontal bar charts
    - Line plots
    - Scatter plots

You can also save figures as a text file. You can do this by using the savefig `figure.savefig("my_figure.txt")` and this will save the ASCII plot as a txt file.

