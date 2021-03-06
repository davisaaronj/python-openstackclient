#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

# NOTE(dtroyer): This file is deprecated in Jun 2016, remove after 4.x release
#                or Jun 2017.

import sys

from osc_lib.logs import *  # noqa
from osc_lib.logs import _FileFormatter  # noqa


sys.stderr.write(
    "WARNING: %s is deprecated and will be removed after Jun 2017. "
    "Please use osc_lib.logs\n" % __name__
)
