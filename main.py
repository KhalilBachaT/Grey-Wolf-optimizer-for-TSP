import plotly.graph_objects as go
from plotly.subplots import make_subplots
import keyboard
import functions
import gwo_tsp


# View the result in simple html file
# give the example of four cities and calculate
def main():
    nb_wolf = 20
    max_iter = 30
    print("/**---------------Welcome to Grey_wolf_optimize_for_TSP---------------**/")
    nb_cities = int(input("Enter the number of cities you want : "))
    print("if you want to change the default parameters press 'y' else press 'n':")
    while True:
        if keyboard.is_pressed('y'):
            nb_wolf = int(
                input("Enter the number of wolves you want (by default it's 20) press enter if not : "))
            max_iter = int(
                input("Enter the number of iterations (by default it's 30) you want press enter if not : "))
            break
        elif keyboard.is_pressed('n'):
            break
        else:
            continue
    X, Y, x_w, y_w, x_p, y_p = [], [], [], [], [], []
    wolves_static = {}
    wolves = {}
    short_path = []
    indices = []
    cost = 0
    cts = functions.init_cities(nb_cities)
    my_wolves = functions.init_wolves(nb_wolf)
    for i, w in my_wolves.items():
        wolves_static[i] = my_wolves[i]
        x_w.append(w[0])
        y_w.append(w[1])
    for c, cc in cts.items():
        X.append(cc[0])
        Y.append(cc[1])

    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(go.Scatter(
        x=X,
        y=Y,
        name='cities',
        mode='markers + text',
        text=list(cts.keys()),
        textposition="top center",
        marker_size=12,
        marker_color='rgba(152, 0, 0, .8)'
    ))

    fig.add_trace(go.Scatter(
        x=x_w, y=y_w,
        name='wolves',
        mode='markers',
        marker_size=10,
        marker_color='rgba(0, 150, 0, .8)'))

    for s in cts.keys():
        print("-------------------------------")

        path, wolves = gwo_tsp.GWO_TSP(cts, s, my_wolves, max_iter)
        path.append(path[0])
        x_w = []
        y_w = []
        for i, w in wolves.items():
            x_w.append(w[0])
            y_w.append(w[1])
        fig.add_trace(go.Scatter(
            x=x_w, y=y_w,
            name='wolves_updated',
            mode='markers',
            marker_size=10,
            marker_color='rgba(0, 0, 150, .8)'), row=1, col=2)
        for p in path:
            cost += cts[s][2][p]
            x_p.append(cts[p][0])
            y_p.append(cts[p][1])
        fig.add_trace(go.Scatter(x=x_p, y=y_p,
                                 mode='lines+markers+text',
                                 text=list(cts.keys()),
                                 textposition="top center",
                                 marker_size=16,
                                 name='shortest path from city: '+str(s)+' cost '+str(
                                     round(cost, 2))), row=1, col=2)
        x_p = []
        y_p = []
        if len(short_path) == 0:
            short_path.append(path)
            short_path.append(cost)
        else:
            if cost < short_path[1]:
                short_path[0] = path
                short_path[1] = cost
            pass
        cost = 0
        #print("path is from start city " + str(s)+" is: ", path)

    x_p = []
    y_p = []
    for i in short_path[0]:
        x_p.append(cts[i][0])
        y_p.append(cts[i][1])
    print(list(cts.keys()))
    print(short_path[0])
    fig.append_trace(go.Scatter(x=x_p, y=y_p,
                                mode='lines+markers+text',
                                text=short_path[0],
                                textposition="top center",
                                marker_size=12,
                                name="the best path is : "+str(short_path[0])+" => : "+str(round(short_path[1], 2))), row=1, col=2)
    x_w = []
    y_w = []

    fig.write_html('GWO-for-TSP.html', auto_open=True)


main()
