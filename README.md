### About

Python script that change all files in project from default language to the target ones (e.g. from English to Russian).

### How It Works

* Config dictionary file (what should be replaced with what). Here is an example for Russian language

```python
MAPPING_DICT = {
    '<p> Some sample text to be replaces. </p>' : '<p> Текст для примера</p>'
}
```

* Put all configs into file in following format:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""SETTINGS"""

ORIGINAL_LANGUAGE = 'en'
TARGET_LANGUAGE = 'ru'

"""DICTIONARY -> english to russian"""

MAPPING_DICT = {
    '<p> Some sample text to be replaces. </p>' : '<p> Текст для примера</p>'
}
```

* Script will apply all existing in folder translations "dictionaries"
* After the script will produce new version and save them accordingly
* Check 'run.bat' for details how to run script via command line

### Dependencies

* Python 2.7
* docopt

```
pip install -r requirements.txt
```

### Authors

* Viktor Dmitriyev
