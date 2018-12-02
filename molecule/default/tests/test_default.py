import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mariadb_is_installed(host):
    package = host.package('mariadb')

    assert package.is_installed


def test_mariadb_server_is_installed(host):
    package = host.package('mariadb-server')

    assert package.is_installed


def test_python2_pymysql_is_installed(host):
    package = host.package('python2-PyMySQL')

    assert package.is_installed


def test_mariadb_openstack_conf_file(host):
    f = host.file('/etc/my.cnf.d/openstack.cnf')

    assert f.exists


def test_mariadb_running_and_enabled(host):
    service = host.service('mariadb')

    assert service.is_running
    assert service.is_enabled
