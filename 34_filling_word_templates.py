# https://blog.formpl.us/how-to-generate-word-documents-from-templates-using-python-cb039ea2c890
# https://github.com/Vnessah/docx-gen/blob/master/generate.py
from docx.shared import Pt
from docxtpl import DocxTemplate, InlineImage

tmplPath = "assets/docxtpl/template_example.docx"

doc = DocxTemplate(tmplPath)

context = {
    'yr_str': "2020-21",
    'wk_num': 18,
    'st_dt': '01.Aug.2020',
    'end_dt': '08.Aug.2020',
    'major_gen_outages': [
        {
            'name': 'unit_name1',
            'owner': 'owner1',
            'capacity': 'Capacity1',
            'outage_time_str': '12:09',
            'outage_date_str': '01-Aug-2020',
            'revival_time_str': '15:38',
            'revival_date_str': '06-Aug-2020',
            'reason': 'REASON 1'
        },
        {
            'name': 'unit_name2',
            'owner': 'owner2',
            'capacity': 'Capacity2',
            'outage_time_str': '22:09',
            'outage_date_str': '02-Aug-2020',
            'revival_time_str': '25:28',
            'revival_date_str': '06-Aug-2020',
            'reason': 'REASON 2'
        },
        {
            'name': 'unit_name3',
            'owner': 'owner3',
            'capacity': 'Capacity3',
            'outage_time_str': '21:09',
            'outage_date_str': '03-Aug-2020',
            'revival_time_str': '03:38',
            'revival_date_str': '06-Aug-2020',
            'reason': 'REASON 3'
        }
    ]
}

# signature Image
signatureImgPath = 'assets/docxtpl/signature.png'
signImg = InlineImage(doc, signatureImgPath)
context['signature'] = signImg

doc.render(context)
doc.save("assets/docxtpl/report_created.docx")
