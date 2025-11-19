from model.author_sqlite_dao import AuthorSqliteDao


if __name__ == '__main__':
    AuthorSqliteDao.create_table()
    print('Author table created successfully.')
