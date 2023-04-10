from pathlib import Path

FILENAME = 'status_summary_{}.csv'
RESULTS_DIR = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
PEP_REG = 'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'
BASE_DIR = Path(__file__).parent.parent

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True
