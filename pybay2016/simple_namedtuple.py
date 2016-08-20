"""
simple_namedtuple.py

This module implements a simplified version of CPython's collections.namedtuple
function, originally written by Raymond Hettinger.
"""

_class_template = """\
class {typename}(tuple):

    def __new__(_cls, {arg_list}):
        return tuple.__new__(_cls, ({arg_list}))

    def __repr__(self):
        return self.__class__.__name__ + '({repr_fmt})' % self

{field_defs}
"""


def simple_namedtuple(typename, field_names, verbose=False, rename=False):
    """Returns a new subclass of tuple with named fields.
    """
    class_definition = _class_template.format(
        typename=typename,
        num_fields=len(field_names),
        arg_list=repr(tuple(field_names)).replace("'", "")[1:-1],
        repr_fmt=', '.join(
            '{name}=%r'.format(name=name)
            for name in field_names
        ),
        field_defs='\n'.join(
            '    {name} = property(lambda t: t[{index:d}])'.format(
                index=index,
                name=name,
            )
            for index, name in enumerate(field_names)
        )
    )

    namespace = {}
    exec(class_definition, namespace)
    result = namespace[typename]

    return result
