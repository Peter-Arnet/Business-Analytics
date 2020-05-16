test = {
  'name': 'Conditional Statements',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 5 # If there is no output, write Nothing
          >>> if x > 4:
          ...     print('Hey!')
          098a11c159347e1458105464107345be
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> dish = 'broccoli' # If there is no output, write Nothing
          >>> if dish == 'potatoes':
          ...     print('My favorite food!')
          >>> else:
          ...     print('Yuck.')
          8877874f0d8eb1a78cc165e09aa11ec4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 0 # If there is no output, write Nothing
          >>> if temp >= 30:
          ...     print('Too hot!')
          >>> elif temp <= 0:
          ...     print('Too cold!')
          >>> else:
          ...     print('Perfect!')
          b252cb55fe69d8750fe623819970cf2e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 18 # If there is no output, write Nothing
          >>> humidity = 90
          >>> if temp >= 30:
          ...     print('Too hot!')
          ...     if humidity > 80:
          ...         print('I\'m out of here!')
          5653be5a07621caf928e87830fc1c634
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 40 # If there is no output, write Nothing
          >>> humidity = 90
          >>> if temp >= 30:
          ...     print('Too hot!')
          ...     if humidity > 80 and humidity < 100:
          ...         print('Hot and kind of humid!')
          ...     elif humidity < 80:
          ...         print('Hot but not too humid!')
          ...     else:
          ...         print('I\'m out of here!')
          deedacd3187b91f1f1f87ecfcdbf55c5
          8993281cd0d50964db7eefb0c4d2046a
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
