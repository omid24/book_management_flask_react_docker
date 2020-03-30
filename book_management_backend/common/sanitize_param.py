def sanitize_param(param):
    if param:
        if type(param) == str:
            param = param.replace("''", "")
            param = param.strip()
        return param
    return None
