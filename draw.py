import pandas as pd
# Импорт Pandas и назначение имени pd
import matplotlib.pyplot as plt
# Импорт matplotlib и назначение имени plt

class Сhart:
    """Класс для построение граффиков """
    def __init__(self, legend_1, legend_2, legend_x, legend_y, filename, column_1, column_2, chart_title):
        self.legend_1 = legend_1
        self.legend_2 = legend_2
        self.legend_x = legend_x
        self.legend_y = legend_y
        self.filename = filename
        self.column_1 = column_1
        self.column_2 = column_2
        self.chart_title = chart_title


def draw_plots(chart):
    """Строит граффик"""
    plt.title(chart.chart_title)
    plt.plot(chart.column_1, label=chart.legend_1)
    plt.plot(chart.column_2, label=chart.legend_2 , alpha=0.3)
    plt.xlabel(chart.legend_x, fontsize=15)
    plt.ylabel(chart.legend_y, fontsize=15)
    plt.legend()
    plt.show()
    plt.savefig(chart.filename)


df = pd.read_json('deviation.json')
# Удаление дубликатов
df = df.drop_duplicates()

# Построение минимальных и максимальных отклонений потолка в градусах
ceiling_chart = Сhart('Минимальное', 'Максимальное', 'Количество потолков', 'Градусы','Отклонение потолка в градусах.',
                    df['ceiling_min'], df['ceiling_max'],
                    f'Сравнение минимальных, максимальных \n Отклонений потолка в градусах.')
draw_plots(ceiling_chart)


# Построение средних отклонений потолка и пола
average_deviations = Сhart('Отклонение потолка', 'Отклонение пола', 'Количество потолков и полов',
                    'Градусы','Сравнение средних отклонений',
                    df['floor_mean'], df['ceiling_mean'],
                    f'Сравнение средних отклонений потолка и пола.')
draw_plots(average_deviations)


# Построение минимальных и максимальных отклонений пола в градусах
gender_chart = Сhart('Минимальное', 'Максимальное', 'Количество полов', 'Градусы','Отклонение пола в градусах.',
                    df['floor_min'], df['floor_max'],
                    f'Сравнение минимальных, максимальных \n Отклонений пола в градусах.')
draw_plots(gender_chart)


# Построение минимальных и максимальных отклонений
min_max = Сhart('Минимальное', 'Максимальное', 'Количество полов и потолков', 'Градусы',
                'Минимальных и максимальных отклонений.',
                df['min'], df['max'],
                'Сравнение минимальных\nи максимальных отклонений.')
draw_plots(min_max)
