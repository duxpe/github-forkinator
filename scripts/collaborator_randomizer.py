from rich.progress import track 
import requests

from dotenv import load_dotenv
import argparse
import random
import math
import os 

# Esse script é apenas uma prova de conceito,
# para configurar e utilizar, certifique-se de instalar as dependências e
# configurar seus dados no arquivo .env 

load_dotenv()

TOKEN = os.environ.get('TOKEN')
OWNER = os.environ.get('OWNER')


headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {TOKEN}',
    'X-GitHub-Api-Version': '2022-11-28'
}


def get_collaborators_url(repo: str) -> str:
    return f"""
    https://api.github.com/repos/{OWNER}/{repo}/collaborators"""


def edit_collaborator_url(repo: str, collaborator: str) -> str:
    return f"""
    https://api.github.com/repos/{OWNER}/{repo}/collaborators/{collaborator}"""


def get_collaborators_from_repository(repo: str) -> list:
    message = f"Listando colaboradores de {repo}..."
    collaborators = []
    r = requests.get(get_collaborators_url(repo), headers=headers)
    if(r.status_code == 200):
        response = r.json()
        for collaborator in track(response or [], description=message):
            name = collaborator.get('login', False)
            if name and name != OWNER:
                collaborators.append(name)
    return collaborators


def remove_collaborator_from_repository(repo: str, collaborator: str):
    r = requests.delete(
        edit_collaborator_url(repo, collaborator), 
        headers=headers
        )
    if(r.status_code != 204):
        print(f'ERRO: falha ao remover {collaborator} de {repo}')


def invite_collaborator_to_repository(repo: str, collaborator: str):
    r = requests.put(
        edit_collaborator_url(repo, collaborator), 
        headers=headers
        )
    if(r.status_code != 201):
        print(f'ERRO: falha ao convidar {collaborator} para {repo}')


def randomize_collaborators_between_repositories(repos: list, fixed_qtt = 0):
    collaborators = []
    average_collaborator_qtd = 0
    
    for repo in repos:
        repo_collaborators = get_collaborators_from_repository(repo)
        average_collaborator_qtd += len(repo_collaborators)
        for collaborator in repo_collaborators:
            remove_collaborator_from_repository(repo, collaborator)
        collaborators.extend(repo_collaborators)
    
    average_collaborator_qtd = fixed_qtt if fixed_qtt > 0 else math.floor(
        average_collaborator_qtd/len(repos or [])
        )
    print('Misturando colaboradores....')
    random.shuffle(collaborators)
    random.shuffle(repos)

    message = 'Convidando colaboradores...'
    for repo in track(repos or [], description=message):
        invites = 0
        while(invites < average_collaborator_qtd and len(collaborators) > 0):
            invite_collaborator_to_repository(repo, collaborators.pop())
            invites+=1
    
    if(len(collaborators) > 0):
        print(f'Convidando colaboradores que sobraram para {repos[0]}....')
        random.shuffle(repos)
        while(len(collaborators) > 0):
            invite_collaborator_to_repository(repos[0], collaborators.pop())
    
    print('Tudo feito! Peça para os colaboradores aceitarem os convites.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Collaborator Randomizer',
        description='Recebe uma lista de repositórios github e embaralha' \
        ' os colaboradores',
        epilog="Insira suas credênciais no .env e passe os repos nos args. " \
        'Certifique-se que você é o dono dos repositórios e que seu token ' \
        'tem as pemissões necessárias.'
        )
    parser.add_argument('--repos', 
                        nargs='+', 
                        default=[], 
                        help='Liste os repos (separados por espaço)' \
                        '\nExemplo: --repos nome-do-meu-projeto1 ' \
                        'meu-projeto2 outro-repo')
    
    parser.add_argument('--qtd',
                        default=0,
                        help='Opcionalmente, informe o número de ' \
                        'colaboradores por repo, se não informado ou < 0 ' \
                        'será utilizada a média de colaboradores entre todos' \
                        ' os repositórios.'
                        )
    args = parser.parse_args()
    repos = args.repos
    qtd = int(args.qtd)
    
    if not repos:
        parser.print_help()
    else:
        randomize_collaborators_between_repositories(repos, qtd)