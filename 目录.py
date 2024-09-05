
from typing import List
class Node:
    def __init__(self, name=None):
        self.name = name
        self.file = []
        self.dir = dict()

class FileSystem:
    def __init__(self):
        self.root = Node(['/'])
        self.cur = self.root

    def make_dir(self, dir_name):
        if dir_name in self.cur.dir or dir_name in self.cur.file:
            return False
        else:
            node = Node(dir_name)
            self.cur.dir[dir_name] = node
            return True

    def create_file(self, file_name):
        if file_name in self.cur.dir or file_name in self.cur.file:
            return False
        else:
            self.cur.file.append(file_name)
            return True

    def change_dir(self, path_name: str):
        if path_name == "":
            return True
        if path_name == '/':
            self.cur = self.root
            return True
        if path_name[-1] == '/':
            path_name = path_name[:-1]

        if path_name[0] == '/':
            cur = self.root
            path = path_name[1:].split('/')
            for i in range(len(path)):
                if path[i] in cur.dir:
                    cur = cur.dir[path[i]]
            if cur.name == path[-1]:
                self.cur = cur
                return True
            return False

        else:
            cur = self.cur
            path = path_name.split('/')
            for i in range(len(path)):
                if path[i] in cur.dir:
                    cur = cur.dir[path[i]]
            if cur.name == path[-1]:
                self.cur = cur
                return True
            return False

    def remove(self, name):
        if name in self.cur.dir:
            del self.cur.dir[name]
            return True
        elif name in self.cur.file:
            self.cur.file.pop()
            return True
        else:
            return False

    def list_dir(self):
        dir = sorted(self.cur.dir.keys())
        file = sorted(self.cur.file)
        res = dir + file
        return res

a = FileSystem()
# print(a.make_dir('dirc'))
# print(a.make_dir('dirb'))
# print(a.make_dir('dirc'))
# print(a.list_dir())
# print(a.change_dir('dirc/'))
# print(a.create_file('fileb'))
# print(a.make_dir('dirb'))
# print(a.create_file('dirb'))
# print(a.list_dir())
# print(a.change_dir('/dirb/dirc'))


print(a.list_dir())
print(a.change_dir(''))
print(a.create_file('gateway'))
print(a.make_dir('home'))
print(a.change_dir('gateway'))
print(a.make_dir('etc'))
print(a.list_dir())
print(a.remove('gateway'))
print(a.change_dir('etc/'))
print(a.create_file('pip'))
print(a.change_dir('/etc/'))
print(a.list_dir())
print(a.change_dir('/'))
print(a.remove('etc'))
print(a.list_dir())