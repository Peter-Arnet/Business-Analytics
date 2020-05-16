test = {
  'name': 'Comparisons',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(2 > 2)
          c685469f4159cffd6a85ec4019511dab
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(2 >= 2)
          1ac56596133f2112dab3e3ff26ecc44f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(not (5 > 2))
          c685469f4159cffd6a85ec4019511dab
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 5
          >>> y = 4
          >>> print(x > y and x < 8)
          1ac56596133f2112dab3e3ff26ecc44f
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
