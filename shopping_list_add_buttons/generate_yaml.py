import sys
import os
import glob


def generate_button(value):
    text_entity = "text.shopping_add_text"

    return f"""
  - show_name: true
    show_icon: false
    type: button
    name: {value}
    tap_action:
      action: call-service
      service: text.set_value
      data:
        value: {value}
      target:
        entity_id: {text_entity}
    show_state: false
    icon: mdi:checkbox-marked-circle-plus-outline
    grid_options:
      columns: 3
      rows: 1
    """.rstrip()

def generate_heading(value):
    return f"""
  - type: heading
    heading: {value}
    heading_style: title"""


def generate_yaml(input_file, output_file):
    try:
        #Use filename as our title
        title =  os.path.splitext(input_file)[0].capitalize()
        
        #open the file
        with open(input_file, 'r', encoding='utf-8') as file:
            groceries = [line.strip() for line in file.readlines()]

        #Grid card
        output = "type: grid\ncards:"
        
        #output += generate_heading(title)
        for item in groceries:
            if item:
                output += generate_button(item)

        #Remove newlines at beginning
        output = output.lstrip("\n")
        

        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(output)

    except FileNotFoundError:
        print("Error: Input file not found. Please provide a valid file path.")

# Example usage:
txt_files = glob.glob("*.txt")

try:
    os.makedirs("out", exist_ok=True)
except:
    pass

#Generate files fo all our txt files
for input_file in txt_files:
    output_file = f"out/{input_file}"
    generate_yaml(input_file, output_file)

