import requests as rq
from dotenv import load_dotenv
from os import environ as env
load_dotenv('../../.env')


def connectaAPI(i:int):
    r = rq.get(f'https://proesc.zendesk.com/api/v2/organizations.json?page={i}', auth=(env['zendesk_email'],env['zendesk_password']))
    return r
    
def filtraAPI(r=24):
    dados=[]
    for i in range(r):
       aux = connectaAPI(i).json()['organizations']
       for obj in aux: 
           dados.append(dict(obj))
    return dados
       
def dadosTratados():
    dados= filtraAPI()
    
    i=0
    for dado in dados:    
        if not dado['organization_fields']['entidade_id']:
            dados.pop(i)
        i+=1  
            
    return dados

