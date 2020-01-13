import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_dmesg_file(host):
    f = host.file('/etc/sudoers.d/dmesg')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_bashrc_file(host):
    f = host.file('/home/arch/.bashrc')

    assert f.exists
    assert f.user == 'arch'
    assert f.group == 'arch'


def test_bash_profile_file(host):
    f = host.file('/home/arch/.bash_profile')

    assert f.exists
    assert f.user == 'arch'
    assert f.group == 'arch'


def test_mongodb_build_system_id_file(host):
    f = host.file('/etc/mongodb-build-system-id')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
