# class Logging():
# 	def __new__(cls):
# 		if not hasattr(cls, 'instance'):
# 			cls.instance = super(Logging, cls).__new__(cls)
# 		return cls.instance

# a=Logging()
# print(a)
# b= Logging()
# print(b)


class Logging():
	_instance =None
	def __new__(cls):
		if not cls._instance:
			cls._instance = super(Logging, cls).__new__(cls)
		return cls._instance

a=Logging()
print(a)
b= Logging()
print(b)



C@jackio90
