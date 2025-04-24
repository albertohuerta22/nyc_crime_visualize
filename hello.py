from preswald import connect, query, table, selectbox, text, sidebar, topbar, separator, plotly
import plotly.express as px
from typing import Dict


class NYCCrimeData:
    def __init__(self):
        connect()
        topbar()
        sidebar(defaultopen=True)

        self.borough_options = ["K", "M", "B", "Q", "S"]
        self.borough_labels: Dict[str, str] = {
            "K": "Brooklyn",
            "M": "Manhattan",
            "B": "Bronx",
            "Q": "Queens",
            "S": "Staten Island"
        }

    def fetch_and_display_table_data(self, selected_borough: str) -> None:
        """
        Fetches and displays violent crime data for the selected borough.
        """
        sql = f"""
            SELECT 
                ARREST_BORO, 
                OFNS_DESC, 
                COUNT(*) as crime_count
            FROM NYPD_Arrest_Data_2023
            WHERE ARREST_BORO = '{selected_borough}'
              AND OFNS_DESC IN (
                  'ROBBERY', 
                  'ASSAULT 3 & RELATED OFFENSES', 
                  'FELONY ASSAULT', 
                  'MURDER & NON-NEGL. MANSLAUGHTER',
                  'RAPE',
                  'SEX CRIMES',
                  'CRIMINAL POSSESSION OF A WEAPON'
              )
            GROUP BY ARREST_BORO, OFNS_DESC
            HAVING COUNT(*) > 0
        """
        filtered_df = query(sql, "NYPD_Arrest_Data_2023")
        text(f"### {self.borough_labels[selected_borough]} Crime")
        text("#### Please Refresh Page After Selecting")
        table(filtered_df, title=f"Select - {self.borough_labels[selected_borough]}")

    def fetch_and_display_scatter_data(self, selected_borough: str) -> None:
        """
        Fetches and displays total arrests per month for the selected borough.
        """
        sql = f"""
            SELECT 
                EXTRACT(MONTH FROM ARREST_DATE) AS month,
                COUNT(*) AS total_arrests
            FROM NYPD_Arrest_Data_2023
            WHERE ARREST_BORO = '{selected_borough}'
            GROUP BY month
            ORDER BY month
        """
        scatter_df = query(sql, "NYPD_Arrest_Data_2023")

      
        month_map = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
            6: 'June', 7: 'July', 8: 'August', 9: 'September',
            10: 'October', 11: 'November', 12: 'December'
        }
        scatter_df['month'] = scatter_df['month'].map(month_map)


        alternating_colors = [
            '#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3',
            '#FF6692', '#B6E880', '#FF97FF', '#FECB52', '#1F77B4', '#FF7F0E'
        ]
        color_map = {
            month: alternating_colors[i % len(alternating_colors)]
            for i, month in enumerate(month_map.values())
        }

        fig = px.bar(
            scatter_df,
            x="month",
            y="total_arrests",
            color="month",
            color_discrete_map=color_map,
            labels={"month": "Month", "total_arrests": "Total Arrests"},
            title=f"Total Arrests per Month - {self.borough_labels[selected_borough]}"
        )

        plotly(fig)

    def display(self) -> None:
        """
        Displays the full UI with borough selection, crime table, and bar chart.
        """
        text("# NYC Crime Data Table")
        selected_borough = selectbox(
            label="Select Borough",
            options=self.borough_options,
            default="K"
        )
        self.fetch_and_display_table_data(selected_borough)
        separator()
        text("# Arrests per Month - Bar Chart")
        self.fetch_and_display_scatter_data(selected_borough)



nyc_crime_data = NYCCrimeData()
nyc_crime_data.display()
