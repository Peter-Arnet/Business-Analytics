test = {
  'name': 'Pandas_Q5',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # reduced_data.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # reduced_data.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'reduced_data' in vars()
          324f0bc3fa670ff02cd11d2a63a789ba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> reduced_data.shape[1] == data.shape[1] - 3
          324f0bc3fa670ff02cd11d2a63a789ba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> reduced_data.shape[0] == data.shape[0]
          324f0bc3fa670ff02cd11d2a63a789ba
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # It looks like the columns requested to be removed
          >>> # do still exist.
          >>> exists = False
          >>> if 'Cabin' in reduced_data.columns: 
          ...     exists = True
          >>> exists
          921fe1d91ffe610e434a73c5a21f45b9
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
