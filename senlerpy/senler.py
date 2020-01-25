# -*- coding: utf-8 -*-
import json
import logging
from .request import RequestApi
from .exceptions import ApiError, WrongId, HttpError

logger = logging.getLogger(__name__)


class Senler:
	def __init__(self, secret, vk_group_id=None):
		self.vk_group = vk_group_id
		self.__secret = str(secret).strip()
		self._rq = RequestApi(self.secret)

	def __error_handler(self, response):
		if bool(response['success']):
			return response
		raise ApiError(response)

	def __call__(self, method, **kwargs):
		if 'vk_group_id' not in kwargs.keys():
			if self.vk_group is None:
				raise WrongId('vk_group_id is not specified by any of the methods')
			kwargs['vk_group_id'] = self.vk_group
		response = self._rq.send(str(method), kwargs)
		json_response = {}
		try:
			json_response = json.loads(response.text)
		except:
			logger.debug(f'{response.status_code}:{response.text}')
			raise HttpError(f'status_code:{response.status_code}, error with decode json')
		return self.__error_handler(json_response)

	@property
	def secret(self):
		return self.__secret

	@property
	def vk_group(self):
		return self.__vk_group

	@vk_group.setter
	def vk_group(self, value):
		self.__vk_group = str(value)
