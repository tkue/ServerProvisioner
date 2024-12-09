import os
from enum import Enum
from json import JSONDecodeError

import requests

KEY = 'PagyGe5e6YguSY7aBYMe6Ubev'
LOGIN = 'tomkuecken@gmail.com'


class ActionType(Enum):
    GET_SERVERS = 'get_servers'
    GET_TEMPLATES = 'get_templates'
    GET_TASKS = 'get_tasks'
    GET_RESOURCES = 'get_resources'

class ServerPowerType(Enum):
    POWERON = 'poweron'
    POWEROFF = 'poweroff'
    RESET = 'reset'

class RunModeType(Enum):
    NORMAL = 'normal'
    SAFE = 'safe'


class CloudAtCost(object):
    base_url = 'https://panel.cloudatcost.com/api/v1/'

    def __init__(self, key: str, login: str):
        self.key = key
        self.base_url = 'https://panel.cloudatcost.com/api/v1/'
        self.login = login

        self.servers = self.get_servers()
        self.templates = self.get_templates()
        self.tasks = self.get_tasks()
        self.resources = self.get_resources()

        self.ram_used = self.get_resources()['data']['used']['ram_used']
        self.cpu_used = self.get_resources()['data']['used']['cpu_used']
        self.storage_used = self.get_resources()['data']['used']['storage_used']
        self.cpu_total = self.get_resources()['data']['total']['cpu_total']
        self.ram_total = self.get_resources()['data']['total']['ram_total']
        self.storage_total = self.get_resources()['data']['total']['storage_total']

    def __generate_url(self, action: ActionType):
        url = [self.base_url]

        if action == ActionType.GET_SERVERS:
            url.append('listservers.php')
        elif action == ActionType.GET_TEMPLATES:
            url.append('listtemplates.php')
        elif action == ActionType.GET_TASKS:
            url.append('listtasks.php')
        elif action == ActionType.GET_RESOURCES:
            url.append('cloudpro/resources.php')

        url.append('?key={0}&login={1}'.format(self.key, self.login))

        return ''.join(url)

    # @property
    # def servers(self):
    #     if not self.servers:
    #         self.servers = self.get_servers()
    #     return self.servers
    #
    # @servers.setter
    # def servers(self, val):
    #     yield
    #
    # @property
    # def templates(self):
    #     if not self.templates:
    #         self.templates = self.get_templates()
    #     return self.templates
    #
    # @templates.setter
    # def templates(self, val):
    #     yield
    #
    # @property
    # def resources(self):
    #     if not self.resources:
    #         self.resources = self.get_resources()
    #     return self.resources
    #
    # @resources.setter
    # def resources(self, val):
    #     yield

    def get_servers(self):
        """
        {
          'status': 'ok',
          'data': [
            {
              'cpuusage': '',
              'ramusage': '',
              'servername': 'c849620468-cloudpro-925306482',
              'mode': 'Safe',
              'cpu': '14',
              'rdns': 'c849620468-cloudpro-925306482.cloudatcost.com',
              'vncpass': 'YReZaNUVeh',
              'hdusage': '',
              'lable': None,
              'id': '254775265',
              'ip': '64.137.189.130',
              'packageid': '14',
              'panel_note': None,
              'rootpass': 'urENy8eMu2',
              'ram': '10240',
              'storage': '180',
              'gateway': '64.137.189.1',
              'sdate': '11/02/2016',
              'label': None,
              'hostname': 'Not Assigned',
              'status': 'Powered Off',
              'vmname': 'c849620468-CloudPRO-905649187-249097918',
              'sid': '254775265',
              'uid': '849620468',
              'netmask': '255.255.255.0',
              'portgroup': 'Cloud-ip-289',
              'template': 'Windows 2012 R2 64bit',
              'servertype': 'cloudpro',
              'vncport': '41333',
              'rdnsdefault': 'notassigned.cloudatcost.com'
            }
          ],
          'action': 'listservers',
          'api': 'v1',
          'time': 1485991613
        }
        :return:
        """
        try:
            url = self.__generate_url(ActionType.GET_SERVERS)
            response = requests.get(url)
            return response.json()
        except JSONDecodeError as e:
            print('Unable to decode servers list JSON')
            print(e)
            return None
        except Exception as ex:
            print('Unable to get servers list')
            print(ex)
            return None

    def get_templates(self):
        try:
            url = self.__generate_url(ActionType.GET_TEMPLATES)
            r = requests.get(url)
            return r.json()
        except JSONDecodeError as e:
            print('Unable to decode templates list JSON')
            print(e)
            return None
        except Exception as ex:
            print('Unable to get templates list')
            print(ex)
            return None

    def get_tasks(self):
        try:
            url = self.__generate_url(ActionType.GET_TASKS)
            r = requests.get(url)
            return r.json()
        except JSONDecodeError as e:
            print('Unable to decode tasks list JSON')
            print(e)
            return None
        except Exception as ex:
            print('Unable to get tasks list')
            print(ex)
            return None

    def lookup_server_json(self, ip_addr: str):
        if not ip_addr:
            return


    def get_operating_system_names(self):
        names = []
        for template in self.templates['data']:
            names.append(template['name'])
        return names

    def get_resources(self):
        url = self.__generate_url(ActionType.GET_RESOURCES)
        r = requests.get(url)
        return r.json()

    def lookup_server_id_by_ip(self, ip_addr: str):
        if not ip_addr:
            return
        for server in self.get_servers()['data']:
            if server['ip'] == ip_addr:
                return server['id']

        return



class BaseServer(object):

    def __init__(self, cloud_at_cost: CloudAtCost, ip_addr: str):
        self.cloud_at_cost = cloud_at_cost
        self.ip_addr = ip_addr


class Server(object):

    def __init__(self, cloud_at_cost: CloudAtCost, ip_addr: str):
        self.name = None
        self.ip = ip_addr
        self.cloud_at_cost = cloud_at_cost

        self.server_json = self.cloud_at_cost.server



    @property
    def cpu(self):
        return self.cpu

    @cpu.setter
    def cpu(self, val: int):
        min_val = 1
        max_val = 16
        if val < min_val or val > max_val:
            print('CPU value must be between {0} and {1}}'.format(min_val, max_val))
            print('Given value: {0}'.format(val))
            raise ValueError

        if self.cloud_at_cost.cpu_used + val > self.cloud_at_cost.cpu_total:
            print('Not enough CPU resources available')
            print('CPU Used / CPU Total Available: {0} / {1}'.format(self.cloud_at_cost.cpu_used, self.cloud_at_cost.cpu_total))
            print('Given value: {0}'.format(val))
            raise ValueError

        self.val = val

    @property
    def ram(self):
        return self.ram

    @ram.setter
    def ram(self, val: int):
        min_val = 1024
        max_val = 32768
        if val < min_val or val > max_val:
            print('Ram value must be between {0} and {1}}'.format(min_val, max_val))
            print('Given value: {0}'.format(val))
            raise ValueError

        if val <= 0:
            print('Ram value must be > 0')

        remainder = val % 1024
        if not remainder == 0:
            print('Ram value for server must be divisible by 1024')
            print('Given value: {0}'.format(val))
            raise ValueError

        if self.cloud_at_cost.ram_used + val > self.cloud_at_cost.ram_total:
            print('Not enough ram resources available for given value: {0}'.format(val))
            print('Ram Used / Ram Total Available: {0} / {1}'.format(self.cloud_at_cost.cpu_used, self.cloud_at_cost.cpu_total))
            raise ValueError

        self.ram = val

    @property
    def storage(self):
        return self.storage

    @storage.setter
    def storage(self, val):
        min_val = 10
        max_val = 1000
        if val < min_val or val > max_val:
            print('Storage value must be between {0} and {1}}'.format(min_val, max_val))
            print('Given value: {0}'.format(val))
            raise ValueError

        remainder = val % 10
        if not remainder == 0:
            print('Storage value must be divisible by 10')
            print('Given value: {0}'.format(val))
            raise ValueError

        if self.cloud_at_cost.storage_used + val > self.cloud_at_cost.storage_total:
            print('Not enough storage resources available for given value: {0}'.format(val))
            print('Storage Used / Storage Total Available: {0} / {1}'.format(self.cloud_at_cost.storage_used,
                                                                     self.cloud_at_cost.storage_total))
            raise ValueError




if __name__ == '__main__':
    cac = CloudAtCost(KEY, LOGIN)

    print(cac.servers)
    print(cac.templates)
    print(cac.tasks)
    print(cac.resources)
