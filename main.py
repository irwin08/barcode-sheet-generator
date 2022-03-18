from reportlab.pdfgen import canvas
from barcode import Code39
from barcode.writer import ImageWriter


# returns filepath string
def generate_barcode_for_sku(sku):
    code = Code39(sku, writer=ImageWriter(), add_checksum=False)
    path = 'barcodes/'+sku
    return code.save(path)

def draw_page(can, skus):
    
    height = 80
    #start_y = -86
    start_y = 15
    barcode_width = 180
    barcode_height = 79

    # expects a tuple of three barcode file paths
    def draw_at_y(y_pos, path_tup):

        x_offsets = [0, 22, 55]

        for index, x_offset in zip(range(0,len(path_tup)), x_offsets):

            can.drawInlineImage(path_tup[index], (x_offset + (barcode_width*index)), y_pos, width=barcode_width, height=79, preserveAspectRatio=False)


    ## BETTER!! :) Thanks se_irl
    tups = [tuple(skus[i:min(i + 3, len(skus))]) for i in range(0, len(skus), 3)]

    tups_of_paths = list(map(lambda tup : tuple(generate_barcode_for_sku(sku) for sku in tup), tups))

    batches = [list(tups_of_paths[i:min(i + 10, len(tups_of_paths))]) for i in range(0, len(tups_of_paths), 10)]

    for batch in batches:
        i = 0
        for tup in batch:
            draw_at_y((start_y + (height*i)), tup)
            i+=1
        can.showPage()




if __name__ == '__main__':
    can = canvas.Canvas('labels.pdf')

    lines = []

    with open('input.txt') as f:
        lines = [line.rstrip() for line in f]

    skus = []

    for line in lines:
        split = line.split('*')
        factor = 1
        if len(split) > 1:
            factor = int(split[1])
        skus.extend([split[0].rstrip() for i in range(0,factor)])
            
        

    draw_page(can, skus)    

    can.save()
    

