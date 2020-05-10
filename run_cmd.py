'''
   @author:    Donald C
   @github:    @DonnC
   @project:   Run CMD zim rates
   @created:   10 May 2020
   @updated:   10 May 2020
'''

from __future__ import print_function, unicode_literals
from __future__ import print_function
from pyfiglet import Figlet
from PyInquirer import style_from_dict, Token, prompt, Separator
from clint.textui import puts, colored, indent
from time import sleep

from getRates import scrapeRates

# Show CMD program
f = Figlet(font='slant')
showName = f.renderText('- ZIM    RATES -')
endName  = f.renderText('github: @DonnC')

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'checkbox',
        'message': 'Run code with internet access!',
        'name': 'permission',
        'choices': [
            Separator('== Allow permission? =='),
            {
                'name': 'Yes',
                'checked': True
            },
            {
                'name': 'No'
            },
        ],
    }
]

# start program message
print(showName)

answers = prompt(questions, style=style)

# FIXME: Validate when user choose both options
answer = answers.get('permission')[0]              # get first option selected

if answer == 'Yes':
   # get news data
   puts(colored.yellow('Loading rates..\n'))

   recv_data = scrapeRates()

   puts(colored.cyan(f'Rates source: {recv_data.get("source")}\nLast Updated: {recv_data.get("updated")}\n', bold=True))

   puts(colored.magenta('\tSOURCE\t\t\t\tRATE', bold=True))

   for row in recv_data.get("rates"):
      with indent(4, quote='>>>'):
         puts(f'''{colored.green(f'{row.get("source")}: '.ljust(35,' '))} {colored.blue(f'{row.get("rate")}')}''')

   print()

else:
   # exit application
   puts(colored.red('Access permission denied. Exiting!'))
   print()
   sleep(2)

# end program message
print(endName)