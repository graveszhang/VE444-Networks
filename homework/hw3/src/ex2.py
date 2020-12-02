from util import Edge
from util import Vertex
import numpy as np
import matplotlib.pyplot as plt

class FriendNet:
    def __init__(self):
        self.mapping = dict() ## map name to id
        self.employee_node = []
        self.employee_name = []
        self.friends = []
        self.num_friend = 0
        self.num_employee = 0
        self.degree = []

    def AddEmployee(self, name):
        if name not in self.employee_name:
            new_employee = Vertex(name)
            self.employee_name.append(name)
            self.employee_node.append(new_employee)
            self.mapping[name] = self.num_employee
            self.num_employee += 1
            self.degree.append(0)
        else:
            print('This employee is already in the network!')

    def AddFriend(self, name_a, name_b, score):
        if name_a not in self.employee_name:
            self.AddEmployee(name_a)
        if name_b not in self.employee_name:
            self.AddEmployee(name_b)

        friendship = Edge(name_a, name_b, score)
        if friendship not in self.friends:
            self.friends.append(friendship)
            index_a = self.mapping[name_a]
            index_b = self.mapping[name_b]
            self.degree[index_a] += 1
            self.degree[index_b] += 1
            self.num_friend += 1
        else:
            print('They are already friends!')

    def plot(self):
        x = np.arange(8)
        plt.bar(self.employee_name, height=self.degree)
        plt.xticks(x, self.employee_name)
        plt.xlabel('Employees')
        plt.ylabel('Degree')
        plt.legend(loc="best")
        plt.savefig('Degree.png')
        plt.show()

if __name__ == '__main__':
    Mynet = FriendNet()
    f = open("Employee_Relationships.txt")
    lines = f.readlines()
    for line in lines:
        score = int(line.split()[-1])
        if score > 0:
            EmployeeA = line.split()[0]
            EmployeeB = line.split()[1]
            Mynet.AddFriend(EmployeeA, EmployeeB, score)
    f.close()
    Mynet.plot()

