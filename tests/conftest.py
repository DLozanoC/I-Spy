import pytest
from app import create_app
from app import db
from app.models.models import Player

#When adding this decorator to a function we are  registering this function as being part of pytest
#When we have a test we can pass a function to a test. the function will act as a variable that 
#stores the result of the function
@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        #Yield is a return statement that pauses a function when it's done
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def players_with_names(app):
    player_1 = Player(name = "Sofia")
    player_2 = Player(name = "Dahlia")
    player_3 = Player(name = "Sully")
    player_4 = Player(name = "Maya")

    db.session.add_all([player_1, player_2, player_3, player_4])
    db.session.commit()

