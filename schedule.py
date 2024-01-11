
from draw import Schedule
# Импорт класса для рисованя графиков

# Построение минимальных и максимальных отклонений потолка в градусах
ceiling_schedule = Schedule()
ceiling_schedule.legend_1 = 'Минимальное'
ceiling_schedule.legend_2 = 'Максимальное'
ceiling_schedule.legend_x = 'Количество потолков'
ceiling_schedule.legend_y = 'Градусы'
ceiling_schedule.column_1 = ceiling_schedule.file_read['ceiling_min']
ceiling_schedule.column_2 = ceiling_schedule.file_read['ceiling_max']
ceiling_schedule.schedule_title = f'Сравнение минимальных, максимальных и средних\nОтклонений потолка в градусах.'
ceiling_schedule.save = 'Отклонений потолка в градусах.'
ceiling_schedule.draw_plots()

