from model.publisher_dao import PublisherDao
from controller.publisher_controller import PublisherController

if __name__ == "__main__":

    PublisherDao.create_table()

    controller = PublisherController()

    controller.register(publisher_id='1', legal_name='Companhia das Letras', city='Rio de Janeiro', state='RJ')
    controller.list()

    controller.update(publisher_id='1', legal_name='Cia das Letras', city='São Paulo', state='SP')
    controller.list()

    controller.delete("1")
    controller.list()

    controller.restore("1")
    controller.list()
