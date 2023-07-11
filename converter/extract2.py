from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pathlib import Path
import shutil
import aspose.slides as asp_slides
import aspose.pydrawing as drawing
import pptx
from docx import Document


def get_image_format(image_type):
    return {
        "jpeg": drawing.imaging.ImageFormat.jpeg,
        "emf": drawing.imaging.ImageFormat.emf,
        "bmp": drawing.imaging.ImageFormat.bmp,
        "png": drawing.imaging.ImageFormat.png,
        "wmf": drawing.imaging.ImageFormat.wmf,
        "gif": drawing.imaging.ImageFormat.gif,
    }.get(image_type, drawing.imaging.ImageFormat.jpeg)


def split_objects(pres_file: str) -> None:
    basename = 'data'
    if Path(basename).exists():
        shutil.rmtree(basename)
        Path(basename).mkdir()
    else:
        Path(basename).mkdir()
    pres1 = Presentation(pres_file)
    pres2 = asp_slides.Presentation(pres_file)
    n_text, n_image, n_links = 0, 0, 0
    sorted_objects, not_sorted_objects, sl_obj_nums = [], [], []
    links_dir = basename + '\\' + 'links'

    for i in range(len(pres1.slides)):
        sl, sl_elems = pres1.slides[i], []
        links = set()

        for sh in sl.shapes:
            num, curr = 0, []
            if sh.has_text_frame:
                for par in sh.text_frame.paragraphs:
                    for run in par.runs:
                        address = run.hyperlink.address
                        if address is None:
                            continue

                        if not Path(links_dir).exists():
                            Path(links_dir).mkdir()
                        n_links += 1
                        num += 1
                        file_name = links_dir + '\\' + f'link_{n_links}'
                        with open(file_name, 'w', encoding='utf-8-sig') as file:
                            file.write(address)
                        links.add(str(address))
                        curr.append([file_name, 'link'])

            if sh.has_text_frame:

                dir_name = basename + '\\' + 'texts'
                if not Path(dir_name).exists():
                    Path(dir_name).mkdir()

                text_frame = sh.text_frame
                if text_frame.paragraphs:
                    num += 1
                    n_text += 1
                    f_name = f'{dir_name}\\text{n_text}.txt'
                    written = False
                    with open(f_name, 'w', encoding='utf-8-sig') as writer:
                        for paragraph in text_frame.paragraphs:
                                text = paragraph.text
                                if text and text not in links:
                                    writer.write(text + '\n')
                                    written = True
                                else:
                                    break
                    if not written:
                        Path(f_name).unlink()
                        n_text -= 1
                    else:
                        curr.append([f_name, 'text'])
                # extracting of hyperlinks

                sl_elems.append(curr)
            # elif sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
            #     n_pic += 1
            #     dir_name = basename + '\\pictures'
            #
            #     if not Path(dir_name).exists():
            #         Path(dir_name).mkdir()
            #
            #     image = sh.image
            #     img_bytes = image.blob
            #     img_filename = f'{dir_name}\\image{str(n_pic)}.{image.ext}'
            #
            #     with open(img_filename, 'wb') as f:
            #         f.write(img_bytes)
            #
            #     sl_elems.extend([img_filename, 'pic'])
            #
            # elif hasattr(sh, 'element') and sh.element.tag.endswith('phMath'):
            #     n_form += 1
            #     formula = sh.text_frame.text
            #     print(f'Найдена формула: {formula}')
            #     dir_name = basename + '\\' + 'formulas'
            #     if not Path(dir_name).exists:
            #         Path(dir_name).mkdir()
            #     file_name = dir_name + '\\' + 'formula{n_form}.txt'
            #     with open(file_name, 'w') as f:
            #         f.write(formula)

            # ???
            # elif sh.has_table:
            # curr = sh.table
            # curr.append('table')
            # sl_elems.append(curr)

            # ???
            # elif sh.has_chart:
            #     curr = []
            #     chart = sh.chart
            #     chart_data = chart.chart_data
            #     curr.extend([chart_data, 'chart'])
            #     sl_elems.append(curr)
# ???
            # elif ' hyperlink ' in sh.part._element.xml or ' action ' in sh.part._element.xml:
            #     text = sh.text_frame.text
            #     href = sh.part._element.rId
            #     n_links += 1
            #     dir_name = basename + '\\' + 'links'
            #     if not Path(dir_name).exists:
            #         Path(dir_name).mkdir()
            #     file_name = dir_name + '\\' + f'{text}{n_links}.txt'
            #     with open(file_name, 'w') as f:
            #         f.write(href)
            #
            #     sl_elems.append([file_name, 'link'])

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
                sl_elems.append(None)

            sorted_objects.append(sl_elems)
            sl_obj_nums.append(len(sl.shapes) - num)

    im_dir, layouts_dir = basename + '\\' + 'images', basename + '\\' + 'layouts'

    # Extracting of images
    if len(pres2.images):
        if not Path(im_dir).exists():
            Path(im_dir).mkdir()
        for image in pres2.images:
            n_image += 1
            file_name = "image_{0}.{1}"
            im_type = image.content_type.split("/")[1]
            im_format = get_image_format(im_type)
            image.system_image.save(im_dir + '\\' + file_name.format(n_image, im_type), im_format)
            file = im_dir + '\\' + file_name.format(n_image, im_type) + f'.{im_format}'
            not_sorted_objects.append([file, 'image'])

    # extracting of background pictures
    slide_index = 0
    for slide in pres2.slides:
        slide_index += 1
        image_format = drawing.imaging.ImageFormat.jpeg
        back_image = None
        file_name = "BackImage_Slide_{0}{1}.{2}"
        is_layout = False

        if slide.background.fill_format.fill_type == asp_slides.FillType.PICTURE:
            back_image = slide.background.fill_format.picture_fill_format.picture.image
        elif slide.layout_slide.background.fill_format.fill_type == asp_slides.FillType.PICTURE:
            back_image = slide.layout_slide.background.fill_format.picture_fill_format.picture.image
            is_layout = True

        if back_image is not None:
            if not Path(layouts_dir).exists():
                Path(layouts_dir).mkdir()
            image_type = back_image.content_type.split("/")[1]
            im_format = get_image_format(image_type)
            file = layouts_dir + '\\' + file_name.format("layout_" if is_layout else "", slide_index, image_type) + f'.{im_format}'
            back_image.system_image.save(file)
            not_sorted_objects.append([file, 'slide_layout'])

    write_json_data(sorted_objects, not_sorted_objects, sl_obj_nums)


def write_json_data(texts: list, objects: list, slide_nums: list) -> None:
    data = {}
    for i in range(len(texts)):
        name = f'slide_{i + 1}'


if __name__ == '__main__':
    pres = r'C:\Users\andre\PycharmProjects\Studying\converter\Test presentation.pptx'
    split_objects(pres)



