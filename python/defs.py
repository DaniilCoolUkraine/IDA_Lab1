from sys import platform


def get_path():
    primary = "dataset/"
    if platform == 'linux':
        return primary
    else:
        return "python/" + primary

