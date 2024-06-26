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


class TestQoSRuleType(base.BaseFunctionalTest):
    QOS_RULE_TYPE = "bandwidth_limit"

    def setUp(self):
        super().setUp()
        if not self.operator_cloud:
            self.skipTest("Operator cloud is required for this test")

        # Skip the tests if qos-rule-type-details extension is not enabled.
        if not self.operator_cloud.network.find_extension(
            "qos-rule-type-details"
        ):
            self.skipTest("Network qos-rule-type-details extension disabled")

    def test_find(self):
        sot = self.operator_cloud.network.find_qos_rule_type(
            self.QOS_RULE_TYPE
        )
        self.assertEqual(self.QOS_RULE_TYPE, sot.type)
        self.assertIsInstance(sot.drivers, list)

    def test_get(self):
        sot = self.operator_cloud.network.get_qos_rule_type(self.QOS_RULE_TYPE)
        self.assertEqual(self.QOS_RULE_TYPE, sot.type)
        self.assertIsInstance(sot.drivers, list)

    def test_list(self):
        rule_types = list(self.operator_cloud.network.qos_rule_types())
        self.assertGreater(len(rule_types), 0)

        for rule_type in rule_types:
            self.assertIsInstance(rule_type.type, str)
