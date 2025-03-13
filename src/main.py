
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

if __name__ == '__main__':
    template_file = 'templates/Template.pptx'
    prs = load_template(template_file)

    print("Slide Layouts: ")
    print_layouts(prs)

    layout_mapping = get_layout_mapping(prs)




