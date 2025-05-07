from . import api
from swagger.namespaces.alunos_namespaces import alunos_ns
from swagger.namespaces.professores_namespaces import professor_ns
from swagger.namespaces.turmas_namespaces import turmas_ns

# Função para registrar os namespaces
def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(professor_ns, path="/professores")
    api.add_namespace(turmas_ns, path="/turmas")
    api.mask_swagger = False