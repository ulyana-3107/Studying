import pylatex
from pylatex import Document, Section, Subsection, Command, Figure
from extract2 import split_objects
from pathlib import Path
import json
import argparse


def split_text(text: str, length: int) -> list:
    arr, t = [], ''
    for i, l in enumerate(text):
        t += l
        if not i % length and i != 0:
            arr.append(t)
            t = ''
    if len(text) % length:
        arr.append(t)

    return arr


def create_latex_file(data: dict, output_file):
    if Path(output_file + '.tex').exists():
        Path(output_file + '.tex').unlink()
        Path(output_file + '.tex').touch()
    g_options = {"tmargin": "1cm", "lmargin": "10cm"}
    doc = Document(geometry_options=g_options)

    for slide in data.values():
        if slide:
            for p, t in slide.items():
                if t == 'text':
                    # with doc.create(Section(f'Text_{texts}')):
                    f = open(p, 'r', encoding='utf-8-sig')
                    text = f.read()
                    if len(text) > 90:
                        all_texts = split_text(text, 90)
                        for text in all_texts:
                            doc.append(text + '\n')
                    else:
                        doc.append(text + '\n')
                    f.close()

                elif t == 'link':
                    # with doc.create(Section(f'Hyperlink_{links}')):
                    f = open(p, 'r', encoding='utf-8-sig')
                    link = f.read()
                    doc.append(link + '\n')
                    f.close()

                elif t == 'image':
                    with doc.create(Figure(position='h!')) as pic:
                        pic.add_image(p, width='120px')

        doc.append('\n'*3)

    doc.generate_pdf(output_file, clean_tex=False)


def read_json(js_file: str):
    with open(js_file, 'r') as read_file:
        result = json.load(read_file)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pres', type=str, help='path to the Presentation')
    parser.add_argument('output_file', type=str, help='name of output file withud extension')
    args = parser.parse_args()
    js_file = split_objects(args.pres)
    data = read_json(js_file)
    create_latex_file(data, args.output_file)
