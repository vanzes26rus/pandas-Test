import pandas as pd
# Импорт Pandas и назначение имени pd
import matplotlib.pyplot as plt
# Импорт matplotlib и назначение имени plt

class Schedule:
    """Класс для построение граффиков """
    def __init__(self):
        self.gt_corners = []
        self.rb_corners = []
        self.name = ['истинное количество углов в комнате', 'количество углов, найденных моделью']
        self.file_read = pd.read_json('deviation.json')
        # Удаление дубликатов
        self.file_read = self.file_read.drop_duplicates()
        # Чтение файла 'deviation.json'
        self.f_h = self.file_read.head()

        for i in self.file_read["gt_corners"]:
            self.gt_corners.append(i)

        for i in self.file_read["rb_corners"]:
            self.rb_corners.append(i)

    def draw_plots(self):
        """Строит граффик"""
        plt.title(f"Сравнение истинного количество углов в комнате\nи количество углов, найденных моделью")

        plt.hist([self.gt_corners, self.rb_corners], label=self.name)
        plt.xlabel('Количество углов', fontsize=15)
        plt.ylabel('Количество комнат', fontsize=15)
        plt.legend()
        plt.savefig('plots.png')
        # вывод изображения
        print(self.f_h)

g = Schedule()
g.draw_plots()


