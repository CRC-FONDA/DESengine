import os
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px

pio.kaleido.scope.mathjax = None


fig = go.Figure()

fig.add_trace(go.Scatter(name="DesisCen", x=[2, 10, 50, 100, 500, 1000], mode='lines+markers'
                         , y=[2655895.53, 984385.516, 226051.66, 136779.975, 55359.736, 46494.372]
                         , line=dict(color='rgb(100, 30, 22)', width=5), marker=dict(size=20, symbol='circle')))
fig.add_trace(go.Scatter(name="DesisIC", x=[2, 10, 50, 100, 500, 1000], mode='lines+markers'
                         , y=[16294481.44, 3731987.076, 655939.378, 279072.098, 56809.41, 27494.24]
                         , line=dict(color='rgb(21, 67, 97)', width=5), marker=dict(size=20, symbol='square')))
fig.add_trace(go.Scatter(name="DesisSW", x=[2, 10, 50, 100, 500, 1000], mode='lines+markers'
                         , y=[29073237.24, 29517521.79, 28812342.55, 28381546.46, 29106038.64, 28742027.52]
                         , line=dict(color='rgb(126, 81, 10)', width=5), marker=dict(size=20, symbol='triangle-up')))
fig.add_trace(go.Scatter(name="Desis", x=[2, 10, 50, 100, 500, 1000], mode='lines+markers'
                         , y=[31774489.07, 31270061.07, 32186826.55, 31516253.98, 31345975.1, 31029385.73]
                         , line=dict(color='rgb(21, 90, 50)', width=5), marker=dict(size=20, symbol='cross')))

# fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.6,
# marker=dict(size=10, symbol='triangle-up'))))

fig.add_trace(go.Scatter(xaxis='x2'))
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
            size=23,
            color="black"
        ),
    ),
    yaxis=dict(
        title_text="events/sec",
        titlefont=dict(size=35),
        exponentformat="e",
        ticktext=["0", "5M", "10M", "15M", "20M", "25M", "30M", "35M"],
        tickvals=[0, 5000000, 10000000, 15000000, 20000000, 25000000, 30000000, 35000000],
        tickmode="array",
        range=[0, 36000000],
        tickfont=dict(size=35),
        # ticks="inside",
        # ticklen=20,
        # tickwidth =5,
    ),
    xaxis=dict(
        title_text="queries",
        titlefont=dict(size=35),
        ticktext=["2","10", '100', "1000"],
        tickvals=[2, 10, 100, 1000],
        range=[0.3,3],
        type="log",
        ticks = "inside",
        ticklen = 20,
        tickwidth = 5,
        tickfont=dict(size=35),
    ),
    xaxis2=dict(
        ticktext=["50", "500"],
        tickvals=[50, 500],
        range=[0,3],
        type="log",
        ticks="inside",
        ticklen=20,
        tickwidth=5,
        overlaying="x",
        side="bottom",
        tickfont=dict(size=15),
    )
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
fig.update_xaxes(showline=True, linewidth=3, linecolor='black'#, mirror=True
                 )
fig.update_yaxes(showline=True, linewidth=3, linecolor='black'#, mirror=True
                 )
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgb(120,120,120)')
fig.show()
if not os.path.exists("E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s2"):
    os.mkdir("E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s2")
# fig.write_image("images/fig1.svg")
pio.write_image(fig, "E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s2\shareWindow\/tumtum.pdf")
pio.write_image(fig, "E:\my paper\DesisPaper\Desis-Optimizing-Decentralized-Window-Aggregation\experiment\s2\shareWindow\/tumtum.svg")