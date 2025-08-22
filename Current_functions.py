# Functions for Flat Lists
def get_element_ids(_elements):
    ids = []
    for element in _elements:
        if element is not None:
            ids.append(element.Id)
    return ids

def reorder_list_by_index(_list1, _value, _list3):
    """
    Finds the index of a value in _list1, retrieves the corresponding element
    from _list3 at that index, and moves it to the start of _list3.
    
    Args:
        _list1 (list): List of numbers to search.
        _value (int/float): Value to find in _list1.
        _list3 (list): List of elements to reorder.
    
    Returns:
        list: Reordered _list3 with the element at the found index moved to the start.
    """
    _index = -1  # Default index if value is not found
    
    # Find the index of the value in _list1
    for i in range(len(_list1)):
        if _list1[i] == _value:
            _index = i
            break
    
    # If the index is valid, reorder _list3
    if 0 <= _index < len(_list3):
        _element = _list3[_index]
        _list3.pop(_index)
        _list3.insert(0, _element)
    
    return _list3
    
def find_indices_with_word(_string_list, _target_word):
    """
    Finds indices of elements containing a specific word (case-insensitive).
    Works on flat lists of strings.
    
    Args:
        _string_list (list): List of strings to search.
        _target_word (str): Word to find.
    
    Returns:
        list: Indices of matching elements.
    """
    _indices = []
    _target_lower = _target_word.lower()
    
    for _index, _item in enumerate(_string_list):
        if _target_lower in _item.lower():
            _indices.append(_index)
    
    return _indices

def extract_elements_by_indices(_source_list, _index_list):
    """
    Extracts elements from a list using specified indices.
    Works on flat lists with bounds checking.
    
    Args:
        _source_list (list): List to extract from.
        _index_list (list): Indices to retrieve.
    
    Returns:
        list: Elements at specified indices.
    """
    _result = []
    
    for _index in _index_list:
        if 0 <= _index < len(_source_list):
            _result.append(_source_list[_index])
    
    return _result

def filter_elements_by_condition(_list1, _list2, condition="has_number"):
    """
    Returns elements from _list1 where the corresponding element in _list2 meets the given condition.

    Parameters:
        _list1 (list): Source list from which elements are returned.
        _list2 (list): Reference list used to check the condition.
        condition (str): The condition to apply on elements of _list2. Default is "has_number".

    Returns:
        list: Filtered elements from _list1.
    """
    result = []

    for i, item in enumerate(_list2):
        if condition == "has_number":
            if isinstance(item, (int, float)):
                result.append(_list1[i])
            elif isinstance(item, str) and any(char.isdigit() for char in item):
                result.append(_list1[i])
            elif isinstance(item, (list, tuple)):
                if any(isinstance(x, (int, float)) for x in item):
                    result.append(_list1[i])

    return result

def calculate_differences(_value_list, _reference_value):
    """
    Calculates differences between reference and each value.
    Works on flat lists of numbers.
    
    Args:
        _value_list (list): Numerical values.
        _reference_value (int/float): Baseline value.
    
    Returns:
        list: Calculated differences.
    """
    _differences = []
    
    for _value in _value_list:
        _differences.append(_reference_value - _value)
    
    return _differences

def apply_operation_to_lists(_list1, _operation, _list2):
    """
    Applies a mathematical operation element-wise between two lists.

    Args:
        _list1 (list): First list of numbers.
        _list2 (list): Second list of numbers (same length as _list1).
        _operation (str): Operation to apply. One of "+", "-", "*", "/".

    Returns:
        list: List of results after applying the operation.
    """
    result = []
    for a, b in zip(_list1, _list2):
        if _operation == "+":
            result.append(a + b)
        elif _operation == "-":
            result.append(a - b)
        elif _operation == "*":
            result.append(a * b)
        elif _operation == "/":
            if b != 0:
                result.append(a / b)
            else:
                result.append(None)  # Avoid division by zero
        else:
            result.append(None)  # Invalid operation
    return result

def get_parameter_values(_elements, _parameter_name):
    """
    Returns a list of parameter values for the given elements using Element.GetParameterValueByName.

    Args:
        elements: List of Revit elements.
        parameter_name: The name of the parameter to retrieve from each element.

    Returns:
        A list of parameter values.
    """
    values = []
    for elem in _elements:
        value = elem.GetParameterValueByName(_parameter_name)
        values.append(value)
    return values

def group_elements_by_parameter_value(_elements, _parameter_name, _target_value):
    """
    Filters and organizes elements into a single list ordered according to _target_value.

    Args:
        _elements (list): List of Revit elements.
        _parameter_name (str): The name of the parameter to check.
        _target_value (list): List of values to group and order by.

    Returns:
        list: A flat list of elements, grouped and ordered by target values.
    """
    # Ensure _target_value is a list
    if not isinstance(_target_value, list):
        _target_value = [_target_value]

    ordered_elements = []
    for target in _target_value:
        for elem in _elements:
            value = elem.GetParameterValueByName(_parameter_name)
            if value == target:
                ordered_elements.append(elem)

    return ordered_elements

# Functions for Nested Lists

def extract_index_from_sublists(_nested_list, _target_index):
    """
    Extracts specific index from each sublist.
    Works on nested lists with variable lengths.
    
    Args:
        _nested_list (list): List containing sublists.
        _target_index (int): Position to extract.
    
    Returns:
        list: Extracted elements or None.
    """
    _extracted = []
    
    for _sublist in _nested_list:
        if len(_sublist) > _target_index:
            _extracted.append(_sublist[_target_index])
        else:
            _extracted.append(None)
    
    return _extracted

def get_parameter_values_nested_at_index(_elements, _parameter_name, _index):
    """
    For each sublist in the nested list, gets the parameter value
    of the element at _index and appends it to the end of the sublist, preserving the structure.

    Args:
        _elements (list of lists): Nested list of elements.
        _parameter_name (str): Name of the parameter.
        _index (int): Index of the element within each sublist from which to get the value.

    Returns:
        list of lists: Nested list with the value appended at the end of each sublist.
    """
    result = []
    for sublist in _elements:
        new_sublist = sublist[:]  # Copy to avoid modifying the original
        if 0 <= _index < len(sublist):
            elem = sublist[_index]
            value = elem.GetParameterValueByName(_parameter_name)
            new_sublist.append(value)
        else:
            # If the index is not valid, do not append anything
            pass
        result.append(new_sublist)
    return result

def find_matching_dataframes(_nested_list, _all_data_frames):
    result = []
    
    # Iterate through each sublist in the nested list
    for nested_sublist in _nested_list:
        # Create a copy of the current sublist to avoid modifying the original
        current_result = list(nested_sublist)
        match_value = str(nested_sublist[1])  # Value to match from [1]
        match_found = False
        
        # Search through all data frames for a match
        for df_sublist in _all_data_frames:
            comparison_value = str(df_sublist[0][0])  # Value to compare from [0][0]
            
            if comparison_value == match_value:
                match_found = True
                # Add all elements from the matching df_sublist except [0][0]
                # First add elements from [0][1:] if they exist
                if len(df_sublist[0]) > 1:
                    for item in df_sublist[0][1:]:
                        current_result.append(item)
                
                # Then add all elements from [1:] if they exist
                if len(df_sublist) > 1:
                    for item in df_sublist[1:]:
                        current_result.append(item)
                break  # Stop after first match
        
        if match_found:
            result.append(current_result)
    
    return result

def calculate_and_append_to_nested_lists(_nested_list, _index1, _operation, _index2):
    result = []
    for sublist in _nested_list:
        new_sublist = sublist[:]
        
        try:
            a = float(sublist[_index1])
            b = float(sublist[_index2])
        except (ValueError, TypeError, IndexError):
            val = None
        else:
            if _operation == "+":
                val = a + b
            elif _operation == "-":
                val = a - b
            elif _operation == "*":
                val = a * b
            elif _operation == "/":
                val = a / b if b != 0 else None
            else:
                val = None

        new_sublist.append(val)
        result.append(new_sublist)
    return result

def remove_sublists_with_zero_at_index(_nested_list, _target_index):
    """
    Filters out sublists with zero at specified index.
    Works on nested lists with numerical values.
    
    Args:
        _nested_list (list): Nested list to filter.
        _target_index (int): Index to check for zero.
    
    Returns:
        list: Filtered nested list.
    """
    _filtered = []
    
    for _sublist in _nested_list:
        if len(_sublist) <= _target_index or _sublist[_target_index] != 0:
            _filtered.append(_sublist)
    
    return _filtered

def remove_sublist_at_index(nested_list, index_to_remove):
    """
    Removes the sublist at a given index from each sublist in a nested list.

    Parameters:
    nested_list (list of lists): The original nested list.
    index_to_remove (int): The index of the sublist to remove in each list.

    Returns:
    list of lists: A new nested list with the specified sublist removed from each sublist.
    """
    result = []
    for sublist in nested_list:
        new_sublist = []
        for i in range(len(sublist)):
            if i != index_to_remove:
                new_sublist.append(sublist[i])
        result.append(new_sublist)
    return result

def group_by_room(_nested_list):
    """
    Groups sublists every time a 'ROOM_' pattern is found.
    Works on nested lists with string identifiers.
    
    Args:
        _nested_list (list): List containing room identifiers.
    
    Returns:
        list: Grouped nested list structure.
    """
    _grouped = []
    _current_group = []
    
    for _sublist in _nested_list:
        if "ROOM_" in str(_sublist[0]):
            if _current_group:
                _grouped.append(_current_group)
            _current_group = [_sublist]
        else:
            _current_group.append(_sublist)
    
    if _current_group:
        _grouped.append(_current_group)
    
    return _grouped

def group_by_string(_list_of_lists, _keyword):
    """
    Groups a list of lists every time a sublist starts with a string that contains the given keyword.

    Args:
        _list_of_lists (list): A list of sublists.
        _keyword (str): The string to search for in the first element of each sublist.

    Returns:
        list: A list of grouped sublists.
    """
    grouped = []
    current_group = []

    for sublist in _list_of_lists:
        if sublist and isinstance(sublist[0], str) and _keyword in sublist[0]:  
            if current_group:
                grouped.append(current_group) 
            current_group = [sublist]  
        else:
            current_group.append(sublist) 

    if current_group: 
        grouped.append(current_group)

    return grouped

def build_dataframes_from_nested_list(_nested_list):
    """
    Converts a nested list (imported from Excel via Dynamo)
    into a list of sublists in the format [dataframe_name, DataFrame].

    Each sublist in the input represents a table with:
    - [0][0] = dataframe name
    - [1][1:] = column names
    - [2:][0] = row index
    - [2:][1:] = data values
    """
    _result = []

    for _table in _nested_list:
        if not _table or len(_table) < 3:
            continue  # skip empty or incomplete tables

        _df_name = _table[0][0]            # dataframe name
        _columns = _table[1][1:]           # column names (skip the first cell)

        _index = []
        _data = []

        for _row in _table[2:]:
            _index.append(_row[0])
            _data.append(_row[1:])

        _df = pd.DataFrame(_data, index=_index, columns=_columns)
        _result.append([_df_name, _df])

    return _result

def build_dataframes_from_nested_list_all_data(_nested_list):
    """
    Processes a nested list, where each sublist is an independent 'table'.
    
    For each table:
    - Row 0 contains labels (single strings)
    - Row 1 contains headers
    - Rows 2+ contain data

    Returns: list of pairs [labels, DataFrame] for each sublist.
    """
    results = []

    for table in _nested_list:
        if not isinstance(table, list) or len(table) < 3:
            results.append([[], pd.DataFrame()])
            continue

        # Extract labels (row 0)
        labels = [cell for cell in table[0] if isinstance(cell, str) and cell.strip() != ""]

        # Extract headers (row 1)
        header_row = table[1]
        if len(header_row) < 2:
            results.append([labels, pd.DataFrame()])
            continue
        columns = header_row[1:]

        # Extract data (rows 2+)
        data = []
        index = []
        for row in table[2:]:
            if not isinstance(row, list) or len(row) < 2:
                continue
            index.append(row[0])
            data.append(row[1:])

        # Create DataFrame
        try:
            df = pd.DataFrame(data, index=index, columns=columns)
        except Exception as e:
            print(f"Error in table: {e}")
            df = pd.DataFrame()

        results.append([labels, df])

    return results


def get_dataframes_indexes(_nested_dfs):
    """
    Takes a nested list where each sublist is in the format [dataframe_name, DataFrame].
    Returns a list of sublists in the format [dataframe_name, list_of_indexes].
    """
    _result = []

    for _item in _nested_dfs:
        if len(_item) != 2:
            continue  # skip invalid structures

        _df_name = _item[0]
        _df = _item[1]

        try:
            _indexes = []
            for _i in _df.index:
                _indexes.append(_i)
            _result.append([_df_name, _indexes])
        except AttributeError:
            continue  # skip if not a valid DataFrame

    return _result

def append_group_if_key_matches(_nested_list, _index, _sorted_data, _data_index=0):
    """
    Compares the element at _index in each sublist of _nested_list with the element at [0][0] of each sublist in _sorted_data.
    If there's a match, appends the group (deep copied) to the sublist in _nested_list.
    If no match is found, appends a 0.

    Args:
        _nested_list (list of lists): The list to enrich with matched groups.
        _index (int): The index in each sublist of _nested_list to compare.
        _sorted_data (list of single-item lists of lists): The grouped data to search.
        _data_index (int): Ignored for now; reserved for future flexibility.

    Returns:
        list of lists: Modified nested list with matched group or 0 appended.
    """
    result = []

    for sublist in _nested_list:
        new_sublist = sublist[:]
        matched = False

        if 0 <= _index < len(sublist):
            key = sublist[_index]

            for group in _sorted_data:
                if isinstance(group, list) and len(group) > 0 and len(group[0]) > 0:
                    if group[0][0] == key:
                        new_sublist.append(copy.deepcopy(group))
                        matched = True
                        break

        if not matched:
            new_sublist.append(0)

        result.append(new_sublist)

    return result

def replace_empty_strings_at_index(_nested_list, _target_index, _replacement_text):
    """
    Replaces empty strings at a specific index in sublists with a given text.
    
    Args:
        _nested_list (list): List containing sublists.
        _target_index (int): Index to check for empty strings.
        _replacement_text (str): Text to insert if an empty string is found.
    
    Returns:
        list: Modified nested list with replacements.
    """
    for _sublist in _nested_list:
        if len(_sublist) > _target_index and _sublist[_target_index] == "":
            _sublist[_target_index] = _replacement_text
    
    return _nested_list

import re
def compute_string_expressions(nested_list, _first_index):
    # Pattern to match potential parameter names (including spaces)
    param_pattern = re.compile(r'([A-Za-z_][\w ]*)')

    for sublist in nested_list:
        if len(sublist) < 3:
            continue  # Skip if sublist is too short

        element = sublist[0]

        # Identify index of DataFrame element (if present)
        df_index = len(sublist)
        for index, item in enumerate(sublist):
            if "DataFrame" in str(type(item)):
                df_index = index
                break

        # Iterate through the target items
        for i in range(_first_index, df_index):
            current = sublist[i]

            if not isinstance(current, str):
                continue  # Only process strings

            expression = current

            # Find all parameter-like words in the expression
            matched_params = param_pattern.findall(expression)

            success = True  # Flag to check if all parameters were successfully replaced

            # Replace each parameter name with its actual value from the Revit element
            for param in matched_params:
                param_name = param.strip()
                try:
                    value = element.GetParameterValueByName(param_name)
                    if value is None:
                        success = False
                        break
                    # Replace the parameter name in the expression (whole word match)
                    expression = re.sub(rf'\b{re.escape(param)}\b', str(value), expression)
                except:
                    success = False
                    break

            if not success:
                continue  # Skip this item if any parameter was not found

            try:
                result = eval(expression)
                if isinstance(result, (int, float)):
                    sublist[i] = round(result, 2)
                else:
                    sublist[i] = result
            except Exception as e:
                print(f" Error evaluating '{expression}': {e}")
                continue

    return nested_list

def replace_value_from_mapping(_nested_list, _1index, _2index):
    for sublist in _nested_list:
        # Skip if the sublist is shorter than the required indices
        if len(sublist) <= max(_1index, _2index):
            continue

        mapping_str = sublist[_1index]
        value_to_check = sublist[_2index]

        # Skip if the mapping is not a valid string
        if not isinstance(mapping_str, str):
            continue

        # Build the mapping dictionary from the string
        mapping = {}
        try:
            pairs = mapping_str.split(',')
            for pair in pairs:
                key_val = pair.split('=')
                if len(key_val) != 2:
                    continue
                key = float(key_val[0].strip())
                val = float(key_val[1].strip())
                mapping[key] = val
        except:
            continue  # Skip this sublist if parsing fails

        # Proceed if value to check is numeric
        if isinstance(value_to_check, (int, float)):
            closest_key = None
            smallest_diff = float('inf')

            # Find the closest key by absolute difference
            for key in mapping:
                diff = abs(value_to_check - key)
                if diff < smallest_diff:
                    smallest_diff = diff
                    closest_key = key

            # Replace the value if a closest key was found
            if closest_key is not None:
                sublist[_2index] = mapping[closest_key]

    return _nested_list

# Functions for Geometry

def get_elements_z_coordinates(_element_list):
    """
    Extracts Z-coordinate property from elements.
    Works on lists of objects with Z attribute.
    
    Args:
        _element_list (list): Objects with Z coordinate.
    
    Returns:
        list: Z values or None for invalid elements.
    """
    _coordinates = []
    
    for _element in _element_list:
        try:
            _coordinates.append(_element.Z)
        except AttributeError:
            _coordinates.append(None)
    
    return _coordinates

def find_intersections(_surface_list, _point_list, _space_list, _element_list):
    """
    Finds geometric intersections between surfaces and points.
    Works with four related lists of geometric objects.
    
    Args:
        _surface_list (list): Surface objects.
        _point_list (list): Point objects.
        _space_list (list): Related space objects.
        _element_list (list): Related element objects.
    
    Returns:
        list: Pairs of intersecting spaces/elements.
    """
    _intersections = []
    
    for _i, _surface in enumerate(_surface_list):
        for _j, _point in enumerate(_point_list):
            if _surface.DoesIntersect(_point):
                if _i < len(_space_list) and _j < len(_element_list):
                    _intersections.append([_space_list[_i], _element_list[_j]])
    
    return _intersections

# Text Processing Functions

def replace_text_in_list(_string_list, _old_text, _new_text):
    """
    Replaces all occurrences of a substring in a list of strings.
    Works on flat lists of strings.
    
    Args:
        _string_list (list): List to modify.
        _old_text (str): Text to replace.
        _new_text (str): New text to insert.
    
    Returns:
        list: Modified list with replacements.
    """
    _modified_list = []
    
    for _item in _string_list:
        _modified_list.append(_item.replace(_old_text, _new_text))
    
    return _modified_list

def add_data_to_strings(_strings_list, _data1):
    """
    Takes a list of strings and appends the corresponding element from _data1 to each element of _strings_list.

    Parameters:
    _strings_list (list): A list of strings to modify.
    _data1 (list): A list of strings to add to the corresponding indices.

    Returns:
    list: A new list with modified strings.
    """
    result = []
    for index in range(len(_strings_list)):
        new_string = (
            "New view called " + _strings_list[index] +
            " showing " + _data1[index] +
            " elements."
        )
        result.append(new_string)
    return result

def split_string_list_by_separator(_string_list, _separator):
    """
    Takes a single string or a list of strings and splits each string by the given separator.

    Args:
        _string_list (str or list): String or list of strings like "Type A, Type B" or ["Type A, Type B"]
        _separator (str): Separator like ","

    Returns:
        list: Flat list like ['Type A', 'Type B']
    """
    # If input is a single string, convert to list
    if isinstance(_string_list, str):
        _string_list = [_string_list]

    result = []
    for item in _string_list:
        parts = item.split(_separator)
        for part in parts:
            result.append(part.strip())  # trim spaces
    return result

def clean_sublist_text(_nested_list):
    """
    Cleans text in sublists by removing prefixes and truncating.
    Works on nested lists containing strings.
    
    Args:
        _nested_list (list): Text-containing nested structure.
    
    Returns:
        list: Structure with cleaned text elements.
    """
    for _sublist in _nested_list:
        if len(_sublist) > 1 and isinstance(_sublist[1], str):
            _sublist[1] = _sublist[1].replace("Family Type: ", "").split(",")[0]
    
    return _nested_list

def remove_indices_with_none(_input_list):
    """
    Removes indices from a list where the value is None.
    
    Args:
        _input_list (list): List to process.
    
    Returns:
        list: List with None values removed.
    """
    _cleaned_list = []
    
    for _item in _input_list:
        if _item is not None:
            _cleaned_list.append(_item)
    
    return _cleaned_list

def split_into_sublists(_lst):
    """
    Takes a list and creates a sublist for each element.

    Args:
        _lst (list): Original list.

    Returns:
        list: List of sublists, each containing a single element.
    """
    result = []
    for element in _lst:
        result.append([element])
    return result

# Advanced Functions

def process_nested_sublists(_nested_list, _source_idx, _target_idx):
    """
    Processes nested lists to move values between indices.
    Works on deeply nested list structures.
    
    Args:
        _nested_list (list): Multi-level nested list.
        _source_idx (int): Index to move from.
        _target_idx (int): Index to move to.
    
    Returns:
        list: Modified structure with moved values.
    """
    for _group in _nested_list:
        for _sublist in _group:
            if len(_sublist) > max(_source_idx, _target_idx):
                if _sublist[_source_idx] is not None:
                    _sublist[_target_idx] = _sublist[_source_idx]
                del _sublist[_source_idx]
    
    return _nested_list

def remove_duplicates_by_index(_nested_list):
    """
    Removes sublists with duplicate values at specific index.
    Works on nested lists while preserving first occurrences.
    
    Args:
        _nested_list (list): Potentially duplicated structure.
    
    Returns:
        list: De-duplicated nested structure.
    """
    _seen = set()
    _result = []
    
    for _sublist in _nested_list:
        if len(_sublist) > 1 and _sublist[1] not in _seen:
            _seen.add(_sublist[1])
            _result.append(_sublist)
    
    return _result