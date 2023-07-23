from lib.shoko.v3.paths.filter_preview.get import ApiForget
from lib.shoko.v3.paths.filter_preview.put import ApiForput
from lib.shoko.v3.paths.filter_preview.delete import ApiFordelete
from lib.shoko.v3.paths.filter_preview.patch import ApiForpatch


class FilterPreview(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
