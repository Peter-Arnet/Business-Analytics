test = {
  'name': 'Comprehensions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> [x**2 for x in range(2)]
          3beab26f7d0eab352e83b7f045375ab3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> [len(name) for name in ['Joe', 'Mary', 'Zoe']]
          4c6a1a4e297fb687c1f239594d30307c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> names = {name:len(name) for name in ['John', 'Mary', 'Zoe']}
          >>> names['Zoe']
          de5a1ee1646a21fe714c3466190c86fa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> names = [name:len(name) for name in ['John', 'Mary', 'Zoe']]
          >>> names['Zoe']
          8d6dfd07d32e42def80164ad76f8b301
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # if there's an error, write Error
          >>> x = {s for s in 'John'}
          >>> 'j' in x
          bc7c4866f6593cc5a61914e675ee18c7
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
