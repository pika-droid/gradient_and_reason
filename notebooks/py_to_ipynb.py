import json
import sys
import os

def py_to_ipynb(py_path, ipynb_path):
    with open(py_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by cell marker
    lines = content.splitlines()
    cells = []
    current_cell_lines = []
    current_cell_type = "code"

    for line in lines:
        if line.startswith("# =========================================="):
            # Save previous cell
            if current_cell_lines:
                cells.append({
                    "cell_type": current_cell_type,
                    "metadata": {},
                    "source": [l + "\n" for l in current_cell_lines]
                })
                current_cell_lines = []
            current_cell_type = "code"
        elif line.startswith("# CELL "):
            # Cell marker, skip
            pass
        else:
            current_cell_lines.append(line)

    if current_cell_lines:
        cells.append({
            "cell_type": current_cell_type,
            "metadata": {},
            "source": [l + "\n" for l in current_cell_lines]
        })

    # Clean up empty cells and refine cell types
    refined_cells = []
    for cell in cells:
        source_str = "".join(cell["source"]).strip()
        if not source_str:
            continue
        
        # If it's a cell that starts with a multi-line docstring, make it a markdown cell
        if source_str.startswith('"""') and source_str.endswith('"""'):
            # Convert to markdown
            md_content = source_str.strip('"""').strip()
            cell["cell_type"] = "markdown"
            cell["source"] = [l + "\n" for l in md_content.splitlines()]
            
        refined_cells.append(cell)

    notebook = {
        "cells": refined_cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    with open(ipynb_path, "w", encoding="utf-8") as f:
        json.dump(notebook, f, indent=2)
    print(f"Generated {ipynb_path} from {py_path}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        py_to_ipynb(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python py_to_ipynb.py <py_path> <ipynb_path>")
