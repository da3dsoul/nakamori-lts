# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lib.shoko.v3.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DEBUG = "Debug"
    INIT = "Init"
    REVERSE_TREE = "ReverseTree"
    TREE = "Tree"
    ACTION = "Action"
    AUTH = "Auth"
    DASHBOARD = "Dashboard"
    EPISODE = "Episode"
    FILE = "File"
    FILTER = "Filter"
    FOLDER = "Folder"
    GROUP = "Group"
    IMAGE = "Image"
    IMPORT_FOLDER = "ImportFolder"
    INTEGRITY_CHECK = "IntegrityCheck"
    PLEX_WEBHOOK = "PlexWebhook"
    RENAMER = "Renamer"
    SERIES = "Series"
    TAG = "Tag"
    USER = "User"
