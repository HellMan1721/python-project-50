def build_diff_dict(data1, data2):
    data1 = data1 or {}
    data2 = data2 or {}

    def make_node(key):
        in1 = key in data1
        in2 = key in data2
        v1 = data1.get(key)
        v2 = data2.get(key)

        if not in1 and in2:
            return {'type': 'added', 'value': v2}
        if in1 and not in2:
            return {'type': 'removed', 'value': v1}

        # both present
        if isinstance(v1, dict) and isinstance(v2, dict):
            return {'type': 'nested', 'children': build_diff_dict(v1, v2)}
        if v1 == v2:
            return {'type': 'unchanged', 'value': v1}
        return {'type': 'changed', 'old_value': v1, 'new_value': v2}

    diff = {}
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_keys:
        diff[key] = make_node(key)
    return diff