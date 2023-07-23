# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lib.shoko.v3.paths.series_path_ends_with_path import Api

from lib.shoko.v3.paths import PathValues

path = PathValues.SERIES_PATH_ENDS_WITH_PATH