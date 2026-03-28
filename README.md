# The Farmer Was Replaced Scripts

Small scripts for **The Farmer Was Replaced**. Maybe it will help someone =)

Небольшие скрипты для **The Farmer Was Replaced**. Может быть, это кому-то поможет =)

---

## RU

### Как это работает

В `main.py` задан `plan` со списком зон:

- `Carrot`: `0-2`
- `Tree`: `3-5`
- `Sunflower`: `6`
- `Grass`: `7-10`
- `Pumpkin`: `11-15`

Скрипт по кругу:

1. сажает культуры по зонам
2. собирает урожай

Для получения дополнительной информации ознакомьтесь с описаниями функций в самих скриптах

### Особенности

- для `Tree` используется шахматный паттерн
- для `Sunflower` есть отдельный сбор по `measure()`
- `Grass` зона остается пустой

### Важно

- это не обычный Python-проект
- скрипты работают внутри игры
- `__builtins__.py` нужен только для удобства в IDE

---

## EN

### How it works

`main.py` defines a zone plan:

- `Carrot`: `0-2`
- `Tree`: `3-5`
- `Sunflower`: `6`
- `Grass`: `7-10`
- `Pumpkin`: `11-15`

The script loops through:

1. planting each zone
2. harvesting crops

For more information, check out the function descriptions in the scripts 

### Features

- checkerboard pattern for `Tree`
- separate `Sunflower` harvest logic based on `measure()`
- empty `Grass` area

### Notes

- this is not a regular Python project
- the scripts are meant to run inside the game
- `__builtins__.py` is only for editor support
