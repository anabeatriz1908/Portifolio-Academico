from flask_restx import Namespace, Resource, fields
from main.Professor.professores_model import *

professor_ns = Namespace("professores", description="Operações relacionadas aos professores")

professores_model = professor_ns.model("Professores", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "materia": fields.String(required=True, description="Materia lecionada"),
    "observacoes": fields.String(required=True, description="Observacoes acerca do professor"),
    "idade": fields.Integer(required=True, description="Idade do professor"),
    
    
})

professores_output_model = professor_ns.model("ProfessoresOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(required=True, description="Nome do professor"),
    "materia": fields.String(required=True, description="Materia lecionada"),
    "observacoes": fields.String(required=True, description="Observacoes acerca do professor"),
    "idade": fields.String(required=True, description="Idade do professor"),
})

@professor_ns.route('/')
class Professores(Resource):
    @professor_ns.marshal_list_with(professores_output_model)
    def get(self):
        return read_professor()
    
    @professor_ns.expect(professores_model)
    def post(self):
        dados_turmas = professor_ns.payload
        resposta= create_professor(dados_turmas)
        return resposta
    
    def delete(self):
        return delete_professores()


@professor_ns.route('/<int:id_professor>')
class ProfessoresId(Resource):

    @professor_ns.marshal_with(professores_output_model)
    def get(self, id_professor):
        return read_professor_id(id_professor)
    
    @professor_ns.expect(professores_model)
    def put(self, id_professor):
        dados_turmas = professor_ns.payload
        resposta= update_professores(id_professor, dados_turmas)
        return resposta
    
    def delete(self, id_professor):
        resposta = delete_professor(id_professor)
        return resposta