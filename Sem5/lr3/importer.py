import re
import sys
from urllib.request import urlopen
from importlib.abc import PathEntryFinder
from importlib.util import spec_from_loader

class URLLoader:
    def create_module(self, target):
        return None
    
    def exec_module(self, module):
        with urlopen(module.__spec__.origin) as page:
            source = page.read()
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)

class URLFinder(PathEntryFinder):
    def __init__(self, url, available):
        self.url = url
        self.available = available
        
    def find_spec(self, name, target=None):
        if name in self.available:
            origin = "{}/{}.py".format(self.url, name)
            loader = URLLoader()
            return spec_from_loader(name, loader, origin=origin)
        else:
            return None

def url_hook(url):
    if not url.startswith(("http", "https")):
        raise ImportError
    with urlopen(url) as page:
        data = page.read().decode("utf-8")
    filenames = re.findall("[a-zA-Z_][a-zA-Z0-0_]*.py", data)
    modnames = {name[:-3] for name in filenames}
    return URLFinder(url, modnames)

sys.path_hooks.append(url_hook)

if __name__ == "__main__":
    url_path1 = 'https://github.com/iamgo100/python-course/tree/master/Sem5/lr3/package'
    # url_path2 = 'http://localhost:8000'
    sys.path.append(url_path1)
    # sys.path.append(url_path2)

    import useful
    print(useful)
    # import calc
    # calc.main()