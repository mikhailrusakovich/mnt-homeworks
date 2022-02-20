# Домашнее задание к занятию "08.03 Использование Yandex Cloud"

## Подготовка к выполнению
1. Создайте свой собственный (или используйте старый) публичный репозиторий на github с произвольным именем.
2. Скачайте [playbook](./playbook/) из репозитория с домашним заданием и перенесите его в свой репозиторий.

## Основная часть
1. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает kibana.
2. При создании tasks рекомендую использовать модули: `get_url`, `template`, `yum`, `apt`.
3. Tasks должны: скачать нужной версии дистрибутив, выполнить распаковку в выбранную директорию, сгенерировать конфигурацию с параметрами.
4. Приготовьте свой собственный inventory файл `prod.yml`.
```commandline
---
all:
  hosts:
    el-instance:
      ansible_host: 84.201.158.104
    ki-instance:
      ansible_host: 84.252.130.20
    f-instance:
      ansible_host: 62.84.115.182
  vars:
    ansible_connection: ssh
    ansible_user: mikhail
elasticsearch:
  hosts:
    el-instance:
kibana:
  hosts:
    ki-instance:
filebeat:
  hosts:
    f-instance:
```
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
```commandline
Убеждаемся, что playbook идемпотентен

Mikhails-MacBook-Pro:playbook mikhailrusakovich$ ansible-playbook -i inventory/prod site.yml --diff

PLAY [Install Elasticsearch] **************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [el-instance]

TASK [Download Elasticsearch's rpm] *******************************************************************************************************************************************
ok: [el-instance]

TASK [Install Elasticsearch] **************************************************************************************************************************************************
ok: [el-instance]

TASK [Configure Elasticsearch] ************************************************************************************************************************************************
ok: [el-instance]

PLAY [Install Kibana] *********************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [ki-instance]

TASK [Download kibana's rpm] **************************************************************************************************************************************************
ok: [ki-instance]

TASK [Install Kibana] *********************************************************************************************************************************************************
ok: [ki-instance]

TASK [Configure Kibana] *******************************************************************************************************************************************************
ok: [ki-instance]

PLAY [Install Filebeat] *******************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [f-instance]

TASK [Download filebeat's rpm] ************************************************************************************************************************************************
ok: [f-instance]

TASK [Install Filebeat] *******************************************************************************************************************************************************
ok: [f-instance]

TASK [Configure filebeat] *****************************************************************************************************************************************************
ok: [f-instance]

TASK [Set filebeat systemwork] ************************************************************************************************************************************************
changed: [f-instance]

TASK [Load Kibana dashboard] **************************************************************************************************************************************************
ok: [f-instance]

PLAY RECAP ********************************************************************************************************************************************************************
el-instance                : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
f-instance                 : ok=6    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ki-instance                : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   


```
9. Проделайте шаги с 1 до 8 для создания ещё одного play, который устанавливает и настраивает filebeat.
```commandline
Mikhails-MacBook-Pro:playbook mikhailrusakovich$ ansible-playbook -i inventory/prod site.yml 

PLAY [Install Elasticsearch] **************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [el-instance]

TASK [Download Elasticsearch's rpm] *******************************************************************************************************************************************
ok: [el-instance]

TASK [Install Elasticsearch] **************************************************************************************************************************************************
ok: [el-instance]

TASK [Configure Elasticsearch] ************************************************************************************************************************************************
ok: [el-instance]

PLAY [Install Kibana] *********************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [ki-instance]

TASK [Download kibana's rpm] **************************************************************************************************************************************************
ok: [ki-instance]

TASK [Install Kibana] *********************************************************************************************************************************************************
ok: [ki-instance]

TASK [Configure Kibana] *******************************************************************************************************************************************************
ok: [ki-instance]

PLAY [Install Filebeat] *******************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [f-instance]

TASK [Download filebeat's rpm] ************************************************************************************************************************************************
ok: [f-instance]

TASK [Install Filebeat] *******************************************************************************************************************************************************
ok: [f-instance]

TASK [Configure filebeat] *****************************************************************************************************************************************************
changed: [f-instance]

TASK [Set filebeat systemwork] ************************************************************************************************************************************************
changed: [f-instance]

TASK [Load Kibana dashboard] **************************************************************************************************************************************************
ok: [f-instance]

RUNNING HANDLER [restart filebeat] ********************************************************************************************************************************************
changed: [f-instance]

PLAY RECAP ********************************************************************************************************************************************************************
el-instance                : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
f-instance                 : ok=7    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ki-instance                : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
---
10. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.
```commandline
[mikhail@el-instance ~]$ sudo systemctl status elasticsearch
● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; disabled; vendor preset: disabled)
   Active: active (running) since Sun 2022-02-20 20:09:48 UTC; 2h 52min ago
     Docs: https://www.elastic.co
 Main PID: 2256 (java)
   CGroup: /system.slice/elasticsearch.service
           ├─2256 /usr/share/elasticsearch/jdk/bin/java -Xshare:auto -Des.networkaddress.cache.ttl=60 -Des.networkaddress.cache.negative.ttl=10 -XX:+AlwaysPreTouch -Xss1m -...
           └─2453 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller

Feb 20 20:09:30 el-instance.ru-central1.internal systemd[1]: Starting Elasticsearch...
Feb 20 20:09:48 el-instance.ru-central1.internal systemd[1]: Started Elasticsearch.


[mikhail@ki-instance ~]$ sudo systemctl status kibana
● kibana.service - Kibana
   Loaded: loaded (/etc/systemd/system/kibana.service; disabled; vendor preset: disabled)
   Active: active (running) since Sun 2022-02-20 22:20:25 UTC; 40min ago
     Docs: https://www.elastic.co
 Main PID: 7598 (node)
   CGroup: /system.slice/kibana.service
           ├─7598 /usr/share/kibana/bin/../node/bin/node /usr/share/kibana/bin/../src/cli/dist --logging.dest="/var/log/kibana/kibana.log" --pid.file="/run/kibana/kibana.pi...
           └─7611 /usr/share/kibana/node/bin/node --preserve-symlinks-main --preserve-symlinks /usr/share/kibana/src/cli/dist --logging.dest="/var/log/kibana/kibana.log" --...

Feb 20 22:20:25 ki-instance.ru-central1.internal systemd[1]: Started Kibana.
[mikhail@ki-instance ~]$ 


Mikhails-MacBook-Pro:playbook mikhailrusakovich$ ssh mikhail@62.84.115.182
[mikhail@f-instance ~]$ sudo systemctl status filebeat
● filebeat.service - Filebeat sends log files to Logstash or directly to Elasticsearch.
   Loaded: loaded (/usr/lib/systemd/system/filebeat.service; enabled; vendor preset: disabled)
   Active: active (running) since Sun 2022-02-20 22:40:41 UTC; 19min ago
     Docs: https://www.elastic.co/beats/filebeat
 Main PID: 25384 (filebeat)
   CGroup: /system.slice/filebeat.service
           └─25384 /usr/share/filebeat/bin/filebeat --environment systemd -c /etc/filebeat/filebeat.yml --path.home /usr/share/filebeat --path.config /etc/filebeat --path.d...

Feb 20 22:55:41 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:55:41.802Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:56:11 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:56:11.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:56:41 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:56:41.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:57:11 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:57:11.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:57:41 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:57:41.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:58:11 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:58:11.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:58:41 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:58:41.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:59:11 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:59:11.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:59:41 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:59:41.801Z        INFO        [monitoring]        log/log.go:145        Non-zero metrics in t...
Feb 20 22:59:51 f-instance.ru-central1.internal filebeat[25384]: 2022-02-20T22:59:51.905Z        INFO        [input.harvester]        log/harvester.go:309        Harvester ...
Hint: Some lines were ellipsized, use -l to show in full.
```
11. Готовый playbook выложите в свой репозиторий, в ответ предоставьте ссылку на него.</br>

Установка и выполнение tasks прошла успешно.

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
