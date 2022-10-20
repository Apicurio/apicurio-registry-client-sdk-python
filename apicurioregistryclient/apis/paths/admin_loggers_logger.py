from apicurioregistryclient.paths.admin_loggers_logger.get import ApiForget
from apicurioregistryclient.paths.admin_loggers_logger.put import ApiForput
from apicurioregistryclient.paths.admin_loggers_logger.delete import ApiFordelete


class AdminLoggersLogger(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
