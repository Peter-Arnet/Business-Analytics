test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> len(l1)
          bccff37f4c1619a432b4d88c87abab31
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> len(l2)
          22d47eaee86a03c9960551d366daa914
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> l3_a = [l1, l2]
          >>> len(l3_a)
          cd99306a8a4d43cdc1bec582c25794e2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> l1 = [1, 2, 4, 8, 16]
          >>> l2 = [1, 3, 9, 27]
          >>> l3_b = l1 + l2
          >>> len(l3_b)
          532c26a54948b866018a64e2bf19e925
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
          >>> cnt = 0
          >>> for i in range(9):
          ...     cnt += 1
          >>> print(cnt)
          532c26a54948b866018a64e2bf19e925
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
