# coding: utf-8

"""
    Shoko API 3

    Shoko Server API.  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from lib.shoko.v3.paths.init_database_test.get import InitDatabaseTestGet
from lib.shoko.v3.paths.init_default_user.get import InitDefaultUserGet
from lib.shoko.v3.paths.init_default_user.post import InitDefaultUserPost
from lib.shoko.v3.paths.init_in_use.get import InitInUseGet
from lib.shoko.v3.paths.init_start_server.get import InitStartServerGet
from lib.shoko.v3.paths.init_status.get import InitStatusGet
from lib.shoko.v3.paths.init_version.get import InitVersionGet


class InitApi(
    InitDatabaseTestGet,
    InitDefaultUserGet,
    InitDefaultUserPost,
    InitInUseGet,
    InitStartServerGet,
    InitStatusGet,
    InitVersionGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
