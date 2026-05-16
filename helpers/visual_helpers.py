def color_element(element, color='red', fon='yellow'):
    element.evaluate(f"""
        (element) => {{
            element.style.border = '3px solid {color}';
            element.style.backgroundColor = '{fon}';  
            element.style.transition = '0.3s';
        }}
    """)

def closing_element(element):
    element.evaluate("""
        (element) => {
            element.style.border = '';
            element.style.backgroundColor = '';
        }
    """)