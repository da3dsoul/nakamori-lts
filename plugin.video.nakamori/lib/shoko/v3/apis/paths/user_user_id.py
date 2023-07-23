from lib.shoko.v3.paths.user_user_id.get import ApiForget
from lib.shoko.v3.paths.user_user_id.put import ApiForput
from lib.shoko.v3.paths.user_user_id.delete import ApiFordelete
from lib.shoko.v3.paths.user_user_id.patch import ApiForpatch


class UserUserID(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
