test = {
  'name': 'Strings',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> word = 'hello!'
          >>> print(word[1:3])
          499bac11dc54d1ee5c0957a92ae79a5f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> word = 'hello!'
          >>> len(word)
          f507732b803696cb16747bfa7416d258
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> word = 'hElLO!'
          >>> print((word.lower()).capitalize())
          821bebaea015a9b455fb47e53678b4fe
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> word = 'lovely day'
          >>> count = 0
          >>> for letter in word:
          ...     if letter in 'hey':
          ...         count += 1
          >>> print(count)
          f1b1400d10ad1bba22ee4d9fcfdef630
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
