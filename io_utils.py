def read_file(path):
    with open(path, 'r') as f:
        return f.read().strip()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content.strip())
