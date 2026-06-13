#Task1

from html.parser import HTMLParser


# Клас вузла дерева
class Node:
    def __init__(self, tag, text=""):
        self.tag = tag
        self.text = text
        self.children = []

    def add_child(self, node):
        self.children.append(node)


# Клас парсера HTML
class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node("document")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        new_node = Node(tag)
        self.stack[-1].add_child(new_node)
        self.stack.append(new_node)

    def handle_endtag(self, tag):
        if len(self.stack) > 1:
            self.stack.pop()

    def handle_data(self, data):
        text = data.strip()
        if text:
            current_node = self.stack[-1]
            if current_node.text:
                current_node.text += " " + text
            else:
                current_node.text = text


# Функція пошуку тексту за тегом
def find_text_by_tag(node, tag):
    result = []

    if node.tag == tag and node.text:
        result.append(node.text)

    for child in node.children:
        result.extend(find_text_by_tag(child, tag))

    return result


# ----------------------------
# Введення даних з клавіатури
# ----------------------------

print("Введіть HTML документ построково.")
print("Коли завершите введення, напишіть: END")

lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

html_doc = "\n".join(lines)

tag_to_find = input("Введіть тег для пошуку: ")

parser = MyHTMLParser()
parser.feed(html_doc)

texts = find_text_by_tag(parser.root, tag_to_find)

print("\nРезультат пошуку:")
if texts:
    for i, text in enumerate(texts, 1):
        print(f"{i}. {text}")
else:
    print("Текст для цього тегу не знайдено.")