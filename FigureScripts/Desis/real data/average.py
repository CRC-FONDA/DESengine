import os
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

import os
import sys
# Append parent directory to import path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
pio.kaleido.scope.mathjax = None



windowType = ['CeBuffer', 'Scotty', "Disco", "Desis"]
widthSin = 0.8
widthAll=[widthSin]

fig = go.Figure()

fig.add_trace(go.Bar(name="Local", x=windowType, y=[49.67879,  49.6, 0.0163515, 0.00001618*10]
                     , legendrank=1, width=widthAll
                     # , text="<b>2.98GB<b>", textposition='outside', textfont = dict(size = 25)
                     , marker_color=config.central))
fig.add_trace(go.Bar(name="Intermediate", x=windowType, y=[49.6738,  49.6076, 0.0163515, 0.00001618*10]
                     , legendrank=2, width=widthAll
                     , text=["<b>99.35MB<b>","<b>99.21MB<b>","<b>32.73KB<b>","<b>0.324KB<b>"], textposition='outside', textfont = dict(size = 25)
                     , marker_color=config.disco))


#legend
fig.update_layout(
    legend=dict(
        orientation="h",
        yanchor="top",
        y=1.2,
        xanchor="left",
        x=-0.05,
        # bordercolor="Black",
        # borderwidth=2,
        # bgcolor="white",
        font=dict(
            size=30,
            color="black"
        ),
    ),
    yaxis=dict(
        title_text="bytes sent in min",
        titlefont=dict(size=35),
        ticktext=["0", "40MB", "80MB", "120MB"],
        tickvals=[0, 40, 80, 120],
        tickmode="array",
        range=[0, 122],
        ticks="inside",
        ticklen=20,
        tickwidth=5,
    ),
    xaxis=dict(
        # title_text="local nodes",
        # titlefont=dict(size=15),
        ticktext=['central', 'Scotty', "Disco", "Desis"],
        # tickvals=[1, 2, 3, 4],
        tickmode="array",
        # range=[0, 6],
    ),
)

# size & color
fig.update_layout(
    autosize=False,
    width=660,
    height=440,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(
        l=5,
        r=5,
        b=5,
        t=5,
        pad=0
    ),
)
fig.update_layout(barmode='stack', bargap=0.15, bargroupgap=0.0)

fig.update_xaxes(showline=True, linewidth=3, linecolor='black'#, mirror=True
                 , tickfont=dict(size=25))
fig.update_yaxes(showline=True, linewidth=3, linecolor='black'#, mirror=True
                 , tickfont=dict(size=35))
# fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(120,120,120)')

fig.show()
if not os.path.exists("E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s3"):
    os.mkdir("E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s3")

# fig.write_image("images/fig1.svg")
pio.write_image(fig, "E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s3\/networkoverhead.pdf")
pio.write_image(fig, "E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s3\/networkoverhead.svg")