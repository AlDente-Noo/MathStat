import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from statsmodels.distributions.empirical_distribution import ECDF
from utilities import utils as u
import seaborn as sns
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
        #plt.show()
        plt.savefig(u.SAVE_PATH + "normal" + str(size) + ".png")
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
            distr = norm.rvs(size=size)
            distr.sort()
            count += u.number_of_emissions(distr)
        result.append(count/(size * repeats))

        distr = norm.rvs(size=size)
        distr.sort()
        tips.append(distr)
    u.draw_boxplot_Tukey(tips, "Tukey")
    u.print_emissions(sizes, result)
    return
def draw_emp_func_normal(sizes : list, left_border : float, right_border : float):
    sns.set_style('whitegrid')
    figures, axs = plt.subplots(ncols=3, figsize=(15,5))
    for size in range(len(sizes)):
        x = np.linspace(left_border, right_border, 10000)
        y = norm.cdf(x)
        sample = norm.rvs(size = sizes[size])
        sample.sort()
        ecdf = ECDF(sample)
        axs[size].plot(x, y, color='blue', label='cdf')
        axs[size].plot(x, ecdf(x), color='black', label='ecdf')
        axs[size].legend(loc='lower right')
        axs[size].set(xlabel='x', ylabel='$F(x)$')
        axs[size].set_title("Normal" + ' n = ' + str(sizes[size]))
    figures.savefig(u.SAVE_PATH + "Normal.jpg")
    return

def draw_kde_normal(sizes : list, left_border : float, right_border : float, koefs : list):
    sns.set_style('whitegrid')
    for size in range(len(sizes)):
        figures, axs = plt.subplots(ncols=len(koefs), figsize=(15,5))
        x = np.linspace(left_border, right_border, 10000)
        for kf in range(len(koefs)):
            y = norm.pdf(x)
            sample = norm.rvs(size = sizes[size])

            axs[kf].plot(x, y, color='blue', label='pdf')
            sns.kdeplot(data=sample, bw_method='silverman', bw_adjust = koefs[kf], ax=axs[kf],
                        fill=True, common_norm=False, palette="crest", alpha=0, linewidth=2, label='kde')
            axs[kf].legend(loc='upper right')
            axs[kf].set(xlabel='x', ylabel='$f(x)$')
            axs[kf].set_xlim([left_border, right_border])
            axs[kf].set_title(' h = ' + str(koefs[kf]))

        figures.suptitle('Normal KDE n = ' + str(sizes[size]))
        figures.savefig(u.SAVE_PATH + "Normal KDE"+ str(sizes[size])+".jpg")
    return
