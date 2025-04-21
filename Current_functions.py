# Functions for Flat Lists

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