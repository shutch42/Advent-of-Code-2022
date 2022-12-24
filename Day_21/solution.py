from copy import deepcopy

init_operations = {}

with open("input.txt") as file:
    # Save operations in txt file to a dict
    for line in file:
        var, terms = line.strip().split(': ')
        if '+' in terms:
            term1, term2 = terms.split(' + ')
            init_operations[var] = ('+', term1, term2)
        elif '-' in terms:
            term1, term2 = terms.split(' - ')
            init_operations[var] = ('-', term1, term2)
        elif '*' in terms:
            term1, term2 = terms.split(' * ')
            init_operations[var] = ('*', term1, term2)
        elif '/' in terms:
            term1, term2 = terms.split(' / ')
            init_operations[var] = ('//', term1, term2)
        else:
            init_operations[var] = int(terms)


def solve_recursive(term, operations):
    # Solve for a term, assuming all terms are derived from terms with a number value
    if term in operations:
        if type(operations[term]) is int:
            t = operations[term]
            return t
        else:
            (op, t1, t2) = operations[term]
            return eval(f"{solve_recursive(t1, operations)}{op}{solve_recursive(t2, operations)}")
    else:
        raise Exception("term not found")


def solve_for(term, known_vars, operations):
    # Rearrange terms to solve for a variable on RHS
    for operation in operations:
        if type(operations[operation]) is tuple and term in operations[operation]:
            # Get index of term and initial equation
            i = operations[operation].index(term)
            (orig_op, tmp_t1, tmp_t2) = operations[operation]
            if orig_op == '+':
                new_op = '-'
            elif orig_op == '-':
                new_op = '+'
            elif orig_op == '*':
                new_op = '//'
            else:
                new_op = '*'
            t1 = operation
            if i == 1:
                t2 = operations[operation][2]
            else:
                t2 = operations[operation][1]

            try:
                # Try solving for val on LHS
                t1_val = solve_recursive(t1, operations)
                if t2 in known_vars:
                    if i == 2 and orig_op == '-' or orig_op == '/':
                        # Example problems where this check is necessary:
                        # t1 = t2 - term -> term = t2 - t1
                        # t1 = t2 / term -> term = t2 / t1
                        return eval(f"{known_vars[t2]}{orig_op}{t1_val}")
                    else:
                        # This format works for all other cases
                        print(f"{t1_val}{new_op}{known_vars[t2]}")
                        return eval(f"{t1_val}{new_op}{known_vars[t2]}")
                else:
                    known_vars[t1] = t1_val
                    if i == 2 and orig_op == '-' or orig_op == '/':
                        return eval(f"{solve_for(t2, known_vars, operations)}{orig_op}{t1_val}")
                    else:
                        return eval(f"{t1_val}{new_op}{solve_for(t2, known_vars, operations)}")
            except:
                # Try solving for val on RHS
                t2_val = solve_recursive(t2, operations)
                if t1 in known_vars:
                    if i == 2 and orig_op == '-' or orig_op == '/':
                        return eval(f"{t2_val}{orig_op}{known_vars[t1]}")
                    else:
                        return eval(f"{known_vars[t1]}{new_op}{t2_val}")
                else:
                    known_vars[t2] = t2_val
                    if i == 2 and orig_op == '-' or orig_op == '/':
                        return eval(f"{t2_val}{orig_op}{solve_for(t1, known_vars, operations)}")
                    else:
                        return eval(f"{solve_for(t1, known_vars, operations)}{new_op}{t2_val}")


# Part 1
pt1_operations = deepcopy(init_operations)
print(f"Root value (pt1): {solve_recursive('root', pt1_operations)}")


# Part 2
pt2_operations = deepcopy(init_operations)

# Remove number for human
del pt2_operations['humn']

# Get values that root checks, delete root
(_, t1, t2) = pt2_operations['root']
del pt2_operations['root']

try:
    # Solve LHS of root, plug value in on RHS
    t1_val = solve_recursive(t1, pt2_operations)
    print(f"Human value (pt2): {solve_for('humn', {t2: t1_val}, pt2_operations)}")
except:
    # If that doesn't work, solve RHS of root, plug value in on LHS
    t2_val = solve_recursive(t2, pt2_operations)
    print(f"Human value (pt2): {solve_for('humn', {t1: t2_val}, pt2_operations)}")
