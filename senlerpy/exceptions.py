# -*- coding: utf-8 -*-


class HttpError(Exception):
	pass


class WrongSecret(Exception):
	pass


class WrongId(Exception):
	pass


class ApiError(Exception):
	def __init__(self, error):
		self.__error_data = error
		if self.code == 3:
			raise WrongSecret('Wrong secret key! No access to senler API')

	@property
	def code(self):
		return self.__error_data.get('error_code', None)

	def __str__(self):
		return '[{}]: {}'.format(
			self.__error_data['error_code'], self.__error_data['error_message']
		)


class TooManyRequests(ApiError):
	def __init__(self, senler, method, data, error):
		self.__senler = senler
		self.method = method
		self.data = data
		self.error = error

	def send_again(self):
		return self.__senler(self.method, self.data)

	def __str__(self):
		return '[{}]: {}'.format(
			self.error['error_code'], self.error['error_msg'])

