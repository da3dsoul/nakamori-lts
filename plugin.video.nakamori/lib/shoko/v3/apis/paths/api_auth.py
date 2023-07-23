from lib.shoko.v3.paths.api_auth.post import ApiForpost
from lib.shoko.v3.paths.api_auth.delete import ApiFordelete


class ApiAuth(
    ApiForpost,
    ApiFordelete,
):
    pass
