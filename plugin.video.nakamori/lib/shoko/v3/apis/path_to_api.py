import typing_extensions

from lib.shoko.v3.paths import PathValues
from lib.shoko.v3.apis.paths.action_run_import import ActionRunImport
from lib.shoko.v3.apis.paths.action_import_new_files import ActionImportNewFiles
from lib.shoko.v3.apis.paths.action_sync_hashes import ActionSyncHashes
from lib.shoko.v3.apis.paths.action_sync_votes import ActionSyncVotes
from lib.shoko.v3.apis.paths.action_sync_trakt import ActionSyncTrakt
from lib.shoko.v3.apis.paths.action_remove_missing_files_remove_from_my_list import ActionRemoveMissingFilesRemoveFromMyList
from lib.shoko.v3.apis.paths.action_update_all_tv_db_info import ActionUpdateAllTvDBInfo
from lib.shoko.v3.apis.paths.action_update_all_images import ActionUpdateAllImages
from lib.shoko.v3.apis.paths.action_update_all_movie_db_info import ActionUpdateAllMovieDBInfo
from lib.shoko.v3.apis.paths.action_update_all_trakt_info import ActionUpdateAllTraktInfo
from lib.shoko.v3.apis.paths.action_validate_all_images import ActionValidateAllImages
from lib.shoko.v3.apis.paths.action_av_dump_mismatched_files import ActionAVDumpMismatchedFiles
from lib.shoko.v3.apis.paths.action_download_missing_ani_db_anime_data import ActionDownloadMissingAniDBAnimeData
from lib.shoko.v3.apis.paths.action_regenerate_all_tv_db_episode_matchings import ActionRegenerateAllTvDBEpisodeMatchings
from lib.shoko.v3.apis.paths.action_sync_my_list import ActionSyncMyList
from lib.shoko.v3.apis.paths.action_update_all_ani_db_info import ActionUpdateAllAniDBInfo
from lib.shoko.v3.apis.paths.action_update_all_media_info import ActionUpdateAllMediaInfo
from lib.shoko.v3.apis.paths.action_update_series_stats import ActionUpdateSeriesStats
from lib.shoko.v3.apis.paths.action_update_missing_ani_db_file_info import ActionUpdateMissingAniDBFileInfo
from lib.shoko.v3.apis.paths.action_update_ani_db_calendar import ActionUpdateAniDBCalendar
from lib.shoko.v3.apis.paths.action_recreate_all_groups import ActionRecreateAllGroups
from lib.shoko.v3.apis.paths.action_rename_all_groups import ActionRenameAllGroups
from lib.shoko.v3.apis.paths.action_plex_sync_all import ActionPlexSyncAll
from lib.shoko.v3.apis.paths.action_add_all_manual_links_to_my_list import ActionAddAllManualLinksToMyList
from lib.shoko.v3.apis.paths.api_auth import ApiAuth
from lib.shoko.v3.apis.paths.api_auth_change_password import ApiAuthChangePassword
from lib.shoko.v3.apis.paths.dashboard_stats import DashboardStats
from lib.shoko.v3.apis.paths.dashboard_top_tags_number import DashboardTopTagsNumber
from lib.shoko.v3.apis.paths.dashboard_top_tags import DashboardTopTags
from lib.shoko.v3.apis.paths.dashboard_queue_summary import DashboardQueueSummary
from lib.shoko.v3.apis.paths.dashboard_series_summary import DashboardSeriesSummary
from lib.shoko.v3.apis.paths.dashboard_recently_added_episodes import DashboardRecentlyAddedEpisodes
from lib.shoko.v3.apis.paths.dashboard_recently_added_series import DashboardRecentlyAddedSeries
from lib.shoko.v3.apis.paths.dashboard_continue_watching_episodes import DashboardContinueWatchingEpisodes
from lib.shoko.v3.apis.paths.dashboard_next_up_episodes import DashboardNextUpEpisodes
from lib.shoko.v3.apis.paths.dashboard_ani_db_calendar import DashboardAniDBCalendar
from lib.shoko.v3.apis.paths.debug_ani_db_udp_call import DebugAniDBUDPCall
from lib.shoko.v3.apis.paths.episode import Episode
from lib.shoko.v3.apis.paths.episode_ani_db import EpisodeAniDB
from lib.shoko.v3.apis.paths.episode_tv_db import EpisodeTvDB
from lib.shoko.v3.apis.paths.episode_episode_id import EpisodeEpisodeID
from lib.shoko.v3.apis.paths.episode_episode_id_set_hidden import EpisodeEpisodeIDSetHidden
from lib.shoko.v3.apis.paths.episode_episode_id_ani_db import EpisodeEpisodeIDAniDB
from lib.shoko.v3.apis.paths.episode_ani_db_anidb_episode_id import EpisodeAniDBAnidbEpisodeID
from lib.shoko.v3.apis.paths.episode_ani_db_anidb_episode_id_episode import EpisodeAniDBAnidbEpisodeIDEpisode
from lib.shoko.v3.apis.paths.episode_episode_id_vote import EpisodeEpisodeIDVote
from lib.shoko.v3.apis.paths.episode_episode_id_tv_db import EpisodeEpisodeIDTvDB
from lib.shoko.v3.apis.paths.episode_episode_id_watched_watched import EpisodeEpisodeIDWatchedWatched
from lib.shoko.v3.apis.paths.episode_with_multiple_files import EpisodeWithMultipleFiles
from lib.shoko.v3.apis.paths.episode_with_no_files import EpisodeWithNoFiles
from lib.shoko.v3.apis.paths.file import File
from lib.shoko.v3.apis.paths.file_file_id import FileFileID
from lib.shoko.v3.apis.paths.file_file_id_ani_db import FileFileIDAniDB
from lib.shoko.v3.apis.paths.file_ani_db_anidb_file_id import FileAniDBAnidbFileID
from lib.shoko.v3.apis.paths.file_ani_db_anidb_file_id_file import FileAniDBAnidbFileIDFile
from lib.shoko.v3.apis.paths.file_file_id_stream import FileFileIDStream
from lib.shoko.v3.apis.paths.file_file_id_media_info import FileFileIDMediaInfo
from lib.shoko.v3.apis.paths.file_file_id_user_stats import FileFileIDUserStats
from lib.shoko.v3.apis.paths.file_file_id_watched_watched import FileFileIDWatchedWatched
from lib.shoko.v3.apis.paths.file_file_id_scrobble import FileFileIDScrobble
from lib.shoko.v3.apis.paths.file_file_id_ignore import FileFileIDIgnore
from lib.shoko.v3.apis.paths.file_file_id_av_dump import FileFileIDAVDump
from lib.shoko.v3.apis.paths.file_file_id_rescan import FileFileIDRescan
from lib.shoko.v3.apis.paths.file_file_id_rehash import FileFileIDRehash
from lib.shoko.v3.apis.paths.file_file_id_link import FileFileIDLink
from lib.shoko.v3.apis.paths.file_file_id_link_from_series import FileFileIDLinkFromSeries
from lib.shoko.v3.apis.paths.file_link_from_series import FileLinkFromSeries
from lib.shoko.v3.apis.paths.file_link import FileLink
from lib.shoko.v3.apis.paths.file_path_ends_with import FilePathEndsWith
from lib.shoko.v3.apis.paths.file_path_ends_with_path import FilePathEndsWithPath
from lib.shoko.v3.apis.paths.file_path_regex_path import FilePathRegexPath
from lib.shoko.v3.apis.paths.file_filename_regex_path import FileFilenameRegexPath
from lib.shoko.v3.apis.paths.file_recent_limit import FileRecentLimit
from lib.shoko.v3.apis.paths.file_recent import FileRecent
from lib.shoko.v3.apis.paths.file_ignored import FileIgnored
from lib.shoko.v3.apis.paths.file_duplicates import FileDuplicates
from lib.shoko.v3.apis.paths.file_linked import FileLinked
from lib.shoko.v3.apis.paths.file_missing_cross_reference_data import FileMissingCrossReferenceData
from lib.shoko.v3.apis.paths.file_unrecognized import FileUnrecognized
from lib.shoko.v3.apis.paths.filter import Filter
from lib.shoko.v3.apis.paths.filter_filter_id import FilterFilterID
from lib.shoko.v3.apis.paths.filter_preview import FilterPreview
from lib.shoko.v3.apis.paths.filter_preview_group import FilterPreviewGroup
from lib.shoko.v3.apis.paths.filter_preview_group_letters import FilterPreviewGroupLetters
from lib.shoko.v3.apis.paths.filter_preview_series import FilterPreviewSeries
from lib.shoko.v3.apis.paths.filter_preview_group_group_id_group import FilterPreviewGroupGroupIDGroup
from lib.shoko.v3.apis.paths.filter_preview_group_group_id_series import FilterPreviewGroupGroupIDSeries
from lib.shoko.v3.apis.paths.folder_drives import FolderDrives
from lib.shoko.v3.apis.paths.folder import Folder
from lib.shoko.v3.apis.paths.group import Group
from lib.shoko.v3.apis.paths.group_letters import GroupLetters
from lib.shoko.v3.apis.paths.group_group_id import GroupGroupID
from lib.shoko.v3.apis.paths.group_group_id_relations import GroupGroupIDRelations
from lib.shoko.v3.apis.paths.group_group_id_recalculate import GroupGroupIDRecalculate
from lib.shoko.v3.apis.paths.group_recreate_all_groups import GroupRecreateAllGroups
from lib.shoko.v3.apis.paths.image_source_type_value import ImageSourceTypeValue
from lib.shoko.v3.apis.paths.image_random_image_type import ImageRandomImageType
from lib.shoko.v3.apis.paths.image_random_image_type_metadata import ImageRandomImageTypeMetadata
from lib.shoko.v3.apis.paths.import_folder import ImportFolder
from lib.shoko.v3.apis.paths.import_folder_folder_id import ImportFolderFolderID
from lib.shoko.v3.apis.paths.import_folder_folder_id_scan import ImportFolderFolderIDScan
from lib.shoko.v3.apis.paths.init_version import InitVersion
from lib.shoko.v3.apis.paths.init_status import InitStatus
from lib.shoko.v3.apis.paths.init_in_use import InitInUse
from lib.shoko.v3.apis.paths.init_default_user import InitDefaultUser
from lib.shoko.v3.apis.paths.init_start_server import InitStartServer
from lib.shoko.v3.apis.paths.init_database_test import InitDatabaseTest
from lib.shoko.v3.apis.paths.integrity_check import IntegrityCheck
from lib.shoko.v3.apis.paths.integrity_check_id_start import IntegrityCheckIdStart
from lib.shoko.v3.apis.paths.plex_json import PlexJson
from lib.shoko.v3.apis.paths.plex import Plex
from lib.shoko.v3.apis.paths.plex_loginurl import PlexLoginurl
from lib.shoko.v3.apis.paths.plex_pin_authenticated import PlexPinAuthenticated
from lib.shoko.v3.apis.paths.plex_token_invalidate import PlexTokenInvalidate
from lib.shoko.v3.apis.paths.plex_sync import PlexSync
from lib.shoko.v3.apis.paths.plex_sync_all import PlexSyncAll
from lib.shoko.v3.apis.paths.plex_sync_id import PlexSyncId
from lib.shoko.v3.apis.paths.plex_libraries import PlexLibraries
from lib.shoko.v3.apis.paths.plex_server_list import PlexServerList
from lib.shoko.v3.apis.paths.plex_server import PlexServer
from lib.shoko.v3.apis.paths.plex_libraries_id import PlexLibrariesId
from lib.shoko.v3.apis.paths.renamer import Renamer
from lib.shoko.v3.apis.paths.renamer_renamer_id import RenamerRenamerID
from lib.shoko.v3.apis.paths.filter_filter_id_parent import FilterFilterIDParent
from lib.shoko.v3.apis.paths.group_group_id_parent import GroupGroupIDParent
from lib.shoko.v3.apis.paths.series_series_id_group import SeriesSeriesIDGroup
from lib.shoko.v3.apis.paths.episode_episode_id_series import EpisodeEpisodeIDSeries
from lib.shoko.v3.apis.paths.file_file_id_episode import FileFileIDEpisode
from lib.shoko.v3.apis.paths.series import Series
from lib.shoko.v3.apis.paths.series_series_id import SeriesSeriesID
from lib.shoko.v3.apis.paths.series_series_id_auto_match_settings import SeriesSeriesIDAutoMatchSettings
from lib.shoko.v3.apis.paths.series_series_id_relations import SeriesSeriesIDRelations
from lib.shoko.v3.apis.paths.series_without_files import SeriesWithoutFiles
from lib.shoko.v3.apis.paths.series_with_manually_linked_files import SeriesWithManuallyLinkedFiles
from lib.shoko.v3.apis.paths.series_ani_db import SeriesAniDB
from lib.shoko.v3.apis.paths.series_ani_db_relations import SeriesAniDBRelations
from lib.shoko.v3.apis.paths.series_series_id_ani_db import SeriesSeriesIDAniDB
from lib.shoko.v3.apis.paths.series_series_id_ani_db_similar import SeriesSeriesIDAniDBSimilar
from lib.shoko.v3.apis.paths.series_series_id_ani_db_related import SeriesSeriesIDAniDBRelated
from lib.shoko.v3.apis.paths.series_series_id_ani_db_relations import SeriesSeriesIDAniDBRelations
from lib.shoko.v3.apis.paths.series_ani_db_recommended_for_you import SeriesAniDBRecommendedForYou
from lib.shoko.v3.apis.paths.series_ani_db_anidb_id import SeriesAniDBAnidbID
from lib.shoko.v3.apis.paths.series_ani_db_anidb_id_similar import SeriesAniDBAnidbIDSimilar
from lib.shoko.v3.apis.paths.series_ani_db_anidb_id_related import SeriesAniDBAnidbIDRelated
from lib.shoko.v3.apis.paths.series_ani_db_anidb_id_relations import SeriesAniDBAnidbIDRelations
from lib.shoko.v3.apis.paths.series_ani_db_anidb_id_series import SeriesAniDBAnidbIDSeries
from lib.shoko.v3.apis.paths.series_ani_db_anidb_id_refresh import SeriesAniDBAnidbIDRefresh
from lib.shoko.v3.apis.paths.series_series_id_ani_db_refresh import SeriesSeriesIDAniDBRefresh
from lib.shoko.v3.apis.paths.series_series_id_ani_db_refresh_force_from_xml import SeriesSeriesIDAniDBRefreshForceFromXML
from lib.shoko.v3.apis.paths.series_series_id_tv_db import SeriesSeriesIDTvDB
from lib.shoko.v3.apis.paths.series_series_id_tvdb_id_refresh import SeriesSeriesIDTvdbIDRefresh
from lib.shoko.v3.apis.paths.series_tv_db_tvdb_id import SeriesTvDBTvdbID
from lib.shoko.v3.apis.paths.series_tv_db_tvdb_id_refresh import SeriesTvDBTvdbIDRefresh
from lib.shoko.v3.apis.paths.series_tv_db_tvdb_id_series import SeriesTvDBTvdbIDSeries
from lib.shoko.v3.apis.paths.series_series_id_vote import SeriesSeriesIDVote
from lib.shoko.v3.apis.paths.series_series_id_images import SeriesSeriesIDImages
from lib.shoko.v3.apis.paths.series_series_id_images_image_type import SeriesSeriesIDImagesImageType
from lib.shoko.v3.apis.paths.series_series_id_tags import SeriesSeriesIDTags
from lib.shoko.v3.apis.paths.series_series_id_tags_filter import SeriesSeriesIDTagsFilter
from lib.shoko.v3.apis.paths.series_series_id_cast import SeriesSeriesIDCast
from lib.shoko.v3.apis.paths.series_series_id_move_group_id import SeriesSeriesIDMoveGroupID
from lib.shoko.v3.apis.paths.series_search import SeriesSearch
from lib.shoko.v3.apis.paths.series_search_query import SeriesSearchQuery
from lib.shoko.v3.apis.paths.series_ani_db_search import SeriesAniDBSearch
from lib.shoko.v3.apis.paths.series_ani_db_search_query import SeriesAniDBSearchQuery
from lib.shoko.v3.apis.paths.series_starts_with_query import SeriesStartsWithQuery
from lib.shoko.v3.apis.paths.series_path_ends_with_path import SeriesPathEndsWithPath
from lib.shoko.v3.apis.paths.tag_ani_db import TagAniDB
from lib.shoko.v3.apis.paths.tag_ani_db_tag_id import TagAniDBTagID
from lib.shoko.v3.apis.paths.tag_user import TagUser
from lib.shoko.v3.apis.paths.tag_user_tag_id import TagUserTagID
from lib.shoko.v3.apis.paths.import_folder_folder_id_file import ImportFolderFolderIDFile
from lib.shoko.v3.apis.paths.filter_filter_id_filter import FilterFilterIDFilter
from lib.shoko.v3.apis.paths.filter_filter_id_group import FilterFilterIDGroup
from lib.shoko.v3.apis.paths.filter_filter_id_group_letters import FilterFilterIDGroupLetters
from lib.shoko.v3.apis.paths.filter_filter_id_series import FilterFilterIDSeries
from lib.shoko.v3.apis.paths.filter_filter_id_group_group_id_group import FilterFilterIDGroupGroupIDGroup
from lib.shoko.v3.apis.paths.filter_filter_id_group_group_id_series import FilterFilterIDGroupGroupIDSeries
from lib.shoko.v3.apis.paths.group_group_id_group import GroupGroupIDGroup
from lib.shoko.v3.apis.paths.group_group_id_series import GroupGroupIDSeries
from lib.shoko.v3.apis.paths.group_group_id_main_series import GroupGroupIDMainSeries
from lib.shoko.v3.apis.paths.series_series_id_episode import SeriesSeriesIDEpisode
from lib.shoko.v3.apis.paths.series_series_id_next_up_episode import SeriesSeriesIDNextUpEpisode
from lib.shoko.v3.apis.paths.series_series_id_file import SeriesSeriesIDFile
from lib.shoko.v3.apis.paths.episode_episode_id_file import EpisodeEpisodeIDFile
from lib.shoko.v3.apis.paths.user import User
from lib.shoko.v3.apis.paths.user_current import UserCurrent
from lib.shoko.v3.apis.paths.user_current_change_password import UserCurrentChangePassword
from lib.shoko.v3.apis.paths.user_user_id import UserUserID
from lib.shoko.v3.apis.paths.user_user_id_change_password import UserUserIDChangePassword

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACTION_RUN_IMPORT: ActionRunImport,
        PathValues.ACTION_IMPORT_NEW_FILES: ActionImportNewFiles,
        PathValues.ACTION_SYNC_HASHES: ActionSyncHashes,
        PathValues.ACTION_SYNC_VOTES: ActionSyncVotes,
        PathValues.ACTION_SYNC_TRAKT: ActionSyncTrakt,
        PathValues.ACTION_REMOVE_MISSING_FILES_REMOVE_FROM_MY_LIST: ActionRemoveMissingFilesRemoveFromMyList,
        PathValues.ACTION_UPDATE_ALL_TV_DBINFO: ActionUpdateAllTvDBInfo,
        PathValues.ACTION_UPDATE_ALL_IMAGES: ActionUpdateAllImages,
        PathValues.ACTION_UPDATE_ALL_MOVIE_DBINFO: ActionUpdateAllMovieDBInfo,
        PathValues.ACTION_UPDATE_ALL_TRAKT_INFO: ActionUpdateAllTraktInfo,
        PathValues.ACTION_VALIDATE_ALL_IMAGES: ActionValidateAllImages,
        PathValues.ACTION_AVDUMP_MISMATCHED_FILES: ActionAVDumpMismatchedFiles,
        PathValues.ACTION_DOWNLOAD_MISSING_ANI_DBANIME_DATA: ActionDownloadMissingAniDBAnimeData,
        PathValues.ACTION_REGENERATE_ALL_TV_DBEPISODE_MATCHINGS: ActionRegenerateAllTvDBEpisodeMatchings,
        PathValues.ACTION_SYNC_MY_LIST: ActionSyncMyList,
        PathValues.ACTION_UPDATE_ALL_ANI_DBINFO: ActionUpdateAllAniDBInfo,
        PathValues.ACTION_UPDATE_ALL_MEDIA_INFO: ActionUpdateAllMediaInfo,
        PathValues.ACTION_UPDATE_SERIES_STATS: ActionUpdateSeriesStats,
        PathValues.ACTION_UPDATE_MISSING_ANI_DBFILE_INFO: ActionUpdateMissingAniDBFileInfo,
        PathValues.ACTION_UPDATE_ANI_DBCALENDAR: ActionUpdateAniDBCalendar,
        PathValues.ACTION_RECREATE_ALL_GROUPS: ActionRecreateAllGroups,
        PathValues.ACTION_RENAME_ALL_GROUPS: ActionRenameAllGroups,
        PathValues.ACTION_PLEX_SYNC_ALL: ActionPlexSyncAll,
        PathValues.ACTION_ADD_ALL_MANUAL_LINKS_TO_MY_LIST: ActionAddAllManualLinksToMyList,
        PathValues.API_AUTH: ApiAuth,
        PathValues.API_AUTH_CHANGE_PASSWORD: ApiAuthChangePassword,
        PathValues.DASHBOARD_STATS: DashboardStats,
        PathValues.DASHBOARD_TOP_TAGS_NUMBER: DashboardTopTagsNumber,
        PathValues.DASHBOARD_TOP_TAGS: DashboardTopTags,
        PathValues.DASHBOARD_QUEUE_SUMMARY: DashboardQueueSummary,
        PathValues.DASHBOARD_SERIES_SUMMARY: DashboardSeriesSummary,
        PathValues.DASHBOARD_RECENTLY_ADDED_EPISODES: DashboardRecentlyAddedEpisodes,
        PathValues.DASHBOARD_RECENTLY_ADDED_SERIES: DashboardRecentlyAddedSeries,
        PathValues.DASHBOARD_CONTINUE_WATCHING_EPISODES: DashboardContinueWatchingEpisodes,
        PathValues.DASHBOARD_NEXT_UP_EPISODES: DashboardNextUpEpisodes,
        PathValues.DASHBOARD_ANI_DBCALENDAR: DashboardAniDBCalendar,
        PathValues.DEBUG_ANI_DB_UDP_CALL: DebugAniDBUDPCall,
        PathValues.EPISODE: Episode,
        PathValues.EPISODE_ANI_DB: EpisodeAniDB,
        PathValues.EPISODE_TV_DB: EpisodeTvDB,
        PathValues.EPISODE_EPISODE_ID: EpisodeEpisodeID,
        PathValues.EPISODE_EPISODE_ID_SET_HIDDEN: EpisodeEpisodeIDSetHidden,
        PathValues.EPISODE_EPISODE_ID_ANI_DB: EpisodeEpisodeIDAniDB,
        PathValues.EPISODE_ANI_DB_ANIDB_EPISODE_ID: EpisodeAniDBAnidbEpisodeID,
        PathValues.EPISODE_ANI_DB_ANIDB_EPISODE_ID_EPISODE: EpisodeAniDBAnidbEpisodeIDEpisode,
        PathValues.EPISODE_EPISODE_ID_VOTE: EpisodeEpisodeIDVote,
        PathValues.EPISODE_EPISODE_ID_TV_DB: EpisodeEpisodeIDTvDB,
        PathValues.EPISODE_EPISODE_ID_WATCHED_WATCHED: EpisodeEpisodeIDWatchedWatched,
        PathValues.EPISODE_WITH_MULTIPLE_FILES: EpisodeWithMultipleFiles,
        PathValues.EPISODE_WITH_NO_FILES: EpisodeWithNoFiles,
        PathValues.FILE: File,
        PathValues.FILE_FILE_ID: FileFileID,
        PathValues.FILE_FILE_ID_ANI_DB: FileFileIDAniDB,
        PathValues.FILE_ANI_DB_ANIDB_FILE_ID: FileAniDBAnidbFileID,
        PathValues.FILE_ANI_DB_ANIDB_FILE_ID_FILE: FileAniDBAnidbFileIDFile,
        PathValues.FILE_FILE_ID_STREAM: FileFileIDStream,
        PathValues.FILE_FILE_ID_MEDIA_INFO: FileFileIDMediaInfo,
        PathValues.FILE_FILE_ID_USER_STATS: FileFileIDUserStats,
        PathValues.FILE_FILE_ID_WATCHED_WATCHED: FileFileIDWatchedWatched,
        PathValues.FILE_FILE_ID_SCROBBLE: FileFileIDScrobble,
        PathValues.FILE_FILE_ID_IGNORE: FileFileIDIgnore,
        PathValues.FILE_FILE_ID_AVDUMP: FileFileIDAVDump,
        PathValues.FILE_FILE_ID_RESCAN: FileFileIDRescan,
        PathValues.FILE_FILE_ID_REHASH: FileFileIDRehash,
        PathValues.FILE_FILE_ID_LINK: FileFileIDLink,
        PathValues.FILE_FILE_ID_LINK_FROM_SERIES: FileFileIDLinkFromSeries,
        PathValues.FILE_LINK_FROM_SERIES: FileLinkFromSeries,
        PathValues.FILE_LINK: FileLink,
        PathValues.FILE_PATH_ENDS_WITH: FilePathEndsWith,
        PathValues.FILE_PATH_ENDS_WITH_PATH: FilePathEndsWithPath,
        PathValues.FILE_PATH_REGEX_PATH: FilePathRegexPath,
        PathValues.FILE_FILENAME_REGEX_PATH: FileFilenameRegexPath,
        PathValues.FILE_RECENT_LIMIT: FileRecentLimit,
        PathValues.FILE_RECENT: FileRecent,
        PathValues.FILE_IGNORED: FileIgnored,
        PathValues.FILE_DUPLICATES: FileDuplicates,
        PathValues.FILE_LINKED: FileLinked,
        PathValues.FILE_MISSING_CROSS_REFERENCE_DATA: FileMissingCrossReferenceData,
        PathValues.FILE_UNRECOGNIZED: FileUnrecognized,
        PathValues.FILTER: Filter,
        PathValues.FILTER_FILTER_ID: FilterFilterID,
        PathValues.FILTER_PREVIEW: FilterPreview,
        PathValues.FILTER_PREVIEW_GROUP: FilterPreviewGroup,
        PathValues.FILTER_PREVIEW_GROUP_LETTERS: FilterPreviewGroupLetters,
        PathValues.FILTER_PREVIEW_SERIES: FilterPreviewSeries,
        PathValues.FILTER_PREVIEW_GROUP_GROUP_ID_GROUP: FilterPreviewGroupGroupIDGroup,
        PathValues.FILTER_PREVIEW_GROUP_GROUP_ID_SERIES: FilterPreviewGroupGroupIDSeries,
        PathValues.FOLDER_DRIVES: FolderDrives,
        PathValues.FOLDER: Folder,
        PathValues.GROUP: Group,
        PathValues.GROUP_LETTERS: GroupLetters,
        PathValues.GROUP_GROUP_ID: GroupGroupID,
        PathValues.GROUP_GROUP_ID_RELATIONS: GroupGroupIDRelations,
        PathValues.GROUP_GROUP_ID_RECALCULATE: GroupGroupIDRecalculate,
        PathValues.GROUP_RECREATE_ALL_GROUPS: GroupRecreateAllGroups,
        PathValues.IMAGE_SOURCE_TYPE_VALUE: ImageSourceTypeValue,
        PathValues.IMAGE_RANDOM_IMAGE_TYPE: ImageRandomImageType,
        PathValues.IMAGE_RANDOM_IMAGE_TYPE_METADATA: ImageRandomImageTypeMetadata,
        PathValues.IMPORT_FOLDER: ImportFolder,
        PathValues.IMPORT_FOLDER_FOLDER_ID: ImportFolderFolderID,
        PathValues.IMPORT_FOLDER_FOLDER_ID_SCAN: ImportFolderFolderIDScan,
        PathValues.INIT_VERSION: InitVersion,
        PathValues.INIT_STATUS: InitStatus,
        PathValues.INIT_IN_USE: InitInUse,
        PathValues.INIT_DEFAULT_USER: InitDefaultUser,
        PathValues.INIT_START_SERVER: InitStartServer,
        PathValues.INIT_DATABASE_TEST: InitDatabaseTest,
        PathValues.INTEGRITY_CHECK: IntegrityCheck,
        PathValues.INTEGRITY_CHECK_ID_START: IntegrityCheckIdStart,
        PathValues.PLEX_JSON: PlexJson,
        PathValues.PLEX: Plex,
        PathValues.PLEX_LOGINURL: PlexLoginurl,
        PathValues.PLEX_PIN_AUTHENTICATED: PlexPinAuthenticated,
        PathValues.PLEX_TOKEN_INVALIDATE: PlexTokenInvalidate,
        PathValues.PLEX_SYNC: PlexSync,
        PathValues.PLEX_SYNC_ALL: PlexSyncAll,
        PathValues.PLEX_SYNC_ID: PlexSyncId,
        PathValues.PLEX_LIBRARIES: PlexLibraries,
        PathValues.PLEX_SERVER_LIST: PlexServerList,
        PathValues.PLEX_SERVER: PlexServer,
        PathValues.PLEX_LIBRARIES_ID: PlexLibrariesId,
        PathValues.RENAMER: Renamer,
        PathValues.RENAMER_RENAMER_ID: RenamerRenamerID,
        PathValues.FILTER_FILTER_ID_PARENT: FilterFilterIDParent,
        PathValues.GROUP_GROUP_ID_PARENT: GroupGroupIDParent,
        PathValues.SERIES_SERIES_ID_GROUP: SeriesSeriesIDGroup,
        PathValues.EPISODE_EPISODE_ID_SERIES: EpisodeEpisodeIDSeries,
        PathValues.FILE_FILE_ID_EPISODE: FileFileIDEpisode,
        PathValues.SERIES: Series,
        PathValues.SERIES_SERIES_ID: SeriesSeriesID,
        PathValues.SERIES_SERIES_ID_AUTO_MATCH_SETTINGS: SeriesSeriesIDAutoMatchSettings,
        PathValues.SERIES_SERIES_ID_RELATIONS: SeriesSeriesIDRelations,
        PathValues.SERIES_WITHOUT_FILES: SeriesWithoutFiles,
        PathValues.SERIES_WITH_MANUALLY_LINKED_FILES: SeriesWithManuallyLinkedFiles,
        PathValues.SERIES_ANI_DB: SeriesAniDB,
        PathValues.SERIES_ANI_DB_RELATIONS: SeriesAniDBRelations,
        PathValues.SERIES_SERIES_ID_ANI_DB: SeriesSeriesIDAniDB,
        PathValues.SERIES_SERIES_ID_ANI_DB_SIMILAR: SeriesSeriesIDAniDBSimilar,
        PathValues.SERIES_SERIES_ID_ANI_DB_RELATED: SeriesSeriesIDAniDBRelated,
        PathValues.SERIES_SERIES_ID_ANI_DB_RELATIONS: SeriesSeriesIDAniDBRelations,
        PathValues.SERIES_ANI_DB_RECOMMENDED_FOR_YOU: SeriesAniDBRecommendedForYou,
        PathValues.SERIES_ANI_DB_ANIDB_ID: SeriesAniDBAnidbID,
        PathValues.SERIES_ANI_DB_ANIDB_ID_SIMILAR: SeriesAniDBAnidbIDSimilar,
        PathValues.SERIES_ANI_DB_ANIDB_ID_RELATED: SeriesAniDBAnidbIDRelated,
        PathValues.SERIES_ANI_DB_ANIDB_ID_RELATIONS: SeriesAniDBAnidbIDRelations,
        PathValues.SERIES_ANI_DB_ANIDB_ID_SERIES: SeriesAniDBAnidbIDSeries,
        PathValues.SERIES_ANI_DB_ANIDB_ID_REFRESH: SeriesAniDBAnidbIDRefresh,
        PathValues.SERIES_SERIES_ID_ANI_DB_REFRESH: SeriesSeriesIDAniDBRefresh,
        PathValues.SERIES_SERIES_ID_ANI_DB_REFRESH_FORCE_FROM_XML: SeriesSeriesIDAniDBRefreshForceFromXML,
        PathValues.SERIES_SERIES_ID_TV_DB: SeriesSeriesIDTvDB,
        PathValues.SERIES_SERIES_ID_TVDB_ID_REFRESH: SeriesSeriesIDTvdbIDRefresh,
        PathValues.SERIES_TV_DB_TVDB_ID: SeriesTvDBTvdbID,
        PathValues.SERIES_TV_DB_TVDB_ID_REFRESH: SeriesTvDBTvdbIDRefresh,
        PathValues.SERIES_TV_DB_TVDB_ID_SERIES: SeriesTvDBTvdbIDSeries,
        PathValues.SERIES_SERIES_ID_VOTE: SeriesSeriesIDVote,
        PathValues.SERIES_SERIES_ID_IMAGES: SeriesSeriesIDImages,
        PathValues.SERIES_SERIES_ID_IMAGES_IMAGE_TYPE: SeriesSeriesIDImagesImageType,
        PathValues.SERIES_SERIES_ID_TAGS: SeriesSeriesIDTags,
        PathValues.SERIES_SERIES_ID_TAGS_FILTER: SeriesSeriesIDTagsFilter,
        PathValues.SERIES_SERIES_ID_CAST: SeriesSeriesIDCast,
        PathValues.SERIES_SERIES_ID_MOVE_GROUP_ID: SeriesSeriesIDMoveGroupID,
        PathValues.SERIES_SEARCH: SeriesSearch,
        PathValues.SERIES_SEARCH_QUERY: SeriesSearchQuery,
        PathValues.SERIES_ANI_DB_SEARCH: SeriesAniDBSearch,
        PathValues.SERIES_ANI_DB_SEARCH_QUERY: SeriesAniDBSearchQuery,
        PathValues.SERIES_STARTS_WITH_QUERY: SeriesStartsWithQuery,
        PathValues.SERIES_PATH_ENDS_WITH_PATH: SeriesPathEndsWithPath,
        PathValues.TAG_ANI_DB: TagAniDB,
        PathValues.TAG_ANI_DB_TAG_ID: TagAniDBTagID,
        PathValues.TAG_USER: TagUser,
        PathValues.TAG_USER_TAG_ID: TagUserTagID,
        PathValues.IMPORT_FOLDER_FOLDER_ID_FILE: ImportFolderFolderIDFile,
        PathValues.FILTER_FILTER_ID_FILTER: FilterFilterIDFilter,
        PathValues.FILTER_FILTER_ID_GROUP: FilterFilterIDGroup,
        PathValues.FILTER_FILTER_ID_GROUP_LETTERS: FilterFilterIDGroupLetters,
        PathValues.FILTER_FILTER_ID_SERIES: FilterFilterIDSeries,
        PathValues.FILTER_FILTER_ID_GROUP_GROUP_ID_GROUP: FilterFilterIDGroupGroupIDGroup,
        PathValues.FILTER_FILTER_ID_GROUP_GROUP_ID_SERIES: FilterFilterIDGroupGroupIDSeries,
        PathValues.GROUP_GROUP_ID_GROUP: GroupGroupIDGroup,
        PathValues.GROUP_GROUP_ID_SERIES: GroupGroupIDSeries,
        PathValues.GROUP_GROUP_ID_MAIN_SERIES: GroupGroupIDMainSeries,
        PathValues.SERIES_SERIES_ID_EPISODE: SeriesSeriesIDEpisode,
        PathValues.SERIES_SERIES_ID_NEXT_UP_EPISODE: SeriesSeriesIDNextUpEpisode,
        PathValues.SERIES_SERIES_ID_FILE: SeriesSeriesIDFile,
        PathValues.EPISODE_EPISODE_ID_FILE: EpisodeEpisodeIDFile,
        PathValues.USER: User,
        PathValues.USER_CURRENT: UserCurrent,
        PathValues.USER_CURRENT_CHANGE_PASSWORD: UserCurrentChangePassword,
        PathValues.USER_USER_ID: UserUserID,
        PathValues.USER_USER_ID_CHANGE_PASSWORD: UserUserIDChangePassword,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACTION_RUN_IMPORT: ActionRunImport,
        PathValues.ACTION_IMPORT_NEW_FILES: ActionImportNewFiles,
        PathValues.ACTION_SYNC_HASHES: ActionSyncHashes,
        PathValues.ACTION_SYNC_VOTES: ActionSyncVotes,
        PathValues.ACTION_SYNC_TRAKT: ActionSyncTrakt,
        PathValues.ACTION_REMOVE_MISSING_FILES_REMOVE_FROM_MY_LIST: ActionRemoveMissingFilesRemoveFromMyList,
        PathValues.ACTION_UPDATE_ALL_TV_DBINFO: ActionUpdateAllTvDBInfo,
        PathValues.ACTION_UPDATE_ALL_IMAGES: ActionUpdateAllImages,
        PathValues.ACTION_UPDATE_ALL_MOVIE_DBINFO: ActionUpdateAllMovieDBInfo,
        PathValues.ACTION_UPDATE_ALL_TRAKT_INFO: ActionUpdateAllTraktInfo,
        PathValues.ACTION_VALIDATE_ALL_IMAGES: ActionValidateAllImages,
        PathValues.ACTION_AVDUMP_MISMATCHED_FILES: ActionAVDumpMismatchedFiles,
        PathValues.ACTION_DOWNLOAD_MISSING_ANI_DBANIME_DATA: ActionDownloadMissingAniDBAnimeData,
        PathValues.ACTION_REGENERATE_ALL_TV_DBEPISODE_MATCHINGS: ActionRegenerateAllTvDBEpisodeMatchings,
        PathValues.ACTION_SYNC_MY_LIST: ActionSyncMyList,
        PathValues.ACTION_UPDATE_ALL_ANI_DBINFO: ActionUpdateAllAniDBInfo,
        PathValues.ACTION_UPDATE_ALL_MEDIA_INFO: ActionUpdateAllMediaInfo,
        PathValues.ACTION_UPDATE_SERIES_STATS: ActionUpdateSeriesStats,
        PathValues.ACTION_UPDATE_MISSING_ANI_DBFILE_INFO: ActionUpdateMissingAniDBFileInfo,
        PathValues.ACTION_UPDATE_ANI_DBCALENDAR: ActionUpdateAniDBCalendar,
        PathValues.ACTION_RECREATE_ALL_GROUPS: ActionRecreateAllGroups,
        PathValues.ACTION_RENAME_ALL_GROUPS: ActionRenameAllGroups,
        PathValues.ACTION_PLEX_SYNC_ALL: ActionPlexSyncAll,
        PathValues.ACTION_ADD_ALL_MANUAL_LINKS_TO_MY_LIST: ActionAddAllManualLinksToMyList,
        PathValues.API_AUTH: ApiAuth,
        PathValues.API_AUTH_CHANGE_PASSWORD: ApiAuthChangePassword,
        PathValues.DASHBOARD_STATS: DashboardStats,
        PathValues.DASHBOARD_TOP_TAGS_NUMBER: DashboardTopTagsNumber,
        PathValues.DASHBOARD_TOP_TAGS: DashboardTopTags,
        PathValues.DASHBOARD_QUEUE_SUMMARY: DashboardQueueSummary,
        PathValues.DASHBOARD_SERIES_SUMMARY: DashboardSeriesSummary,
        PathValues.DASHBOARD_RECENTLY_ADDED_EPISODES: DashboardRecentlyAddedEpisodes,
        PathValues.DASHBOARD_RECENTLY_ADDED_SERIES: DashboardRecentlyAddedSeries,
        PathValues.DASHBOARD_CONTINUE_WATCHING_EPISODES: DashboardContinueWatchingEpisodes,
        PathValues.DASHBOARD_NEXT_UP_EPISODES: DashboardNextUpEpisodes,
        PathValues.DASHBOARD_ANI_DBCALENDAR: DashboardAniDBCalendar,
        PathValues.DEBUG_ANI_DB_UDP_CALL: DebugAniDBUDPCall,
        PathValues.EPISODE: Episode,
        PathValues.EPISODE_ANI_DB: EpisodeAniDB,
        PathValues.EPISODE_TV_DB: EpisodeTvDB,
        PathValues.EPISODE_EPISODE_ID: EpisodeEpisodeID,
        PathValues.EPISODE_EPISODE_ID_SET_HIDDEN: EpisodeEpisodeIDSetHidden,
        PathValues.EPISODE_EPISODE_ID_ANI_DB: EpisodeEpisodeIDAniDB,
        PathValues.EPISODE_ANI_DB_ANIDB_EPISODE_ID: EpisodeAniDBAnidbEpisodeID,
        PathValues.EPISODE_ANI_DB_ANIDB_EPISODE_ID_EPISODE: EpisodeAniDBAnidbEpisodeIDEpisode,
        PathValues.EPISODE_EPISODE_ID_VOTE: EpisodeEpisodeIDVote,
        PathValues.EPISODE_EPISODE_ID_TV_DB: EpisodeEpisodeIDTvDB,
        PathValues.EPISODE_EPISODE_ID_WATCHED_WATCHED: EpisodeEpisodeIDWatchedWatched,
        PathValues.EPISODE_WITH_MULTIPLE_FILES: EpisodeWithMultipleFiles,
        PathValues.EPISODE_WITH_NO_FILES: EpisodeWithNoFiles,
        PathValues.FILE: File,
        PathValues.FILE_FILE_ID: FileFileID,
        PathValues.FILE_FILE_ID_ANI_DB: FileFileIDAniDB,
        PathValues.FILE_ANI_DB_ANIDB_FILE_ID: FileAniDBAnidbFileID,
        PathValues.FILE_ANI_DB_ANIDB_FILE_ID_FILE: FileAniDBAnidbFileIDFile,
        PathValues.FILE_FILE_ID_STREAM: FileFileIDStream,
        PathValues.FILE_FILE_ID_MEDIA_INFO: FileFileIDMediaInfo,
        PathValues.FILE_FILE_ID_USER_STATS: FileFileIDUserStats,
        PathValues.FILE_FILE_ID_WATCHED_WATCHED: FileFileIDWatchedWatched,
        PathValues.FILE_FILE_ID_SCROBBLE: FileFileIDScrobble,
        PathValues.FILE_FILE_ID_IGNORE: FileFileIDIgnore,
        PathValues.FILE_FILE_ID_AVDUMP: FileFileIDAVDump,
        PathValues.FILE_FILE_ID_RESCAN: FileFileIDRescan,
        PathValues.FILE_FILE_ID_REHASH: FileFileIDRehash,
        PathValues.FILE_FILE_ID_LINK: FileFileIDLink,
        PathValues.FILE_FILE_ID_LINK_FROM_SERIES: FileFileIDLinkFromSeries,
        PathValues.FILE_LINK_FROM_SERIES: FileLinkFromSeries,
        PathValues.FILE_LINK: FileLink,
        PathValues.FILE_PATH_ENDS_WITH: FilePathEndsWith,
        PathValues.FILE_PATH_ENDS_WITH_PATH: FilePathEndsWithPath,
        PathValues.FILE_PATH_REGEX_PATH: FilePathRegexPath,
        PathValues.FILE_FILENAME_REGEX_PATH: FileFilenameRegexPath,
        PathValues.FILE_RECENT_LIMIT: FileRecentLimit,
        PathValues.FILE_RECENT: FileRecent,
        PathValues.FILE_IGNORED: FileIgnored,
        PathValues.FILE_DUPLICATES: FileDuplicates,
        PathValues.FILE_LINKED: FileLinked,
        PathValues.FILE_MISSING_CROSS_REFERENCE_DATA: FileMissingCrossReferenceData,
        PathValues.FILE_UNRECOGNIZED: FileUnrecognized,
        PathValues.FILTER: Filter,
        PathValues.FILTER_FILTER_ID: FilterFilterID,
        PathValues.FILTER_PREVIEW: FilterPreview,
        PathValues.FILTER_PREVIEW_GROUP: FilterPreviewGroup,
        PathValues.FILTER_PREVIEW_GROUP_LETTERS: FilterPreviewGroupLetters,
        PathValues.FILTER_PREVIEW_SERIES: FilterPreviewSeries,
        PathValues.FILTER_PREVIEW_GROUP_GROUP_ID_GROUP: FilterPreviewGroupGroupIDGroup,
        PathValues.FILTER_PREVIEW_GROUP_GROUP_ID_SERIES: FilterPreviewGroupGroupIDSeries,
        PathValues.FOLDER_DRIVES: FolderDrives,
        PathValues.FOLDER: Folder,
        PathValues.GROUP: Group,
        PathValues.GROUP_LETTERS: GroupLetters,
        PathValues.GROUP_GROUP_ID: GroupGroupID,
        PathValues.GROUP_GROUP_ID_RELATIONS: GroupGroupIDRelations,
        PathValues.GROUP_GROUP_ID_RECALCULATE: GroupGroupIDRecalculate,
        PathValues.GROUP_RECREATE_ALL_GROUPS: GroupRecreateAllGroups,
        PathValues.IMAGE_SOURCE_TYPE_VALUE: ImageSourceTypeValue,
        PathValues.IMAGE_RANDOM_IMAGE_TYPE: ImageRandomImageType,
        PathValues.IMAGE_RANDOM_IMAGE_TYPE_METADATA: ImageRandomImageTypeMetadata,
        PathValues.IMPORT_FOLDER: ImportFolder,
        PathValues.IMPORT_FOLDER_FOLDER_ID: ImportFolderFolderID,
        PathValues.IMPORT_FOLDER_FOLDER_ID_SCAN: ImportFolderFolderIDScan,
        PathValues.INIT_VERSION: InitVersion,
        PathValues.INIT_STATUS: InitStatus,
        PathValues.INIT_IN_USE: InitInUse,
        PathValues.INIT_DEFAULT_USER: InitDefaultUser,
        PathValues.INIT_START_SERVER: InitStartServer,
        PathValues.INIT_DATABASE_TEST: InitDatabaseTest,
        PathValues.INTEGRITY_CHECK: IntegrityCheck,
        PathValues.INTEGRITY_CHECK_ID_START: IntegrityCheckIdStart,
        PathValues.PLEX_JSON: PlexJson,
        PathValues.PLEX: Plex,
        PathValues.PLEX_LOGINURL: PlexLoginurl,
        PathValues.PLEX_PIN_AUTHENTICATED: PlexPinAuthenticated,
        PathValues.PLEX_TOKEN_INVALIDATE: PlexTokenInvalidate,
        PathValues.PLEX_SYNC: PlexSync,
        PathValues.PLEX_SYNC_ALL: PlexSyncAll,
        PathValues.PLEX_SYNC_ID: PlexSyncId,
        PathValues.PLEX_LIBRARIES: PlexLibraries,
        PathValues.PLEX_SERVER_LIST: PlexServerList,
        PathValues.PLEX_SERVER: PlexServer,
        PathValues.PLEX_LIBRARIES_ID: PlexLibrariesId,
        PathValues.RENAMER: Renamer,
        PathValues.RENAMER_RENAMER_ID: RenamerRenamerID,
        PathValues.FILTER_FILTER_ID_PARENT: FilterFilterIDParent,
        PathValues.GROUP_GROUP_ID_PARENT: GroupGroupIDParent,
        PathValues.SERIES_SERIES_ID_GROUP: SeriesSeriesIDGroup,
        PathValues.EPISODE_EPISODE_ID_SERIES: EpisodeEpisodeIDSeries,
        PathValues.FILE_FILE_ID_EPISODE: FileFileIDEpisode,
        PathValues.SERIES: Series,
        PathValues.SERIES_SERIES_ID: SeriesSeriesID,
        PathValues.SERIES_SERIES_ID_AUTO_MATCH_SETTINGS: SeriesSeriesIDAutoMatchSettings,
        PathValues.SERIES_SERIES_ID_RELATIONS: SeriesSeriesIDRelations,
        PathValues.SERIES_WITHOUT_FILES: SeriesWithoutFiles,
        PathValues.SERIES_WITH_MANUALLY_LINKED_FILES: SeriesWithManuallyLinkedFiles,
        PathValues.SERIES_ANI_DB: SeriesAniDB,
        PathValues.SERIES_ANI_DB_RELATIONS: SeriesAniDBRelations,
        PathValues.SERIES_SERIES_ID_ANI_DB: SeriesSeriesIDAniDB,
        PathValues.SERIES_SERIES_ID_ANI_DB_SIMILAR: SeriesSeriesIDAniDBSimilar,
        PathValues.SERIES_SERIES_ID_ANI_DB_RELATED: SeriesSeriesIDAniDBRelated,
        PathValues.SERIES_SERIES_ID_ANI_DB_RELATIONS: SeriesSeriesIDAniDBRelations,
        PathValues.SERIES_ANI_DB_RECOMMENDED_FOR_YOU: SeriesAniDBRecommendedForYou,
        PathValues.SERIES_ANI_DB_ANIDB_ID: SeriesAniDBAnidbID,
        PathValues.SERIES_ANI_DB_ANIDB_ID_SIMILAR: SeriesAniDBAnidbIDSimilar,
        PathValues.SERIES_ANI_DB_ANIDB_ID_RELATED: SeriesAniDBAnidbIDRelated,
        PathValues.SERIES_ANI_DB_ANIDB_ID_RELATIONS: SeriesAniDBAnidbIDRelations,
        PathValues.SERIES_ANI_DB_ANIDB_ID_SERIES: SeriesAniDBAnidbIDSeries,
        PathValues.SERIES_ANI_DB_ANIDB_ID_REFRESH: SeriesAniDBAnidbIDRefresh,
        PathValues.SERIES_SERIES_ID_ANI_DB_REFRESH: SeriesSeriesIDAniDBRefresh,
        PathValues.SERIES_SERIES_ID_ANI_DB_REFRESH_FORCE_FROM_XML: SeriesSeriesIDAniDBRefreshForceFromXML,
        PathValues.SERIES_SERIES_ID_TV_DB: SeriesSeriesIDTvDB,
        PathValues.SERIES_SERIES_ID_TVDB_ID_REFRESH: SeriesSeriesIDTvdbIDRefresh,
        PathValues.SERIES_TV_DB_TVDB_ID: SeriesTvDBTvdbID,
        PathValues.SERIES_TV_DB_TVDB_ID_REFRESH: SeriesTvDBTvdbIDRefresh,
        PathValues.SERIES_TV_DB_TVDB_ID_SERIES: SeriesTvDBTvdbIDSeries,
        PathValues.SERIES_SERIES_ID_VOTE: SeriesSeriesIDVote,
        PathValues.SERIES_SERIES_ID_IMAGES: SeriesSeriesIDImages,
        PathValues.SERIES_SERIES_ID_IMAGES_IMAGE_TYPE: SeriesSeriesIDImagesImageType,
        PathValues.SERIES_SERIES_ID_TAGS: SeriesSeriesIDTags,
        PathValues.SERIES_SERIES_ID_TAGS_FILTER: SeriesSeriesIDTagsFilter,
        PathValues.SERIES_SERIES_ID_CAST: SeriesSeriesIDCast,
        PathValues.SERIES_SERIES_ID_MOVE_GROUP_ID: SeriesSeriesIDMoveGroupID,
        PathValues.SERIES_SEARCH: SeriesSearch,
        PathValues.SERIES_SEARCH_QUERY: SeriesSearchQuery,
        PathValues.SERIES_ANI_DB_SEARCH: SeriesAniDBSearch,
        PathValues.SERIES_ANI_DB_SEARCH_QUERY: SeriesAniDBSearchQuery,
        PathValues.SERIES_STARTS_WITH_QUERY: SeriesStartsWithQuery,
        PathValues.SERIES_PATH_ENDS_WITH_PATH: SeriesPathEndsWithPath,
        PathValues.TAG_ANI_DB: TagAniDB,
        PathValues.TAG_ANI_DB_TAG_ID: TagAniDBTagID,
        PathValues.TAG_USER: TagUser,
        PathValues.TAG_USER_TAG_ID: TagUserTagID,
        PathValues.IMPORT_FOLDER_FOLDER_ID_FILE: ImportFolderFolderIDFile,
        PathValues.FILTER_FILTER_ID_FILTER: FilterFilterIDFilter,
        PathValues.FILTER_FILTER_ID_GROUP: FilterFilterIDGroup,
        PathValues.FILTER_FILTER_ID_GROUP_LETTERS: FilterFilterIDGroupLetters,
        PathValues.FILTER_FILTER_ID_SERIES: FilterFilterIDSeries,
        PathValues.FILTER_FILTER_ID_GROUP_GROUP_ID_GROUP: FilterFilterIDGroupGroupIDGroup,
        PathValues.FILTER_FILTER_ID_GROUP_GROUP_ID_SERIES: FilterFilterIDGroupGroupIDSeries,
        PathValues.GROUP_GROUP_ID_GROUP: GroupGroupIDGroup,
        PathValues.GROUP_GROUP_ID_SERIES: GroupGroupIDSeries,
        PathValues.GROUP_GROUP_ID_MAIN_SERIES: GroupGroupIDMainSeries,
        PathValues.SERIES_SERIES_ID_EPISODE: SeriesSeriesIDEpisode,
        PathValues.SERIES_SERIES_ID_NEXT_UP_EPISODE: SeriesSeriesIDNextUpEpisode,
        PathValues.SERIES_SERIES_ID_FILE: SeriesSeriesIDFile,
        PathValues.EPISODE_EPISODE_ID_FILE: EpisodeEpisodeIDFile,
        PathValues.USER: User,
        PathValues.USER_CURRENT: UserCurrent,
        PathValues.USER_CURRENT_CHANGE_PASSWORD: UserCurrentChangePassword,
        PathValues.USER_USER_ID: UserUserID,
        PathValues.USER_USER_ID_CHANGE_PASSWORD: UserUserIDChangePassword,
    }
)
