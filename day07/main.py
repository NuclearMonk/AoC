from itertools import chain


class File():

    def __init__(self, name: str, size: int, parent):
        self._name = name
        self._size = size

    def get_size(self):
        return self._size

    def get_name(self):
        return self._name

    def to_string(self, depth) -> str:
        return '\t'*depth + f"-{self._name} (file, size={self.get_size()})"


class Directory(File):
    def __init__(self, name: str, parent):
        self._name = name
        self._dirs = {'..': parent}
        self._files = {}

    def get_size(self):
        return sum(file.get_size() for file in self.get_directories()) + sum(file.get_size() for file in self.get_files())

    def get_directory(self, name):
        if name in self._dirs:
            return self._dirs[name]
        else:
            raise ValueError(f"{name} does not exist in {self._name}")

    def get_directories(self):
        for d, x in self._dirs.items():
            if d != '..':
                yield x

    def get_files(self):
        for d, x in self._files.items():
            if d != '..':
                yield x

    def add(self, string):
        s = string.split()
        if s[1] in self._dirs:
            return
        if s[0] == 'dir':
            self._dirs[s[1]] = Directory(s[1], self)
        else:
            self._files[s[1]] = File(s[1], int(s[0]), self)

    def to_string(self, depth=0) -> str:
        return '\t'*depth + f">{self._name} (dir,size = {self.get_size()}):\n" + "".join(file.to_string(depth+1)+'\n' for file in self.get_files()) + "".join(file.to_string(depth+1)+'\n' for file in self.get_directories())

    def __repr__(self) -> str:
        return f"<Directory: {self._name}>"


def raw_commands(f):
    data = f.read().split('$')
    for i in data:
        yield i


def command_output_pairs(iterable):
    for i in iterable:
        command, *output = i.split('\n')
        if command:
            yield (command.strip(), [o.strip() for o in filter(lambda x: x, output)])


def recreate_from_commands(iterable):
    root = Directory('/', None)
    current_dir = root
    for command, output in iterable:
        match command.split():
            case 'cd', '/':
                current_dir = root
            case 'cd', x:
                current_dir = current_dir.get_directory(x)
            case 'ls', :
                for entry in output:
                    current_dir.add(entry)
    return root


def iter_through_dirs(root: Directory):
    yield root
    for d in root.get_directories():
        for i in iter_through_dirs(d):
            yield i


if __name__ == '__main__':
    total_size = 70000000
    update_size = 30000000
    with open('input.txt', 'r') as f:
        root = recreate_from_commands(command_output_pairs(raw_commands(f)))
        print(sum(map(lambda x:x.get_size(),filter(lambda x : x.get_size()<100000, iter_through_dirs(root)))))
        # free_space = total_size - root.get_size()
        # needed_space = update_size - free_space
        # print(min(filter(lambda x: x >= needed_space, map(
        #     lambda x: x.get_size(), iter_through_dirs(root)))))
