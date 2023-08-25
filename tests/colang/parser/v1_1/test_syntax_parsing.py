# SPDX-FileCopyrightText: Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest

from nemoguardrails.colang.v1_1.lang.parser import ColangParser

tests_root = os.path.join(os.path.dirname(__file__), "../../..")


@pytest.mark.parametrize(
    "filename",
    [
        "colang/parser/v1_1/inputs/test.co",
        "colang/parser/v1_1/inputs/test2.co",
        "colang/parser/v1_1/inputs/test3.co",
        "colang/parser/v1_1/inputs/test4.co",
        "colang/parser/v1_1/inputs/test5.co",
        "colang/parser/v1_1/inputs/test6.co",
        "test_configs/example_interactions/faq_questions.co",
        "test_configs/example_interactions/core_flows.co",
        "test_configs/example_interactions/confirmation_question.co",
        "test_configs/example_interactions/multi_modal_actions.co",
        "test_configs/example_interactions/action_conflicts.co",
    ],
)
def test_parsing_syntax(filename):
    colang_parser = ColangParser()
    with open(os.path.join(tests_root, filename), "r") as file:
        content = file.read()

    # We only check that there is no syntax error
    colang_parser.parse_content(content)
