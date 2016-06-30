from datetime import datetime
from lib.utils import address_in_blacklist


class Project:

    def __init__(self, name):
        """
        :param name: Project's name
        """
        self._project_name = name
        self._created_at = datetime.now().isoformat()


    def get_name(self):
        """
        :return: string: project's name
        """
        return self._project_name


    def get_date(self):
        """
        :return: string: project's creation date
        """
        return self._created_at


class Pentest(Project):

    def __init__(self, name, domaines, ignored_subdomaines):
        """
        :param name: project's name
        :param domaines: project's basic domaine names
        :param ignored_subdomaines: Subdomaines to be ignored when detected
        """
        super(WebProject, self).__init__(name)
        self._initial_domaines = domaines
        self._ignored_sbdomaines = ignored_subdomaines
        self._detected_domaines = {}


    def add_detected_domaine(self, domaine, ip_address):
        """
        Add detected domaine to dictionary
        :param domaine: detected (sub)domaine name
        :param ip_address: detected (sub)domaine IP address
        """
        if not domaine in self._ignored_sbdomaines and not address_in_blacklist(ip_address):
            if domaine in self._detected_domaines:
                if not ip_address in self._detected_domaines[domaine]:
                    self._detected_domaines[domaine].append(ip_address)
            else:
                self._detected_domaines[domaine] = [ip_address]


    def get_domaine_ips(self, domaine):
        """
        Get the domaine's IP addresses
        :param domaine: (sub)domaine name
        :return: List|None: list of domaine's IP addresses or None
        """
        if domaine in self._detected_domaines:
            return self._detected_domaines[domaine]
        return None
