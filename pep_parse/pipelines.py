import csv
from collections import Counter
from datetime import datetime as dt

from scrapy.exceptions import DropItem

from pep_parse.settings import BASE_DIR, FILENAME, RESULTS_DIR, TIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.total = Counter()
        self.now_time = dt.now().strftime(TIME_FORMAT)

    def process_item(self, item, spider):
        self.total[item['status']] += 1
        if 'status' not in item:
            raise DropItem('Статус отсутствует')
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        file_path = results_dir / FILENAME.format(self.now_time)
        file = csv.writer(open(file_path, 'w'))
        file.writerow(['Статус', 'Количество'])
        self.total['Total'] = sum(self.total.values())
        file.writerows(self.total.items())
