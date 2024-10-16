# File responsible for converting objects and images to the ones we use

import imageio
from PIL import Image

def convert_squares_to_triangles(input_obj, output_obj):
    '''
    Convert .obj files guided by squares into files guided by triangles
    '''

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
                outfile.write(line)

def convert_dds_to_png(dds_file, png_file):
    '''
    Convert .dds file to a .png file.
    '''

    # Read the DDS file using imageio
    dds_image = imageio.imread(dds_file)
    
    # Convert the numpy array to a Pillow image
    image = Image.fromarray(dds_image)
    
    # Save as PNG
    image.save(png_file)
    print(f"Converted {dds_file} to {png_file}")

if __name__ == "__main__":
    
    option = int(input("0 para converter imagem, 1 para converter obj\n"))
    if option == 0:
        src = input("Path to .dds image\n")
        dest = input("Path to save as .png\n")
        convert_dds_to_png(src, dest)
    if option == 1:
        src = input("Path to.obj\n")
        dest = input("Path to save .obj\n")
        convert_squares_to_triangles(src, dest)