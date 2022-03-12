from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        deser_content = toml.loads(content)
        print(deser_content)
        return Project("Test name", "Test description", [], [])

obj = ProjectReader('https://github.com/henkkah/ohtu-tehtavat/blob/64ea5c6ad111e41e5b597b32d675cc97969bd11f/viikko2/poetry-web/pyproject.toml')
obj.get_project()
