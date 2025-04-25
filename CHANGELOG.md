## Samba-ansible 1.1.6-1

* Modified variables for the ceph stable repo and the mon group name so they're now set directly in the group_vars file. Altered the task for creating the samba.client user to fix issue on Rocky9/Ubuntu22.