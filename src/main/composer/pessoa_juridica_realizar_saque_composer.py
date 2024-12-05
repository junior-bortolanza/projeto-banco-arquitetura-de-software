from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.controllers.pessoa_juridica_realizar_saque_controller import PessoaJuridicaRealizarSaqueController
from src.views.pessoa_juridica_realizar_saque_view import PessoaJuridicaRealizarSaqueView

def pessoa_juridica_realizar_saque_composer():
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaRealizarSaqueController(model)
    view = PessoaJuridicaRealizarSaqueView(controller)

    return view
