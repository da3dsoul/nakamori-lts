# coding: utf-8

"""
    Shoko API 3

    Shoko Server API.  # noqa: E501

    The version of the OpenAPI document: 3
    Generated by: https://openapi-generator.tech
"""

from lib.shoko.v3.paths.group.get import GroupGet
from lib.shoko.v3.paths.group_group_id.delete import GroupGroupIdDelete
from lib.shoko.v3.paths.group_group_id.get import GroupGroupIdGet
from lib.shoko.v3.paths.group_group_id.patch import GroupGroupIdPatch
from lib.shoko.v3.paths.group_group_id.put import GroupGroupIdPut
from lib.shoko.v3.paths.group_group_id_recalculate.post import GroupGroupIdRecalculatePost
from lib.shoko.v3.paths.group_group_id_relations.get import GroupGroupIdRelationsGet
from lib.shoko.v3.paths.group_letters.get import GroupLettersGet
from lib.shoko.v3.paths.group.post import GroupPost
from lib.shoko.v3.paths.group_recreate_all_groups.get import GroupRecreateAllGroupsGet


class GroupApi(
    GroupGet,
    GroupGroupIdDelete,
    GroupGroupIdGet,
    GroupGroupIdPatch,
    GroupGroupIdPut,
    GroupGroupIdRecalculatePost,
    GroupGroupIdRelationsGet,
    GroupLettersGet,
    GroupPost,
    GroupRecreateAllGroupsGet,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
