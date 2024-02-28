import os
import subprocess
import shutil
from Templates import BinaryTree
from Templates import Node as Node1

def create_file():

    folder_name = "compile"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open('preloaded/template.txt', 'r') as f1:
        with open('compile/main.tex', 'w') as f2:
            f2.write(f1.read())

def check_files(Name, PreTopics):
    folder_name = "algorithms"
    print("Do you want to add all the files to the document? 1)Yes 2)No")
    op=int(input())
    if op==1:
        for filename in os.listdir(folder_name):
            file_path = os.path.join(folder_name, filename)
            with open(file_path, 'r') as f1:
                topic = search_topic(f1.read())
                #topic = del_parenthesis(topic)
                #print(topic, filename)
                Name.add_file(Node(topic, filename),PreTopics)
    else:
        for filename in os.listdir(folder_name):
            file_path = os.path.join(folder_name, filename)
            with open(file_path, 'r') as f1:
                topic = search_topic(f1.read())
                #topic = del_parenthesis(topic)
                #print(topic, filename)
                print("Do you want to add "+filename+" to the document? 1)Yes 2)No")
                op=int(input())
                if op==1:
                    Name.add_file(Node(topic, filename),PreTopics)


def end_file():
    with open('compile/main.tex', 'a') as f:
        f.write("\\end{multicols}\n")
        f.write("\\end{document}\n")    
    

def del_parenthesis(text):
    my_string = ""
    i=0
    while True:
        char = text[i]
        if char == '(' or char == ' ':
            break
        my_string += char
        i += 1
    return my_string

def bin_search(topic, PreTopics):
    left = 0
    right = len(PreTopics) - 1
    while left <= right:
        mid = (left + right) // 2
        if PreTopics[mid][0] == topic:
            return PreTopics[mid][1]
        elif PreTopics[mid][0] < topic:
            left = mid + 1
        else:
            right = mid - 1
    return None

def search_topic(text):
    words = iter(text.split())
    for word in words:
        if word[0] == '/' and word[1] == '/':
            if len(word) > 2:
                return word[2:]
            else:
                return next(words)
        
class Node:
    def __init__(self, topic, filename):
        self.topic = topic
        self.filename = filename
        self.children = []

class Graph:
    def __init__(self, start_node):
        self.initialVertex = start_node
        self.initialVertex.children = []

    def check_topic(self, topic):
        return self._check_topic(topic, self.initialVertex)
    
    def _check_topic(self, topic, node):
        for child in node.children:
            if child.topic == topic:
                return True
        return False

    def add_topic(self, topic):
        new_node = Node(topic, None)
        self.initialVertex.children.append(new_node)

    def add_node(self, Node, Island):
        for child in self.initialVertex.children:
            if child.topic == Island:
                child.children.append(Node)
                return


    def add_file(self, Node, PreTopics):
        Island=bin_search(Node.topic, PreTopics)
        if Island is None:
            Island = "Others"
        if not self.check_topic(Island):
            self.add_topic(Island)
        self.add_node(Node,Island)

    def print_graph(self, node=None, indent=0):
        if node is None:
            node = self.initialVertex
        if node.filename is None:
            print(" " * indent + node.topic)
        else:
            print(" " * indent + node.topic+" "+str(node.filename))
        for child in node.children:
            self.print_graph(child, indent + 2)
        
    def writeTex(self, node=None, indent=0):
        global i
        i += 1
        if node is None:
            node = self.initialVertex
        #print(" " * indent + node.topic+" "+str(node.filename))
        if node.filename is None and node != self.initialVertex:
            with open('compile/main.tex', 'a') as f:
                f.write("\\section{"+node.topic.replace('_',' ')+"}\n")
                #f.write(str(i))
                #f.write("\n")
                #print(i)
        elif node.filename is not None:
            with open('compile/main.tex', 'a') as f:
                f.write("\\subsection{"+node.topic.replace('_',' ')+"}\n")
                #f.write("\\lstinputlisting[language=C++]{algorithms/"+node.filename+"}\n")
                f.write("\\begin{lstlisting}[linewidth=\columnwidth,breaklines=true,language=C++]")
                #f.write(str(i))
                f.write("\n")
                #print(i)
                with open('algorithms/'+node.filename, 'r') as f1:
                    f.write(f1.read())
                f.write("\\end{lstlisting}\n")
        for child in node.children:
            self.writeTex(child, indent + 2)


def pre_topics(PreTopics):
    with open('preloaded/topics.txt', 'r') as f:
        for line in f:
            words = line.strip().split()
            if len(words) == 2:
                PreTopics.append((words[0], words[1]))

def Quick_sort(PreTopics):
    if len(PreTopics) <= 1:
        return PreTopics
    pivot = PreTopics[len(PreTopics) // 2][0]
    left = []
    middle = []
    right = []
    for topic in PreTopics:
        if topic[0] < pivot:
            left.append(topic)
        elif topic[0] == pivot:
            middle.append(topic)
        else:
            right.append(topic)
    return Quick_sort(left) + middle + Quick_sort(right)
    
def print_pre_topics(PreTopics):
    for topic in PreTopics:
        print(topic)


templateTree=BinaryTree()
for template in os.listdir('preloaded_templates'):
    file_name=os.path.basename(template)
    #print(file_name[len(file_name)-3:])
    if(file_name[len(file_name)-3:]=='tex'):
        templateTree.insert(templateTree.root, Node1(file_name, None, None))

print('Would you like to see preloaded templates? 1)Yes 2)No')
op=int(input())
if op==1:
    while True:
        templateTree.print_post(templateTree.root)
        print('Which template would you like to access->input the name of the file?')
        file_to_open=input()
        if templateTree.search(templateTree.root, file_to_open)==True:
            subprocess.run(['open', 'preloaded_templates/'+file_to_open], check=True)
        else:
            print('File does not exist')
        op1=int(input('Would you like to open another file? 1)Yes 2)No\n'))
        if op1!=1:
            break

PreTopics = []
pre_topics(PreTopics)
PreTopics = Quick_sort(PreTopics)
#print_pre_topics(PreTopics)
Generator = Graph(Node("start", None))
create_file()
check_files(Generator, PreTopics)
i=0
Generator.writeTex()

end_file()
Generator.print_graph()

op3=int(input('Would you like to add this file to existing templates? 1)Yes 2)No\n'))
if(op3==1):
    while True:
        new_file_name=input('Insert the name of the new template\n')
        if templateTree.search(templateTree.root, new_file_name)==False:
            break
        else:
            print('Name already exists, try again')

    shutil.copy2('compile/main.tex', 'preloaded_templates/'+new_file_name)
