# NYC Crime Visualization

This project visualizes violent crime data in New York City using interactive components from [Preswald](https://preswald.ai/). The app includes:

- 📊 A **data table** showing violent crime categories per borough.
- 📈 A **bar chart** displaying total arrests per month.

## 📁 Data Source

- Kaggle dataset: `NYPD Arrest Data 2023`

## 🔍 Features

- Query-based filtering using SQL
- Borough selection dropdown
- Clean visuals with no React required

## 🛠️ Tech Stack

- Python
- Preswald
- Plotly Express
- SQL

## 🐞 Known Bugs

- Dropdown does not auto-trigger chart/table rerender.
- Manual page refresh is required after selection change.

## 🚀 Deployment

This proejct is hosted on [Render](https://render.com) using the command:
-build: pip install -r requirements.txt
-start: preswald run
