# NYC Crime Visualization

This project visualizes violent crime data in New York City using interactive components from [Preswald](https://docs.preswald.com/introduction).

This was part of a previous project I worked with using Google CoLab: https://colab.research.google.com/drive/1xetEZseenXIPxxRpjnrpe3PUh9Y-T_jJ#scrollTo=Tds8uYn7ECJ1.

I avoided using any frontend framework for the purpose of experimenting with preswald using python scripts.

The app includes:

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

This proejct is hosted on [Render](https://nyc-crime-visualize.onrender.com/) using the command:
-build: pip install -r requirements.txt
-start: preswald run
