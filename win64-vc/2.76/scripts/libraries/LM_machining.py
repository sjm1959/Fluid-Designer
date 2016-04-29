import fd

def add_dado(part):
    tokens = []
    tokens.append(part.add_machine_token('Left Dado' ,'DADO','3'))
    tokens.append(part.add_machine_token('Right Dado' ,'DADO','4'))

    for token in tokens:
        token[1].lead_in = fd.inches(.125)
        token[1].lead_out = fd.inches(.125)
        token[1].beginning_depth = fd.inches(.5)
        token[1].double_pass = fd.inches(.5)
        token[1].distance_between_holes = fd.inches(5)
        token[1].panel_penetration = fd.inches(.25)
        
def add_adj_shelf_holes(part):
    obj, left_token = part.add_machine_token('Left Shelf Holes' ,'SHLF','3')
    obj, right_token = part.add_machine_token('Right Shelf Holes' ,'SHLF','4')

def add_cams(part):
    obj, left_token = part.add_machine_token('Left Cams' ,'CAMLOCK','3')
    obj, right_token = part.add_machine_token('Right Cams' ,'CAMLOCK','4')

def add_drilling(part):
    Width = part.get_var('dim_y','Width')
    
    tokens = []
    tokens.append(part.add_machine_token('Left Drilling' ,'CONST','3'))
    tokens.append(part.add_machine_token('Right Drilling' ,'CONST','4'))
    
    for token in tokens:
        token[1].dim_to_first_const_hole = fd.inches(1)
        token[1].add_driver(token[0],'dim_to_last_const_hole','fabs(Width)-INCH(1)',[Width])
        token[1].edge_bore_depth = fd.inches(.5)
        token[1].edge_bore_dia = 5
        token[1].face_bore_depth = fd.inches(.5)
        token[1].face_bore_dia = 5
        token[1].distance_between_holes = fd.inches(5)