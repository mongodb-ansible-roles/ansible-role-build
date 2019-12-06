Ansible role for build account
==============================

Ansible role to set up build account

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-build/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-build)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `build_user` | Name of the user that will run Evergreen tasks | string | `root` | yes |

Dependencies
------------

None

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
