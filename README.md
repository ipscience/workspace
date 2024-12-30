# workspace

## Analyzing Patent Data

This repository contains a CSV file named `特実_国内文献 .csv` with patent data. The CSV file includes columns such as "文献番号", "出願番号", "出願日", "公知日", "発明の名称", "出願人/権利者", "FI", "公開番号", "公告番号", "登録番号", "審判番号", "その他", "ステージ", "イベント詳細", and "文献URL".

## Running the Analysis Script

A Python script `analyze_patents.py` has been added to analyze the CSV file and generate graphs. The script reads the `特実_国内文献 .csv` file and processes the data. The script generates graphs for various analyses such as the number of patents per year, patents by company, and patents by status.

### Prerequisites

Make sure you have the following libraries installed:

- pandas
- matplotlib
- seaborn

You can install them using pip:

```sh
pip install pandas matplotlib seaborn
```

### Running the Script

To run the script, use the following command:

```sh
python analyze_patents.py
```

### Generated Graphs

The script generates the following graphs:

1. **Number of Patents per Year**: A bar graph showing the number of patents filed each year.
2. **Number of Patents by Company**: A bar graph showing the number of patents filed by the top 10 companies.
3. **Number of Patents by Status**: A pie chart showing the distribution of patents by their status.

The generated graphs will be saved as `patents_per_year.png`, `patents_by_company.png`, and `patents_by_status.png` in the current directory.

### Interpreting the Graphs

- **Number of Patents per Year**: This graph helps to understand the trend of patent filings over the years. A higher number of patents in a particular year indicates increased innovation or activity in that year.
- **Number of Patents by Company**: This graph shows which companies are leading in patent filings. It helps to identify the major players in the industry.
- **Number of Patents by Status**: This pie chart provides an overview of the current status of the patents. It helps to understand how many patents are active, expired, or in other stages.
