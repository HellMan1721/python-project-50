def _format_primitive(value, in_nested=False):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return value
    return str(value)


def _stringify(value, depth=0, in_nested=False):
    indent_unit = '    '
    if not isinstance(value, dict):
        return _format_primitive(value, in_nested=in_nested)

    inner_indent = indent_unit * (depth + 1)
    closing_indent = indent_unit * depth
    lines = ['{']
    for k in sorted(value.keys()):
        v = value[k]
        lines.append(
            f'{inner_indent}{k}: {_stringify(v, depth + 1, in_nested=True)}'
            )
    lines.append(f'{closing_indent}}}')
    return '\n'.join(lines)


def format_diff(diff_dict, depth=0):
    indent_unit = '    '
    base_indent = indent_unit * depth
    lines = ['{']

    for key in sorted(diff_dict.keys()):
        node = diff_dict[key]
        ntype = node['type']

        nested_flag = depth > 0

        if ntype == 'nested':
            children = format_diff(node['children'], depth + 1)
            lines.append(f'{base_indent}{indent_unit}{key}: {children}')
        elif ntype == 'unchanged':
            val = _stringify(node['value'], depth + 1, in_nested=nested_flag)
            lines.append(f'{base_indent}{indent_unit}{key}: {val}')
        elif ntype == 'removed':
            val = _stringify(node['value'], depth + 1, in_nested=nested_flag)
            lines.append(f'{base_indent}  - {key}: {val}')
        elif ntype == 'added':
            val = _stringify(node['value'], depth + 1, in_nested=nested_flag)
            lines.append(
                f'{base_indent}  + {key}: {val}'
                )
        elif ntype == 'changed':
            old = _stringify(
                node['old_value'], depth + 1, in_nested=nested_flag
                )
            new = _stringify(
                node['new_value'], depth + 1, in_nested=nested_flag
                )
            lines.append(f'{base_indent}  - {key}: {old}')
            lines.append(f'{base_indent}  + {key}: {new}')

    lines.append(f'{base_indent}}}')
    return '\n'.join(lines)