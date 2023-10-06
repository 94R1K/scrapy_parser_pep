### [![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Парсер+документации+PEP+на+Scrapy)](https://git.io/typing-svg)
# *Проект асинхронного парсинга документации PEP*

# _Описание_
Выполняется парсинг данных со страницы с общей информацией о PEP (https://peps.python.org/), 
переход по ссылкам и сбор данных о каждом PEP.
Парсер подготавливает данные и сохраняет их в два файла формата ```csv``` в папку ```results```.

### _Перед использованием_
Клонируйте репозиторий к себе на компьютер:

```
git clone https://github.com/94R1K/scrapy_parser_pep.git
```

### _В корневой папке создайте виртуальное окружение и установите зависимости:_
```
python -m venv venv
```

```
pip install -r requirements.txt
```

### _Запуск парсера из командной строки:_
```
scrapy crawl pep
```

### _Вывод результатов_
Результатом работы парсера будет создание двух файлов:
1. ``pep_ДатаВремя.csv`` - содержит список всех PEP (``number``, ``name``, ``status``);
2. ``status_summary_ДатаВремя.csv`` - содержит сводку по статусам PEP: 
сколько найдено документов в каждом статусе (``Status``, ``Quantity``). 
В последней строке этого файла в колонке ``Total`` выводится общее количество всех документов.

# Об авторе
Лошкарев Ярослав Эдуардович \
Python-разработчик (Backend) \
Россия, г. Москва \
E-mail: real-man228@yandex.ru 

[![VK](https://img.shields.io/badge/Вконтакте-%232E87FB.svg?&style=for-the-badge&logo=vk&logoColor=white)](https://vk.com/yalluv)
[![TG](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/yallluv)
