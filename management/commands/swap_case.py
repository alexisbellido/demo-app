import argparse

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Swap case in a provided string.
    """

    help = """
Examples:

    $ django-admin swap_case "Up and Down 1.2"
"""

    def create_parser(self, *args, **kwargs):
        parser = super(Command, self).create_parser(*args, **kwargs)
        parser.formatter_class = argparse.RawTextHelpFormatter
        return parser

    def add_arguments(self, parser):
        parser.add_argument(
            'input',
            help='The string.'
        )

    def handle(self, *args, **options):
        self.stdout.write('Original string: %s' % options['input'])
        self.stdout.write('Swapped case: %s' % self.swap_case(options['input']))
        self.stdout.write(self.style.SUCCESS("Processed"))

    def swap_case(self, input):
        """
        We could just return input.swapcase() but for the sake of the exercise
        let's process each character.
        """

        output = []
        for character in input:
            output.append(character.swapcase())

        return ''.join(output)
