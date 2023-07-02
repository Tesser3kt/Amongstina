from PIL import Image
import os

#################################################################
#################### AMONGŠTINA TRANSLATE #######################
#################################################################
################## Created by: Eric Dusart ######################
#################################################################

# CONFIG
AMOGUS_SIZE = 64
ACCESORY_HEIGHT = 16
ACCESORY_WIDTH = 64

slovo = input("Zadejte slovo k přeložení: ")
slovo = slovo.upper()

if "X" in slovo:
    slovo = slovo.replace("X", "KS")
if "Y" in slovo:
    slovo = slovo.replace("Y", "I")
if "W" in slovo:
    slovo = slovo.replace("W", "V")
if "Z" in slovo:
    slovo = slovo.replace("Z", "S")

dictionary = {
    "Á": "A",
    "Č": "C",
    "Ď": "D",
    "É": "E",
    "Ě": "E",
    "Í": "I",
    "Ň": "N",
    "Š": "S",
    "Ť": "T",
    "Ú": "U",
    "Ů": "U",
    "Ý": "Y",
    "Ž": "Z",
}
for letter in slovo:
    if letter in dictionary:
        slovo = slovo.replace(letter, dictionary[letter])

upper = ["C", "D", "H", "J", "K", "Q", "S", "N"]
oci = ["B"]
middle = ["F", "P", "T", "I", "R"]
lower = ["L", "M"]
effects = ["V", "G"]

end_splitters = ["A", "E", "I", "O", "U"]
bean = [",", ".", ":", ";", "!", "?"]
bodies = ["A", "E", "O", "bean"]

# Pravidla
# 1. Samohlasky se ctou vzdycky na konci, ale kdyz to je flipnute, tak to je na zacatku
# 2. Cte se odshora dolu
# 3. V a G jsou vzdy na konci a samohlasky jsou jeste poslednejsi



flipped_components = []
actual_component = []
number_of_samohlasky = 0

upper_block = False
oci_block = False
middle_block = False
lower_block = False

for letter in slovo:
    if len(actual_component) == 0:
        number_of_samohlasky = 0
        upper_block = False
        oci_block = False
        middle_block = False
        lower_block = False

    if letter in end_splitters:
        if len(actual_component) > 0 and number_of_samohlasky == 0:
            # Napise do stare a vytvori novou komponentu, samohlaska na konci
            actual_component += letter
            flipped_components.append(actual_component)
            actual_component = []
        elif len(actual_component) == 0:
            # Komponenta je prazdna, samohlaska na prvnim miste
            actual_component.insert(0, "//")
            actual_component += letter
            number_of_samohlasky += 1
        else:
            # Vytvori novou komponentu, samohlaska na prvnim miste
            flipped_components.append(actual_component)
            actual_component = []
            actual_component.insert(0, "//")
            actual_component += letter
            number_of_samohlasky += 1

        upper_block = False
        oci_block = False
        middle_block = False
        lower_block = False

    elif (len(actual_component)>0) and (actual_component[-1] in effects):
        # Kdyz za effects neni samohlaska, protoze effects je na konci ale pred samohlaskou
        flipped_components.append(actual_component)
        actual_component = []

        upper_block = False
        oci_block = False
        middle_block = False
        lower_block = False
    
    if letter in end_splitters:
        pass

    elif letter in upper:
        if upper_block:
            flipped_components.append(actual_component)
            actual_component = []

            upper_block = False
            oci_block = False
            middle_block = False
            lower_block = False

        actual_component += letter
    elif letter in oci:
        upper_block = True
        if oci_block:
            flipped_components.append(actual_component)
            actual_component = []

            upper_block = False
            oci_block = False
            middle_block = False
            lower_block = False

        actual_component += letter
    elif letter in middle:
        upper_block = True
        oci_block = True
        if middle_block:
            flipped_components.append(actual_component)
            actual_component = []

            upper_block = False
            oci_block = False
            middle_block = False
            lower_block = False

        actual_component += letter
    elif letter in lower:
        upper_block = True
        oci_block = True
        middle_block = True
        if lower_block:
            flipped_components.append(actual_component)
            actual_component = []

            upper_block = False
            oci_block = False
            middle_block = False
            lower_block = False

        actual_component += letter
    elif letter in effects:
        upper_block = True
        oci_block = True
        middle_block = True
        lower_block = True
        actual_component += letter
    elif letter == " ": # mezery
        flipped_components.append(actual_component)
        flipped_components.append(["mezera"])
        actual_component = []
    elif letter in bean:
        if len(actual_component) > 0:
            flipped_components.append(actual_component)
        flipped_components.append(["bean"])
        actual_component = [] 
    else:
        print("Unknown letter: " + letter)

if len(actual_component)>0:
    flipped_components.append(actual_component)
#print(f'Flipovaci verze (Pocet amogusů: {len(flipped_components)})', flipped_components)


# odstraneni \\ a prazdne seznamy

for i, item in enumerate(flipped_components):
    if item == ["//"]:
        flipped_components.remove(item)
    elif item == []:
        flipped_components.remove(item)
    elif len(item) == 2 and item[0] == "//":
        flipped_components[i].remove("//")
print(flipped_components)

# Pridani nejakych samohlasek do skupin protoze tam predtim nemohly byt
lower.append("U")


p_horni = []
p_stredni = []
p_dolni = []
odstupy = 0
for komponenta in flipped_components:
    max_hornich = 0
    max_strednich = 0
    max_dolnich = 0
    for item in komponenta:
        if item in upper:
            max_hornich += 1
        elif item in middle:
            max_strednich += 1
        elif item in lower:
            max_dolnich += 1

    p_horni.append(max_hornich)
    p_stredni.append(max_strednich)
    p_dolni.append(max_dolnich)

max_hornich = max(p_horni)
max_strednich = max(p_stredni)
max_dolnich = max(p_dolni)

# Set the path to the directory containing the images
image_dir = os.path.join(os.getcwd(), "assets")

# Create a dictionary to hold the images
images_dict = {}

# Loop through each file in the directory
for filename in os.listdir(image_dir):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image file and add it to the dictionary
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)
        key = filename.replace(".png", "")
        images_dict[key] = image

height = AMOGUS_SIZE+(max_hornich*ACCESORY_HEIGHT)+(max_dolnich*ACCESORY_HEIGHT)
width = AMOGUS_SIZE*len(flipped_components)+ACCESORY_HEIGHT*odstupy
canvas = Image.new("RGBA", (width, height), (255, 255, 255, 255))

for i, komponenta in enumerate(flipped_components):
    platno_amongus = Image.new("RGBA", (AMOGUS_SIZE, height), (255, 255, 255, 255))
    upper_accesories = 0
    lower_accesories = 0
    to_flip_up = False
    to_flip_side = False
    to_resize = False
    body_crop = False
    is_body = False
    without_eyes = False
    amongus_body = None

    # Number of upper accesories
    for item in komponenta:
        if item in upper:
            upper_accesories += 1
        elif item in lower:
            lower_accesories += 1
    
    # Some options
    if "G" in komponenta:
        to_flip_up = True
    if "V" in komponenta:
        to_resize = True
    if "//" in komponenta:
        to_flip_side = True
    if "mezera" in komponenta:
        is_body = True
    if "B" in komponenta:
        without_eyes = True


    # Choose a body
    if not is_body:
        for body in bodies:
            if body in komponenta:
                if without_eyes:
                    pass #TODO
                platno_amongus.paste(images_dict[body], (0, ACCESORY_HEIGHT*max_hornich), images_dict[body] )
                is_body = True
                amongus_body = body

    if not is_body:
        platno_amongus.paste(images_dict["amogus"], (0, ACCESORY_HEIGHT*max_hornich), images_dict["amogus"])
        amongus_body = "amogus"
    
    # Start creating
    
    upper_index = 0
    lower_index = 0
    for item in komponenta:
        if item in upper:
            platno_amongus.paste(images_dict[item], (0, platno_amongus.height-ACCESORY_HEIGHT*max_dolnich-AMOGUS_SIZE-ACCESORY_HEIGHT-ACCESORY_HEIGHT*(upper_accesories-upper_index)+ACCESORY_HEIGHT),images_dict[item])
            #platno_amongus.paste(images_dict[item], (0, platno_amongus.height-max_dolnich*ACCESORY_HEIGHT-AMOGUS_SIZE-ACCESORY_HEIGHT-ACCESORY_HEIGHT*upper_index),images_dict[item])
            upper_index += 1
        elif item in middle:
            if item == "F":
                platno_amongus.paste(images_dict[item], (0, ACCESORY_HEIGHT*max_hornich+ACCESORY_HEIGHT+20), images_dict[item])
            else:
                platno_amongus.paste(images_dict[item], (0, ACCESORY_HEIGHT*max_hornich+ACCESORY_HEIGHT+10), images_dict[item])
        elif item in lower:
            if item  == "L":
                # L jako lyze mohou byt vyse
                spec_height = (ACCESORY_HEIGHT*max_hornich+AMOGUS_SIZE+ACCESORY_HEIGHT*lower_index)-14
            elif item == "M" or "U":
                spec_height = (ACCESORY_HEIGHT*max_hornich+AMOGUS_SIZE+ACCESORY_HEIGHT*lower_index)-16
            else:
                #nestane se
                spec_height = ACCESORY_HEIGHT*max_hornich+AMOGUS_SIZE+ACCESORY_HEIGHT*lower_index
            platno_amongus.paste(images_dict[item], (0, spec_height), images_dict[item])
            lower_index += 1
        elif item in oci:
            if amongus_body == "O":
                platno_amongus.paste(images_dict[item], (12, ACCESORY_HEIGHT*max_hornich+19), images_dict[item])
            elif amongus_body == "A":
                platno_amongus.paste(images_dict[item], (0, ACCESORY_HEIGHT*max_hornich+10), images_dict[item])
            elif amongus_body == "E":
                platno_amongus.paste(images_dict[item], (3, ACCESORY_HEIGHT*max_hornich+14), images_dict[item])  
            else:         
                platno_amongus.paste(images_dict[item], (3, ACCESORY_HEIGHT*max_hornich+14), images_dict[item])
    if to_flip_side:
        region = platno_amongus.crop((0, 0, platno_amongus.width, platno_amongus.height))
        region = region.transpose(Image.FLIP_LEFT_RIGHT)
        platno_amongus.paste(region, (0, 0), (region))
    if to_flip_up:
        region = platno_amongus.crop((0, 0, platno_amongus.width, platno_amongus.height))
        region = region.transpose(Image.FLIP_TOP_BOTTOM)
        platno_amongus.paste(region, (0, 0), (region))
    if to_resize:
            # scale the region to 50%
        region = platno_amongus.crop((0, 0, platno_amongus.width, platno_amongus.height))
        region = region.resize((platno_amongus.width//2, platno_amongus.height//2))
        platno_amongus.paste((255, 255, 255), (0, 0, platno_amongus.width, platno_amongus.height))#vymazat pozadi
        platno_amongus.paste(region, (platno_amongus.width//4, platno_amongus.height//4), (region))




    canvas.paste(platno_amongus, (i*AMOGUS_SIZE, 0), platno_amongus)
canvas.save("output.png")