# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lib.shoko.v3.paths.init_start_server import Api

from lib.shoko.v3.paths import PathValues

path = PathValues.INIT_START_SERVER