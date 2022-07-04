import logging

logger = logging.getLogger(__name__)


def returns_four():
	"""
	Returns 4
	"""
	logger.info('why 4')
	return 4

print(returns_four())
logger.info('some info')
