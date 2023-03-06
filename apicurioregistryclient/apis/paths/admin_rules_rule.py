from apicurioregistryclient.paths.admin_rules_rule.get import ApiForget
from apicurioregistryclient.paths.admin_rules_rule.put import ApiForput
from apicurioregistryclient.paths.admin_rules_rule.delete import ApiFordelete


class AdminRulesRule(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
