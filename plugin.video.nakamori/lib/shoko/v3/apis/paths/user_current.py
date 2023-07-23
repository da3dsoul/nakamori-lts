from lib.shoko.v3.paths.user_current.get import ApiForget
from lib.shoko.v3.paths.user_current.put import ApiForput
from lib.shoko.v3.paths.user_current.patch import ApiForpatch


class UserCurrent(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
