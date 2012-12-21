# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 OpenStack LLC
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

import uuid

from keystoneclient.v3 import mappings
from tests.v3 import utils


class MappingTests(utils.TestCase, utils.CrudTests):
    def setUp(self):
        super(MappingTests, self).setUp()
        self.additionalSetUp()
        self.key = 'mapping'
        self.collection_key = 'mappings'
        self.model = mappings.Mapping
        self.manager = self.client.mappings

    def new_ref(self, **kwargs):
        kwargs = super(MappingTests, self).new_ref(**kwargs)
        kwargs.setdefault('name', uuid.uuid4().hex)
        kwargs.setdefault('org_attribute_set', uuid.uuid4().hex)
        kwargs.setdefault('os_attribute_set', uuid.uuid4().hex)
        return kwargs
