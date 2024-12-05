from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.controllers.pessoa_fisica_realizar_saque import PessoaFisicaRealizarSaqueController
from src.views.pessoa_fisica_realizar_saque_view import PessoaFisicaRealizarSaqueView

def pessoa_fisica_realizar_saque_composer():
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaRealizarSaqueController(model)
    view = PessoaFisicaRealizarSaqueView(controller)

    return view
