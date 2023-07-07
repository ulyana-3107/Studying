from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pathlib import Path
import shutil
from docx import Document


def split_objects(pres_file: str) -> list:
    basename = 'data'
    if Path(basename).exists():
        shutil.rmtree(basename)
        Path(basename).mkdir()
    else:
        Path(basename).mkdir()

    n_pic, n_text, n_part = 0, 0, 0
    pres = Presentation(pres_file)
    objects = []

    for i in range(len(pres.slides)):
        sl, sl_elems = pres.slides[i], []

        for sh in sl.shapes:

            if sh.has_text_frame:
                curr = []
                dir_name = basename + '\\' + 'texts'
                if not Path(dir_name).exists():
                    Path(dir_name).mkdir()

                text_frame = sh.text_frame
                if text_frame.paragraphs:
                    n_text += 1
                    f_name = f'{dir_name}\\text{n_text}.txt'
                    with open(f_name, 'w', encoding='utf-8-sig') as writer:
                        for paragraph in text_frame.paragraphs:
                            text = paragraph.text
                            if text:
                                writer.write(text + '\n')
                    curr.extend([f_name, 'text'])
                else:
                    curr.append(None)

                sl_elems.append(curr)

            # Later
            # elif sh.has_table:
            #     table = sh.table
            #     for row in table.rows:
            #         for cell in row.cells:
            #             text = cell.text
            #             if text:
            #                 curr.append(('table', text))
            #
            # elif sh.has_chart:
            #     chart = sh.chart
            #     chart_data = chart.chart_data
            #     if chart_data:
            #         curr.append(('chart', chart_data))

            elif sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
                n_pic += 1
                dir_name = basename + '\\pictures'

                if not Path(dir_name).exists():
                    Path(dir_name).mkdir()

                image = sh.image
                img_bytes = image.blob
                img_filename = f'{dir_name}\\image{str(n_pic)}.{image.ext}'

                with open(img_filename, 'wb') as f:
                    f.write(img_bytes)

                sl_elems.extend([img_filename, 'pic'])

            # UNDERDONE!!!
            elif sh.shape_type == MSO_SHAPE_TYPE.PLACEHOLDER:
                pass
            # elif sh.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE:
            #     n_part += 1
            #     auto_sh = sl.shapes.add_shape(sh.auto_shape_type, sh.left, sh.top, sh.width, sh.height)
            #     img_path = f'{basename}\\pictures\\{sl.slide_id}_{auto_sh.shape_id}{str(n_part)}.jpeg'
            #     auto_sh.image.save(img_path)
            #     curr.append(('picture', img_path))

            # elif sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            #     n_group += 1
            #     group_shape = sl.shapes.add_group_shape()
            #     for member_shape in sh.shapes:
            #         member_shape._element.add_to_group(group_shape._element)
            #     group_shape.crop_left = Inches(0)
            #     img_path = f"{sl.slide_id}_{sh.shape_id}{str(n_group)}.jpeg"
            #     sl.save_picture(img_path, group_shape.left, group_shape.top, group_shape.width, group_shape.height)
            #     # удаление временного объекта
            #     sl.shapes._spTree.remove(group_shape._element)
            else:
                sl_elems.append([None])

            objects.append(sl_elems)

    return objects


if __name__ == '__main__':
    pres = r'C:\Users\andre\PycharmProjects\Studying\converter\Test presentation.pptx'
    pres_objects = split_objects(pres)
    for sl_elems in pres_objects:
        print(sl_elems)