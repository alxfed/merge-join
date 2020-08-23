# -*- coding: utf-8 -*-
"""...
"""
import pandas as pd
import sqlalchemy as sqla

class Dataset:
    def __init__(self, source_table:str):
        self.source_table = source_table
        self.data = {}

    def __del__(self):
        pass

    def load_sql_data(self, set_name:str, sql:str):
        sql = sql.format(**dict(source_table=self.source_table))
        data_query = sqla.text(sql)
        self.data[set_name] = pd.read_sql_query(sql=data_query,
                                                con=dwh_conn,
                                                parse_dates=parse_dates,
                                                params={'start': self.start_date_str,
                                                        'stop': self.stop_date_str})


if __name__ == '__main__':
    dset = Dataset(source_table='project_ac.af_normalized_events')
    query = '''
                SELECT client_id,
                FROM {source_table}
                WHERE event_date BETWEEN :start AND :stop;
    '''
    dset.load_sql_data(set_name='new_players')
    print('\ndone')