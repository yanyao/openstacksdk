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

import testtools

from openstack.cluster.v1 import action


FAKE_ID = '633bd3c6-520b-420f-8e6a-dc2a47022b53'
FAKE_NAME = 'node_create_c3783474'

FAKE = {
    'name': FAKE_NAME,
    'target': 'c378e474-d091-43a3-b083-e19719291358',
    'action': 'NODE_CREATE',
    'cause': 'RPC Request',
    'owner': None,
    'interval': -1,
    'start_time': 144450000.0,
    'end_time': 144450000.0,
    'timeout': 3600,
    'status': 'SUCCEEDED',
    'status_reason': 'Action completed successfully.',
    'inputs': {},
    'outputs': {},
    'depends_on': [],
    'depended_by': [],
    'created_time': '2015-10-10T04:46:36.000000',
    'updated_time': None,
    'deleted_time': None,
}


class TestCluster(testtools.TestCase):

    def setUp(self):
        super(TestCluster, self).setUp()

    def test_basic(self):
        sot = action.Action()
        self.assertEqual('action', sot.resource_key)
        self.assertEqual('actions', sot.resources_key)
        self.assertEqual('/actions', sot.base_path)
        self.assertEqual('clustering', sot.service.service_type)
        self.assertTrue(sot.allow_retrieve)
        self.assertTrue(sot.allow_list)

    def test_instantiate(self):
        sot = action.Action(FAKE)
        self.assertIsNone(sot.id)
        self.assertEqual(FAKE['name'], sot.name)
        self.assertEqual(FAKE['target'], sot.target)
        self.assertEqual(FAKE['action'], sot.action)
        self.assertEqual(FAKE['cause'], sot.cause)
        self.assertEqual(FAKE['owner'], sot.owner)
        self.assertEqual(FAKE['interval'], sot.interval)
        self.assertEqual(FAKE['start_time'], sot.start_time)
        self.assertEqual(FAKE['end_time'], sot.end_time)
        self.assertEqual(FAKE['timeout'], sot.timeout)
        self.assertEqual(FAKE['status'], sot.status)
        self.assertEqual(FAKE['status_reason'], sot.status_reason)
        self.assertEqual(FAKE['inputs'], sot.inputs)
        self.assertEqual(FAKE['outputs'], sot.outputs)
        self.assertEqual(FAKE['depends_on'], sot.depends_on)
        self.assertEqual(FAKE['depended_by'], sot.depended_by)
        self.assertEqual(FAKE['created_time'], sot.created_at)
        self.assertEqual(FAKE['updated_time'], sot.updated_at)
        self.assertEqual(FAKE['deleted_time'], sot.deleted_at)
