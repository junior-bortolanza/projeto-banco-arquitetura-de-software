from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_lister_controller import PessoaFisicaListerController
from src.views.pessoa_fisica_lister_view import PessoaFisicaListerView

def pessoa_fisica_lister_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaListerController(model)
    view = PessoaFisicaListerView(controller)

    return view
