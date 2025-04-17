def find_indices_with_word(list1, word):
    """
    Finds indices of elements in list1 that contain a specific word (case-insensitive).
    """
    indices = []
    word_lower = word.lower()  
    
    for index in range(len(list1)):
        current_string = list1[index].lower()  
        if word_lower in current_string:
            indices.append(index)
    
    return indices

def extract_elements_by_indices(list1, list2):
    """
    Extracts elements from list2 based on the indices provided in list1.
    Returns a list of elements from list2 at the specified indices.
    """
    extracted_elements = []  # List to store the extracted elements from list2

    for index in list1:
        if index < len(list2):  # Ensure the index is within the bounds of list2
            extracted_elements.append(list2[index])  # Add the element at the specified index

    return extracted_elements  

def get_elements_coordinates(elements_list):
    """
    Extracts the Z-coordinate from each element in a list of elements.
    """
    z_coordinates = []
    
    for element in elements_list:
        try:
            z_coordinates.append(element.GetLocation())
        except AttributeError:
            z_coordinates.append(None) 
    
    return z_coordinates
  
def get_elements_z_coordinates(elements_list):
    """
    Extracts the Z-coordinate from each element in a list of elements.
    """
    z_coordinates = []
    
    for element in elements_list:
        try:
            z_coordinates.append(element.Z)
        except AttributeError:
            z_coordinates.append(None)  
    
    return z_coordinates

def extract_elements_by_indices(list1, list2):
    """
    Extracts elements from list2 based on the indices provided in list1.
    Returns a list of elements from list2 at the specified indices.
    """
    extracted_elements = []  

    for index in list1:
        if index < len(list2):
            extracted_elements.append(list2[index]) 

    return extracted_elements  

def calculate_differences(list1, reference_value):
    """
    Calculates the difference between each element in list1 and a reference value.
    """
    differences = []
    
    for num in list1:
        differences.append(reference_value - num)
    
    return differences

def translate_elements(list1, m, n, o):
    """
    Extracts the Z-coordinate from each element in a list of elements.
    """
    z_coordinates = []
    
    for element in elements_list:
        try:
            z_coordinates.append(element.GetLocation())
        except AttributeError:
            z_coordinates.append(None) 
    
    return z_coordinates

def extract_index_from_sublists(list_of_lists, index):
    """
    Extracts elements at a specific index from each sublist in a list of lists.
    """
    extracted_elements = []
    
    for sublist in list_of_lists:
        if index < len(sublist): 
            extracted_elements.append(sublist[index])
        else:
            extracted_elements.append(None) 
    
    return extracted_elements

def find_string_indices(_list1, target_string):
    """
    Finds the indices in _list1 where the target_string is present.    
    """
    matching_indices = []
    
    for index, item in enumerate(_list1):
        if isinstance(item, str) and item == target_string:
            matching_indices.append(index)
    
    return matching_indices

def extract_elements_by_indices(list1, list2):
    """
    Extracts elements from list2 based on the indices provided in list1.
    Returns a list of elements from list2 at the specified indices.
    """
    extracted_elements = []  # List to store the extracted elements from list2

    for index in list1:
        if index < len(list2):  # Ensure the index is within the bounds of list2
            extracted_elements.append(list2[index])  # Add the element at the specified index

    return extracted_elements

def find_mechanical_supply_air_indices(input_list):
    """
    Finds indices of items containing the string "Mechanical Supply Air" in a list.
    """
    indices = []
    search_string = "Mechanical Supply Air"
    
    for index, item in enumerate(input_list):
        if search_string in str(item):  # Convert to string in case items aren't strings
            indices.append(index)
    
    return indices   

def extract_elements_by_indices(list1, list2):
    """
    Extracts elements from list2 based on the indices provided in list1.
    Returns a list of elements from list2 at the specified indices.
    """
    extracted_elements = []  # List to store the extracted elements from list2

    for index in list1:
        if index < len(list2):  # Ensure the index is within the bounds of list2
            extracted_elements.append(list2[index])  # Add the element at the specified index

    return extracted_elements   

def find_intersections(_surfaces, _points, _spaces, _elements):
    """
    Finds intersections between surfaces and points, and returns corresponding spaces and elements.
    
    Args:
        _surfaces: List of surface objects
        _points: List of point objects
        _spaces: List of space objects corresponding to surfaces
        _elements: List of elements corresponding to points
    """
    _intersections = []
    
    for _i, _surface in enumerate(_surfaces):
        for _j, _point in enumerate(_points):
            if _surface.DoesIntersect(_point): 
                if _i < len(_spaces) and _j < len(_elements):  
                    _intersections.append([_spaces[_i], _elements[_j]])  
    
    return _intersections

def add_parameter_to_nested_list(nested_list, parameter_name, target_index):
    """
    Iterates over a nested list and appends the value of a given parameter 
    """
    for sublist in nested_list:
        if len(sublist) > target_index:
            element = sublist[target_index]
            if hasattr(element, "GetParameterValueByName"): 
                try:
                    param_value = element.GetParameterValueByName(parameter_name)
                    sublist.append(param_value)
                except Exception as e:
                    sublist.append(None) 
            else:
                sublist.append(None)  

    return nested_list
    
def append_to_index_2(nested_list, string_to_append):
    """
    Adds a string to the end of the element at index 2 of each sub-list
    """
    modified_list = [sublist.copy() for sublist in nested_list]
    
    for sublist in modified_list:
        if len(sublist) > 2:  
            sublist[2] = str(sublist[2]) + str(string_to_append)
    
    return modified_list 

def compare_partial_strings_flat(nested_list, _list1, _list2):
    """
    Compares strings and adds flat values after index 2.
    
    Args:
    nested_list: List of lists with specific structure
    _list1: List of reference strings
    _list2: List of values to be added
    """
    modified_list = []
    
    for sublist in nested_list:
        new_sublist = sublist.copy()
        
        if len(sublist) > 2:
            target_str = str(sublist[2])
            matches = []
            
            for i, long_str in enumerate(_list1):
                if target_str in str(long_str) and i < len(_list2):
                    matches.append(_list2[i])
            
            insert_pos = 3
            for match in (matches if matches else [0]):
                new_sublist.insert(insert_pos, match)
                insert_pos += 1
                
        modified_list.append(new_sublist)
    
    return modified_list

def remove_sublists_with_zero_at_index_3(nested_list):
    """
    Deletes the sublists that have the value 0 in their index 3.    
    """
    return [sublist for sublist in nested_list 
            if not (len(sublist) > 3 and sublist[3] == 0)]