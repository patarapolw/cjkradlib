import click
import regex

from . import RadicalFinder


@click.command()
@click.argument('hanzi_list')
@click.option('-l', '--lang', default='zh')
def cli_rad_finder(hanzi_list, lang):
    finder = RadicalFinder(lang=lang)

    for hanzi in regex.findall(r'\p{IsHan}', hanzi_list):
        result = finder.search(hanzi)

        click.echo('Parsing character: {}'.format(hanzi))
        click.echo('Compositions: {}'.format(', '.join(result.compositions)))
        click.echo('Supercompositions: {}'.format(', '.join(result.supercompositions)))
        click.echo('Variants: {}'.format(', '.join(result.variants)))
        click.echo()


def main():
    cli_rad_finder()


if __name__ == '__main__':
    main()
