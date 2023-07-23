from lib.shoko.v3.paths.import_folder.get import ApiForget
from lib.shoko.v3.paths.import_folder.put import ApiForput
from lib.shoko.v3.paths.import_folder.post import ApiForpost


class ImportFolder(
    ApiForget,
    ApiForput,
    ApiForpost,
):
    pass
