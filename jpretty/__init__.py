import json


def _make_pretty(emit, indent_unit, sort_keys,
        _encode=json.encoder.encode_basestring,
        _posinf=float('+inf'),
        _neginf=float('-inf'),
        _floatstr=float.__repr__,
        _intstr=int.__repr__,
        simple_type=(str, int, float, bool, type(None)),
        isinstance=isinstance,
        len=len,
        all=all,
        str=str,
        int=int,
        float=float,
        tuple=tuple,
        list=list,
        dict=dict
    ):
    def _iterate_list(items, iterate_item, bracket_indent, inline):
        if inline:
            element_indent = None
            separator = ''
        else:
            element_indent = bracket_indent + indent_unit
            separator = '\n' + element_indent
        first = True
        for item in items:
            iterate_item(item, element_indent, separator)
            if first:
                first = False
                separator = ',' + (separator or ' ')
        if not inline:
            emit('\n' + bracket_indent)

    def _iterate_pair(item, indent, sep=''):
        key, value = item
        if not isinstance(key, str):
            raise TypeError('Invalid JSON key "{}"'.format(key))
        emit(sep + _encode(key))
        _iterate_obj(value, indent, ': ')

    def _iterate_obj(obj, indent, sep=''):
        if isinstance(obj, str):
            emit(sep + _encode(obj))
        elif obj is True:
            emit(sep + 'true')
        elif obj is False:
            emit(sep + 'false')
        elif obj is None:
            emit(sep + 'null')
        elif isinstance(obj, int):
            emit(sep + _intstr(obj))
        elif isinstance(obj, float):
            if obj != obj or obj == _posinf or obj == _neginf:
                raise ValueError('Invalid JSON number "{}"'.format(obj))
            emit(sep + _floatstr(obj))
        elif isinstance(obj, (list, tuple)):
            if len(obj) > 0:
                emit(sep + '[')
                _iterate_list(obj, _iterate_obj, indent,
                    inline or all(isinstance(x, simple_type) for x in obj))
                emit(']')
            else:
                emit(sep + '[]')
        elif isinstance(obj, dict):
            if len(obj) > 0:
                emit(sep + '{')
                items = obj.items()
                if sort_keys:
                    items = sorted(items)
                _iterate_list(items, _iterate_pair, indent, inline)
                emit('}')
            else:
                emit(sep + '{}')
        else:
            raise TypeError('Invalid JSON object "{}"'.format(obj))

    inline = indent_unit is None
    return _iterate_obj


def dumps(obj, indent=4, sort_keys=False):
    if isinstance(indent, int):
        indent = indent * ' '
    parts = []
    pretty = _make_pretty(parts.append, indent, sort_keys)
    pretty(obj, '')
    return ''.join(parts)


def _make_iter_pretty(indent_unit, sort_keys,
        _encode=json.encoder.encode_basestring,
        _posinf=float('+inf'),
        _neginf=float('-inf'),
        _floatstr=float.__repr__,
        _intstr=int.__repr__,
        simple_type=(str, int, float, bool, type(None)),
        isinstance=isinstance,
        len=len,
        all=all,
        str=str,
        int=int,
        float=float,
        tuple=tuple,
        list=list,
        dict=dict
    ):
    def _iterate_list(items, iterate_item, bracket_indent, inline):
        if inline:
            element_indent = None
            separator = ''
        else:
            element_indent = bracket_indent + indent_unit
            separator = '\n' + element_indent
        first = True
        for item in items:
            yield from iterate_item(item, element_indent, separator)
            if first:
                first = False
                separator = ',' + (separator or ' ')
        if not inline:
            yield '\n' + bracket_indent

    def _iterate_pair(item, indent, sep=''):
        key, value = item
        if not isinstance(key, str):
            raise TypeError('Invalid JSON key "{}"'.format(key))
        yield sep + _encode(key)
        yield from _iterate_obj(value, indent, ': ')

    def _iterate_obj(obj, indent, sep=''):
        if isinstance(obj, str):
            yield sep + _encode(obj)
        elif obj is True:
            yield sep + 'true'
        elif obj is False:
            yield sep + 'false'
        elif obj is None:
            yield sep + 'null'
        elif isinstance(obj, int):
            yield sep + _intstr(obj)
        elif isinstance(obj, float):
            if obj != obj or obj == _posinf or obj == _neginf:
                raise ValueError('Invalid JSON number "{}"'.format(obj))
            yield sep + _floatstr(obj)
        elif isinstance(obj, (list, tuple)):
            if len(obj) > 0:
                yield sep + '['
                yield from _iterate_list(obj, _iterate_obj, indent,
                    inline or all(isinstance(x, simple_type) for x in obj))
                yield ']'
            else:
                yield sep + '[]'
        elif isinstance(obj, dict):
            if len(obj) > 0:
                yield sep + '{'
                items = obj.items()
                if sort_keys:
                    items = sorted(items)
                yield from _iterate_list(items, _iterate_pair, indent, inline)
                yield '}'
            else:
                yield sep + '{}'
        else:
            raise TypeError('Invalid JSON object "{}"'.format(obj))

    inline = indent_unit is None
    return _iterate_obj


def gdumps(obj, indent=4, sort_keys=False):
    if isinstance(indent, int):
        indent = indent * ' '
    iter_pretty = _make_iter_pretty(indent, sort_keys)
    parts = list(iter_pretty(obj, ''))
    return ''.join(parts)
