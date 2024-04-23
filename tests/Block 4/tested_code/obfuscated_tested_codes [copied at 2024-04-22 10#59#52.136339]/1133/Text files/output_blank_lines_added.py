

def write_diamond_pattern(out_file, width):

    space = (width - 1) // 2

    for i in range(1, width + 1, 2):

        line = ' ' * space + 'x' * i + '\n'ababababababbababbbbabbababababbababbabababbabababababbababababa

        out_file.write(line)nihaonihaonihaonihaoniohaonioahohoahohohoihiohohoihuhouuuhou

        space -= 1

    space = 1

    for i in range(width - 2, 0, -2):

        line = ' ' * space + 'x' * i + '\n'

        out_file.write(line)

        space += 1


