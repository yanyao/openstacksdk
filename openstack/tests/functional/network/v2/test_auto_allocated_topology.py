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

from openstack.tests.functional import base


class TestAutoAllocatedTopology(base.BaseFunctionalTest):
    NETWORK_NAME = "auto_allocated_network"
    NETWORK_ID = None
    PROJECT_ID = None

    def setUp(self):
        super().setUp()
        if not self.operator_cloud:
            self.skipTest("Operator cloud is required for this test")
        if not self.operator_cloud._has_neutron_extension(
            "auto-allocated-topology"
        ):
            self.skipTest(
                "Neutron auto-allocated-topology extension is "
                "required for this test"
            )

        projects = [o.id for o in self.operator_cloud.identity.projects()]
        self.PROJECT_ID = projects[0]

    def tearDown(self):
        res = self.operator_cloud.network.delete_auto_allocated_topology(
            self.PROJECT_ID
        )
        self.assertIsNone(res)
        super().tearDown()

    def test_dry_run_option_pass(self):
        # Dry run will only pass if there is a public network
        networks = self.operator_cloud.network.networks()
        self._set_network_external(networks)

        # Dry run option will return "dry-run=pass" in the 'id' resource
        top = self.operator_cloud.network.validate_auto_allocated_topology(
            self.PROJECT_ID
        )
        self.assertEqual(self.PROJECT_ID, top.project)
        self.assertEqual("dry-run=pass", top.id)

    def test_show_no_project_option(self):
        top = self.operator_cloud.network.get_auto_allocated_topology()
        project = self.conn.session.get_project_id()
        network = self.operator_cloud.network.get_network(top.id)
        self.assertEqual(top.project_id, project)
        self.assertEqual(top.id, network.id)

    def test_show_project_option(self):
        top = self.operator_cloud.network.get_auto_allocated_topology(
            self.PROJECT_ID
        )
        network = self.operator_cloud.network.get_network(top.id)
        self.assertEqual(top.project_id, network.project_id)
        self.assertEqual(top.id, network.id)
        self.assertEqual(network.name, "auto_allocated_network")

    def _set_network_external(self, networks):
        for network in networks:
            if network.name == "public":
                self.operator_cloud.network.update_network(
                    network, is_default=True
                )
