Ansible role for build account
==============================

Ansible role to set up build account

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-build/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-build/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-build/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-build/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `build_user` | Name of the user that will run Evergreen tasks | string | `root` | yes |

Example Playbook
----------------

```yaml
    - hosts: all
      roles:
         - role: ansible-role-build
```

License
-------

[Apache License](LICENSE)
