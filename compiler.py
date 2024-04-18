import os
import re
from syntax_mappings import mappings_syntax_event_values
from syntax_mappings import mappings_syntax_effects
from syntax_mappings import mappings_syntax_expressions
from syntax_mappings import mappings_symbols
from syntax_mappings import mappings_general
from syntax_mappings import mappings_syntax_types
from syntax_mappings import mappings_syntax_events
from syntax_mappings import mappings_syntax_math
from syntax_mappings import mappings_syntax_functions
import math

# Checks if there are spaces or nothing around a word:
# content = re.sub(r'(^|\s)word(\s|$)', r'\1word\2', content)

def convert_syntax():
    global content
# Does NOT check for spaces
    for key, value in mappings_syntax_event_values.items():
        pattern = re.compile(rf'{re.escape(key)}')
        content = pattern.sub(fr'{value}', content)
    for key, value in mappings_syntax_effects.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = pattern.sub(fr'\1{value}\2', content)
    for key, value in mappings_syntax_expressions.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = pattern.sub(fr'\1{value}\2', content)
# Does NOT check for spaces
    for key, value in mappings_symbols.items():
        pattern = re.compile(rf'{re.escape(key)}')
        content = pattern.sub(fr'{value}', content)
    for key, value in mappings_general.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = pattern.sub(fr'\1{value}\2', content)
    for key, value in mappings_syntax_types.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = pattern.sub(fr'\1{value}\2', content)
    for key, value in mappings_syntax_types.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = pattern.sub(fr'\1{value}\2', content)
    for key, value in mappings_syntax_events.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = pattern.sub(fr'\1{value}\2', content)
    for key, value in mappings_syntax_math.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = pattern.sub(fr'\1{value}\2', content)
# Does NOT check for spaces
    for key, value in mappings_syntax_functions.items():
        pattern = re.compile(rf'{re.escape(key)}')
        content = pattern.sub(fr'{value}', content)
    
def process_file(input_file, output_file):
    global content
    try:
        with open(input_file, 'r') as csk_file:
            content = csk_file.read()
            convert_syntax()
            with open(output_file, 'w') as sk_file:
                sk_file.write(content)
            print(f"Conversion successful: {input_file} -> {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")

if __name__ == "__main__":
    current_directory = os.getcwd()
    input_file_name = input("Enter the name of the .csk file: ")
    input_file_path = os.path.join(current_directory, input_file_name)
    if not input_file_name.endswith('.csk'):
        print("Error: Pls give a file with .csk extension.")
    else:
        output_file_name = input_file_name.replace('.csk', '.sk')
        output_file_path = os.path.join(current_directory, output_file_name)
        process_file(input_file_path, output_file_path)