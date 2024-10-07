# Analysis

This folder contains several scripts & notebooks to document the analysis

If you just want to read the results, have a look at this static markdown file for the full [report](full_report.md).

The corresponding code documenting how each figure in the report was created can be found in jupyter notebook `tea_survey_narrative_report.ipynb`

All figures generated through this notebook as well as those figures that have been further formatted / adapted in illustartor can be found in folder `report_plots`.

## Content Analysis

To view the notebook documenting the content analysis process follow these steps:

- Step 1: Download the files in this folder (or clone but note this will download the entire survey app!)
- Step 2: Create notebook environment using conda

```
conda env create -f content_environment.yml
conda activate myenv
```

- Step 3: Move data file into data_analysis folder
- Step 4: Run notebook

```
jupyter notebook
```
