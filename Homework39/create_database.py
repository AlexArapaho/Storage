from models.database import create_db, Session
from faker import Faker
from models.Client import Client
from models.Salesdep import Salesdep


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())

def _load_fake_data(session):

    manager1 = Salesdep(manager_name="Иванов")
    manager2 = Salesdep(manager_name="Петров")
    manager3 = Salesdep(manager_name="Сидоров")
    session.add(manager1)
    session.add(manager2)
    session.add(manager3)


    faker = Faker('ru_RU')
    manager_list = [manager1, manager2, manager3]
    session.commit()

    for _ in range(30):
        name = faker.name()
        discount = faker.random.randint(5, 30)
        salesdep = faker.random.choice(manager_list)
        client = Client(name, discount, salesdep.id)
        session.add(client)

    session.commit()
    session.close()

