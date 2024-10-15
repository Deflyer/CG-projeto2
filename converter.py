def convert_quads_to_triangles(input_obj, output_obj):
    with open(input_obj, 'r') as infile, open(output_obj, 'w') as outfile:
        for line in infile:
            if line.startswith('f '):
                vertices = line.split()[1:]
                if len(vertices) == 4:  # If it's a quad, split it into two triangles
                    outfile.write(f"f {vertices[0]} {vertices[1]} {vertices[2]}\n")
                    outfile.write(f"f {vertices[0]} {vertices[2]} {vertices[3]}\n")
                else:
                    outfile.write(line)  # Leave triangles or other faces untouched
            else:
                outfile.write(line)  # Copy other lines (e.g., vertex definitions) as is

# Call the function with input and output .obj filenames
convert_quads_to_triangles('objetos/uploads_files_4053544_house+creep.obj', 'objetos/casa.obj')