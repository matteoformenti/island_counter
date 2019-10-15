from PIL import Image

island_count = 0
original = Image.open("image2.png")
image = original.copy()
mat = image.load()


def reduce_island(white_pixel_row, white_pixel_col, matrix):
    if matrix[(white_pixel_row, white_pixel_col)] == (255, 255, 255):
        matrix[(white_pixel_row, white_pixel_col)] = (0, 0, 0)
        matrix = reduce_island(white_pixel_row - 1, white_pixel_col, matrix)
        matrix = reduce_island(white_pixel_row, white_pixel_col + 1, matrix)
        matrix = reduce_island(white_pixel_row, white_pixel_col - 1, matrix)
        matrix = reduce_island(white_pixel_row + 1, white_pixel_col, matrix)
    return matrix


width, height = original.size

for row in range(width):
    for col in range(height):
        if mat[(row, col)] == (255, 255, 255):
            island_count += 1
            mat = reduce_island(row, col, mat)

print("Island count: " + str(island_count))
original.show()
