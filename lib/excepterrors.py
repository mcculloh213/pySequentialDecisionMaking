import lib.logger as lg

__author__ = "H.D. 'Chip' McCullough IV"

log = lg.Logger("Proj04.ERRORS", "ERRORS", '%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def excepterrors(exc, msg):
    """
    Log fatal errors and exceptions using a simple function.
    :param exc: Exception/Error
    :param msg: Message
    """
    log.logger.error(exc)
    log.logger.error(msg)
