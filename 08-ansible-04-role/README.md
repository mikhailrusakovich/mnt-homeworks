# Домашнее задание к занятию "8.4 Работа с Roles"

## Подготовка к выполнению
1. Создайте два пустых публичных репозитория в любом своём проекте: kibana-role и filebeat-role.
2. Добавьте публичную часть своего ключа к своему профилю в github.

## Основная часть

Наша основная цель - разбить наш playbook на отдельные roles. Задача: сделать roles для elastic, kibana, filebeat и написать playbook для использования этих ролей. Ожидаемый результат: существуют два ваших репозитория с roles и один репозиторий с playbook.

1. Создать в старой версии playbook файл `requirements.yml` и заполнить его следующим содержимым:
   ``` 
   yaml
   ---
     - src: git@github.com:netology-code/mnt-homeworks-ansible.git
       scm: git
       version: "2.0.0"
       name: elastic 
   ```
2. При помощи `ansible-galaxy` скачать себе эту роль.</br>
выполнено
3. Создать новый каталог с ролью при помощи `ansible-galaxy role init kibana-role`.</br>
выполнено
4. На основе tasks из старого playbook заполните новую role. Разнесите переменные между `vars` и `default`. </br>
выполнено
5. Перенести нужные шаблоны конфигов в `templates`.</br>
выполнено
6. Создать новый каталог с ролью при помощи `ansible-galaxy role init filebeat-role`.</br>
выполнено
7. На основе tasks из старого playbook заполните новую role. Разнесите переменные между `vars` и `default`. 
8. Перенести нужные шаблоны конфигов в `templates`.</br>
выполнено
9. Описать в `README.md` обе роли и их параметры. </br>
даны комментарии для роли kibana-role (filebeat-role и elasticsearch_role выполняются по аналогии)
10. Выложите все roles в репозитории. Проставьте тэги, используя семантическую нумерацию.
11. Добавьте roles в `requirements.yml` в playbook.
```commandline
---
- src: git@github.com:netology-code/mnt-homeworks-ansible.git
  scm: git
  version: "2.1.4"
  name: elasticsearch_role
- src: git@github.com:netology-code/mnt-homeworks-ansible.git
  scm: git
  version: "1.0.1"
  name: kibana-role
- src: git@github.com:netology-code/mnt-homeworks-ansible.git
  scm: git
  version: "1.0.1"
  name: filebeat-role

```
12. Переработайте playbook на использование roles.
```commandline
Mikhails-MacBook-Pro:playbook mikhailrusakovich$ ansible-playbook -i inventory/hosts.yml site.yml

PLAY [Assert elasticsearch_role] **********************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [el]

TASK [elasticsearch_role : Fail if unsupported system detected] ***************************************************************************************************************
skipping: [el]

TASK [elasticsearch_role : Check files directory exists] **********************************************************************************************************************
ok: [el -> localhost]

TASK [elasticsearch_role : include_tasks] *************************************************************************************************************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/download_yum.yml for el

TASK [elasticsearch_role : Download Elasticsearch's rpm] **********************************************************************************************************************
ok: [el -> localhost]

TASK [elasticsearch_role : Copy Elasticsearch to managed node] ****************************************************************************************************************
ok: [el]

TASK [elasticsearch_role : include_tasks] *************************************************************************************************************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/elasticsearch_role/tasks/install_yum.yml for el

TASK [elasticsearch_role : Install Elasticsearch] *****************************************************************************************************************************
ok: [el]

TASK [elasticsearch_role : Configure Elasticsearch] ***************************************************************************************************************************
ok: [el]

PLAY [Assert kibana-role] *****************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [el2]

TASK [kibana-role : Fail if unsupported system detected] **********************************************************************************************************************
skipping: [el2]

TASK [kibana-role : Check files directory exists] *****************************************************************************************************************************
ok: [el2 -> localhost]

TASK [kibana-role : include_tasks] ********************************************************************************************************************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role/tasks/download_yum.yml for el2

TASK [kibana-role : Download Kibana's rpm] ************************************************************************************************************************************
ok: [el2 -> localhost]

TASK [kibana-role : Copy Kibana to managed node] ******************************************************************************************************************************
ok: [el2]

TASK [kibana-role : include_tasks] ********************************************************************************************************************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/kibana-role/tasks/install_yum.yml for el2

TASK [kibana-role : Install Kibana] *******************************************************************************************************************************************
ok: [el2]

TASK [kibana-role : Configure kibana] *****************************************************************************************************************************************
ok: [el2]

PLAY [Assert filebeat-role] ***************************************************************************************************************************************************

TASK [Gathering Facts] ********************************************************************************************************************************************************
ok: [el3]

TASK [filebeat-role : Fail if unsupported system detected] ********************************************************************************************************************
skipping: [el3]

TASK [filebeat-role : Check files directory exists] ***************************************************************************************************************************
ok: [el3 -> localhost]

TASK [filebeat-role : include_tasks] ******************************************************************************************************************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/tasks/download_yum.yml for el3

TASK [filebeat-role : Download Filebeat's rpm] ********************************************************************************************************************************
ok: [el3 -> localhost]

TASK [filebeat-role : Copy Filebeat to managed node] **************************************************************************************************************************
ok: [el3]

TASK [filebeat-role : include_tasks] ******************************************************************************************************************************************
included: /Users/mikhailrusakovich/devops-netology/mnt-11/mnt-homeworks/08-ansible-04-role/playbook/roles/filebeat-role/tasks/install_yum.yml for el3

TASK [filebeat-role : Install Filebeat] ***************************************************************************************************************************************
ok: [el3]

TASK [filebeat-role : Configure Filebeat] *************************************************************************************************************************************
changed: [el3]

TASK [filebeat-role : Set filebeat systemwork] ********************************************************************************************************************************
changed: [el3]

TASK [filebeat-role : Load Kibana dashboard] **********************************************************************************************************************************
ok: [el3]

RUNNING HANDLER [filebeat-role : restart filebeat] ****************************************************************************************************************************
changed: [el3]

PLAY RECAP ********************************************************************************************************************************************************************
el                         : ok=8    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
el2                        : ok=8    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
el3                        : ok=11   changed=3    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
```
13. Выложите playbook в репозиторий.
14. В ответ приведите ссылки на оба репозитория с roles и одну ссылку на репозиторий с playbook.

## Необязательная часть

1. Проделайте схожие манипуляции для создания роли logstash.
2. Создайте дополнительный набор tasks, который позволяет обновлять стек ELK.
3. Убедитесь в работоспособности своего стека: установите logstash на свой хост с elasticsearch, настройте конфиги logstash и filebeat так, чтобы они взаимодействовали друг с другом и elasticsearch корректно.
4. Выложите logstash-role в репозиторий. В ответ приведите ссылку.

---

### Как оформить ДЗ?

Выполненное домашнее задание пришлите ссылкой на .md-файл в вашем репозитории.

---
