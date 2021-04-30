from matchers import And, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, clauses=[]):
        self._clauses = clauses

    def playsIn(self, team):
        return QueryBuilder([*self._clauses, PlaysIn(team)])

    def hasAtLeast(self, value, attr):
        return QueryBuilder([*self._clauses, HasAtLeast(value, attr)])

    def hasFewerThan(self, value, attr):
        return QueryBuilder([*self._clauses, HasFewerThan(value, attr)])

    def oneOf(self, *clauses):
        return QueryBuilder([*self._clauses, Or(*clauses)])

    def build(self):
        return And(*self._clauses)
