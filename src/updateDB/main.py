from ConsomeAPI import dadosTratados
from UpdateDB import fazQuery




if __name__ =="__main__": 
    dados = dadosTratados()
    for dado in dados:
        if dado['organization_fields']['entidade_id']:
            print('\tid\tnome\tentidade')
            print('=>',dado['id'],dado['name'],dado['organization_fields']['entidade_id'],'\n\n\n' )
            fazQuery(f"update entidades set zendesk_external_id={dado['id']} where entidades.id={dado['organization_fields']['entidade_id']} ")