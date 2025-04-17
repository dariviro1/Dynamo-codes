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

def remove_index_from_main_list(list_of_lists, index):
    """
    Removes the specified index from the main list (not from sublists).
    """
    if 0 <= index < len(list_of_lists):
        return list_of_lists[:index] + list_of_lists[index+1:]
    return list_of_lists
    
def group_by_room(list_of_lists):
    """
    Groups a list of lists every time a sublist has 'ROOM_' in its first index.
    """
    grouped = []
    current_group = []

    for sublist in list_of_lists:
        if sublist and isinstance(sublist[0], str) and "ROOM_" in sublist[0]:  
            if current_group:
                grouped.append(current_group) 
            current_group = [sublist]  
        else:
            current_group.append(sublist) 

    if current_group: 
        grouped.append(current_group)

    return grouped

def remove_room_prefix(nested_list):
    """
    Removes all characters up to and including the first underscore ('_') 
    from the string in index 0 of each sublist.
    """
    for group in nested_list:  # Nivel 1
        if isinstance(group, list):
            for sublist in group:  # Nivel 2
                if isinstance(sublist, list) and sublist:  
                    value = sublist[0]
                    if isinstance(value, str):  
                        sublist[0] = re.sub(r'^[^_]*_', '', value, count=1)  # Elimina hasta el primer "_"
    return nested_list    

def separate_first_and_second_word(nested_list):
    """
    Takes a deeply nested list and splits the string in index 0 of each sub-sub-list at the first space.
    - The first part remains in index 0.
    - The second part (if it exists) is placed in index 1 without modifying the length of the list.
    """
    for outer_list in nested_list:
        for sublist in outer_list:
            if sublist and isinstance(sublist[0], str):
                parts = sublist[0].split(" ", 1)  
                
                sublist[0] = parts[0]  
                
                if len(parts) > 1:
                    if len(sublist) > 1:
                        sublist[1] = parts[1]  
                    else:
                        sublist.append(parts[1])  

    return nested_list 
    
def grouping_specific_indexes(nested_list_of_lists, start_index, end_index, insert_position, start_from_sublist=0):
    """
    Groups elements from a specified index range into a new sublist and inserts it at a given position.
    Allows skipping the first N sublists before applying the function.
    """
    for group in nested_list_of_lists:
        new_sublist = []
        
        for i, sublist in enumerate(group):
            if i < start_from_sublist:  
                continue
            
            if len(sublist) > start_index:
                new_sublist.extend(sublist[start_index:end_index])
                del sublist[start_index:end_index]  

        group.insert(insert_position, new_sublist)
    
    return nested_list_of_lists 

def process_nested_sublists(nested_list_of_lists, source_index, target_index):
    """
    Iterates through a nested list structure, processes each sublist to check a given source index,
    moves the value to the target index if it's not None, and removes the source index from every sublist.
    """
    for group in nested_list_of_lists:
        for sublist in group:
            if len(sublist) > source_index and sublist[source_index] is not None:
                sublist[target_index] = sublist[source_index]  # Move the value to target index
            if len(sublist) > source_index:
                del sublist[source_index]  # Remove the source index regardless of value

    return nested_list_of_lists

def remove_null_indices(nested_list_of_lists):
    """
    Iterates through a nested list structure and removes all occurrences of None in each sublist.
    """
    for group in nested_list_of_lists:
        for sublist in group:
            sublist[:] = [item for item in sublist if item is not None]  # Remove None values in place

    return nested_list_of_lists

def remove_empty_sublists(nested_list_of_lists):
    """
    Iterates through a nested list structure and removes empty sublists from each group.
    """
    for group in nested_list_of_lists:
        group[:] = [sublist for sublist in group if sublist]  # Remove empty sublists

    return nested_list_of_lists 

def find_matching_groups(list1, list2):
    """
    Finds elements in list1 that match the first element of any subgroup in list2.
    Returns three lists:
    1. Indices of matching elements in list1.
    2. Matching elements from list1.
    3. Corresponding groups from list2.
    """
    matching_indices = []  
    matching_elements = []  
    matching_groups = []    

    for index, element in enumerate(list1):  
        for group in list2:
            
            if group[0][0] == element:
                matching_indices.append(index)  
                matching_elements.append(element) 
                matching_groups.append(group)       
                break  

    return matching_indices, matching_elements, matching_groups

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

def extract_all_values(nested_list, sublist_index, sub_sublist_index):
    """
    Extracts all values from a specific sub-sublist in a deeply nested list.
    """
    extracted_values = []

    for sublist in nested_list:
        if len(sublist) > sublist_index: 
            sub_sublist = sublist[sublist_index]

            if len(sub_sublist) > sub_sublist_index: 
                extracted_values.append(sub_sublist[sub_sublist_index]) 

    return extracted_values

def extract_all_values_Kw(nested_list, sublist_index, sub_sublist_index):
    """
    Extracts all values from a specific sub-sublist in a deeply nested list 
    and multiplies each value by -0.2931.
    """
    extracted_values = []

    for sublist in nested_list:
        if len(sublist) > sublist_index: 
            sub_sublist = sublist[sublist_index]

            if len(sub_sublist) > sub_sublist_index: 
                extracted_values.append(sub_sublist[sub_sublist_index] * -0.2931)  

    return extracted_values



def extract_all_values_multiple_10(nested_list, sublist_index, sub_sublist_index):
    """
    Extracts all values from a specific sub-sublist in a deeply nested list.
    - If the value is 0, it remains 0.
    - If the value is already a multiple of 10, it remains unchanged.
    - If the value is greater than 0 and not a multiple of 10, it rounds up to the nearest multiple of 10.
    """
    extracted_values = []

    for sublist in nested_list:
        if len(sublist) > sublist_index:  
            sub_sublist = sublist[sublist_index]

            if len(sub_sublist) > sub_sublist_index:  
                value = sub_sublist[sub_sublist_index]  

                if value == 0:
                    extracted_values.append(0)  
                elif value % 10 == 0:
                    extracted_values.append(value)  
                else:                    
                    rounded_value = math.ceil(value / 10) * 10
                    extracted_values.append(rounded_value)

    return extracted_values

def find_matching_strings(_ppal_parameters, _parameters):
    """
    Finds matching strings between two lists and returns the matching elements.    
    """
    matching_strings = []
    index_to_keep = []
    
    for i, param in enumerate(_ppal_parameters):
        if param in _parameters:
            matching_strings.append(param)
            index_to_keep.append(i)
    
    return matching_strings, index_to_keep

def keep_indices_from_list(_headers, _index_to_keep):
    """
    Keeps only the elements from a list based on specified indices.
    """
    filtered_headers = []
    
    for i, header in enumerate(_headers):
        if i in _index_to_keep:
            filtered_headers.append(header)
    
    return filtered_headers

def clean_family_type(_data, index):   
    cleaned_data = []
    
    for sublist in _data:
        if len(sublist) > index:  
            text = sublist[index]
            text = text.replace("Family Type: ", "")
            text = text.split(",")[0]
            sublist[index] = text
        cleaned_data.append(sublist)

    return cleaned_data

def insert_values(_list, _include_list, index):
    """
    Inserts elements from _include_list into each sublist of _list at the specified index.     
    """
    updated_list = []
    
    for i, sublist in enumerate(_list):
        if i < len(_include_list):  
            sublist[index] = _include_list[i]
        
        updated_list.append(sublist)
    
    return updated_list

def find_index_in_list(_list, _parameter):
    """
    Finds the index of a target string in a list.
    """
    for i in range(len(_list)):
        if _list[i] == _parameter:
            return i
    return -1

def clean_family_type(_data, index):   
    cleaned_data = []
    
    for sublist in _data:
        if len(sublist) > index:  
            text = sublist[index]
            text = text.replace("Family Type: ", "")
            text = text.split(",")[0]
            sublist[index] = text
        cleaned_data.append(sublist)

    return cleaned_data

def replace_text_in_list(_list, _text1, _text2):
    # Replaces occurrences of _text1 with _text2 in a list of strings.
    new_list = []
    for item in _list:
        if _text1 in item:
            new_item = item.replace(_text1, _text2)
        else:
            new_item = item
        new_list.append(new_item)
    return new_list

def prepend_elements(elements, parameters):    
    # Prepend each element from `elements` to the corresponding sublist in `parameters`.
    for i in range(len(parameters)):
        parameters[i].insert(0, elements[i])
    return parameters

def fill_empty_parameters(list_of_lists):  
    #  Replace empty values in sublists with 'Parameter not found'.
    for sublist in list_of_lists:
        for i in range(len(sublist)):
            if sublist[i] == "" or sublist[i] is None:
                sublist[i] = "Empty Parameter"
    return result

def remove_duplicates_by_index(list_of_lists):
    """
    Removes sublists with duplicate values in index 1.
    Only the first occurrence of a unique value in index 1 is kept.
    """    
    seen = set()
    unique_list = []
    
    for sublist in list_of_lists:
        if len(sublist) > 1:  
            value = sublist[1]
            if value not in seen:
                seen.add(value)
                unique_list.append(sublist)
    
    return unique_list

def move_first_to_last(list_of_lists):   
    # Moves the first element of each sublist to the end of the same sublist.
    return [sublist[1:] + [sublist[0]] for sublist in list_of_lists]

def clean_sublist_text(list_of_lists):
    """
    Cleans the text in index 1 of each sublist by removing the prefix
    'Family Type: ' and anything after the first comma.
    """    
    cleaned_list = []
    for sublist in list_of_lists:
        if len(sublist) > 1: 
            cleaned_text = sublist[1].replace("Family Type: ", "").split(",")[0]
            sublist[1] = cleaned_text
        cleaned_list.append(sublist)
    return cleaned_list
        