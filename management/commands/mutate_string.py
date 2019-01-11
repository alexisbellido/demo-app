import argparse

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """
    Mutate string.
    """

    help = """
Examples:

    $ django-admin mutate_string "pythom" --position 5 --character n
"""

    def create_parser(self, *args, **kwargs):
        parser = super(Command, self).create_parser(*args, **kwargs)
        parser.formatter_class = argparse.RawTextHelpFormatter
        return parser

    def add_arguments(self, parser):
        parser.add_argument(
            'input',
            help='Input string.'
        )

        parser.add_argument(
            '--position',
            type=int,
            help='Position to change.',
        )

        parser.add_argument(
            '--character',
            help='Character to use in position.',
        )

    def handle(self, *args, **options):
        """
        Process command.
        """
        if options['position'] is not None and options['character'] is not None:
            if len(options['character']) > 1:
                raise CommandError("You can only replace one character.")
            self.stdout.write('Original string: %s' % options['input'])
            self.stdout.write('Mutated string: %s' % self.mutate_string(
                options['input'],
                options['position'],
                options['character'])
            )
            self.stdout.write(self.style.SUCCESS('Processed.'))

    def mutate_string(self, input, position, character):
        """
        Loop over string's characters and replace the one at the provided position.
        """
        output = []
        for index, original_character in enumerate(input):
            if index == position:
                output.append(character)
            else:
                output.append(original_character)
        return ''.join(output)
