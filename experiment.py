import mmap
import re
with open("/home/dfadeev/pp-complete.csv", "r+") as file:
    with mmap.mmap(file.fileno(), 0) as m:
        # Слова, начинающиеся с заглавной буквы
        pattern = re.compile(rb'\b[A-Z].*?\b')
        for match in pattern.findall(m):
            print(len(pattern.findall(m)))
            # b'Lorem'
            # b'Morbi'
            # b'Nullam'
            # ...
        # Удалить первые 10 символов
        start = 0
        end = 10
        length = end - start
        size = len(m)
        new_size = size - length
        m.move(start, end, size - end)
        m.flush()
    file.truncate(new_size)