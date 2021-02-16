from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        de = toml.loads(content)
        poetry = de["tool"]["poetry"]

        return Project(
            poetry["name"],
            poetry["description"],
            poetry["dependencies"].keys(),
            poetry["dev-dependencies"].keys()
        )
