# 导入
from docx import Document
# 从文件创建文档对象
document = Document('./test.docx');

paragraph = document.add_paragraph()
styles = document.style;
# print(styles.name);
# # 显示每段的内容
# for p in document.paragraphs:
# 	print('***********************');
# 	print(p.paragraph_format)
# 	print(p.text);
# # 添加段落
# document.add_paragraph('这是新的段落内容');
# # 保存文档
# document.save('demo.docx');