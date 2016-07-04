import os
from datetime import datetime
from settings import PROJECTS_DIR
from lib.utils import address_in_blacklist, dump_object, create_directory


class Project(object):

    def __init__(self, name):
        """
        :param name: Project's name
        """
        self._project_name = name.lower()
        self._created_at = datetime.now().isoformat()
        self._project_dir = PROJECTS_DIR+self._project_name+'/'
        create_directory(self._project_dir)


    def get_name(self):
        """
        :return String: project's name
        """
        return self._project_name


    def get_date(self):
        """
        :return String: project's creation date
        """
        return self._created_at


    def save(self):
        """
        Serialize and save object
        """
        class_name = self.__class__.__name__.lower()
        if not class_name == Project.__name__.lower():
            project_type_dir = self._project_dir+class_name+'/'
            create_directory(project_type_dir)
            file_name = project_type_dir+str(self._created_at)+'.pvap'
            dump_object(file_name, self)


class Pentest(Project):

    def __init__(self, name, domaines, ignored_subdomaines=[]):
        """
        :param name: project's name
        :param domaines: project's basic domaine names
        :param ignored_subdomaines: Subdomaines to be ignored when detected
        """
        super(Pentest, self).__init__(name)
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
        :return List|None: list of domaine's IP addresses or None
        """
        if domaine in self._detected_domaines:
            return self._detected_domaines[domaine]
        return None
