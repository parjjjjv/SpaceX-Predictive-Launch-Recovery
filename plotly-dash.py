# ============================================================
# IMPORT LIBRARIES
# ============================================================

import pandas as pd

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import plotly.express as px

# ============================================================
# LOAD DATASET
# ============================================================

spacex_df = pd.read_csv(r"C:\Users\parja\OneDrive\Desktop\DATASETS\spacex_launch_geo.csv")

# ============================================================
# PAYLOAD RANGE
# ============================================================

max_payload = spacex_df['Payload Mass (kg)'].max()

min_payload = spacex_df['Payload Mass (kg)'].min()

# ============================================================
# CREATE DASH APP
# ============================================================

app = dash.Dash(__name__)

# ============================================================
# APP LAYOUT
# ============================================================

app.layout = html.Div(children=[

    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    html.H1(

        'SpaceX Launch Records Dashboard',

        style={
            'textAlign': 'center',
            'color': '#503D36',
            'font-size': 40
        }

    ),

    # ========================================================
    # DROPDOWN
    # ========================================================

    dcc.Dropdown(

        id='site-dropdown',

        options=[

            {'label': 'All Sites', 'value': 'ALL'}

        ] + [

            {
                'label': site,
                'value': site
            }

            for site in spacex_df['Launch Site'].unique()

        ],

        value='ALL',

        placeholder='Select a Launch Site here',

        searchable=True

    ),

    html.Br(),

    # ========================================================
    # PIE CHART
    # ========================================================

    html.Div(

        dcc.Graph(id='success-pie-chart')

    ),

    html.Br(),

    # ========================================================
    # PAYLOAD TEXT
    # ========================================================

    html.P("Payload range (Kg):"),

    # ========================================================
    # RANGE SLIDER
    # ========================================================

    dcc.RangeSlider(

        id='payload-slider',

        min=0,

        max=10000,

        step=1000,

        marks={

            0: '0',
            2500: '2500',
            5000: '5000',
            7500: '7500',
            10000: '10000'

        },

        value=[min_payload, max_payload]

    ),

    html.Br(),

    # ========================================================
    # SCATTER PLOT
    # ========================================================

    html.Div(

        dcc.Graph(id='success-payload-scatter-chart')

    )

])

# ============================================================
# CALLBACK FOR PIE CHART
# ============================================================

@app.callback(

    Output(

        component_id='success-pie-chart',

        component_property='figure'

    ),

    Input(

        component_id='site-dropdown',

        component_property='value'

    )

)

def get_pie_chart(entered_site):

    # --------------------------------------------------------
    # ALL SITES
    # --------------------------------------------------------

    if entered_site == 'ALL':

        fig = px.pie(

            spacex_df,

            names='Launch Site',

            values='class',

            title='Total Successful Launches By Site'

        )

        return fig

    # --------------------------------------------------------
    # SPECIFIC SITE
    # --------------------------------------------------------

    else:

        filtered_df = spacex_df[

            spacex_df['Launch Site'] == entered_site

        ]

        success_counts = filtered_df['class'].value_counts()

        fig = px.pie(

            names=['Failure', 'Success'],

            values=success_counts.values,

            title=f'Success Rate for {entered_site}'

        )

        return fig

# ============================================================
# CALLBACK FOR SCATTER PLOT
# ============================================================

@app.callback(

    Output(

        component_id='success-payload-scatter-chart',

        component_property='figure'

    ),

    [

        Input(

            component_id='site-dropdown',

            component_property='value'

        ),

        Input(

            component_id='payload-slider',

            component_property='value'

        )

    ]

)

def update_scatter_chart(selected_site, payload_range):

    # --------------------------------------------------------
    # PAYLOAD RANGE
    # --------------------------------------------------------

    low, high = payload_range

    # --------------------------------------------------------
    # FILTER PAYLOAD RANGE
    # --------------------------------------------------------

    filtered_df = spacex_df[

        (spacex_df['Payload Mass (kg)'] >= low) &

        (spacex_df['Payload Mass (kg)'] <= high)

    ]

    # --------------------------------------------------------
    # ALL SITES
    # --------------------------------------------------------

    if selected_site == 'ALL':

        fig = px.scatter(

            filtered_df,

            x='Payload Mass (kg)',

            y='class',

            color='Booster Version',

            title='Correlation between Payload and Success for All Sites'

        )

        return fig

    # --------------------------------------------------------
    # SPECIFIC SITE
    # --------------------------------------------------------

    else:

        site_df = filtered_df[

            filtered_df['Launch Site'] == selected_site

        ]

        fig = px.scatter(

            site_df,

            x='Payload Mass (kg)',

            y='class',

            color='Booster Version',

            title=f'Correlation between Payload and Success for {selected_site}'

        )

        return fig

# ============================================================
# RUN APP
# ============================================================

if __name__ == '__main__':

    app.run(debug=True)