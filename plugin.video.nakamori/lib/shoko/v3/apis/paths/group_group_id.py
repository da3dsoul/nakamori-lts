from lib.shoko.v3.paths.group_group_id.get import ApiForget
from lib.shoko.v3.paths.group_group_id.put import ApiForput
from lib.shoko.v3.paths.group_group_id.delete import ApiFordelete
from lib.shoko.v3.paths.group_group_id.patch import ApiForpatch


class GroupGroupID(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
