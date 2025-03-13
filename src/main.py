
from template_manager import load_template, print_layouts, get_layout_mapping
from input_parser import parse_input_text
from ppt_generator import generate_presentation
input_text = """
# 人类历史之光

## 人类历史之光 [Title Only]

## 历史十大人物 [Title and Content]
- xxx
- xxx

## 近代史十大人物 [Title and Content]
- xxx
- xxx
![名人肖像](images/farmous.png)
"""

def main():

    template_file = 'templates/Template.pptx'
    prs = load_template(template_file)

    print("Slide Layouts: ")
    print_layouts(prs)

    layout_mapping = get_layout_mapping(prs)

    powerpoint_data, presentation_title = parse_input_text(input_text, layout_mapping)

    output_pptx = f"outputs/{presentation_title}.pptx"
    generate_presentation(powerpoint_data, template_file, output_pptx)

if __name__ == '__main__':
    main()





