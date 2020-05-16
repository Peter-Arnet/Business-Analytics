test = {
  'name': 'Numpy - Q3',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It looks like you didn't give anything the name
          >>> # fb_returns.  Maybe there's a typo, or maybe you
          >>> # just need to run the cell above this test cell where you defined
          >>> # fb_returns.  (Click that cell and then click the "run
          >>> # cell" button in the menu bar above.)
          >>> 'fb_returns' in vars()
          5a1061509e718fe6d88f58d01d238cee
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> sum(fb_returns)//0.0001 == 3212.0
          5a1061509e718fe6d88f58d01d238cee
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
