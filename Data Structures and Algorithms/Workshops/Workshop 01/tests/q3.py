test = {
  'name': 'Functions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def mult(x, y):
          ...     product = x * y
          ...     return product
          >>> mult(5,2)
          1f3616be5b4d1a3c69b54acaaebd3223
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def some_printing(text):
          ...     if text == 'hey':
          ...         print(text)
          ...     else:
          ...         print('hello')
          >>> some_printing('hi')
          d4c54bca3f47e2c940d5a4a4943be5f7
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> def go(n):
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4)  # If this loops forever, type Infinite Loop.  If it produces and error, write Error. If it displays nothing, write Nothing
          fe1755d1dbcee201e8d46e3d0833fbe8
          5f11241a9f43d2345eaee1368e2af949
          5528a2a333a76419cf9fa2b9250633c7
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
