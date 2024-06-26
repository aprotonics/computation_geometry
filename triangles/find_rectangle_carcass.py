import os
import importlib
import cv2


class Loader():
    def __init__(self):
        current_dir = os.path.curdir
        dir_to_create = current_dir + "/__cache__"
        if not os.path.exists(dir_to_create):
            os.mkdir(os.path.abspath(dir_to_create))
    
    def load_module(self, module_name, file_path):
        module_name = module_name
        file_path = file_path

        file = file_path
        file2 = "__cache__/" + f"__{module_name}__"
        text = ""

        with open(file=file, mode="rt", encoding="utf-8") as f:
            text = f.read()
        
        if text.find(" from") != -1:
            left_index = text.find(" from") + len("from") + 1
            right_index = text.find("import", left_index) - 1
            module_name_to_fix = text[left_index:right_index]

            old_value = module_name_to_fix
            new_value = f"__{module_name_to_fix}__"
            text = text.replace(old_value, new_value)

        file2 += ".py"

        with open(file=file2, mode="wt", encoding="utf-8") as f:
            f.write(text)
        
        importlib.invalidate_caches()
        loaded_module = importlib.import_module(f"__cache__.__{module_name}__")

        return loaded_module


file_name = "structures"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
structures = loader.load_module(file_name, file_path)

squareGrid = structures.SquareGrid
rectangularGrid = structures.RectangularGrid


file_name = "breadth_first_search"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
breadth_first_search = loader.load_module(file_name, file_path)

breadth_first_search4 = breadth_first_search.breadth_first_search4
breadth_first_search2 = breadth_first_search.breadth_first_search2


file_name = "utils"
par_dir = "utils"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
utils = loader.load_module(file_name, file_path)

create_graph = utils.create_graph
create_rectangular_graph = utils.create_rectangular_graph
count_length_of_sides_of_rectangle = utils.count_length_of_sides_of_rectangle
count_value_of_angles_in_rectangle = utils.count_value_of_angles_in_rectangle
find_angles_coordinates = utils.find_angles_coordinates
find_outer_angles_coordinates = utils.find_outer_angles_coordinates
find_inner_angles_coordinates = utils.find_inner_angles_coordinates
modify_src = utils.modify_src


file_name = "console_log"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
console_log = loader.load_module(file_name, file_path)

console_log = console_log.console_log


file_name = "get_length"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
get_length = loader.load_module(file_name, file_path)

length = get_length.length


file_name = "push"
par_dir = "utils_functions"
path = __file__
for i in range(3):
    path = os.path.dirname(path)
file_path = path + "/" + par_dir + "/" + file_name + ".py"
loader = Loader()
push = loader.load_module(file_name, file_path)

push = push.push


img_name = "data/rectangle18.jpg"
img = cv2.imread(img_name)

quality = 95                 # %

console_log(img.shape)
console_log()

width = img.shape[0]
height = img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, img, quality)
console_log(length(rectangle_area))
console_log()

graph = create_graph(rectangle_area)
console_log(length(graph.edges.keys()))

angles_coordinates = []
angles_coordinates1 = []
for i in range(2, 8):
    console_log(f"Iterations: {i}")
    angles_coordinates1 = push(find_outer_angles_coordinates(graph, 4, i, img, quality), angles_coordinates1)

angles_coordinates = push(angles_coordinates1, angles_coordinates)

console_log("angles coordinates")

for angles_coordinates in angles_coordinates1:
    console_log(angles_coordinates)
    console_log()


modified_img = modify_src(img)
cv2.imwrite("data/modified_rectangle18.jpg", modified_img)


console_log(modified_img.shape)
console_log()

width = modified_img.shape[0]
height = modified_img.shape[1]
height_to_width_ratio = (3, 2)

grid = squareGrid(width, height)
grid_center = (int(width / 2), int(height / 2))

rectangle_area = breadth_first_search2(grid, grid_center, modified_img, quality)
console_log(length(rectangle_area))
console_log()

graph = create_graph(rectangle_area)
console_log(length(graph.edges.keys()))

angles_coordinates2 = []
for i in range(2, 8):
    console_log(f"Iterations: {i}")
    angles_coordinates2 = push(find_inner_angles_coordinates(graph, 4, i, modified_img, quality), angles_coordinates2)

angles_coordinates = push(angles_coordinates2, angles_coordinates)

console_log("angles coordinates")

for angles_coordinates in angles_coordinates2:
    console_log(angles_coordinates)
    console_log()
