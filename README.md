# diffa   
_A simple CLI tool for generating nice HTML diffs between two files._  

## 🌟 Features  
- Generates pretty colour-coded **HTML diffs**.  
- Supports both **unified view** and **side-by-side view**.  

## 📦 Installation  
Use pip to install diffa from PyPI:  
```bash
pip install diffa
```

## 🛠️ Usage
Run diffa from the command line to create a shiny HTML diff.

```bash
diffa file1.txt file2.txt output.html
````

### Options
`--side-by-side`: Adds a side-by-side comparison to the output.

## The Output
Open the generated HTML file in your browser to see:

- Lines added in green
- Lines removed in red
- Matching lines in white

## 💡 Ideas for Use
- Code Reviews: Quickly generate diffs for commits or branches.
- Document Comparison: Spot the differences between document revisions.
- Configuration Changes: Compare config files across environments.
