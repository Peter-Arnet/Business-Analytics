test = {
  'name': 'Sets and tuples',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> cities = set()
          >>> cities.add('London')
          >>> cities.add('Paris')
          >>> 'Rome' in cities
          bc7c4866f6593cc5a61914e675ee18c7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities.add('Amsterdam')
          8d6dfd07d32e42def80164ad76f8b301
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities.append('Amsterdam')
          8d6dfd07d32e42def80164ad76f8b301
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cities = ('London', 'Paris', 'Rome')
          >>> cities[0] = 'Amsterdam'
          8d6dfd07d32e42def80164ad76f8b301
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def sum_and_difference(x, y):
          ...     return x + y, x - y
          >>> z = sum_and_difference(5, 3)
          >>> type(z)
          b955c8cd8ad568a040f660a9cdbe5823
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def sum_and_difference(x, y):
          ...     return x + y, x - y
          >>> z, w = sum_and_difference(5, 3)
          >>> type(z)
          f9232c4324b3ae2aeff96729f417872c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
