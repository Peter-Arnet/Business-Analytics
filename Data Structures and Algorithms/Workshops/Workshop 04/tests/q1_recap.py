test = {
  'name': 'Recap Lists and Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d = {'dog': 'bone', 'cat': 'mouse', 'bird': 'work', 'cow': 'grass'}
          >>> 'mouse' in d
          9a80b552ea9008bd2d5d8606b3a9300c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> points = {'Maria':[4,2], 'Tom':[1,4], 'John':[1,2]}
          >>> total = []
          >>> for i in points:
          >>>   total.append(sum(points[i]))
          >>> total
          663127cc12337e261eaed8a1e7a2498c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = [3, 6, 8, 2]
          >>> b = ['a','A','er']
          >>> c = a[3::-2]+b[:-1]
          >>> c
          4ccade6592dde571b71be7dab68ca0ea
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
