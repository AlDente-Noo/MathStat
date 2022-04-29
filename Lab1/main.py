from Normal_Dist.NormalDist import task2
from Normal_Dist.NormalDist import task1
from Normal_Dist.NormalDist import task3
from Normal_Dist.NormalDist import draw_kde_normal
from Normal_Dist.NormalDist import draw_emp_func_normal
if __name__ == '__main__':
    sizes_1 = [10, 50, 1000]
    sizes_2 = [10, 100, 1000]
    sizes_3 = [20, 100]
    SIZES_4 = [20, 60, 100]
    times = 1000
    koefs = [0.5, 1, 2]
    common_l, common_r = -4, 4
    poisson_l, poisson_r = 6, 14
    task1(sizes_1)
    task2(sizes_2)
    task3(sizes_3, times)
    draw_emp_func_normal(SIZES_4, common_l, common_r)
    draw_kde_normal(SIZES_4, common_l, common_r, koefs)
