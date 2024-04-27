from re import search
from pathlib import Path


def run():
    for x in Path(Path.cwd()).rglob(r'*.lnk'):
        r = r'([^\\]*)\.lnk'
        print(x)
        try:
            new_name = search(r, str(x))[0].replace(" - 快捷方式.lnk", '').replace(".exe", '')
            print(new_name)
        except TypeError:
            continue
        new_file = Path(x).with_name(new_name + '.lnk')
        x.replace(new_file)


if __name__ == '__main__':
    run()
