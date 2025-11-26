from model.author_sqlite_dao import AuthorSqliteDao
from controller.author_controller import AuthorController

if __name__ == "__main__":

    AuthorSqliteDao.create_table()

    controller = AuthorController()

    controller.register(author_id="2", name="George Orwell")
    controller.list()

    controller.update(author_id="2", name="G. Orwell")
    controller.list()

    controller.delete("2")
    controller.list()

    controller.restore("2")
    controller.list()
