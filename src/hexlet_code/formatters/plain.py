def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff_tree):
    def walk(tree, path=''):
        lines = []
        for node in tree:
            key = node['key']
            ntype = node['type']
            full_path = f"{path}.{key}" if path else key

            if ntype == 'nested':
                lines.extend(walk(node['children'], full_path))
            elif ntype == 'added':
                value = to_str(node['value'])
                lines.append(f"Property '{full_path}' was added with value: {value}")
            elif ntype == 'removed':
                lines.append(f"Property '{full_path}' was removed")
            elif ntype == 'changed':
                old = to_str(node['old_value'])
                new = to_str(node['new_value'])
                lines.append(f"Property '{full_path}' was updated. From {old} to {new}")
        return lines

    return '\n'.join(walk(diff_tree))
