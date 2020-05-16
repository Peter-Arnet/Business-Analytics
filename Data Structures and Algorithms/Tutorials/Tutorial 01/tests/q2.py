test = {
  'name': 'Variables',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = 5
          >>> b = 6
          >>> c = a * b
          >>> c
          dd292ea7fd8c8e5be0b8e84b58332bb8
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
          >>> z = 1
          >>> b = 5
          >>> z = z + b
          >>> z
          2c476b02f8ba0c2a7ba16d80ad3a9b84
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
          >>> a = 5
          >>> b = 6
          >>> c = a * b
          >>> a = 100
          >>> c
          dd292ea7fd8c8e5be0b8e84b58332bb8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = 5
          >>> b = 6
          >>> temp = a
          >>> a = b
          >>> b = temp
          >>> print(a)
          >>> print(b)
          2c476b02f8ba0c2a7ba16d80ad3a9b84
          379a92d554955ef9651d0899c9f66740
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
