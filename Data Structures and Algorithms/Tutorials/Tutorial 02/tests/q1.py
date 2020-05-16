test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 1: # In case of infinite loop, type Infinite loop
          ...     n = n - 1
          ...     print(n)
          8dc46e1446cb7879cc9855ad0e7de734
          579281ecdc4acf52f16031a54d018b4a
          3a18f6493aa8e1a4bd954815525d8ea4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> n = 0.8
          >>> while n <= 1: # In case of infinite loop, type Infinite loop
          ...     n = n * n
          ...     print(n)
          12723aec3146fc43af065293c82c6315
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def some_function(i):
          ...     if type(i) == str:
          ...         print('A string')
          ...     else:
          ...         print('Something else')
          >>> some_function('Hello there!' + str(float('3.14')))
          5d2a8a7356d968d5dc136cfc2a8da62c
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
