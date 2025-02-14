#  coding=utf-8
#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from argilla import __version__ as argilla_version
from argilla.server.services.info import ApiInfo, ApiStatus


def test_api_info(mocked_client):

    response = mocked_client.get("/api/_info")
    assert response.status_code == 200

    info = ApiInfo.parse_obj(response.json())

    assert info.version == argilla_version


def test_api_status(mocked_client):

    response = mocked_client.get("/api/_status")

    assert response.status_code == 200

    info = ApiStatus.parse_obj(response.json())

    assert info.version == argilla_version

    # Checking to not get the error dictionary service.py includes whenever something goes wrong
    assert not "error" in info.elasticsearch

    # Checking that the first key into mem_info dictionary has a nont-none value
    assert "rss" in info.mem_info is not None
