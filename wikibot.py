from mylib.bot import scrape
import click



@click.command()
@click.option('--name',    '-n',
              default='Microsoft',
              help='Wikipedia page to scrape')
@click.option('--length',  '-l',
              default=1,
              type=int,
              help='Number of sentences to return')

def cli(name, length):
    result = scrape(name, length)
    click.echo(click.style(f"{result}:", fg='white', bg='blue', bold=True))

if __name__ == '__main__':
    cli()