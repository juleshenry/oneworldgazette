class _1WJ:
	"""
	Main class for 1wg. Absorbs url strings and returns headlines with hyperlinks
	Can optionally translate in-situ to target language
	Open source, supporting 100+ languages
	"""
	def __init__(_s, **kwargs):
		"""
		parser = strategy
		"""
		for k,v in kwargs
			_s.k = v
		default = {}
		default["strategy"] = lambda x : x
		if not hasattr(_s,"strategy"):
			_s.strategy = default["strategy"]

	def absorb(url: str):
		return _s.strategy(url)


