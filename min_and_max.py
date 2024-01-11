from draw import Schedule
# Построение минимальных и максимальных отклонений
min_max = Schedule()
min_max.legend_1 = 'Минимальное'
min_max.legend_2 = 'Максимальное'
min_max.legend_x = 'Количество полов и потолков'
min_max.legend_y = 'Градусы'
min_max.column_1 = min_max.file_read['min']
min_max.column_2 = min_max.file_read['max']
min_max.schedule_title = f'Минимальных и максимальных отклонений.'
min_max.save = 'минимальных и максимальных отклонений'
min_max.draw_plots()