from Cauchy_Dist.Cauchy_Dist import plot_cauchy, print_table_cauchy, draw_kde_cauchy, draw_emp_func_cauchy, boxplot_Tukey_cauchy
from Normal_Dist.NormalDist import task1, task2, task3, draw_kde_normal, draw_emp_func_normal
from Poisson_Dist.Poisson_Dist import plot_poisson, print_table_poisson, boxplot_Tukey_poisson, draw_kde_poisson, \
    draw_emp_func_poisson
from Uniform_Dist.Uniform_Dist import plot_uniform, print_table_uniform, boxplot_Tukey_uniform, draw_kde_uniform, \
    draw_emp_func_uniform

if __name__ == '__main__':
    sizes_1 = [10, 50, 1000]
    sizes_2 = [10, 100, 1000]
    sizes_3 = [20, 100]
    SIZES_4 = [20, 60, 100]
    times = 1000
    koefs = [0.5, 1, 2]
    common_l, common_r = -4, 4
    poisson_l, poisson_r = 6, 14
    M = 10.0
    begin = -1.7320508
    length = begin * 2
    # task1(sizes_1)
    #plot_cauchy(sizes_1, "cauchy nums", "denstiny", "cyan")
    #plot_poisson(M, sizes_1, "poisson nums", "denstiny", "cyan")
    plot_uniform(begin, length, sizes_1, "uniform nums", "denstiny", "royalblue")

    # task2(sizes_2)
    #print_table_cauchy(sizes_2, times)
    #print_table_poisson(M, sizes_2, times)
    print_table_uniform(sizes_2, times)

    # task3(sizes_3, times)
    #boxplot_Tukey_cauchy(sizes_3, times)
    #boxplot_Tukey_poisson(M, sizes_3, times)
    boxplot_Tukey_uniform(sizes_3, times)


    # draw_emp_func_normal(SIZES_4, common_l, common_r)
    # draw_kde_normal(SIZES_4, common_l, common_r, koefs)
    #draw_emp_func_cauchy(SIZES_4, common_l, common_r)
    #draw_kde_cauchy(SIZES_4, common_l, common_r, koefs)
    #draw_emp_func_poisson(M, SIZES_4, poisson_l, poisson_r)
    #draw_kde_poisson(M, SIZES_4, poisson_l, poisson_r, koefs)
    draw_emp_func_uniform(SIZES_4, common_l, common_r)
    draw_kde_uniform(SIZES_4, common_l, common_r, koefs)