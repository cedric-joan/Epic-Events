import click
from django.core.management import call_command

@click.group()
def cli():
    pass

@cli.command('create_user')
@click.option('--user')
@click.option('--username', prompt='username')
@click.option('--email', prompt='email')
@click.option('--password', prompt='password')
@click.option('--role', prompt='role')
def create_user(username, email, password, role):
    """Create a new user."""
    call_command('create_user', username=username, email=email, password=password, role=role)

@cli.command()
@click.option('--client-id', type=int, required=True, help='Client ID')
def get_client(client_id):
    """Get client details by ID"""
    call_command('get_client', client_id=client_id)

if __name__ == '__main__':
    cli()