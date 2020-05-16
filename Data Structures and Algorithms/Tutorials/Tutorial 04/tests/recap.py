test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d={'Joe':123, 'Jane':234}
          >>> sorted(list(d.keys()))
          92fccd529eb46cf09bce8db079a90f6c
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
          >>> a= (1 , 2 , 3)
          >>> a[1]=6 # In case of error, type Error
          8d3f432f282db29ae0cef7fb84344ac8
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
