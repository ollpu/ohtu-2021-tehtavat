from matchers import And, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self):
        self._clauses = []

    def playsIn(self, team):
        self._clauses.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._clauses.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._clauses.append(HasFewerThan(value, attr))
        return self

    def build(self):
        return And(*self._clauses)
