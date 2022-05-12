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

from openstack import resource
from openstack import utils


class ShareGroupSnapshot(resource.Resource):
    resource_key = "share_group_snapshot"
    resources_key = "share_group_snapshots"
    base_path = "/share-group-snapshots"

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True
    allow_head = False

    _query_mapping = resource.QueryParameters(
        'project_id', 'all_tenants', 'name', 'description',
        'status', 'share_group_id', 'limit', 'offset',
        'sort_key', 'sort_dir'
    )

    # Share group snapshots were considered non-experimental
    # since API version 2.55
    _max_microversion = '2.55'

    #: Properties
    #: The ID of the project that owns the resource.
    project_id = resource.Body("project_id", type=str)
    #: Filters by a share group snapshot status. A valid value is creating,
    #: error, available, deleting, error_deleting.
    status = resource.Body("status", type=str)
    #: The UUID of the share group.
    share_group_id = resource.Body("share_group_id", type=str)
    #: The user defined description of the resource.
    description = resource.Body("description", type=str)
    #: The date and time stamp when the resource was created.
    created_at = resource.Body("created_at", type=str)
    #: The share group snapshot members.
    members = resource.Body("members", type=str)
    #: The snapshot size, in GiBs.
    size = resource.Body("size", type=int)
    #: NFS, CIFS, GlusterFS, HDFS, CephFS or MAPRFS.
    share_protocol = resource.Body("share_proto", type=str)
    #: The share group snapshot ID.
    # share_group_snapshot_id
    #: The UUID of the source share that was used to create the snapshot.
    share_id = resource.Body("share_id", type=str)

    def _action(self, session, body):
        """Perform ShareGroupSnapshot actions given the message body."""
        # NOTE: This is using ShareGroupSnapshot.base_path instead of
        # self.base_path as ShareGroupSnapshot instances can be acted on,
        # but the URL used is sans any additional /detail/ part.
        url = utils.urljoin(self.base_path, self.id, 'action')
        headers = {'Accept': ''}
        session.post(
            url, json=body, headers=headers,
            microversion=self._max_microversion)

    def reset_status(self, session, status):
        body = {"reset_status": {"status": status}}
        self._action(session, body)

    def members(self, session):
        url = utils.urljoin(self.base_path, self.id, 'members')
        headers = {'Accept': ''}
        response = session.get(
            url, headers=headers, microversion=self._max_microversion)
        return response.json()
