import click
import regex
import json

from . import RadicalFinder


@click.command()
@click.argument('hanzi_list')
@click.option('-l', '--lang', default='zh')
@click.option('-j', '--json', 'is_json', is_flag=True)
def cli_rad_finder(hanzi_list, lang, is_json):
    finder = RadicalFinder(lang=lang)

    for hanzi in regex.findall(r'\p{IsHan}', hanzi_list):
        result = finder.search(hanzi)

        if is_json:
            click.echo(json.dumps({
                hanzi: {
                    "compositions": result.compositions,
                    "supercompositions": result.supercompositions,
                    "variants": result.variants
                }
            }, ensure_ascii=False))
        else:
            click.echo('Parsing: {}'.format(hanzi))
            click.echo('Compositions: {}'.format(', '.join(result.compositions)))
            click.echo('Supercompositions: {}'.format(', '.join(result.supercompositions)))
            click.echo('Variants: {}'.format(', '.join(result.variants)))
            click.echo()


def main():
    cli_rad_finder()


if __name__ == '__main__':
    main()
