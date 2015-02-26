if __name__ == '__main__':
    import sys
    import ast
    alister = ast.literal_eval(sys.argv[1])
    for line in alister:
        print line
