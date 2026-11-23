# Learning References

Use this guide alongside the example scripts in this project. The links point to official documentation for the libraries and tools used here.

## Suggested reading order

1. **Python virtual environments** — [Python `venv` documentation](https://docs.python.org/3/library/venv.html). Covers creating and activating an isolated environment for this project.
2. **Pandas fundamentals** — [Pandas getting-started tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html). Covers Series and DataFrames, selecting and filtering rows, reading and writing tabular files, and summary statistics. Pair this with `pandas_understanding/series_dataframe.py` and `pandas_understanding/exercise_series_dataframe.py`.
3. **CSV and Excel data** — [Pandas I/O guide](https://pandas.pydata.org/docs/user_guide/io.html). Use it with `pandas_understanding/csv_exercise.py` and `pandas_understanding/excel_csv_exercise.py` to learn file input and output.
4. **Summarizing test results** — [Pandas introductory tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html). Review filtering, derived values, and summary statistics while working through `pandas_automation_exercise/automation_report.py` and `automation_visualization/automation_visualization.py`.
5. **Matplotlib charts** — [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html) and the [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html). These explain figures, axes, chart types, labels, legends, and saving plots. Pair them with the scripts in `matplotlib_understanding/`.
6. **Excel workbook engine** — [openpyxl documentation](https://openpyxl.readthedocs.io/en/stable/). Pandas uses an Excel engine such as openpyxl to write `.xlsx` workbooks.

## Quick lookup

| Project topic | Example files | Documentation |
| --- | --- | --- |
| Series and DataFrames | `pandas_understanding/series_dataframe.py`, `pandas_understanding/exercise_series_dataframe.py` | [Pandas data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html) |
| Filtering and selecting rows | `pandas_understanding/csv_exercise.py` | [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html) |
| CSV and Excel | `pandas_understanding/excel_csv_exercise.py` | [Pandas I/O guide](https://pandas.pydata.org/docs/user_guide/io.html) |
| Bar and line charts | `matplotlib_understanding/` | [Matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html) |
| Automation metrics and charts | `pandas_automation_exercise/`, `automation_visualization/` | [Pandas tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html), [Matplotlib tutorials](https://matplotlib.org/stable/tutorials/index.html) |
