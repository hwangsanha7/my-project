# Copyright 2024 Your Name <your.email@example.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ament_flake8.main import main
import pytest

# 이 파일도 거의 모든 프로젝트에서 이대로 사용하면 됩니다.
@pytest.mark.flake8
@pytest.mark.linter
def test_flake8():
    rc = main(argv=[])
    assert rc == 0, "Found errors"
