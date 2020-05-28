test = {
  'name': 'Big O Extra',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'ab4753ae8566144542c28b281bdd6c71',
          'choices': [
            'O(n)',
            'O(n!)',
            'O(n**2)',
            'O(log(n)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the big-O complexity in terms of the size of the input (e.g. assuming a list L of length n)?:
          
          >>> u = 0
          >>> for item in L:
          >>>   u = u + item**2
          >>>   u = u - item
          """
        },
        {
          'answer': '575cf4866906b6cf1980034a65c6522c',
          'choices': [
            'O(n)',
            'O(log(n)',
            'O(n**2)',
            'O(n!)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the big-O complexity in terms of the size of the input (e.g. assuming a list L of length n)?:
          
          >>> s = 0
          >>> for index in range(len(L)):
          >>>   L[index] = L[index] + 1
          >>>   for item in L:
          >>>     s = s + item
          """
        },
        {
          'answer': '575cf4866906b6cf1980034a65c6522c',
          'choices': [
            'O(n**2)',
            'O(n)',
            'O(log(n)',
            'O(n!)'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What is the big-O complexity in terms of the size of the input (e.g. assuming n is a non-negative integer)?:
          
          >>> y = 0
          >>> i = n
          >>> while i > 0:
          >>>   j = i
          >>>   while j > 0:
          >>>     y += 1
          >>>     j -= 1
          >>>   i -= 1
          """
        },
        {
          'answer': '67730c72a6de86bab153cd974e9cb5c9',
          'choices': [
            'A, D, C, B',
            'D, A, B, C',
            'A, B, C, D',
            'B, A, D, C',
            'None of the others'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How would you rate the following functions in increasing order of big-O complexity?
          		  A: n*log(n) 
          		  B: n**2
          		  C: 2**n
          		  D: n*log(2)
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
