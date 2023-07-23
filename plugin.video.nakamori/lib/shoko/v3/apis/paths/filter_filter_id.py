from lib.shoko.v3.paths.filter_filter_id.get import ApiForget
from lib.shoko.v3.paths.filter_filter_id.put import ApiForput
from lib.shoko.v3.paths.filter_filter_id.delete import ApiFordelete
from lib.shoko.v3.paths.filter_filter_id.patch import ApiForpatch


class FilterFilterID(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
