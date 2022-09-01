import texttable as txtt
import latextable
import numpy as np


def to_LaTeX(data: list) -> str:
    table = txtt.Texttable()
    table.set_header_align(["c"] * len(data[0]))
    table.set_cols_align(["c"] * len(data[0]))
    table.set_cols_valign(["m"] * len(data[0]))
    table.set_deco(table.HEADER)
    for i in range(len(data)):
        table.add_row(data[i])
    print(table.draw())
    print()
    print(latextable.draw_latex(table, caption="An example table.", label="table:example_table", position='h'))
    return


# data
t = np.array(['t, c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x = np.array(['x, m', 0, 1, 2.1, 2.9, 4.2, 5.1, 6.2, 6.9, 8.1, 9])
terr_syst = np.array(['t_err,c', 0.2, 0.2, 0.3, 0.2, 0.3, 0.4, 0.2, 0.1, 0.2, 0.3])
xerr_syst = np.array(['x_err, m', 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
set_of_data = [t, terr_syst, x, xerr_syst]
to_LaTeX(set_of_data)
