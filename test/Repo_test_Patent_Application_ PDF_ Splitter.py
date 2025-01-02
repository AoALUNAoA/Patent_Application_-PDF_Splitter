# Author: LUN
# Email: lun@tmy.red
# version: 1.0

import PyPDF2

def split_pdf(input_path, output_path, keywords):
    # 打开专利申请PDF文档
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # 存储关键词出现的页码
        pages = {keyword: None for keyword in keywords}
        # 查找关键词出现的页码
        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text()
            for keyword in keywords:
                if keyword in text and pages[keyword] is None:
                    pages[keyword] = page_num

        # 确保所有关键词都被找到
        if None in pages.values():
            missing_keywords = [k for k, v in pages.items() if v is None]
            raise ValueError(f"以下关键词没有在文档中找到: {missing_keywords}")

        # 根据关键词出现的页码，分割专利申请五书PDF
        for i, keyword in enumerate(keywords):
            start_page = pages[keyword]
            # 如果不是最后一个关键词，结束页码是下一个关键词的前一页
            end_page = pages[keywords[i + 1]] - 1 if i < len(keywords) - 1 else len(reader.pages) - 1
            # 检查页码范围
            if start_page is not None and (0 <= start_page < len(reader.pages)):
                end_page = min(end_page, len(reader.pages) - 1)
                # 创建子PDF文档
                pdf_writer = PyPDF2.PdfWriter()
                for page_num in range(start_page, end_page + 1):
                    pdf_writer.add_page(reader.pages[page_num])
                # 输出子PDF文档
                with open(f'{output_path}/{keyword}.pdf', 'wb') as output_file:
                    pdf_writer.write(output_file)
            else:
                print(f"关键词'{keyword}'的起始页码不在文档范围内。")

# 指定文档输入路径和输出路径
input_path = 'sample application file.pdf'
output_path = ''

# 指定关键词
keywords = ['说  明  书  摘  要', '摘   要   附   图', '权  利  要  求  书', '说     明     书', '说  明  书  附  图']

# 调用函数
split_pdf(input_path, output_path, keywords)
