import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from statsmodels.distributions.empirical_distribution import ECDF
from utilities import utils as u
def task1(sizes : list):
    for size in sizes:
        fig, ax = plt.subplots(1, 1)
        x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
        ax.plot(x, norm.pdf(x),
                'r-', lw=5, alpha=0.6, label='norm pdf')

        hist = norm.rvs(size = size)
        ax.hist(hist, density=True)
        plt.grid()
        ax.set_xlabel('normalNumbers')
        ax.set_ylabel('Density')
        ax.set_title("n = " + str(size))
        plt.show()
def task2(sizes : list):
    for size in sizes:
        means, meds, zRs, zQs, zTRs = [], [], [], [], []
        table = [means, meds, zRs, zQs, zTRs]
        E, D = [], []
        for i in range(1000):
            distr = norm.rvs(size=size)
            distr.sort()
            means.append(u.mean(distr))
            meds.append(u.median(distr))
            zRs.append(u.zR(distr))
            zQs.append(u.zQ(distr))
            zTRs.append(u.zTR(distr))
        for column in table:
            E.append(round(u.mean(column), u.ROUND_SIGNS))
            D.append(round(u.dispersion(column), u.ROUND_SIGNS))
        # print("size: " + str(size))
        u.print_table_rows(E, D, "Normal E(z) " + str(size), "Normal D(z) " + str(size))
    return
def task3(sizes : list, repeats : int):
    tips, result, count = [], [], 0
    for size in sizes:
        for i in range(repeats):
            distr = norm.rvs(size = size)
            distr.sort()
            count += u.number_of_emissions(distr)
        result.append(count/(size * repeats))

        distr = norm.rvs(size = size)
        distr.sort()
        tips.append(distr)
    u.draw_boxplot_Tukey(tips, "Tukey")
    u.print_emissions(sizes, result)
    return

