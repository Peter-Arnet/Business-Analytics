test = {
  'name': 'For loops',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> temp = 0
          >>> for i in range(5):
          ...     temp += 2
          >>> print(temp)
          a0315e2a729bacd22061c44184981d64
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cnt1 = 0
          >>> cnt2 = 0
          >>> for i in range(2):
          ...     cnt1 += 1
          ...     for j in range(3):
          ...         cnt2 += 1
          >>> print(cnt1, cnt2)
          2af8a847d84c882812b3c5fb22e24fdc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def loop_fun(n):
          ...     x = n
          ...     for i in range(n):
          ...         y = 0         
          ...         for j in range(n):
          ...             y += x
          ...         x += y
          ...     return x
          >>> loop_fun(2)
          0984abc438a2d82aece5442b733ce157
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
