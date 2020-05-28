test = {
  'name': 'q1_recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def lsum(L):
          ...     # L is a list with at least two items
          ...     list_sum = L[0]
          ...     for item in L[1:]:
          ...         list_sum =  list_sum + item
          ...     print(list_sum)
          >>> lsum([1, 2, 3])
          1c98c3b641a550803f159414a096d823
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> lsum(['a', 'b', 'c'])
          efcfdd2fc99003cbba028c5016fd815a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = lsum([2, 2, 1])
          >>> print(x)
          879fa07761097163f59ff73644745607
          9590014f354e6b540a42868a334b3d26
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
