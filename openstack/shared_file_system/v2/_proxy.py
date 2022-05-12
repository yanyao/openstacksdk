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

from openstack import proxy
from openstack import resource
from openstack.shared_file_system.v2 import (
    availability_zone as _availability_zone)
from openstack.shared_file_system.v2 import (
    share_access_rule as _share_access_rule
)
from openstack.shared_file_system.v2 import (
    share_group as _share_group
)
from openstack.shared_file_system.v2 import (
    share_group_snapshot as _share_group_snapshot)
from openstack.shared_file_system.v2 import (
    share_snapshot as _share_snapshot
)
from openstack.shared_file_system.v2 import (
    storage_pool as _storage_pool
)
from openstack.shared_file_system.v2 import (
    user_message as _user_message
)
from openstack.shared_file_system.v2 import limit as _limit
from openstack.shared_file_system.v2 import share as _share


class Proxy(proxy.Proxy):

    def availability_zones(self):
        """Retrieve shared file system availability zones

        :returns: A generator of availability zone resources
        :rtype:
            :class:`~openstack.shared_file_system.v2.availability_zone.AvailabilityZone`
        """
        return self._list(_availability_zone.AvailabilityZone)

    def shares(self, details=True, **query):
        """Lists all shares with details

        :param kwargs query: Optional query parameters to be sent to limit
            the shares being returned.  Available parameters include:

            * status: Filters by a share status
            * share_server_id: The UUID of the share server.
            * metadata: One or more metadata key and value pairs as a url
              encoded dictionary of strings.
            * extra_specs: The extra specifications as a set of one or more
              key-value pairs.
            * share_type_id: The UUID of a share type to query resources by.
            * name: The user defined name of the resource to filter resources
              by.
            * snapshot_id: The UUID of the share’s base snapshot to filter
              the request based on.
            * host: The host name of the resource to query with.
            * share_network_id: The UUID of the share network to filter
              resources by.
            * project_id: The ID of the project that owns the resource.
            * is_public: A boolean query parameter that, when set to true,
              allows retrieving public resources that belong to
              all projects.
            * share_group_id: The UUID of a share group to filter resource.
            * export_location_id: The export location UUID that can be used
              to filter shares or share instances.
            * export_location_path: The export location path that can be used
              to filter shares or share instances.
            * name~: The name pattern that can be used to filter shares, share
              snapshots, share networks or share groups.
            * description~: The description pattern that can be used to filter
              shares, share snapshots, share networks or share groups.
            * with_count: Whether to show count in API response or not,
              default is False.
            * limit: The maximum number of shares to return.
            * offset: The offset to define start point of share or share group
              listing.
            * sort_key: The key to sort a list of shares.
            * sort_dir: The direction to sort a list of shares. A valid value
              is asc, or desc.

        :returns: Details of shares resources
        :rtype: :class:`~openstack.shared_file_system.v2.share.Share`
        """
        base_path = '/shares/detail' if details else None
        return self._list(_share.Share, base_path=base_path, **query)

    def get_share(self, share_id):
        """Lists details of a single share

        :param share: The ID of the share to get
        :returns: Details of the identified share
        :rtype: :class:`~openstack.shared_file_system.v2.share.Share`
        """
        return self._get(_share.Share, share_id)

    def delete_share(self, share, ignore_missing=True):
        """Deletes a single share

        :param share: The ID of the share to delete
        :returns: Result of the ``delete``
        :rtype: ``None``
        """
        self._delete(_share.Share, share,
                     ignore_missing=ignore_missing)

    def update_share(self, share_id, **attrs):
        """Updates details of a single share.

        :param share: The ID of the share to update
        :param dict attrs: The attributes to update on the share
        :returns: the updated share
        :rtype: :class:`~openstack.shared_file_system.v2.share.Share`
        """
        return self._update(_share.Share, share_id, **attrs)

    def create_share(self, **attrs):
        """Creates a share from attributes

        :returns: Details of the new share
        :param dict attrs: Attributes which will be used to create
            a :class:`~openstack.shared_file_system.v2.shares.Shares`,
            comprised of the properties on the Shares class. 'size' and 'share'
            are required to create a share.
        :rtype: :class:`~openstack.shared_file_system.v2.share.Share`
        """
        return self._create(_share.Share, **attrs)

    def revert_share_to_snapshot(self, share_id, snapshot_id):
        """Reverts a share to the specified snapshot, which must be
            the most recent one known to manila.

        :param share_id: The ID of the share to revert
        :param snapshot_id: The ID of the snapshot to revert to
        :returns: Result of the ``revert``
        :rtype: ``None``
        """
        res = self._get(_share.Share, share_id)
        res.revert_to_snapshot(self, snapshot_id)

    def share_groups(self, **query):
        """Lists all share groups.

        :param kwargs query: Optional query parameters to be sent to limit
            the share groups being returned.  Available parameters include:

            * status: Filters by a share group status.
            * name: The user defined name of the resource to filter resources
                by.
            * description: The user defined description text that can be used
                to filter resources.
            * project_id: The project ID of the user or service.
            * share_server_id: The UUID of the share server.
            * snapshot_id: The UUID of the share’s base snapshot to filter
                the request based on.
            * host: The host name for the back end.
            * share_network_id: The UUID of the share network to filter
                resources by.
            * share_group_type_id: The share group type ID to filter
                share groups.
            * share_group_snapshot_id: The source share group snapshot ID to
                list the share group.
            * share_types: A list of one or more share type IDs. Allows
                filtering share groups.
            * limit: The maximum number of share groups members to return.
            * offset: The offset to define start point of share or share
                group listing.
            * sort_key: The key to sort a list of shares.
            * sort_dir: The direction to sort a list of shares
            * name~: The name pattern that can be used to filter shares,
                share snapshots, share networks or share groups.
            * description~: The description pattern that can be used to
                filter shares, share snapshots, share networks or share groups.

        :returns: A generator of manila share group resources
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_group.ShareGroup`
        """
        return self._list(
            _share_group.ShareGroup, **query)

    def get_share_group(self, share_group_id):
        """Lists details for a share group.

        :param share: The ID of the share group to get
        :returns: Details of the identified share group
        :rtype: :class:`~openstack.shared_file_system.v2.
                                    share_group.ShareGroup`
        """
        return self._get(_share_group.ShareGroup, share_group_id)

    def find_share_group(self, name_or_id, ignore_missing=True):
        """Finds a single share group

        :param name_or_id: The name or ID of a share group.
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be
            raised when the resource does not exist.
            When set to ``True``, None will be returned when
            attempting to find a nonexistent resource.
        :returns: One :class:`~openstack.shared_file_system.v2.
                                        share_group.ShareGroup`
                                        or None
        """
        return self._find(_share_group.ShareGroup, name_or_id,
                          ignore_missing=ignore_missing)

    def create_share_group(self, **attrs):
        """Creates a share group from attributes

        :returns: Details of the new share group
        :rtype: :class:`~openstack.shared_file_system.v2.
                                    share_group.ShareGroup`
        """
        return self._create(_share_group.ShareGroup, **attrs)

    def update_share_group(self, share_group_id, **kwargs):
        """Updates details of a single share group

        :param share: The ID of the share group
        :returns: Updated details of the identified share group
        :rtype: :class:`~openstack.shared_file_system.v2.
                                    share_group.ShareGroup`
        """
        return self._update(
            _share_group.ShareGroup, share_group_id, **kwargs)

    def delete_share_group(self, share_group_id, ignore_missing=True):
        """Deletes a single share group

        :param share: The ID of the share group
        :returns: Result of the "delete" on share group
        :rtype: :class:`~openstack.shared_file_system.v2.
                                    share_group.ShareGroup`
        """
        return self._delete(
            _share_group.ShareGroup, share_group_id,
            ignore_missing=ignore_missing)

    def wait_for_status(self, res, status='active', failures=None,
                        interval=2, wait=120):
        """Wait for a resource to be in a particular status.
        :param res: The resource to wait on to reach the specified status.
            The resource must have a ``status`` attribute.
        :type resource: A :class:`~openstack.resource.Resource` object.
        :param status: Desired status.
        :param failures: Statuses that would be interpreted as failures.
        :type failures: :py:class:`list`
        :param interval: Number of seconds to wait before to consecutive
            checks. Default to 2.
        :param wait: Maximum number of seconds to wait before the change.
            Default to 120.
        :returns: The resource is returned on success.
        :raises: :class:`~openstack.exceptions.ResourceTimeout` if transition
            to the desired status failed to occur in specified seconds.
        :raises: :class:`~openstack.exceptions.ResourceFailure` if the resource
            has transited to one of the failure statuses.
        :raises: :class:`~AttributeError` if the resource does not have a
            ``status`` attribute.
        """
        failures = [] if failures is None else failures
        return resource.wait_for_status(
            self, res, status, failures, interval, wait)

    def storage_pools(self, details=True, **query):
        """Lists all back-end storage pools with details

        :param kwargs query: Optional query parameters to be sent to limit
            the storage pools being returned.  Available parameters include:

            * pool_name: The pool name for the back end.
            * host_name: The host name for the back end.
            * backend_name: The name of the back end.
            * capabilities: The capabilities for the storage back end.
            * share_type: The share type name or UUID.
        :returns: A generator of manila storage pool resources
        :rtype:
            :class:`~openstack.shared_file_system.v2.storage_pool.StoragePool`
        """
        base_path = '/scheduler-stats/pools/detail' if details else None
        return self._list(
            _storage_pool.StoragePool, base_path=base_path, **query)

    def user_messages(self, **query):
        """List shared file system user messages

        :param kwargs query: Optional query parameters to be sent to limit
            the messages being returned.  Available parameters include:

            * action_id: The ID of the action during which the message
              was created.
            * detail_id: The ID of the message detail.
            * limit: The maximum number of shares to return.
            * message_level: The message level.
            * offset: The offset to define start point of share or share
              group listing.
            * sort_key: The key to sort a list of messages.
            * sort_dir: The direction to sort a list of shares.
            * project_id: The ID of the project for which the message
              was created.
            * request_id: The ID of the request during which the message
              was created.
            * resource_id: The UUID of the resource for which the message
              was created.
            * resource_type: The type of the resource for which the message
              was created.

        :returns: A generator of user message resources
        :rtype:
            :class:`~openstack.shared_file_system.v2.user_message.UserMessage`
        """
        return self._list(
            _user_message.UserMessage, **query)

    def get_user_message(self, message_id):
        """List details of a single user message

        :param message_id: The ID of the user message
        :returns: Details of the identified user message
        :rtype:
            :class:`~openstack.shared_file_system.v2.user_message.UserMessage`
        """
        return self._get(_user_message.UserMessage, message_id)

    def delete_user_message(self, message_id, ignore_missing=True):
        """Deletes a single user message

        :param message_id: The ID of the user message
        :returns: Result of the "delete" on the user message
        :rtype:
            :class:`~openstack.shared_file_system.v2.user_message.UserMessage`
        """
        return self._delete(
            _user_message.UserMessage, message_id,
            ignore_missing=ignore_missing)

    def limits(self, **query):
        """Lists all share limits.

        :param kwargs query: Optional query parameters to be sent to limit
            the share limits being returned.

        :returns: A generator of manila share limits resources
        :rtype: :class:`~openstack.shared_file_system.v2.limit.Limit`
        """
        return self._list(
            _limit.Limit, **query)

    def share_snapshots(self, details=True, **query):
        """Lists all share snapshots with details.

        :param kwargs query: Optional query parameters to be sent to limit
            the snapshots being returned.  Available parameters include:

            * project_id: The ID of the user or service making the API request.

        :returns: A generator of manila share snapshot resources
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_snapshot.ShareSnapshot`
        """
        base_path = '/snapshots/detail' if details else None
        return self._list(
            _share_snapshot.ShareSnapshot, base_path=base_path, **query)

    def get_share_snapshot(self, snapshot_id):
        """Lists details of a single share snapshot

        :param snapshot_id: The ID of the snapshot to get
        :returns: Details of the identified share snapshot
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_snapshot.ShareSnapshot`
        """
        return self._get(_share_snapshot.ShareSnapshot, snapshot_id)

    def create_share_snapshot(self, **attrs):
        """Creates a share snapshot from attributes

        :returns: Details of the new share snapshot
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_snapshot.ShareSnapshot`
        """
        return self._create(_share_snapshot.ShareSnapshot, **attrs)

    def update_share_snapshot(self, snapshot_id, **attrs):
        """Updates details of a single share.

        :param snapshot_id: The ID of the snapshot to update
        :pram dict attrs: The attributes to update on the snapshot
        :returns: the updated share snapshot
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_snapshot.ShareSnapshot`
        """
        return self._update(_share_snapshot.ShareSnapshot, snapshot_id,
                            **attrs)

    def delete_share_snapshot(self, snapshot_id, ignore_missing=True):
        """Deletes a single share snapshot

        :param snapshot_id: The ID of the snapshot to delete
        :returns: Result of the ``delete``
        :rtype: ``None``
        """
        self._delete(_share_snapshot.ShareSnapshot, snapshot_id,
                     ignore_missing=ignore_missing)

    def wait_for_delete(self, res, interval=2, wait=120):
        """Wait for a resource to be deleted.
        :param res: The resource to wait on to be deleted.
        :type resource: A :class:`~openstack.resource.Resource` object.
        :param interval: Number of seconds to wait before to consecutive
            checks. Default to 2.
        :param wait: Maximum number of seconds to wait before the change.
            Default to 120.
        :returns: The resource is returned on success.
        :raises: :class:`~openstack.exceptions.ResourceTimeout` if transition
                 to delete failed to occur in the specified seconds.
        """
        return resource.wait_for_delete(self, res, interval, wait)

    def access_rules(self, share, **query):
        """Lists the share access rules on a share.

        :returns: A generator of the share access rules.
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_access_rules.ShareAccessRules`
        """
        share = self._get_resource(_share.Share, share)
        return self._list(
            _share_access_rule.ShareAccessRule,
            share_id=share.id, **query)

    def get_access_rule(self, access_id):
        """List details of an access rule.

        :returns: Details of the identified access rule.
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_access_rules.ShareAccessRules`
        """
        return self._get(
            _share_access_rule.ShareAccessRule, access_id)

    def share_group_snapshots(self, details=True, **query):
        """Lists all share group snapshots.

        :param kwargs query: Optional query parameters to be sent
            to limit the share group snapshots being returned.
            Available parameters include:

            * project_id: The ID of the project that owns the resource.
            * name: The user defined name of the resource to filter resources.
            * description: The user defined description text that can be used
              to filter resources.
            * status: Filters by a share status
            * share_group_id: The UUID of a share group to filter resource.
            * limit: The maximum number of share group snapshot members
              to return.
            * offset: The offset to define start point of share or
              share group listing.
            * sort_key: The key to sort a list of shares.
            * sort_dir: The direction to sort a list of shares. A valid
              value is asc, or desc.

        :returns: Details of share group snapshots resources
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_group_snapshot.ShareGroupSnapshot`
        """
        base_path = '/share-group-snapshots/detail' if details else None
        return self._list(
            _share_group_snapshot.ShareGroupSnapshot,
            base_path=base_path, **query)

    def share_group_snapshot_members(self, group_snapshot_id):
        """Lists all share group snapshots members.

        :param group_snapshot_id: The ID of the group snapshot to get
        :returns: List of the share group snapshot members, which are
            share snapshots.
        :rtype: :dict: Attributes of the share snapshots.
        """
        res = self._get(
            _share_group_snapshot.ShareGroupSnapshot, group_snapshot_id)
        response = res.members(self)
        return response

    def get_share_group_snapshot(self, group_snapshot_id):
        """Show share group snapshot details

        :param group_snapshot_id: The ID of the group snapshot to get
        :returns: Details of the group snapshot
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_group_snapshot.ShareGroupSnapshot`
        """
        return self._get(
            _share_group_snapshot.ShareGroupSnapshot, group_snapshot_id)

    def create_share_group_snapshot(self, share_group_id, **attrs):
        """Creates a point-in-time snapshot copy of a share group.

        :returns: Details of the new snapshot
        :param dict attrs: Attributes which will be used to create
            a :class:`~openstack.shared_file_system.v2.
            share_group_snapshots.ShareGroupSnapshots`,
            'share_group_id' are required to create a share.
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_group_snapshot.ShareGroupSnapshot`
        """
        return self._create(_share_group_snapshot.ShareGroupSnapshot,
                            share_group_id=share_group_id, **attrs)

    def reset_share_group_snapshot_status(self, group_snapshot_id, status):
        """Reset share group snapshot state.

        :param group_snapshot_id: The ID of the share group snapshot to reset
        :param status: The state of the server to be set, A valid value is
            "creating", "error", "available", "deleting", "error_deleting".
        :rtype: ``None``
        """
        res = self._get(
            _share_group_snapshot.ShareGroupSnapshot, group_snapshot_id)
        res.reset_status(self, status)

    def update_share_group_snapshot(self, group_snapshot_id, **attrs):
        """Updates a share group snapshot.

        :param group_snapshot_id: The ID of the share group snapshot to update
        :param dict attrs: The attributes to update on the share group snapshot
        :returns: the updated share group snapshot
        :rtype: :class:`~openstack.shared_file_system.v2.
            share_group_snapshot.ShareGroupSnapshot`
        """
        return self._update(_share_group_snapshot.ShareGroupSnapshot,
                            group_snapshot_id, **attrs)

    def delete_share_group_snapshot(
            self, group_snapshot_id, ignore_missing=True):
        """Deletes a share group snapshot.

        :param group_snapshot_id: The ID of the share group snapshot to delete
        :rtype: ``None``
        """
        self._delete(_share_group_snapshot.ShareGroupSnapshot,
                     group_snapshot_id,
                     ignore_missing=ignore_missing)
