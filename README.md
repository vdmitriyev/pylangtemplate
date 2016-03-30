### About

Python script that change all files in project from default language to the target ones (e.g. from English to Russian).

### How It Works

* Config dictionary file (what should be replaced with what). Here is an example for Russian language
```
MAPPING_DICT = {
    '<a href="index.html">Main</a>' : '<a href="index.html">Главная</a>'
}
* Put all configs into file in following format:
```
# coding: utf-8

ORIGINAL_LANGUAGE = 'en'
TARGET_LANGUAGE = 'ru'

# mapping from English to Russian

MAPPING_DICT = {
    'Main</a>' : 'Главная</a>',
    'Labs</a>' : 'Лабы</a>',
    'Publications</a>' : 'Публикации</a>'
}
```
* Script will apply all existing in folder translations "dictionaries"
* After the script will produce new version, copy and paste new files to the desired web directory

* Run 'run.bat' or use command line

### Dependencies

* Python 2.7
* docopt

```
pip install -r requirements.txt
```

### Authors

* Viktor Dmitriyev
