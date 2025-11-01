def plain(diff_tree):
    def format_value(value):
        if isinstance(value, dict):
            return '[complex value]'
        if isinstance(value, str):
            return f"'{value}'"
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)

    def walk(tree, path=''):
        lines = []
        for key, node in tree.items():
            node_type = node['type']
            property_path = f"{path}.{key}" if path else key

            if node_type == 'nested':
                lines.extend(walk(node['children'], property_path))
            elif node_type == 'added':
                val = format_value(node['value'])
                lines.append(f"Property '{property_path}' was added with value: {val}")
            elif node_type == 'removed':
                lines.append(f"Property '{property_path}' was removed")
            elif node_type == 'changed':
                old = format_value(node['old_value'])
                new = format_value(node['new_value'])
                lines.append(f"Property '{property_path}' was updated. From {old} to {new}")

        return lines

    return '\n'.join(walk(diff_tree))