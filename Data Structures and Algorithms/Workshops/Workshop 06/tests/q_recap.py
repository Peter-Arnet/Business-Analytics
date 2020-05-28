test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d = {'dog', 'cat', 'bird', 'cow'}
          >>> type(d)
          8b89179909f16fb9ae1f8b21205574be
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 'cat' in d
          533ebb8d5a6c8967cb5d349b039b3190
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> d.add('mouse')
          >>> len(d)
          bd8347cadc29d8ec46e51bcc965bd9c2
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
          >>> # Write Error if there's an error
          >>> x, y = [9,3,1], 1 
          >>> y
          ce45b3ff5e74cb911e1c2a4b902c1201
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> x, y = 4, 1 
          >>> y, x = x, y 
          >>> x
          ce45b3ff5e74cb911e1c2a4b902c1201
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Write Error if there's an error
          >>> def f(x, y):
          ...     a, b = 3*x, 2*y
          ...     return a, b
          >>> x, y = f(2, 2)
          >>> x
          4a99e1c28b3b0ef39a5b81b923fd9210
          # locked
          >>> y
          169dba4ab7397962e053202d7c8724dc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> animals = {'eagle': 'bird', 'hawk': 'bird', 'manatee': 'mammal', 'finch': 'bird'}
          >>> bird_count = 0
          >>> for animal in animals:
          ...    if animals[animal] == 'bird':
          ...        bird_count += 1
          >>> bird_count
          82c58072024086e94ee1cbf5d53ad198
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
