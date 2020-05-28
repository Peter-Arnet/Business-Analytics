test = {
  'name': 'Loops',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 2
          >>> while n >= 0: # In case of infinite loop, type Infinite loop
          ...     n = n - 1
          ...     print(n)
          5528a2a333a76419cf9fa2b9250633c7
          8fc5f586611ef9f8cdc9b1cf6394102d
          3b1ab051437a3b460ee4db79cd77075f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> n = 1
          >>> while n >= 0: # In case of infinite loop, type Infinite loop
          ...     n = n + 1
          ...     print(n)
          8191237a334564c2d2e4091b23bb3e58
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> y = 2
          >>> while y != 0: # In case of infinite loop, type Infinite loop
          ...     y = y // 2
          ...     print(y)
          5528a2a333a76419cf9fa2b9250633c7
          8fc5f586611ef9f8cdc9b1cf6394102d
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
