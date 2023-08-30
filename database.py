import configparser
import pymysql

config = configparser.ConfigParser()
config.read('config.ini')


def connection_creator():
    connect = pymysql.connect(
        host=config['sql']['host'],
        user=config['sql']['user'],
        password=config['sql']['password'],
        db=config['sql']['db'],
        charset='utf8mb4',
        # cursorclass=DictCursor
    )

    return connect


def clear_table_members(bot_number):
    connection = connection_creator()
    cursor = connection.cursor()

    cursor.execute(f'DELETE FROM members{bot_number}')
    connection.commit()

    connection.close()