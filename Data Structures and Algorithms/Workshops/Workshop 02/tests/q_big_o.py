test = {
  'name': 'Big O ',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '31db841416d6796889c9e815965c6131',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>   print('Hello!')
          """
        },
        {
          'answer': 'd8779613f51c35368ddb482849df0a75',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>   for j in range(n):
          >>>     print('Hello!')
          """
        },
        {
          'answer': 'd7edbb943e65b6f05bafddf67133cb40',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> for i in range(n):
          >>>   print('Hello!')
          >>>   print('Hello!')
          """
        },
        {
          'answer': 'f0725d321f05b3516aa8dc9622f6fcb9',
          'choices': [
            'n times',
            '2n times',
            'n**2 times',
            'log(n) times'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many times will python print 'Hello!'?:
          (n is a positive integer number)
          
          >>> while n>1:
          >>>    n=int(n/2)
          >>>    print(Hello!)
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
