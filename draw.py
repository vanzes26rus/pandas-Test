import pandas as pd
# Импорт Pandas и назначение имени pd
import matplotlib.pyplot as plt
# Импорт matplotlib и назначение имени plt

class Schedule:
    """Класс для построение граффиков """
    def __init__(self):
        self.legend_1 = ''
        self.legend_2 = ''
        self.legend_x = ''
        self.legend_y = ''
        self.save = ''
        self.file_read = pd.read_json('deviation.json')
        # Удаление дубликатов
        self.file_read = self.file_read.drop_duplicates()
        # Чтение файла 'deviation.json'
        self.f_h = self.file_read.head()
        self.column_1 = self.file_read
        self.column_2 = self.file_read
        self.name = list(self.file_read.columns.values)
        self.schedule_title = f""


    def draw_plots(self):
        """Строит граффик"""
        plt.title(self.schedule_title)
        plt.plot(self.column_1, label=self.legend_1)
        plt.plot(self.column_2, label=self.legend_2 , alpha=0.3)
        plt.xlabel(self.legend_x, fontsize=15)
        plt.ylabel(self.legend_y, fontsize=15)
        plt.legend()
        plt.savefig(self.save)

    def p(self):
        print(self.name)


# ['name', 'gt_corners', 'rb_corners', 'mean', 'max', 'min', 'floor_mean', 'floor_max', 'floor_min', 'ceiling_mean', 'ceiling_max', 'ceiling_min']