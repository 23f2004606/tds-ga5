# Marimo Notebook
# Author email: 23f2004606@ds.study.iitm.ac.in
# This notebook demonstrates interactive variable exploration.

import marimo
from marimo import slider, md

# Cell 1: Create a slider widget
# Data flow: slider_value -> used in next cell for computation and markdown output
s = slider(start=1, stop=10, value=5, label="Select a multiplier")
s

# Cell 2: Dependent computation
# Data flow: uses slider state `s.value` to compute a derived variable
x = s.value * 2
x

# Cell 3: Dynamic markdown based on widget
# Data flow: md output updates automatically when `s.value` changes
md(f"You selected **{s.value}**, so the computed value is **{x}**.")
