from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_create_controller import PessoaFisicaCreateController
from src.views.pessoa_fisica_create_view import PessoaFisicaCreateView


def pessoa_fisica_create_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaCreateController(model)
    view = PessoaFisicaCreateView(controller)

    return view
