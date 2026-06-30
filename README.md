# Data Cleaning & Reporting Automation

## Overview

Data Cleaning & Reporting Automation is a Python-based project that automates the process of cleaning raw datasets and generating summary reports. It helps improve data quality by handling missing values, removing duplicate records, correcting inconsistent data, and creating visual reports for easy analysis.

## Features

* Import data from CSV files
* Remove duplicate records
* Handle missing values automatically
* Clean inconsistent data
* Generate a cleaned dataset
* Create summary statistics
* Generate bar chart visualizations
* Save reports automatically

## Technologies Used

* Python
* Pandas
* Matplotlib
* CSV

## Project Structure

```
DataCleaningProject/
│── data.csv
│── data_cleaning.py
│── cleaned_data.csv
└── report.png
```

## How to Run

1. Install the required libraries:

   ```
   pip install pandas matplotlib
   ```
2. Place your dataset (`data.csv`) in the project folder.
3. Run the program:

   ```
   python data_cleaning.py
   ```
4. The program will generate:

   * `cleaned_data.csv`
   * `report.png`

## Expected Output

* Cleaned dataset with missing values handled
* Duplicate records removed
* Summary report displayed in the terminal
* Bar chart showing average salary by department

## Learning Outcomes

* Data preprocessing using Python
* Data cleaning techniques
* Report automation
* Data visualization with Matplotlib
* CSV file handling using Pandas

## Future Enhancements

* Excel (.xlsx) file support
* Interactive dashboard using Power BI
* Automatic PDF report generation
* GUI using Tkinter
* Database integration with MySQL

## Author

Developed as a mini project for learning Data Cleaning & Reporting Automation using Python.
