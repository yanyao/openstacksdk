# Copyright (c) 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# TODO(mordred) This is only here to ease the OSC transition

from openstack.config import cloud_region


class CloudConfig(cloud_region.CloudRegion):
    def __init__(self, name, region, config, **kwargs):
        super().__init__(name, region, config, **kwargs)
        self.region = region
