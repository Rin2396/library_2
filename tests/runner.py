from typing import Any
from django.db.backends.base.base import BaseDatabaseWrapper
from django.test.runner import DiscoverRunner
from django.db import connections
from types import MethodType


def prepare_db(self):
    self.connect()
    self.connection.cursor().execute('CREATE SCHEMA IF NOT EXISTS library;')

class PostgresSchemaRunner(DiscoverRunner):
    def setup_databases(self, **kwargs: Any) -> list[tuple[BaseDatabaseWrapper, str, bool]]:
        for conn_name in connections:
            connection = connections[conn_name]
            connection.prepare_database = MethodType(prepare_db, connection)
        return super().setup_databases(**kwargs)