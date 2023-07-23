# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lib.shoko.v3.paths.plex_pin_authenticated import Api

from lib.shoko.v3.paths import PathValues

path = PathValues.PLEX_PIN_AUTHENTICATED