test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a = [2, 2, 3, 1]
          >>> b = []
          >>> for i in a:
          >>>   b.append(i**2)
          >>> b # enter lists in format [a, b, c, d] including spaces
          6822ddb831a2581d4e07d8261bdf4df9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def calculate(x):
          >>>     return len(x)
          >>> a = ['a','A','er','cere']
          >>> b = []
          >>> for i in a:
          >>>   b.append(calculate(i))
          >>> b
          0ba34e76e0f7df71150c53b743f763aa
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = [3, 6, 8, 7]
          >>> b = []
          >>> for i in range(len(a)):
          >>>   b.append(a[len(a)-1-i])
          >>> b
          a8dea5b107c7073e053450e0bbf0d1c0
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
          >>> a = [3, 6, 8, 1, 78, 2, 23, 45, 9]
          >>> x = 2
          >>> def f(s, i):
          ...     for elem in s:          
          ...         if elem == i:
          ...             return True
          ...     return False
          >>> f(a, x)
          09c13baeb52db0ae5eeb720234f850d2
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
          'answer': '5cd9f78d29e494e1dd7234f4d7f6cbfc',
          'choices': [
            'O(n)',
            'O(n**3)',
            'O(n**2)',
            'O(n*log(n))'
          ],
          'hidden': False,
          'locked': True,
          'question': 'What is the complexity of the previous code? (if n = len(a)):'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
