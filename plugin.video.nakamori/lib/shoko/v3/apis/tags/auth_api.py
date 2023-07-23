# coding: utf-8

"""
    Shoko API 3

    Shoko Server API.  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from lib.shoko.v3.paths.api_auth_change_password.post import ApiAuthChangePasswordPost
from lib.shoko.v3.paths.api_auth.delete import ApiAuthDelete
from lib.shoko.v3.paths.api_auth.post import ApiAuthPost


class AuthApi(
    ApiAuthChangePasswordPost,
    ApiAuthDelete,
    ApiAuthPost,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
