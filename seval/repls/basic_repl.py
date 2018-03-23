from seval.seval import parse_string
from seval import global_env

def main():
    env = global_env.globalenv

    while True:
        x = input("> ")
        responses, env = parse_string(env, x)
        for r in responses:
            print(repr(r))


if __name__ == "__main__":
    main()
