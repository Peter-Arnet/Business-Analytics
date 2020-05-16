test = {
  'name': 'Lists',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> len(l1)
          9a9ce737951afcd1db6333d658194b98
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l2 = ['g', 3, 'k']
          >>> len(l1) + len(l2)
          0bdff5da92bca2a9b461a0ca31b91d67
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l1[2] 
          8dc46e1446cb7879cc9855ad0e7de734
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [17, 'a', 2, 'tokyo']
          >>> l1[1:3] # in case of list, write in the following format: [a, b, c, d, e, f]
          f4dbf94b7bf6a93b9fbf268428c4cc06
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 5, 3]
          >>> for number in l1:
          ...     print(number**2)
          579281ecdc4acf52f16031a54d018b4a
          f9134ffc7fb1d74e799ae7e94cb3af18
          b641e6ef0b2d578dc6dad17a6a05b23b
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
