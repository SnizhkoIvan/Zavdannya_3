import os
import docx
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

doc = Document()

# Налаштування полів сторінки (Верхнє, Нижнє, Праве: 2 см; Ліве: 2.5 см)
for section in doc.sections:
    section.top_margin = Inches(0.79)
    section.bottom_margin = Inches(0.79)
    section.left_margin = Inches(0.98)
    section.right_margin = Inches(0.79)

def p(text, align=WD_ALIGN_PARAGRAPH.LEFT, bold=False, italic=False, size=11, space_after=4, space_before=0, color=None):
    paragraph = doc.add_paragraph()
    paragraph.alignment = align
    paragraph.paragraph_format.space_after = Pt(space_after)
    paragraph.paragraph_format.space_before = Pt(space_before)
    r = paragraph.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    if color:
        r.font.color.rgb = color
    return paragraph

def add_code_block(code_text):
    table = doc.add_table(rows=1, cols=1)
    table.autofit = False
    cell = table.cell(0, 0)
    set_cell_background(cell, "F4F4F4")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    cp = cell.paragraphs[0]
    cp.paragraph_format.space_after = Pt(2)
    cp.paragraph_format.space_before = Pt(2)
    run = cp.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0x1E, 0x1E, 0x1E)

# --- ТИТУЛЬНА СТОРІНКА ---
p("МІНІСТЕРСТВО ОСВІТИ І НАУКИ УКРАЇНИ\nНАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ БІОРЕСУРСІВ І ПРИРОДОКОРИСТУВАННЯ УКРАЇНИ\nФакультет інформаційних технологій", WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=12)

doc.add_paragraph().paragraph_format.space_before = Pt(72)
p("ЗВІТ\nз лабораторної роботи №5\nна тему: «Обробка текстових даних, кодувань та серіалізація об'єктів у Python»", WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=16)

doc.add_paragraph().paragraph_format.space_before = Pt(96)
p("Виконав:\nстудент групи ІТ-31\nСніжко І.О.\n\nПеревірив:\nвикладач _____________", WD_ALIGN_PARAGRAPH.RIGHT, size=12)

doc.add_paragraph().paragraph_format.space_before = Pt(72)
p("Київ – 2026", WD_ALIGN_PARAGRAPH.CENTER, size=12)

doc.add_page_break()

# --- ТЕКСТ ЗАВДАННЯ ---
p("1. Текст завдання", bold=True, size=14, space_after=6)
task_text = (
    "Мета роботи: Ознайомитися з методами обробки текстових даних, кодуваннями та серіалізацією об'єктів у формат JSON.\n\n"
    "Завдання:\n"
    "1. Створити віртуальне оточення (Snizhko).\n"
    "2. Програма 1: Створити текстовий файл з ПІБ та фрагментом тексту. Реалізувати алгоритм сортування слів: "
    "спочатку українські літери (незалежно від регістру), потім латинські літери.\n"
    "3. Програма 2: Отримати інтернет-посилання з кирилицею у %-кодуванні (Punycode), декодувати його у читабельний формат та скопіювати в буфер обміну.\n"
    "4. Програма 3: Створити словник з 10+ записів українською мовою, зберегти його у JSON файл у кодуванні UTF-8 (з збереженням літер, а не кодів) та зчитати його.\n"
    "5. Зберегти списки модулів у requirements.txt та завантажити проєкт на GitHub."
)
p(task_text, size=11, space_after=12)

# --- КОДИ ПРОГРАМ ---
p("2. Коди програм", bold=True, size=14, space_after=6)

files_to_include = [
    ("Код програми 1 (prog1_sort.py):", "prog1_sort.py"),
    ("Код програми 2 (prog2_url.py):", "prog2_url.py"),
    ("Код програми 3 (prog3_json.py):", "prog3_json.py")
]

for title, fname in files_to_include:
    p(title, bold=True, size=12, space_before=6, space_after=4)
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf-8") as f:
            add_code_block(f.read())
    else:
        add_code_block(f"# Файл {fname} не знайдено")

# --- СКУРІНШОТИ ТА СИСТЕМА ---
doc.add_paragraph().paragraph_format.space_before = Pt(12)
p("3. Результати виконання та скріншоти", bold=True, size=14, space_after=6)

p("Нижче наведено місця для вставки підтверджуючих скріншотів виконання у віртуальному оточенні Snizhko:")

p("[Вставити скріншот повного вікна VS Code з кодом програми 1]", italic=True, space_after=4, color=RGBColor(0x7F, 0x7F, 0x7F))
p("[Вставити скріншот виконання програми 1 у терміналі (Snizhko)]", italic=True, space_after=4, color=RGBColor(0x7F, 0x7F, 0x7F))
p("[Вставити скріншот виконання програми 2 з копіюванням у буфер обміну]", italic=True, space_after=4, color=RGBColor(0x7F, 0x7F, 0x7F))
p("[Вставити скріншот виконання програми 3 у терміналі]", italic=True, space_after=4, color=RGBColor(0x7F, 0x7F, 0x7F))
p("[Вставити скріншот створеного файлу students_data.json у Блокноті з коректною кирилицею]", italic=True, space_after=4, color=RGBColor(0x7F, 0x7F, 0x7F))
p("[Вставити скріншот терміналу з версією Python (python --version)]", italic=True, space_after=4, color=RGBColor(0x7F, 0x7F, 0x7F))
p("[Вставити скріншот терміналу з виконанням команди pip list]", italic=True, space_after=12, color=RGBColor(0x7F, 0x7F, 0x7F))

p("Посилання на GitHub-репозиторій проєкту:", bold=True, size=11, space_after=2)
p("https://github.com/vanya-snizhko/lab_project", size=11, color=RGBColor(0x00, 0x00, 0xEE))

output_filename = "Звіт_Лабораторна_5_Сніжко.docx"
doc.save(output_filename)
print(f"✅ Файл успішно створено: {output_filename}")