test = {
  'name': 'q_recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def f(x):
          ...     y = x - 1
          ...     z = y*2
          ...     return y + z
          >>> y = 1
          >>> z = 2
          >>> x = 3
          >>> y = f(z + x)
          >>> print(x, y, z)
          dde952419c17f89f66545ead49949bc1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def g(x):
          ...     y = x - 1
          ...     return y
          ...     z = y*2
          ...     return y + z
          >>> x = 1
          >>> y = g(x)
          >>> y
          d8a523aa3c7bca42ea6e1a147a83dff7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 1
          >>> while x<=8 or x%2==0:
          ...     x = x+3
          ...     print(x)
          5b465020ff20a7eb54ec5a1cb2a7dc83
          3971834c7f1c30241b7a5ee15730a00d
          2a652c0d811821f3e9c6b4e09c9b8283
          999e8a299ca37060651c7fad7df362b3
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
