import toml

with open('config.toml') as f:
    config = toml.load(f)

with open('template.svg') as f:
    svg_template = f.read()

for key, value in config.items():
    width = value['width']
    height = value['height']
    size = value['size']
    if value['type'] == 'image':
        text = f"""<image x="315" y="315" width="{size}" height="{size}" xlink:href="../icons/{value['text']}" />"""
    elif value['type'] == 'text':
        text = f"""<text x="20%" y="35%" fill="#333333" font-size="{size}" font-family="CourierPrime-Regular" text-anchor="start" alignment-baseline="hanging">{value['text']}</text>"""
    output_file = f"./keys/{key}.svg"
    svg_output = svg_template.replace('<key_value />', text).replace('svg_width', str(width)).replace('svg_height', str(height)).replace('width_200', str(width-200)).replace('height_200', str(height-200)).replace('svg_viewbox', f"0 0 {width} {height}")
    with open(output_file, 'w') as f:
        f.write(svg_output)
