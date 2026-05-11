# Functions goes here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

# Main Routine Goes here
make_statement(statement="programing is fun", decoration="💦")