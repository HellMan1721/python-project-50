def _format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def _walk(tree, path=''):
    lines = []
    for key, node in tree.items():
        node_type = node['type']
        property_path = f"{path}.{key}" if path else key

        if node_type == 'nested':
            lines.extend(_walk(node['children'], property_path))

        if node_type == 'added':
            val = _format_value(node['value'])
            msg = (
                f"Property '{property_path}' was added with value: "
                f"{val}"
            )
            lines.append(msg)
            continue

        if node_type == 'removed':
            lines.append(f"Property '{property_path}' was removed")
            continue

        if node_type == 'changed':
            old = _format_value(node['old_value'])
            new = _format_value(node['new_value'])
            msg = (
                f"Property '{property_path}' was updated. "
                f"From {old} to {new}"
            )
            lines.append(msg)
            continue

    return lines


def plain(diff_tree):
    return '\n'.join(_walk(diff_tree))