Using OpenStack Shared File Systems
===================================

Before working with the Shared File System service, you'll need to create a
connection to your OpenStack cloud by following the :doc:`connect` user
guide. This will provide you with the ``conn`` variable used in the examples
below.

.. contents:: Table of Contents
   :local:


List Availability Zones
-----------------------

A Shared File System service **availability zone** is a failure domain for
your shared file systems. You may create a shared file system (referred
to simply as **shares**) in a given availability zone, and create replicas
of the share in other availability zones.

.. literalinclude:: ../examples/shared_file_system/availability_zones.py
   :pyobject: list_availability_zones


List Share Group Snapshots
--------------------------

A share group snapshot is a point-in-time, read-only copy of the data that is
contained in a share group. You can list all share group snapshots

.. literalinclude:: ../examples/shared_file_system/share_group_snapshots.py
   :pyobject: list_share_group_snapshots


Get Share Group Snapshot
------------------------

Show share group snapshot details

.. literalinclude:: ../examples/shared_file_system/share_group_snapshots.py
   :pyobject: get_share_group_snapshot


List Share Group Snapshot Members
---------------------------------

Lists all share group snapshots members.

.. literalinclude:: ../examples/shared_file_system/share_group_snapshots.py
   :pyobject: share_group_snapshot_members


Create Share Group Snapshot
---------------------------

Creates a snapshot from a share.

.. literalinclude:: ../examples/shared_file_system/share_group_snapshots.py
   :pyobject: create_share_group_snapshot


Reset Share Group Snapshot
---------------------------

Reset share group snapshot state.

.. literalinclude:: ../examples/shared_file_system/share_group_snapshots.py
   :pyobject: reset_share_group_snapshot_status


Update Share Group Snapshot
---------------------------

Updates a share group snapshot.

.. literalinclude:: ../examples/shared_file_system/share_group_snapshots.py
   :pyobject: update_share_group_snapshot


Delete Share Group Snapshot
---------------------------

Deletes a share group snapshot.

.. literalinclude:: ../examples/shared_file_system/share_group_snapshots.py
   :pyobject: delete_share_group_snapshot
