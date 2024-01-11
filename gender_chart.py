from draw import Schedule
# Построение минимальных и максимальных отклонений пола в градусах
gender_chart = Schedule()
gender_chart.legend_1 = 'Минимальное'
gender_chart.legend_2 = 'Максимальное'
gender_chart.legend_x = 'Количество полов'
gender_chart.legend_y = 'Градусы'
gender_chart.column_1 = gender_chart.file_read['floor_min']
gender_chart.column_2 = gender_chart.file_read['floor_max']
gender_chart.schedule_title = f'Сравнение минимальных и максимальных\nОтклонений пола в градусах.'
gender_chart.save = 'Отклонений пола в градусах.'
gender_chart.draw_plots()