from ._utils import (
    flatten as flatten,
    extract_files as extract_files,
    is_mapping as is_mapping,
    is_dict as is_dict,
    is_list as is_list,
    is_annotated_type as is_annotated_type,
    is_list_type as is_list_type,
    is_union_type as is_union_type,
    is_required_type as is_required_type,
    strip_annotated_type as strip_annotated_type,
    extract_type_arg as extract_type_arg,
    required_args as required_args,
    deprecated_positional_args as deprecated_positional_args,
    deepcopy_minimal as deepcopy_minimal,
)
from ._transform import PropertyInfo as PropertyInfo, transform as transform, maybe_transform as maybe_transform
