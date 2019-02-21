from plotly import __version__
from plotly.offline import plot
import plotly.graph_objs as go
import math



#this is all the stuff to graph the data
def plot_it(x_a, data1):
    e1 = go.Scatter(x=x_a, y=data1, name='Test Results')

    data_set = [e1]
    layout = go.Layout(title='IR Data Test', xaxis=dict(title='Time (s)'), yaxis=dict(title='Distance (mm)'))
    fig = go.Figure(data = data_set, layout = layout)
    plot_url = plot(fig, filename='results.html')

if __name__ == "__main__":
    data1 = []
    x = []
    i = 1
    info = open("info2.txt", "r")
    for line in info:
        try:
            voltage = float(line)
            distance = voltage/100
            # voltage = voltage / 222.2222
            # voltage = voltage * 1.967
            # total = math.exp(voltage)
            # distance = 1.3927 * total
        except OverflowError:
            distance = 1000000000
        data1.append(distance)
        x.append(i)
        i+=1

    plot_it(x, data1)

