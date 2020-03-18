import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_build_account(host):
    assert host.file("/etc/sudoers.d/dmesg").exists
    assert host.file("/root/.bashrc").exists
    assert host.file("/root/.bash_profile").exists
    assert host.file("/etc/mongodb-build-system-id").exists
