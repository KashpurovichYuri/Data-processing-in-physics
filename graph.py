# libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import chi2
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator, NullFormatter


def graph_build(x, xerr, y, yerr):
    # font settings
    mpl.rcParams['font.fantasy'] = 'Arial', 'Times New Roman', 'Tahoma'
    mpl.rcParams['font.family'] = 'fantasy'
    mpl.rcParams.get('font.family')[0]
    mpl.rcParams.get('font.fantasy')[1]

    # figsize settings
    mpl.rcParams['figure.figsize'] = 7.5, 4.5
    # preamble for working with LaTeX (r'text' as attributes for objects of matplotlib.text.Text)
    # plt.rc('text', usetex=True)

    # Figure
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='.k', mew=0.25)
    for ax in fig.axes:  # minor grid for axes
        ax.grid(visible=True, which='both', ls='--')
    ax.set_title('Plot of coordinate versus time')
    ax.set_xlabel('t^2, c')
    ax.set_ylabel('x, m')
    ax.set_xlim(left=min(t), right=max(t))
    ax.set_ylim(bottom=min(x), top=max(x))

    # axis
    majorLocator = MultipleLocator(20)
    xaxminorLocator = AutoMinorLocator(n=20)
    yaxminorLocator = AutoMinorLocator(n=10)
    # OX
    xax = ax.get_xaxis()
    xlabels = xax.get_ticklabels()
    xlines = xax.get_ticklines()
    for label in xlabels:
        label.set_color('black')  # цвет подписи деленений оси OX
        label.set_rotation(0)  # поворот подписей деленений оси OX 
        label.set_fontsize(11)  # размер шрифта подписей делений оси OX
    for line in xlines:
        line.set_color('black')  # задаём цвет линии деления
        line.set_markersize(3.5)  # задаём длину линии деления
        line.set_markeredgewidth(0.75)  # задаём толщину линии деления
    # xax.set_label_text('t, c')
    xax.set_major_locator(majorLocator)
    xax.set_minor_locator(xaxminorLocator)
    xax.set_minor_formatter(NullFormatter())
    # OY
    yax = ax.get_yaxis()
    ylabels = yax.get_ticklabels()
    ylines = yax.get_ticklines()
    for label in ylabels:
        label.set_color('black')  # цвет подписи деленений оси OY
        label.set_rotation(0)  # поворот подписей деленений оси OY
        label.set_fontsize(11)  # размер шрифта подписей делений оси OY
    for line in ylines:
        line.set_color('black')  # задаём цвет линии деления
        line.set_markersize(3.5)  # задаём длину линии деления
        line.set_markeredgewidth(0.75)  # задаём толщину линии деления
    xax.set_major_locator(majorLocator)
    yax.set_minor_locator(yaxminorLocator)
    yax.set_minor_formatter(NullFormatter())

    # data processing
    model = LinearRegression()
    model.fit(t.reshape(-1, 1), x)
    # print(model.coef_, model.intercept_)
    plt.plot(t, model.predict(t.reshape(-1, 1)))

    # legend
    for ax in fig.axes:  
        ax.legend(loc = 'best')
    plt.legend([
        'Predicted line, k = ' + str(model.coef_[0]),
        'Observed data'
        ])

    plt.tight_layout()  # autodistances beetwen axes
    fig.savefig('C:\MIPT\Labs\pic.png', format='png')
    plt.show()

    return

# data_example
t = np.arange(10)
x = np.array([0, 1, 2.1, 2.9, 4.2, 5.1, 6.2, 6.9, 8.1, 9])
x **= 2
terr_syst = np.array([0.2, 0.2, 0.3, 0.2, 0.3, 0.4, 0.2, 0.1, 0.2, 0.3])
xerr_syst = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
t **= 2
terr_syst *= 2
graph_build(t, terr_syst, x, xerr_syst)
