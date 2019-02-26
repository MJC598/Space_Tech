from plotly import __version__
from plotly.offline import plot
import plotly.graph_objs as go
import math

def plot_me(x_a, acx_data, acy_data, acz_data, tmp_data, gyx_data, gyy_data, gyz_data):
    e1 = go.Scatter(x=x_a, y=acx_data, name='ACX')
    e2 = go.Scatter(x=x_a, y=acy_data, name='ACY')
    e3 = go.Scatter(x=x_a, y=acz_data, name='ACZ')
    e4 = go.Scatter(x=x_a, y=tmp_data, name='TMP')
    e5 = go.Scatter(x=x_a, y=gyx_data, name='GYX')
    e6 = go.Scatter(x=x_a, y=gyy_data, name='GYY')
    e7 = go.Scatter(x=x_a, y=gyz_data, name='GYZ')
    data_set = [e1]
    layout = go.Layout(title='Accelerometer', xaxis=dict(title='Time (s)'), yaxis=dict(title='Various Info'))
    fig = go.Figure(data = data_set, layout = layout)
    plot_url = plot(fig, filename='results.html')


if __name__ == "__main__":
    #TODO
    acx_data = []
    acy_data = []
    acz_data = []
    tmp_data = []
    gyx_data = []
    gyy_data = []
    gyz_data = []
    x = []
    i = 1
    info = open("accelerometer.txt", "r")

    for line in info:
        try:
            line = line.split(" ")
            acx_data.append(line[0])
            acy_data.append(line[1])
            acz_data.append(line[2])
            tmp_data.append(line[3])
            gyx_data.append(line[4])
            gyy_data.append(line[5])
            gyz_data.append(line[6])
        except OverflowError:
            pass
        x.append(i)
        i+=1 #x = x + 1

    plot_me(x, acx_data, acy_data, acz_data, tmp_data, gyx_data, gyy_data, gyz_data)