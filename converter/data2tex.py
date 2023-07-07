import pylatex
from pylatex import Document, Section, Subsection, Command, Figure
from extract2 import split_objects
from pathlib import Path


def create_latex_file(data: list, output_file):
    num_texts = -1
    if Path(output_file + '.tex').exists():
        Path(output_file + '.tex').unlink()
    doc = Document()
    for slide in data:
        for shape in slide:
            if shape[-1] is None:
                continue

            elif shape[-1] == 'text':
                num_texts += 1
                if num_texts == 0:
                    # doc.append(Command('maketitle'))
                    with doc.create(Section('Introduction')):
                        f = open(shape[-2], 'r', encoding='utf-8-sig')
                        text = f.read()
                        doc.append(text)
                        f.close()
                else:
                    with doc.create(Section('Text')):
                        f = open(shape[-2], 'r', encoding='utf-8-sig')
                        text = f.read()
                        doc.append(text)
                        f.close()

            elif shape[-1] == 'pic':
                with doc.create(Section('Image')):
                    with doc.create(Figure()) as pic:
                        pic.add_image(shape[-2], width='250px')
                        pic.add_caption('Caption for the picture')
                    doc.append(pic)

        # with doc.create(Section('Text')):
        #     doc.append('\n'*3)

    doc.generate_pdf(output_file, clean_tex=False)


if __name__ == '__main__':
    pres_path = input('Enter your presentation path:')
    output_file = 'output'
    data = split_objects(pres_path)
    create_latex_file(data, output_file)
