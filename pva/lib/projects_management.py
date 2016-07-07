import os
from datetime import datetime
from settings import PROJECTS_DIR, PVA_PROJECT_EXT
from lib.utils import *

class ProjectManagement(object):

    def get_projects_list(self):
        """
        Get projects list
        :return List: list of project names
        """
        return os.listdir(PROJECTS_DIR)


    def get_project_types(self, project_name):
        """
        Get project types
        :return List|None: list of project's types
        """
        project_dirname = PROJECTS_DIR+project_name.lower()
        if not os.path.exists(project_dirname):
            return None
        return [p[0].upper()+p[1:] for p in os.listdir(project_dirname)]


    def get_project_instances(self, project_name, project_type):
        """
        Get list of processed project instances
        :return List|None: list of processed project instances
        """
        dirname = PROJECTS_DIR+project_name.lower()+'/'+project_type.lower()
        if not os.path.exists(dirname):
            return None
        return [p[:-5] for p in os.listdir(dirname)]


    def load_project_instance(self, project_name, project_type, project_instance):
        """
        Get project instance
        :param project_name: project name
        :param project_type: project type [pentest]
        :param project_instance: project instance's name
        :return Project|None: Project instance
        """
        filepath = PROJECTS_DIR+project_name.lower()+'/'+project_type.lower()+
                    '/'+project_instance+'.'+PROJECT_EXT
        if os.path.isfile(filepath):
            return load_dumped_object(filepath)
        return None
        

    def load_last_instance(self, project_name, project_type):
        """
        Load most recent instance
        :param project_name: project name
        :param project_type: project type [pentest]
        :return Project|None: latest Project instance
        """
        dirname = PROJECTS_DIR+project_name.lower()+'/'+project_type.lower()+'/'
        return load_dumped_object(get_recent_file(dirname, ext=PROJECT_EXT))


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
