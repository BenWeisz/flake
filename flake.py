from ast import build_ast

if __name__ == "__main__":
    with open("template.flake", "r") as in_file:
        lines = in_file.readlines()
    
    ast = build_ast(lines)
    print(ast)