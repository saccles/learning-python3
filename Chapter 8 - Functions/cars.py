def store_car_info(manufacturer, model_name, **car_info):
	"""
	Build a dictionary containing everything we know about
	a certain car.
	"""
	car_info['manufacturer'] = manufacturer
	car_info['model_name'] = model_name
	return car_info

car_1 = store_car_info('toyota', 'prius', color='dark blue', model_year='1999')
print(car_1)
