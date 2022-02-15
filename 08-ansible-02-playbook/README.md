# Домашнее задание к занятию "08.02 Работа с Playbook"

## Подготовка к выполнению
1. Создайте свой собственный (или используйте старый) публичный репозиторий на github с произвольным именем.
2. Скачайте [playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.
3. Подготовьте хосты в соотвтествии с группами из предподготовленного playbook. 
4. Скачайте дистрибутив [java](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) и положите его в директорию `playbook/files/`. 

## Основная часть
1. Приготовьте свой собственный inventory файл `prod.yml`.
```commandline
---
elasticsearch:
  hosts:
    elasticsearch:
      ansible_connection: docker
kibana:
  hosts:
    kibana:
      ansible_connection: docker

```
2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает kibana.
```commandline
name: Install kibana
  hosts: kibana
  tasks:
    - name: Upload tar.gz kibana from remote URL
      get_url:
        url: "https://artifacts.elastic.co/downloads/kibana/kibana-{{ kibana_version }}-linux-x86_64.tar.gz"
        dest: "/tmp/kibana-{{ elastic_version }}-linux-x86_64.tar.gz"
        mode: 0755
        timeout: 60
        force: true
        validate_certs: false
        register: get_kibana
        until: get_kibana is succeeded
        tags: kibana
    - name: Create directrory for kibana
      file:
        state: directory
        path: "{{ kibana_home }}"
      tags: kibana
    - name: Extract Kibana in the installation directory
      #become: true
      unarchive:
        copy: false
        src: "/tmp/kibana-{{ kibana_version }}-linux-x86_64.tar.gz"
        dest: "{{ kibana_home }}"
        extra_opts: [--strip-components=1]
        creates: "{{ kibana_home }}/bin/kibana"
      tags:
          - skip_ansible_lint
          - kibana
    - name: Set environment Kibana
      #become: true
      template:
        src: templates/kib.sh.j2
        dest: /etc/profile.d/kib.sh
      tags: kibana
```
3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`. </br>
выполнено
4. Tasks должны: скачать нужной версии дистрибутив, выполнить распаковку в выбранную директорию, сгенерировать конфигурацию с параметрами. </br>
выполнено
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.</br>
выполнено
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
```commandline
Mikhails-MacBook-Pro:playbook mikhailrusakovich$ ansible-playbook -i inventory/prod.yml site.yml --check
[WARNING]: Found both group and host with same name: elasticsearch
[WARNING]: Found both group and host with same name: kibana

PLAY [Install Java] ***********************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Set facts for Java 11 vars] *********************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Upload .tar.gz file containing binaries from local storage] *************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Ensure installation dir exists] *****************************************************************************************************************************************
ok: [kibana]
ok: [elasticsearch]

TASK [Extract java in the installation directory] *****************************************************************************************************************************
skipping: [kibana]
skipping: [elasticsearch]

TASK [Export environment variables] *******************************************************************************************************************************************
changed: [kibana]
changed: [elasticsearch]

PLAY [Install Elasticsearch] **************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [elasticsearch]

TASK [Upload tar.gz Elasticsearch from remote URL] ****************************************************************************************************************************
changed: [elasticsearch]

TASK [Create directrory for Elasticsearch] ************************************************************************************************************************************
changed: [elasticsearch]

TASK [Extract Elasticsearch in the installation directory] ********************************************************************************************************************
An exception occurred during task execution. To see the full traceback, use -vvv. The error was: NoneType: None
fatal: [elasticsearch]: FAILED! => {"changed": false, "msg": "dest '/opt/elastic/7.10.1' must be an existing dir"}

PLAY RECAP ********************************************************************************************************************************************************************
elasticsearch              : ok=8    changed=3    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0   
kibana                     : ok=5    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   


```
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
```commandline
Mikhails-MacBook-Pro:playbook mikhailrusakovich$ ansible-playbook -i inventory/prod.yml site.yml --diff
[WARNING]: Found both group and host with same name: elasticsearch
[WARNING]: Found both group and host with same name: kibana

PLAY [Install Java] ***********************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [kibana]
ok: [elasticsearch]

TASK [Set facts for Java 11 vars] *********************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Upload .tar.gz file containing binaries from local storage] *************************************************************************************************************
ok: [kibana]
ok: [elasticsearch]

TASK [Ensure installation dir exists] *****************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Extract java in the installation directory] *****************************************************************************************************************************
skipping: [elasticsearch]
skipping: [kibana]

TASK [Export environment variables] *******************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

PLAY [Install Elasticsearch] **************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [elasticsearch]

TASK [Upload tar.gz Elasticsearch from remote URL] ****************************************************************************************************************************
ok: [elasticsearch]

TASK [Create directrory for Elasticsearch] ************************************************************************************************************************************
ok: [elasticsearch]

TASK [Extract Elasticsearch in the installation directory] ********************************************************************************************************************
skipping: [elasticsearch]

TASK [Set environment Elastic] ************************************************************************************************************************************************
ok: [elasticsearch]

PLAY [Install kibana] *********************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [kibana]

TASK [Upload tar.gz kibana from remote URL] ***********************************************************************************************************************************
fatal: [kibana]: FAILED! => {"changed": false, "msg": "Unsupported parameters for (get_url) module: register, tags, until. Supported parameters include: force (thirsty), attributes (attr), url_password (password), owner, client_key, group, use_gssapi, unsafe_writes, serole, validate_certs, setype, unredirected_headers, client_cert, dest, selevel, force_basic_auth, sha256sum, http_agent, url_username (username), use_proxy, url, checksum, seuser, headers, mode, timeout, backup, tmp_dest."}

PLAY RECAP ********************************************************************************************************************************************************************
elasticsearch              : ok=9    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana                     : ok=6    changed=0    unreachable=0    failed=1    skipped=1    rescued=0    ignored=0   

Mikhails-MacBook-Pro:playbook mikhailrusakovich$ ansible-playbook -i inventory/prod.yml site.yml --diff
[WARNING]: Found both group and host with same name: kibana
[WARNING]: Found both group and host with same name: elasticsearch

PLAY [Install Java] ***********************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Set facts for Java 11 vars] *********************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Upload .tar.gz file containing binaries from local storage] *************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Ensure installation dir exists] *****************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

TASK [Extract java in the installation directory] *****************************************************************************************************************************
skipping: [elasticsearch]
skipping: [kibana]

TASK [Export environment variables] *******************************************************************************************************************************************
ok: [elasticsearch]
ok: [kibana]

PLAY [Install Elasticsearch] **************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [elasticsearch]

TASK [Upload tar.gz Elasticsearch from remote URL] ****************************************************************************************************************************
ok: [elasticsearch]

TASK [Create directrory for Elasticsearch] ************************************************************************************************************************************
ok: [elasticsearch]

TASK [Extract Elasticsearch in the installation directory] ********************************************************************************************************************
skipping: [elasticsearch]

TASK [Set environment Elastic] ************************************************************************************************************************************************
ok: [elasticsearch]

PLAY [Install kibana] *********************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [kibana]

TASK [Upload tar.gz kibana from remote URL] ***********************************************************************************************************************************
changed: [kibana]

TASK [Create directrory for kibana] *******************************************************************************************************************************************
--- before
+++ after
@@ -1,4 +1,4 @@
 {
     "path": "/opt/kibana/8.0.0",
-    "state": "absent"
+    "state": "directory"
 }

changed: [kibana]

TASK [Extract Kibana in the installation directory] ***************************************************************************************************************************
changed: [kibana]

TASK [Set environment Kibana] *************************************************************************************************************************************************
--- before
+++ after: /Users/mikhailrusakovich/.ansible/tmp/ansible-local-8619cjdhfv52/tmphqvblz81/kib.sh.j2
@@ -0,0 +1,5 @@
+# Warning: This file is Ansible Managed, manual changes will be overwritten on next playbook run.
+#!/usr/bin/env bash
+
+export KIBANA_HOME=/opt/kibana/8.0.0
+export PATH=$PATH:$KIBANA_HOME/bin
\ No newline at end of file

changed: [kibana]

PLAY RECAP ********************************************************************************************************************************************************************
elasticsearch              : ok=9    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana                     : ok=10   changed=4    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   


```
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
```commandline
PLAY RECAP ********************************************************************************************************************************************************************
elasticsearch              : ok=9    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   
kibana                     : ok=9    changed=0    unreachable=0    failed=0    skipped=2    rescued=0    ignored=0   


```
9. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.
10. Готовый playbook выложите в свой репозиторий, в ответ предоставьте ссылку на него.

## Необязательная часть

1. Приготовьте дополнительный хост для установки logstash.
2. Пропишите данный хост в `prod.yml` в новую группу `logstash`.
3. Дополните playbook ещё одним play, который будет исполнять установку logstash только на выделенный для него хост.
4. Все переменные для нового play определите в отдельный файл `group_vars/logstash/vars.yml`.
5. Logstash конфиг должен конфигурироваться в части ссылки на elasticsearch (можно взять, например его IP из facts или определить через vars).
6. Дополните README.md, протестируйте playbook, выложите новую версию в github. В ответ предоставьте ссылку на репозиторий.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
