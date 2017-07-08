from tkinter import *
from re import findall

# 다음 단어들을 text에서 정규식으로 찾으시오.

#  experiences
#  laughters
#  perceive
#  difference
#  between
#  perceptual
#  experience
#  something
#  considered
#  considered
#  researchers
#  between

text = '''Humor, the tendency of particular cognitive experiences to provoke
laughters and provide amusement, affects how we perceive and respond to
life. It enhances the quality of life and may relieve the body from so many
health problems. In fact, humans are the only creatures on earth that are
endowed with the ability to laugh.
The difference between humor and laughter is that humor is a perceptual
process while laughter is a behavioral response. People of all ages and
cultures respond to humor. The majority of people are able to experience
humor, i.e., to be amused, to laugh or smile at something funny, and thus
they are considered to have a sense of humor. Regular laugh sessions can have
important effects on our health and well being. For instance, laughter is
considered to be a stress buster and researchers found a direct link between
laughter and healthy function of blood vessels. Laughter causes the dilatation of
the inner lining of blood vessels, the endothelium, and increases blood flow.
It also has been shown to lead to deductions in stress hormones such as cortisol
and epinephrine. When laughing the brain also releases endorphins.
Laughter also boosts the number of antibody-producing cells and enhances the 
effectiveness of T-cells, a type of cells that lead to a stronger immune system.
'''

def find_terms():
    results_text.delete(1.0, END)
    answerlist=[]
    for answers in findall('',text): 
        answerlist.append(answers)
    for answer in findall('',text):
        answerlist.append(answer)        
    for answer_print in answerlist:
        results_text.insert(END,answer_print)
        results_text.insert(END,"\n")   


display_window = Tk()

display_window.title('Term Extractor')

results_text = Text(display_window, width = 25, height = 12,
                    wrap = WORD, bg = 'grey', font = ('Arial', 16),
                    borderwidth = 2, relief = 'groove')
results_text.pack(padx = 4, pady = 4)       

Button(display_window, text = 'Find terms', command = find_terms).\
    pack(pady = 3)

display_window.mainloop()
