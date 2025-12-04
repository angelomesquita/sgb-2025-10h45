from model.book_dao import BookDao
from controller.book_controller import BookController

if __name__ == "__main__":

    BookDao.create_table()

    controller = BookController()

    controller.register(isbn="987789123123", title="Book 1", author_id="2", publisher_id="1", year=2025, quantity=1)
    controller.list()

    controller.update(isbn="987789123123", title="Book 1 UP", author_id="3", publisher_id="2", year=2024, quantity=2)
    controller.list()

    controller.delete("987789123123")
    controller.list()

    controller.restore("987789123123")
    controller.list()
