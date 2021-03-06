import ast

from seval.nodes.evals import eval_stmt
from seval.blacklist import blacklist

def parse_string(env, text):
    body = ast.parse(text, mode='single').body
    responses = []
    for stmt_or_expr in body:
        response = eval_stmt(env, stmt_or_expr, blacklist)
        if response is not None:
            responses.append(response)
    return responses, env


def parse_file(self, file, mode='exec'):
    pass
