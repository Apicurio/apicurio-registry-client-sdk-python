from apicurioregistryclient.paths.admin_rules.get import ApiForget
from apicurioregistryclient.paths.admin_rules.post import ApiForpost
from apicurioregistryclient.paths.admin_rules.delete import ApiFordelete


class AdminRules(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
