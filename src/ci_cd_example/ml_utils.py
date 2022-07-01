import logging

logger = logging.getLogge(__name__)


def returns_four():
	"""
	Returns 4
	"""
	logger.info('why 4')
	return 4

