from draw import Schedule
# Построение средних отклонений потолка и пола
average_deviations = Schedule()
average_deviations.legend_1 = 'Отклонение потолка'
average_deviations.legend_2 = 'Отклонение пола'
average_deviations.legend_x = 'Количество полов и потолков'
average_deviations.legend_y = 'Градусы'
average_deviations.column_1 = average_deviations.file_read['floor_mean']
average_deviations.column_2 = average_deviations.file_read['ceiling_mean']
average_deviations.schedule_title = f'Сравнение средних отклонений потолка и пола.'
average_deviations.save = 'Сравнение средних отклонений'
average_deviations.draw_plots()