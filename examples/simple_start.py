# -*- coding: utf-8 -*-
from senlerpy import Senler, methods

# Создаём объект с секретным ключом
api = Senler('SECRET')

# Выполняем запросы к апи используя встроенные схемы
data = api(
	methods.Deliveries.stat,
	date_from='2018-01-01 10:00:00',
	date_to='2018-12-30 23:00:00',
	vk_group_id=1,
)
print(data['items'])

# Или прямо указывая URL метода
data = api('utms/get', vk_group_id=1)
print(data['items'])

# Группу ВК можно назначить как для каждого запроса, так и глобально, используя свойство или аргумент конструктора
api = Senler('SECRET', vk_group_id=1)
data = api(methods.Utms.get)
print(data['items'])

api = Senler('SECRET')
api.vk_group = 1
data = api(methods.Utms.get)
print(data['items'])