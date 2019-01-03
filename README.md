# SenlerPy

Библиотека на python для работы с api сервиса senler.ru

[![N|Solid](https://img.shields.io/pypi/pyversions/smsactivateru.svg)](https://pypi.python.org/pypi/smsactivateru)

### Установка
Установка с помощью стандартного пакетного менеджера pip:
```
$ pip install senlerpy --upgrade
```
Либо установка напрямую из репозитория, с ручной сборкой
```
$ git clone https://github.com/tezmen/senlerpy
$ cd senlerpy
$ python setup.py install
```
...либо установка через pip но из репозитория, минуя сервера pypi
```
$ pip install git+https://github.com/tezmen/senlerpy
```
### Простой пример
```python
api = Senler('SECRET')

data = api(
	methods.Deliveries.stat,
	date_from='2018-01-01 10:00:00',
	date_to='2018-12-30 23:00:00',
	vk_group_id=1,
)

print(data['items'])
```
Больше примеров смотрите в папке /example/