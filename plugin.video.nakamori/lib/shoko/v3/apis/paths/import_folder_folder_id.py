from lib.shoko.v3.paths.import_folder_folder_id.get import ApiForget
from lib.shoko.v3.paths.import_folder_folder_id.delete import ApiFordelete
from lib.shoko.v3.paths.import_folder_folder_id.patch import ApiForpatch


class ImportFolderFolderID(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
