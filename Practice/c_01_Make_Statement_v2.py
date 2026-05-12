# Functions goes here
def make_statement(statement, decoration, lines):

    """ Creates headings (3 lines), subheadings (2 lines) andemphasised text / mini - headings(1 line).Only use emoji for single line statements"""
    middle=f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom=decoration*len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

# Main Routine Goes here
make_statement(statement="programing is fun" , decoration="=",lines=3)
make_statement(statement="programing is still fun" , decoration="+",lines=2)
make_statement(statement="Emoji in action" , decoration="🔒",lines=1)