import typing_extensions

from lib.shoko.v3.apis.tags import TagValues
from lib.shoko.v3.apis.tags.debug_api import DebugApi
from lib.shoko.v3.apis.tags.init_api import InitApi
from lib.shoko.v3.apis.tags.reverse_tree_api import ReverseTreeApi
from lib.shoko.v3.apis.tags.tree_api import TreeApi
from lib.shoko.v3.apis.tags.action_api import ActionApi
from lib.shoko.v3.apis.tags.auth_api import AuthApi
from lib.shoko.v3.apis.tags.dashboard_api import DashboardApi
from lib.shoko.v3.apis.tags.episode_api import EpisodeApi
from lib.shoko.v3.apis.tags.file_api import FileApi
from lib.shoko.v3.apis.tags.filter_api import FilterApi
from lib.shoko.v3.apis.tags.folder_api import FolderApi
from lib.shoko.v3.apis.tags.group_api import GroupApi
from lib.shoko.v3.apis.tags.image_api import ImageApi
from lib.shoko.v3.apis.tags.import_folder_api import ImportFolderApi
from lib.shoko.v3.apis.tags.integrity_check_api import IntegrityCheckApi
from lib.shoko.v3.apis.tags.plex_webhook_api import PlexWebhookApi
from lib.shoko.v3.apis.tags.renamer_api import RenamerApi
from lib.shoko.v3.apis.tags.series_api import SeriesApi
from lib.shoko.v3.apis.tags.tag_api import TagApi
from lib.shoko.v3.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DEBUG: DebugApi,
        TagValues.INIT: InitApi,
        TagValues.REVERSE_TREE: ReverseTreeApi,
        TagValues.TREE: TreeApi,
        TagValues.ACTION: ActionApi,
        TagValues.AUTH: AuthApi,
        TagValues.DASHBOARD: DashboardApi,
        TagValues.EPISODE: EpisodeApi,
        TagValues.FILE: FileApi,
        TagValues.FILTER: FilterApi,
        TagValues.FOLDER: FolderApi,
        TagValues.GROUP: GroupApi,
        TagValues.IMAGE: ImageApi,
        TagValues.IMPORT_FOLDER: ImportFolderApi,
        TagValues.INTEGRITY_CHECK: IntegrityCheckApi,
        TagValues.PLEX_WEBHOOK: PlexWebhookApi,
        TagValues.RENAMER: RenamerApi,
        TagValues.SERIES: SeriesApi,
        TagValues.TAG: TagApi,
        TagValues.USER: UserApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DEBUG: DebugApi,
        TagValues.INIT: InitApi,
        TagValues.REVERSE_TREE: ReverseTreeApi,
        TagValues.TREE: TreeApi,
        TagValues.ACTION: ActionApi,
        TagValues.AUTH: AuthApi,
        TagValues.DASHBOARD: DashboardApi,
        TagValues.EPISODE: EpisodeApi,
        TagValues.FILE: FileApi,
        TagValues.FILTER: FilterApi,
        TagValues.FOLDER: FolderApi,
        TagValues.GROUP: GroupApi,
        TagValues.IMAGE: ImageApi,
        TagValues.IMPORT_FOLDER: ImportFolderApi,
        TagValues.INTEGRITY_CHECK: IntegrityCheckApi,
        TagValues.PLEX_WEBHOOK: PlexWebhookApi,
        TagValues.RENAMER: RenamerApi,
        TagValues.SERIES: SeriesApi,
        TagValues.TAG: TagApi,
        TagValues.USER: UserApi,
    }
)
