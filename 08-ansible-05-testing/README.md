# Домашнее задание к занятию "08.05 Тестирование Roles"

## Подготовка к выполнению
1. Установите molecule: `pip3 install "molecule==3.4.0"` </br>
выполнено
2. Соберите локальный образ на основе [Dockerfile](./Dockerfile)</br>
выполнено

## Основная часть

Наша основная цель - настроить тестирование наших ролей. Задача: сделать сценарии тестирования для kibana, logstash. Ожидаемый результат: все сценарии успешно проходят тестирование ролей.

### Molecule

1. Запустите  `molecule test` внутри корневой директории elasticsearch-role, посмотрите на вывод команды.
```commandline
Mikhails-MacBook-Pro:elasticsearch_role mikhailrusakovich$ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
INFO     Guessed /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks as project root directory
WARNING  Computed fully qualified role name of elasticsearch_role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

INFO     Using /Users/mikhailrusakovich/.cache/ansible-lint/e3a24c/roles/elasticsearch_role symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Added ANSIBLE_ROLES_PATH=~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/Users/mikhailrusakovich/.cache/ansible-lint/e3a24c/roles
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > lint
INFO     Lint is disabled.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos7)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=centos7)
ok: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos7', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos7', 'pre_build_image': True}) 
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}) 

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'item': {'image': 'docker.io/pycontribs/centos:7', 'name': 'centos7', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 1, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/centos:7) 
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/ubuntu:latest) 

TASK [Create docker network(s)] ************************************************

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos7', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=centos7)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '118726617097.39083', 'results_file': '/Users/mikhailrusakovich/.ansible_async/118726617097.39083', 'changed': True, 'item': {'image': 'docker.io/pycontribs/centos:7', 'name': 'centos7', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '590816706326.39104', 'results_file': '/Users/mikhailrusakovich/.ansible_async/590816706326.39104', 'changed': True, 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos7]

TASK [elasticsearch_role] ******************************************************

TASK [elasticsearch_role : Fail if unsupported system detected] ****************
skipping: [centos7]
skipping: [ubuntu]

TASK [elasticsearch_role : Check files directory exists] ***********************
changed: [centos7 -> localhost]

TASK [elasticsearch_role : include_tasks] **************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/download_yum.yml for centos7
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/download_apt.yml for ubuntu

TASK [elasticsearch_role : Download Elasticsearch's rpm] ***********************
changed: [centos7 -> localhost]

TASK [elasticsearch_role : Copy Elasticsearch to managed node] *****************
changed: [centos7]

TASK [elasticsearch_role : Download Elasticsearch's deb] ***********************
changed: [ubuntu -> localhost]

TASK [elasticsearch_role : Copy Elasticsearch to manage host] ******************
changed: [ubuntu]

TASK [elasticsearch_role : include_tasks] **************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/install_yum.yml for centos7
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/install_apt.yml for ubuntu

TASK [elasticsearch_role : Install Elasticsearch] ******************************
changed: [centos7]

TASK [elasticsearch_role : Install Elasticsearch] ******************************
changed: [ubuntu]

TASK [elasticsearch_role : Configure Elasticsearch] ****************************
changed: [ubuntu]
changed: [centos7]

RUNNING HANDLER [elasticsearch_role : restart Elasticsearch] *******************
skipping: [centos7]
skipping: [ubuntu]

PLAY RECAP *********************************************************************
centos7                    : ok=8    changed=5    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
ubuntu                     : ok=7    changed=4    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

INFO     Running default > idempotence

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos7]

TASK [elasticsearch_role] ******************************************************

TASK [elasticsearch_role : Fail if unsupported system detected] ****************
skipping: [centos7]
skipping: [ubuntu]

TASK [elasticsearch_role : Check files directory exists] ***********************
ok: [centos7 -> localhost]

TASK [elasticsearch_role : include_tasks] **************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/download_yum.yml for centos7
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/download_apt.yml for ubuntu

TASK [elasticsearch_role : Download Elasticsearch's rpm] ***********************
ok: [centos7 -> localhost]

TASK [elasticsearch_role : Copy Elasticsearch to managed node] *****************
ok: [centos7]

TASK [elasticsearch_role : Download Elasticsearch's deb] ***********************
ok: [ubuntu -> localhost]

TASK [elasticsearch_role : Copy Elasticsearch to manage host] ******************
ok: [ubuntu]

TASK [elasticsearch_role : include_tasks] **************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/install_yum.yml for centos7
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/install_apt.yml for ubuntu

TASK [elasticsearch_role : Install Elasticsearch] ******************************
ok: [centos7]

TASK [elasticsearch_role : Install Elasticsearch] ******************************
ok: [ubuntu]

TASK [elasticsearch_role : Configure Elasticsearch] ****************************
ok: [centos7]
ok: [ubuntu]

PLAY RECAP *********************************************************************
centos7                    : ok=8    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
ubuntu                     : ok=7    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Idempotence completed successfully.
INFO     Running default > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running default > verify
INFO     Running Ansible Verifier

PLAY [Verify] ******************************************************************

TASK [Example assertion] *******************************************************
ok: [centos7] => {
    "changed": false,
    "msg": "All assertions passed"
}
ok: [ubuntu] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
centos7                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
ubuntu                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos7)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=centos7)
changed: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory


```
2. Перейдите в каталог с ролью kibana-role и создайте сценарий тестирования по умолчанию при помощи `molecule init scenario --driver-name docker`.
```commandline
Mikhails-MacBook-Pro:kibana-role mikhailrusakovich$ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
INFO     Guessed /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role as project root directory
WARNING  Computed fully qualified role name of kibana-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

INFO     Using /Users/mikhailrusakovich/.cache/ansible-lint/73b008/roles/kibana-role symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Added ANSIBLE_ROLES_PATH=~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/Users/mikhailrusakovich/.cache/ansible-lint/73b008/roles
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > lint
INFO     Lint is disabled.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=centos)
ok: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True}) 
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}) 

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'item': {'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 1, 'ansible_index_var': 'i'})
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 2, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *****************************
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/centos:7) 
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/ubuntu:latest) 

TASK [Create docker network(s)] ************************************************

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '335064310385.44105', 'results_file': '/Users/mikhailrusakovich/.ansible_async/335064310385.44105', 'changed': True, 'item': {'image': 'docker.io/pycontribs/centos:8', 'name': 'instance', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '209022976054.44126', 'results_file': '/Users/mikhailrusakovich/.ansible_async/209022976054.44126', 'changed': True, 'item': {'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '785434300828.44147', 'results_file': '/Users/mikhailrusakovich/.ansible_async/785434300828.44147', 'changed': True, 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos]

TASK [Include kibana-role] *****************************************************

TASK [kibana-role : Fail if unsupported system detected] ***********************
skipping: [centos]
skipping: [ubuntu]

TASK [kibana-role : Check files directory exists] ******************************
ok: [centos -> localhost]

TASK [kibana-role : include_tasks] *********************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role/tasks/download_yum.yml for centos

TASK [kibana-role : Download Kibana's rpm] *************************************
ok: [centos -> localhost]

TASK [kibana-role : Copy Kibana to managed node] *******************************
changed: [centos]

TASK [kibana-role : Download Kibana's deb] *************************************
ok: [ubuntu -> localhost]

TASK [kibana-role : Copy Kibana to manage host] ********************************
changed: [ubuntu]

TASK [kibana-role : include_tasks] *********************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role/tasks/install_yum.yml for centos
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role/tasks/install_apt.yml for ubuntu

TASK [kibana-role : Install Kibana] ********************************************
changed: [centos]

TASK [kibana-role : Install Kibana] ********************************************
changed: [ubuntu]

TASK [kibana-role : Configure kibana] ******************************************
changed: [centos]
changed: [ubuntu]

RUNNING HANDLER [kibana-role : restart kibana] *********************************
skipping: [centos]
skipping: [ubuntu]

PLAY RECAP *********************************************************************
centos                     : ok=8    changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0
ubuntu                     : ok=7    changed=3    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0

CRITICAL Ansible return code was 2, command was: ['ansible-playbook', '--inventory', '/Users/mikhailrusakovich/.cache/molecule/kibana-role/default/inventory', '--skip-tags', 'molecule-notest,notest', '/Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role/molecule/default/converge.yml']
WARNING  An error occurred during the test sequence action: 'converge'. Cleaning up.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=instance)
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
changed: [localhost] => (item=instance)
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory


```
4. Добавьте несколько assert'ов в verify.yml файл, для проверки работоспособности kibana-role (проверка, что web отвечает, проверка логов, etc). Запустите тестирование роли повторно и проверьте, что оно прошло успешно.
```commandline
---
# This is an example playbook to execute Ansible tests.

- name: Verify
  hosts: all
  gather_facts: false
  tasks:
  - name: Example assertion
    assert:
      that: true
  - name: check if port 5601 is open
    ansible.builtin.wait_for:
      port: 5601
  - name: Get Kibana health status
    uri:
      url: "http://127.0.0.1:5601/api/task_manager/_health"
    register: kibana_status
  - name: Check if Kibana is health
    assert:
      that: kibana_status.json.status == "OK"
      quiet: true

```
5. Повторите шаги 2-4 для filebeat-role.
```commandline
Mikhails-MacBook-Pro:filebeat-role mikhailrusakovich$ molecule test
INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun...
INFO     Guessed /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role as project root directory
WARNING  Computed fully qualified role name of filebeat-role does not follow current galaxy requirements.
Please edit meta/main.yml and assure we can correctly determine full role name:

galaxy_info:
role_name: my_name  # if absent directory name hosting role is used instead
namespace: my_galaxy_namespace  # if absent, author is used instead

Namespace: https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations
Role: https://galaxy.ansible.com/docs/contributing/creating_role.html#role-names

As an alternative, you can add 'role-name' to either skip_list or warn_list.

INFO     Using /Users/mikhailrusakovich/.cache/ansible-lint/64c06e/roles/filebeat-role symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Added ANSIBLE_ROLES_PATH=~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:/Users/mikhailrusakovich/.cache/ansible-lint/64c06e/roles
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > lint
INFO     Lint is disabled.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=centos)
ok: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True}) 
skipping: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}) 

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'item': {'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 1, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/centos:7) 
skipping: [localhost] => (item=molecule_local/docker.io/pycontribs/ubuntu:latest) 

TASK [Create docker network(s)] ************************************************

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True})
ok: [localhost] => (item={'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '712656116770.66776', 'results_file': '/Users/mikhailrusakovich/.ansible_async/712656116770.66776', 'changed': True, 'item': {'image': 'docker.io/pycontribs/centos:7', 'name': 'centos', 'pre_build_image': True}, 'ansible_loop_var': 'item'})
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '341739107920.66798', 'results_file': '/Users/mikhailrusakovich/.ansible_async/341739107920.66798', 'changed': True, 'item': {'image': 'docker.io/pycontribs/ubuntu:latest', 'name': 'ubuntu', 'pre_build_image': True}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=2    unreachable=0    failed=0    skipped=4    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [ubuntu]
ok: [centos]

TASK [Include filebeat-role] ***************************************************

TASK [filebeat-role : Fail if unsupported system detected] *********************
skipping: [centos]
skipping: [ubuntu]

TASK [filebeat-role : Check files directory exists] ****************************
ok: [centos -> localhost]

TASK [filebeat-role : include_tasks] *******************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/tasks/download_yum.yml for centos
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/tasks/download_apt.yml for ubuntu

TASK [filebeat-role : Download Filebeat's rpm] *********************************
ok: [centos -> localhost]

TASK [filebeat-role : Copy Filebeat to managed node] ***************************
changed: [centos]

TASK [filebeat-role : Download Filebeat's deb] *********************************
ok: [ubuntu -> localhost]

TASK [filebeat-role : Copy Filebeat to manage host] ****************************
changed: [ubuntu]

TASK [filebeat-role : include_tasks] *******************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/tasks/install_yum.yml for centos
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/tasks/install_apt.yml for ubuntu

TASK [filebeat-role : Install Filebeat] ****************************************
changed: [centos]

TASK [filebeat-role : Install Filebeat] ****************************************
changed: [ubuntu]

TASK [filebeat-role : Configure Filebeat] **************************************
changed: [centos]
changed: [ubuntu]

TASK [filebeat-role : Set filebeat systemwork] *********************************
changed: [ubuntu]
changed: [centos]

TASK [filebeat-role : Load Kibana dashboard] ***********************************
FAILED - RETRYING: [ubuntu]: Load Kibana dashboard (3 retries left).
FAILED - RETRYING: [centos]: Load Kibana dashboard (3 retries left).
FAILED - RETRYING: [ubuntu]: Load Kibana dashboard (2 retries left).
FAILED - RETRYING: [centos]: Load Kibana dashboard (2 retries left).
FAILED - RETRYING: [ubuntu]: Load Kibana dashboard (1 retries left).
FAILED - RETRYING: [centos]: Load Kibana dashboard (1 retries left).
fatal: [ubuntu]: FAILED! => {"attempts": 3, "changed": false, "cmd": ["filebeat", "setup"], "delta": "0:00:00.200043", "end": "2022-03-02 01:08:18.574312", "msg": "non-zero return code", "rc": 1, "start": "2022-03-02 01:08:18.374269", "stderr": "Exiting: couldn't connect to any of the configured Elasticsearch hosts. Errors: [error connecting to Elasticsearch at http://localhost:9200: Get \"http://localhost:9200\": dial tcp [::1]:9200: connect: cannot assign requested address]", "stderr_lines": ["Exiting: couldn't connect to any of the configured Elasticsearch hosts. Errors: [error connecting to Elasticsearch at http://localhost:9200: Get \"http://localhost:9200\": dial tcp [::1]:9200: connect: cannot assign requested address]"], "stdout": "", "stdout_lines": []}
fatal: [centos]: FAILED! => {"attempts": 3, "changed": false, "cmd": ["filebeat", "setup"], "delta": "0:00:00.410820", "end": "2022-03-02 01:08:19.135639", "msg": "non-zero return code", "rc": 1, "start": "2022-03-02 01:08:18.724819", "stderr": "Exiting: couldn't connect to any of the configured Elasticsearch hosts. Errors: [error connecting to Elasticsearch at http://localhost:9200: Get \"http://localhost:9200\": dial tcp [::1]:9200: connect: cannot assign requested address]", "stderr_lines": ["Exiting: couldn't connect to any of the configured Elasticsearch hosts. Errors: [error connecting to Elasticsearch at http://localhost:9200: Get \"http://localhost:9200\": dial tcp [::1]:9200: connect: cannot assign requested address]"], "stdout": "", "stdout_lines": []}

RUNNING HANDLER [filebeat-role : restart filebeat] *****************************

PLAY RECAP *********************************************************************
centos                     : ok=9    changed=4    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0
ubuntu                     : ok=8    changed=4    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0

CRITICAL Ansible return code was 2, command was: ['ansible-playbook', '--inventory', '/Users/mikhailrusakovich/.cache/molecule/filebeat-role/default/inventory', '--skip-tags', 'molecule-notest,notest', '/Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/molecule/default/converge.yml']
WARNING  An error occurred during the test sequence action: 'converge'. Cleaning up.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=centos)
changed: [localhost] => (item=ubuntu)

TASK [Delete docker networks(s)] ***********************************************

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory

```
6. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

### Tox

1. Запустите `docker run --privileged=True -v <path_to_repo>:/opt/elasticsearch-role -w /opt/elasticsearch-role -it <image_name> /bin/bash`, где path_to_repo - путь до корня репозитория с elasticsearch-role на вашей файловой системе.
2. Внутри контейнера выполните команду `tox`, посмотрите на вывод.
```
py36-ansible28 create: /opt/elasticsearch-role/.tox/py36-ansible28
py36-ansible28 installdeps: -rtest-requirements.txt, ansible<2.9
py36-ansible28 installed: ansible==2.8.20,ansible-compat==1.0.0,ansible-lint==5.4.0,arrow==1.2.2,bcrypt==3.2.0,binaryornot==0.4.4,bracex==2.2.1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2021.10.8,cffi==1.15.0,chardet==4.0.0,charset-normalizer==2.0.12,click==8.0.4,click-help-colors==0.9.1,colorama==0.4.4,commonmark==0.9.1,cookiecutter==1.7.3,cryptography==36.0.1,dataclasses==0.8,distro==1.7.0,docker==5.0.3,enrich==1.2.7,idna==3.3,importlib-metadata==4.8.3,Jinja2==3.0.3,jinja2-time==0.2.0,MarkupSafe==2.0.1,molecule==3.4.0,molecule-docker==1.1.0,packaging==21.3,paramiko==2.9.2,pathspec==0.9.0,pluggy==0.13.1,poyo==0.5.0,pycparser==2.21,Pygments==2.11.2,PyNaCl==1.5.0,pyparsing==3.0.7,python-dateutil==2.8.2,python-slugify==6.1.1,PyYAML==5.4.1,requests==2.27.1,rich==11.2.0,ruamel.yaml==0.17.21,ruamel.yaml.clib==0.2.6,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.0.1,text-unidecode==1.3,typing_extensions==4.1.1,urllib3==1.26.8,wcmatch==8.3,websocket-client==1.3.1,yamllint==1.26.3,zipp==3.6.0
py36-ansible28 run-test-pre: PYTHONHASHSEED='1064376408'
[root@7d0d92e7a13b elasticsearch-role]# tox
py36-ansible28 create: /opt/elasticsearch-role/.tox/py36-ansible28
py36-ansible28 installdeps: -rtest-requirements.txt, ansible<2.9
py36-ansible28 installed: ansible==2.8.20,ansible-compat==1.0.0,ansible-lint==5.4.0,arrow==1.2.2,bcrypt==3.2.0,binaryornot==0.4.4,bracex==2.2.1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2021.10.8,cffi==1.15.0,chardet==4.0.0,charset-normalizer==2.0.12,click==8.0.4,click-help-colors==0.9.1,colorama==0.4.4,commonmark==0.9.1,cookiecutter==1.7.3,cryptography==36.0.1,dataclasses==0.8,distro==1.7.0,docker==5.0.3,enrich==1.2.7,idna==3.3,importlib-metadata==4.8.3,Jinja2==3.0.3,jinja2-time==0.2.0,MarkupSafe==2.0.1,molecule==3.4.0,molecule-docker==1.1.0,packaging==21.3,paramiko==2.9.2,pathspec==0.9.0,pluggy==0.13.1,poyo==0.5.0,pycparser==2.21,Pygments==2.11.2,PyNaCl==1.5.0,pyparsing==3.0.7,python-dateutil==2.8.2,python-slugify==6.1.1,PyYAML==5.4.1,requests==2.27.1,rich==11.2.0,ruamel.yaml==0.17.21,ruamel.yaml.clib==0.2.6,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.0.1,text-unidecode==1.3,typing_extensions==4.1.1,urllib3==1.26.8,wcmatch==8.3,websocket-client==1.3.1,yamllint==1.26.3,zipp==3.6.0
py36-ansible28 run-test-pre: PYTHONHASHSEED='3526761901'
py36-ansible30 create: /opt/elasticsearch-role/.tox/py36-ansible30
___________________________________________________________________________________ summary ___________________________________________________________________________________
  py36-ansible28: commands succeeded

```
3. Добавьте файл `tox.ini` в корень репозитория каждой своей роли.
```
[tox]
minversion = 1.8
basepython = python3.6
envlist = py{36,39}-ansible{28,30}
skipsdist = true

[testenv]
deps =
    -r test-requirements.txt
    ansible28: ansible<2.9
    ansible29: ansible<2.10
    ansible210: ansible<3.0
    ansible30: ansible<3.1
```
4. Создайте облегчённый сценарий для `molecule`. Проверьте его на исполнимость.
```commandline
---
dependency:
  name: galaxy
driver:
  name: podman
platforms:
  - name: instance
    image: docker.io/pycontribs/centos:7
    pre_build_image: true
provisioner:
  name: ansible
verifier:
  name: ansible
scenario:
  test_sequence:
    - destroy
    - create
    - converge
    - destroy

```
5. Пропишите правильную команду в `tox.ini` для того чтобы запускался облегчённый сценарий.
```commandline
commands =
    {posargs:molecule test -s alternative --destroy=always}
```
6. Запустите `docker` контейнер так, чтобы внутри оказались обе ваши роли.
```commandline
[root@7d0d92e7a13b elasticsearch-role]# tox
py36-ansible28 installed: ansible==2.8.20,ansible-compat==1.0.0,ansible-lint==5.4.0,arrow==1.2.2,bcrypt==3.2.0,binaryornot==0.4.4,bracex==2.2.1,cached-property==1.5.2,Cerberus==1.3.2,certifi==2021.10.8,cffi==1.15.0,chardet==4.0.0,charset-normalizer==2.0.12,click==8.0.4,click-help-colors==0.9.1,colorama==0.4.4,commonmark==0.9.1,cookiecutter==1.7.3,cryptography==36.0.1,dataclasses==0.8,distro==1.7.0,docker==5.0.3,enrich==1.2.7,idna==3.3,importlib-metadata==4.8.3,Jinja2==3.0.3,jinja2-time==0.2.0,MarkupSafe==2.0.1,molecule==3.4.0,molecule-docker==1.1.0,packaging==21.3,paramiko==2.9.2,pathspec==0.9.0,pluggy==0.13.1,poyo==0.5.0,pycparser==2.21,Pygments==2.11.2,PyNaCl==1.5.0,pyparsing==3.0.7,python-dateutil==2.8.2,python-slugify==6.1.1,PyYAML==5.4.1,requests==2.27.1,rich==11.2.0,ruamel.yaml==0.17.21,ruamel.yaml.clib==0.2.6,selinux==0.2.1,six==1.16.0,subprocess-tee==0.3.5,tenacity==8.0.1,text-unidecode==1.3,typing_extensions==4.1.1,urllib3==1.26.8,wcmatch==8.3,websocket-client==1.3.1,yamllint==1.26.3,zipp==3.6.0
py36-ansible28 run-test-pre: PYTHONHASHSEED='3173382637'
py36-ansible30 create: /opt/elasticsearch-role/.tox/py36-ansible30
ERROR: cowardly refusing to delete `envdir` (it does not look like a virtualenv): /opt/elasticsearch-role/.tox/py36-ansible30
___________________________________________________________________________________ summary ___________________________________________________________________________________
  py36-ansible28: commands succeeded

```
7. Зайдти поочерёдно в каждую из них и запустите команду `tox`. Убедитесь, что всё отработало успешно.
8. Добавьте новый тег на коммит с рабочим сценарием в соответствии с семантическим версионированием.

После выполнения у вас должно получится два сценария molecule и один tox.ini файл в каждом репозитории. Ссылки на репозитории являются ответами на домашнее задание. Не забудьте указать в ответе теги решений Tox и Molecule заданий.

## Необязательная часть

1. Проделайте схожие манипуляции для создания роли logstash.
2. Создайте дополнительный набор tasks, который позволяет обновлять стек ELK.
3. В ролях добавьте тестирование в раздел `verify.yml`. Данный раздел должен проверять, что logstash через команду `logstash -e 'input { stdin { } } output { stdout {} }'`  отвечате адекватно.
4. Создайте сценарий внутри любой из своих ролей, который умеет поднимать весь стек при помощи всех ролей.
5. Убедитесь в работоспособности своего стека. Создайте отдельный verify.yml, который будет проверять работоспособность интеграции всех инструментов между ними.
6. Выложите свои roles в репозитории. В ответ приведите ссылки.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
